#include "hoo.h"
static hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *objects;
static hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo **roots;
static size_t root_count, root_cap, allocations;
static int hargc, source_line, source_column;
static char **hargv;
_Noreturn void hoooooo(const char *message) {
    fprintf(stderr,"hoo runtime %d:%d: %s\n",source_line,source_column,message);
    exit(70);
}
void hooooo(int line,int column) { source_line=line; source_column=column; }
void *hooooooo(size_t bytes) {
    void *p=calloc(1,bytes ? bytes : 1);
    if(!p) hoooooo("out of memory");
    return p;
}
static void *hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(void *p,size_t bytes) {
    void *q=realloc(p,bytes ? bytes : 1);
    if(!q) hoooooo("out of memory");
    return q;
}
static hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(int type) {
    hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *o=hooooooo(sizeof(*o)); o->type=type; o->next=objects; objects=o; allocations++;
    hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v={.type=type}; v.as.object=o; return v;
}
void hoooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *value) {
    if(root_count==root_cap) { root_cap=root_cap ? root_cap*2 : 128; roots=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(roots,root_cap*sizeof(*roots)); }
    roots[root_count++]=value;
}
size_t hooooooooo(void) { return root_count; }
void hoooooooooo(size_t frame) { if(frame>root_count) hoooooo("corrupt root frame"); root_count=frame; }
static void hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(int force) {
    if(!force && allocations<256) return;
    for(size_t i=0;i<root_count;i++) {
        hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v=*roots[i];
        if(v.type==hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo || v.type==hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo || v.type==hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo) v.as.object->marked=1;
    }
    hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo **p=&objects;
    while(*p) {
        hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *o=*p;
        if(o->marked) { o->marked=0; p=&o->next; }
        else { *p=o->next;
            if(o->type==hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo) free(o->as.text);
            if(o->type==hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo) free(o->as.list.data);
            free(o);
        }
    }
    allocations=0;
}
void hooooooooooo(void) { hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(0); }
void hoo(int argc,char **argv) { hargc=argc; hargv=argv; }
void hooo(void) { hoooo(); root_count=0; hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(1); free(roots); roots=NULL; root_cap=0; }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v) { if(v.type==hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo) hoooooo("variable used before initialization"); return v; }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooo(void) { return (hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo){.type=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo}; }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooo(int64_t n) { hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v={.type=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo}; v.as.number=n; return v; }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooo(int b) { hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v={.type=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo}; v.as.number=!!b; return v; }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooo(hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo fn) { hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v={.type=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo}; v.as.callback=fn; return v; }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooo(const char *s) { hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo); size_t len=strlen(s)+1; v.as.object->as.text=hooooooo(len); memcpy(v.as.object->as.text,s,len); return v; }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooo(void *native,int kind) { hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo); v.as.object->as.widget.native=native; v.as.object->as.widget.kind=kind; return v; }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo b) { int64_t n; if(__builtin_add_overflow(a.as.number,b.as.number,&n)) hoooooo("integer addition overflow"); return hoooooooooooooo(n); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo b) { int64_t n; if(__builtin_sub_overflow(a.as.number,b.as.number,&n)) hoooooo("integer subtraction overflow"); return hoooooooooooooo(n); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo b) { int64_t n; if(__builtin_mul_overflow(a.as.number,b.as.number,&n)) hoooooo("integer multiplication overflow"); return hoooooooooooooo(n); }
static void hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo b) { if(!b.as.number) hoooooo("division by zero"); if(a.as.number==INT64_MIN && b.as.number==-1) hoooooo("integer division overflow"); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo b) { hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(a,b); return hoooooooooooooo(a.as.number/b.as.number); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo b) { hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(a,b); return hoooooooooooooo(a.as.number%b.as.number); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a) { if(a.as.number==INT64_MIN) hoooooo("integer negation overflow"); return hoooooooooooooo(-a.as.number); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo b) { return hooooooooooooooo(a.type==hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo ? !strcmp(a.as.object->as.text,b.as.object->as.text) : a.as.number==b.as.number); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo b) { return hooooooooooooooo(a.as.number<b.as.number); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a) { return hooooooooooooooo(!a.as.number); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooo(size_t count,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *values) { hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo); hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *o=v.as.object; o->as.list.len=count; o->as.list.cap=count ? count : 4; o->as.list.data=hooooooo(o->as.list.cap*sizeof(int64_t)); for(size_t i=0;i<count;i++) o->as.list.data[i]=values[i].as.number; return v; }
static size_t hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo list,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo index) { if(index.as.number<0 || (uint64_t)index.as.number>=list.as.object->as.list.len) hoooooo("list index out of bounds"); return (size_t)index.as.number; }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo list,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo index) { size_t i=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(list,index); return hoooooooooooooo(list.as.object->as.list.data[i]); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo list,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo index,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a) { size_t i=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(list,index); list.as.object->as.list.data[i]=a.as.number; return hooooooooooooo(); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo list,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a) { hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *o=list.as.object; if(o->as.list.len==o->as.list.cap) { if(o->as.list.cap>SIZE_MAX/(2*sizeof(int64_t))) hoooooo("list too large"); o->as.list.cap*=2; o->as.list.data=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(o->as.list.data,o->as.list.cap*sizeof(int64_t)); } o->as.list.data[o->as.list.len++]=a.as.number; return hooooooooooooo(); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a) {
    if(a.type==hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo) return hoooooooooooooo((int64_t)a.as.object->as.list.len);
    int64_t count=0; const unsigned char *p=(unsigned char *)a.as.object->as.text;
    while(*p) { if((*p & 0xc0)!=0x80) count++; p++; }
    return hoooooooooooooo(count);
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo b) { size_t x=strlen(a.as.object->as.text),y=strlen(b.as.object->as.text); if(x>SIZE_MAX-y-1) hoooooo("string too large"); hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo); char *s=hooooooo(x+y+1); memcpy(s,a.as.object->as.text,x); memcpy(s+x,b.as.object->as.text,y+1); v.as.object->as.text=s; return v; }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a) { char s[32]; snprintf(s,sizeof(s),"%" PRId64,a.as.number); return hooooooooooooooooo(s); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a) { const char *s=a.as.object->as.text; char *end; errno=0; int64_t n=strtoll(s,&end,10); if(errno || end==s || *end) hoooooo("invalid decimal integer"); return hoooooooooooooo(n); }
/* Validate external text so source and filesystem strings share the UTF-8 invariant. */
static int hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(const unsigned char *s,size_t n) {
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
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo path) {
    FILE *f=fopen(path.as.object->as.text,"rb"); if(!f) hoooooo("cannot open file for reading");
    size_t cap=4096,len=0; char *s=hooooooo(cap);
    for(;;) { if(len==cap-1) { if(cap>SIZE_MAX/2) hoooooo("file too large"); cap*=2; s=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(s,cap); }
        size_t got=fread(s+len,1,cap-1-len,f); len+=got;
        if(!got) { if(ferror(f)) hoooooo("file read failed"); break; }
    }
    fclose(f); s[len]=0; if(!hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo((unsigned char*)s,len)) hoooooo("file must contain UTF-8 text without NUL bytes");
    hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo); v.as.object->as.text=s; return v;
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo path,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo content) { FILE *f=fopen(path.as.object->as.text,"wb"); if(!f) hoooooo("cannot open file for writing"); const char *s=content.as.object->as.text; size_t n=strlen(s); int ok=fwrite(s,1,n,f)==n; if(fclose(f)!=0) ok=0; if(!ok) hoooooo("file write failed"); return hooooooooooooo(); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo path) { struct stat st; return hooooooooooooooo(stat(path.as.object->as.text,&st)==0); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo index) { if(index.as.number<0 || index.as.number>=hargc-1) hoooooo("argument index out of bounds"); const char *s=hargv[index.as.number+1]; if(!hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo((const unsigned char*)s,strlen(s))) hoooooo("argument is not UTF-8"); return hooooooooooooooooo(s); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooo(void) { return hoooooooooooooo(hargc-1); }
void hoooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo a) { if(a.type==hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo) puts(a.as.object->as.text); else if(a.type==hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo) puts(a.as.number ? "true" : "false"); else printf("%" PRId64 "\n",a.as.number); }

hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooo(void) { const char *s=getenv("HOME"); if(!s || !*s || !hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo((const unsigned char*)s,strlen(s))) hoooooo("HOME must contain a valid UTF-8 path"); return hooooooooooooooooo(s); }
