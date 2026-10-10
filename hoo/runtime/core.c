#include "hoo_runtime.h"
static HObject *objects;
static HValue **roots;
static size_t root_count, root_cap, allocations;
static int hargc, source_line, source_column;
static char **hargv;
_Noreturn void ho_fail(const char *message) {
    fprintf(stderr,"hoo runtime %d:%d: %s\n",source_line,source_column,message);
    exit(70);
}
void ho_location(int line,int column) { source_line=line; source_column=column; }
void *ho_alloc(size_t bytes) {
    void *p=calloc(1,bytes ? bytes : 1);
    if(!p) ho_fail("out of memory");
    return p;
}
static void *resize(void *p,size_t bytes) {
    void *q=realloc(p,bytes ? bytes : 1);
    if(!q) ho_fail("out of memory");
    return q;
}
static HValue object(int type) {
    HObject *o=ho_alloc(sizeof(*o)); o->type=type; o->next=objects; objects=o; allocations++;
    HValue v={.type=type}; v.as.object=o; return v;
}
void ho_root(HValue *value) {
    if(root_count==root_cap) { root_cap=root_cap ? root_cap*2 : 128; roots=resize(roots,root_cap*sizeof(*roots)); }
    roots[root_count++]=value;
}
size_t ho_frame(void) { return root_count; }
void ho_restore(size_t frame) { if(frame>root_count) ho_fail("corrupt root frame"); root_count=frame; }
static void collect(int force) {
    if(!force && allocations<256) return;
    for(size_t i=0;i<root_count;i++) {
        HValue v=*roots[i];
        if(v.type==H_TEXT || v.type==H_LIST || v.type==H_WIDGET) v.as.object->marked=1;
    }
    HObject **p=&objects;
    while(*p) {
        HObject *o=*p;
        if(o->marked) { o->marked=0; p=&o->next; }
        else { *p=o->next;
            if(o->type==H_TEXT) free(o->as.text);
            if(o->type==H_LIST) free(o->as.list.data);
            free(o);
        }
    }
    allocations=0;
}
void ho_collect(void) { collect(0); }
void ho_init(int argc,char **argv) { hargc=argc; hargv=argv; }
void ho_shutdown(void) { ho_ui_shutdown(); root_count=0; collect(1); free(roots); roots=NULL; root_cap=0; }
HValue ho_load(HValue v) { if(v.type==H_VOID) ho_fail("variable used before initialization"); return v; }
HValue ho_void(void) { return (HValue){.type=H_VOID}; }
HValue ho_number(int64_t n) { HValue v={.type=H_NUMBER}; v.as.number=n; return v; }
HValue ho_boolean(int b) { HValue v={.type=H_BOOLEAN}; v.as.number=!!b; return v; }
HValue ho_callback(HCallback fn) { HValue v={.type=H_CALLBACK}; v.as.callback=fn; return v; }
HValue ho_text(const char *s) { HValue v=object(H_TEXT); size_t len=strlen(s)+1; v.as.object->as.text=ho_alloc(len); memcpy(v.as.object->as.text,s,len); return v; }
HValue ho_widget(void *native,int kind) { HValue v=object(H_WIDGET); v.as.object->as.widget.native=native; v.as.object->as.widget.kind=kind; return v; }
HValue ho_add(HValue a,HValue b) { int64_t n; if(__builtin_add_overflow(a.as.number,b.as.number,&n)) ho_fail("integer addition overflow"); return ho_number(n); }
HValue ho_subtract(HValue a,HValue b) { int64_t n; if(__builtin_sub_overflow(a.as.number,b.as.number,&n)) ho_fail("integer subtraction overflow"); return ho_number(n); }
HValue ho_multiply(HValue a,HValue b) { int64_t n; if(__builtin_mul_overflow(a.as.number,b.as.number,&n)) ho_fail("integer multiplication overflow"); return ho_number(n); }
static void divisor(HValue a,HValue b) { if(!b.as.number) ho_fail("division by zero"); if(a.as.number==INT64_MIN && b.as.number==-1) ho_fail("integer division overflow"); }
HValue ho_divide(HValue a,HValue b) { divisor(a,b); return ho_number(a.as.number/b.as.number); }
HValue ho_remainder(HValue a,HValue b) { divisor(a,b); return ho_number(a.as.number%b.as.number); }
HValue ho_negate(HValue a) { if(a.as.number==INT64_MIN) ho_fail("integer negation overflow"); return ho_number(-a.as.number); }
HValue ho_equal(HValue a,HValue b) { return ho_boolean(a.type==H_TEXT ? !strcmp(a.as.object->as.text,b.as.object->as.text) : a.as.number==b.as.number); }
HValue ho_less(HValue a,HValue b) { return ho_boolean(a.as.number<b.as.number); }
HValue ho_not(HValue a) { return ho_boolean(!a.as.number); }
HValue ho_array(size_t count,HValue *values) { HValue v=object(H_LIST); HObject *o=v.as.object; o->as.list.len=count; o->as.list.cap=count ? count : 4; o->as.list.data=ho_alloc(o->as.list.cap*sizeof(int64_t)); for(size_t i=0;i<count;i++) o->as.list.data[i]=values[i].as.number; return v; }
static size_t index_of(HValue list,HValue index) { if(index.as.number<0 || (uint64_t)index.as.number>=list.as.object->as.list.len) ho_fail("list index out of bounds"); return (size_t)index.as.number; }
HValue ho_get(HValue list,HValue index) { size_t i=index_of(list,index); return ho_number(list.as.object->as.list.data[i]); }
HValue ho_put(HValue list,HValue index,HValue a) { size_t i=index_of(list,index); list.as.object->as.list.data[i]=a.as.number; return ho_void(); }
HValue ho_push(HValue list,HValue a) { HObject *o=list.as.object; if(o->as.list.len==o->as.list.cap) { if(o->as.list.cap>SIZE_MAX/(2*sizeof(int64_t))) ho_fail("list too large"); o->as.list.cap*=2; o->as.list.data=resize(o->as.list.data,o->as.list.cap*sizeof(int64_t)); } o->as.list.data[o->as.list.len++]=a.as.number; return ho_void(); }
HValue ho_length(HValue a) {
    if(a.type==H_LIST) return ho_number((int64_t)a.as.object->as.list.len);
    int64_t count=0; const unsigned char *p=(unsigned char *)a.as.object->as.text;
    while(*p) { if((*p & 0xc0)!=0x80) count++; p++; }
    return ho_number(count);
}
HValue ho_concat(HValue a,HValue b) { size_t x=strlen(a.as.object->as.text),y=strlen(b.as.object->as.text); if(x>SIZE_MAX-y-1) ho_fail("string too large"); HValue v=object(H_TEXT); char *s=ho_alloc(x+y+1); memcpy(s,a.as.object->as.text,x); memcpy(s+x,b.as.object->as.text,y+1); v.as.object->as.text=s; return v; }
HValue ho_decimal(HValue a) { char s[32]; snprintf(s,sizeof(s),"%" PRId64,a.as.number); return ho_text(s); }
HValue ho_parse_number(HValue a) { const char *s=a.as.object->as.text; char *end; errno=0; int64_t n=strtoll(s,&end,10); if(errno || end==s || *end) ho_fail("invalid decimal integer"); return ho_number(n); }
/* Validate external text so source and filesystem strings share the UTF-8 invariant. */
static int utf8(const unsigned char *s,size_t n) {
    size_t i=0;
    while(i<n) { unsigned c=s[i++], cp; size_t extra;
        if(c==0) return 0;
        if(c<128) continue;
        if(c>=0xc2 && c<=0xdf) { cp=c&31; extra=1; }
        else if(c>=0xe0 && c<=0xef) { cp=c&15; extra=2; }
        else if(c>=0xf0 && c<=0xf4) { cp=c&7; extra=3; }
        else return 0;
        size_t width=extra;
        if(extra>n-i) return 0;
        while(extra--) { unsigned d=s[i++]; if((d&0xc0)!=0x80) return 0; cp=(cp<<6)|(d&63); }
        if((width==1 && cp<128)||(width==2 && cp<2048)||(width==3 && cp<65536)||cp>0x10ffff||(cp>=0xd800 && cp<=0xdfff)) return 0;
    }
    return 1;
}
HValue ho_read(HValue path) {
    FILE *f=fopen(path.as.object->as.text,"rb"); if(!f) ho_fail("cannot open file for reading");
    size_t cap=4096,len=0; char *s=ho_alloc(cap);
    for(;;) { if(len==cap-1) { if(cap>SIZE_MAX/2) ho_fail("file too large"); cap*=2; s=resize(s,cap); }
        size_t got=fread(s+len,1,cap-1-len,f); len+=got;
        if(!got) { if(ferror(f)) ho_fail("file read failed"); break; }
    }
    fclose(f); s[len]=0; if(!utf8((unsigned char*)s,len)) ho_fail("file must contain UTF-8 text without NUL bytes");
    HValue v=object(H_TEXT); v.as.object->as.text=s; return v;
}
HValue ho_write(HValue path,HValue content) { FILE *f=fopen(path.as.object->as.text,"wb"); if(!f) ho_fail("cannot open file for writing"); const char *s=content.as.object->as.text; size_t n=strlen(s); int ok=fwrite(s,1,n,f)==n; if(fclose(f)!=0) ok=0; if(!ok) ho_fail("file write failed"); return ho_void(); }
HValue ho_exists(HValue path) { struct stat st; return ho_boolean(stat(path.as.object->as.text,&st)==0); }
HValue ho_argument(HValue index) { if(index.as.number<0 || index.as.number>=hargc-1) ho_fail("argument index out of bounds"); const char *s=hargv[index.as.number+1]; if(!utf8((const unsigned char*)s,strlen(s))) ho_fail("argument is not UTF-8"); return ho_text(s); }
HValue ho_argument_count(void) { return ho_number(hargc-1); }
void ho_print(HValue a) { if(a.type==H_TEXT) puts(a.as.object->as.text); else if(a.type==H_BOOLEAN) puts(a.as.number ? "true" : "false"); else printf("%" PRId64 "\n",a.as.number); }

HValue ho_home(void) { const char *s=getenv("HOME"); if(!s || !*s || !utf8((const unsigned char*)s,strlen(s))) ho_fail("HOME must contain a valid UTF-8 path"); return ho_text(s); }
