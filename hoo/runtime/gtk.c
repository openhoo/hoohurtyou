#include <gtk/gtk.h>
#include "hoo_runtime.h"
static int ready,windows;
static GPtrArray *retained;
static void initialize(void) {
    if(!ready) { if(!gtk_init_check(NULL,NULL)) ho_fail("cannot connect to desktop display"); ready=1; retained=g_ptr_array_new_with_free_func(g_object_unref); }
}
static void dead(GtkWidget *widget,gpointer data) { (void)data; g_object_set_data(G_OBJECT(widget),"hoo-closed",GINT_TO_POINTER(1)); }
static void retain(GtkWidget *widget) { g_object_ref_sink(widget); g_ptr_array_add(retained,widget); g_signal_connect(widget,"destroy",G_CALLBACK(dead),NULL); }
static void closed(GtkWidget *widget,gpointer data) { (void)widget;(void)data; if(--windows==0 && gtk_main_level()) gtk_main_quit(); }
static void invoke(GtkWidget *widget,gpointer data) { (void)widget; HCallback *fn=data; (*fn)(); ho_collect(); }
static void destroy_callback(gpointer data,GClosure *closure) { (void)closure; free(data); }
static GtkWidget *native(HValue w) { GtkWidget *v=w.as.object->as.widget.native; if(g_object_get_data(G_OBJECT(v),"hoo-closed")) ho_fail("widget belongs to a closed window"); return v; }
static GtkWidget *parent(HValue w) { if(w.as.object->as.widget.kind!=0) ho_fail("control parent must be a window"); return g_object_get_data(G_OBJECT(native(w)),"hoo-fixed"); }
HValue ho_window(HValue title,HValue width,HValue height) {
    if(width.as.number<160 || height.as.number<100 || width.as.number>10000 || height.as.number>10000) ho_fail("invalid window dimensions");
    initialize(); GtkWidget *w=gtk_window_new(GTK_WINDOW_TOPLEVEL); retain(w);
    gtk_window_set_title(GTK_WINDOW(w),title.as.object->as.text); gtk_window_set_default_size(GTK_WINDOW(w),width.as.number,height.as.number);
    GtkWidget *fixed=gtk_fixed_new(); gtk_container_add(GTK_CONTAINER(w),fixed);
    g_object_set_data(G_OBJECT(w),"hoo-fixed",fixed); g_object_set_data(G_OBJECT(fixed),"hoo-width",GINT_TO_POINTER((int)width.as.number));
    g_object_set_data(G_OBJECT(fixed),"hoo-next",GINT_TO_POINTER(20));
    g_signal_connect(w,"destroy",G_CALLBACK(closed),NULL); windows++; return ho_widget(w,0);
}
static HValue control(HValue window,GtkWidget *v,int kind,int height) {
    GtkWidget *fixed=parent(window); int y=GPOINTER_TO_INT(g_object_get_data(G_OBJECT(fixed),"hoo-next"));
    int width=GPOINTER_TO_INT(g_object_get_data(G_OBJECT(fixed),"hoo-width"));
    retain(v); gtk_widget_set_size_request(v,width-40,height); gtk_fixed_put(GTK_FIXED(fixed),v,20,y);
    g_object_set_data(G_OBJECT(fixed),"hoo-next",GINT_TO_POINTER(y+height+12)); return ho_widget(v,kind);
}
HValue ho_label(HValue window,HValue text) { GtkWidget *v=gtk_label_new(text.as.object->as.text); gtk_label_set_xalign(GTK_LABEL(v),0); return control(window,v,1,28); }
HValue ho_input(HValue window,HValue text) { GtkWidget *v=gtk_entry_new(); gtk_entry_set_text(GTK_ENTRY(v),text.as.object->as.text); return control(window,v,2,28); }
HValue ho_button(HValue window,HValue text,HValue callback) { GtkWidget *v=gtk_button_new_with_label(text.as.object->as.text); HCallback *fn=ho_alloc(sizeof(*fn)); *fn=callback.as.callback; g_signal_connect_data(v,"clicked",G_CALLBACK(invoke),fn,destroy_callback,0); return control(window,v,3,32); }
HValue ho_textarea(HValue window,HValue text) {
    GtkWidget *scroll=gtk_scrolled_window_new(NULL,NULL),*view=gtk_text_view_new();
    gtk_text_view_set_wrap_mode(GTK_TEXT_VIEW(view),GTK_WRAP_WORD_CHAR);
    gtk_text_buffer_set_text(gtk_text_view_get_buffer(GTK_TEXT_VIEW(view)),text.as.object->as.text,-1);
    gtk_container_add(GTK_CONTAINER(scroll),view); g_object_set_data(G_OBJECT(scroll),"hoo-textview",view);
    return control(window,scroll,4,140);
}
HValue ho_text_get(HValue widget) {
    GtkWidget *v=native(widget); const char *s;
    switch(widget.as.object->as.widget.kind) {
        case 0:s=gtk_window_get_title(GTK_WINDOW(v));break; case 1:s=gtk_label_get_text(GTK_LABEL(v));break;
        case 2:s=gtk_entry_get_text(GTK_ENTRY(v));break; case 3:s=gtk_button_get_label(GTK_BUTTON(v));break;
        default: { GtkTextBuffer *buffer=gtk_text_view_get_buffer(g_object_get_data(G_OBJECT(v),"hoo-textview"));
            GtkTextIter start,end; gtk_text_buffer_get_bounds(buffer,&start,&end); char *content=gtk_text_buffer_get_text(buffer,&start,&end,FALSE);
            HValue value=ho_text(content); g_free(content); return value;
        }
    }
    return ho_text(s ? s : "");
}
HValue ho_text_set(HValue widget,HValue text) {
    GtkWidget *v=native(widget); const char *s=text.as.object->as.text;
    switch(widget.as.object->as.widget.kind) {
        case 0:gtk_window_set_title(GTK_WINDOW(v),s);break; case 1:gtk_label_set_text(GTK_LABEL(v),s);break;
        case 2:gtk_entry_set_text(GTK_ENTRY(v),s);break; case 3:gtk_button_set_label(GTK_BUTTON(v),s);break;
        default:gtk_text_buffer_set_text(gtk_text_view_get_buffer(g_object_get_data(G_OBJECT(v),"hoo-textview")),s,-1);
    }
    return ho_void();
}
HValue ho_alert(HValue window,HValue text) {
    (void)parent(window); GtkWidget *dialog=gtk_message_dialog_new(GTK_WINDOW(native(window)),GTK_DIALOG_MODAL,GTK_MESSAGE_INFO,GTK_BUTTONS_OK,"%s",text.as.object->as.text);
    gtk_dialog_run(GTK_DIALOG(dialog)); gtk_widget_destroy(dialog); return ho_void();
}
static HValue choose(HValue window,int save) {
    (void)parent(window); GtkWidget *dialog=gtk_file_chooser_dialog_new(save ? "Save Hoo File" : "Open Hoo File",GTK_WINDOW(native(window)),save ? GTK_FILE_CHOOSER_ACTION_SAVE : GTK_FILE_CHOOSER_ACTION_OPEN,"Cancel",GTK_RESPONSE_CANCEL,save ? "Save" : "Open",GTK_RESPONSE_ACCEPT,NULL);
    if(save) gtk_file_chooser_set_do_overwrite_confirmation(GTK_FILE_CHOOSER(dialog),TRUE);
    HValue result;
    if(gtk_dialog_run(GTK_DIALOG(dialog))==GTK_RESPONSE_ACCEPT) { char *path=gtk_file_chooser_get_filename(GTK_FILE_CHOOSER(dialog)); result=ho_text(path); g_free(path); }
    else result=ho_text("");
    gtk_widget_destroy(dialog); return result;
}
HValue ho_open_file(HValue window) { return choose(window,0); }
HValue ho_save_file(HValue window) { return choose(window,1); }
HValue ho_place(HValue widget,HValue x,HValue y,HValue width,HValue height) {
    if(widget.as.object->as.widget.kind==0) ho_fail("place requires a control");
    if(x.as.number<0 || y.as.number<0 || width.as.number<1 || height.as.number<1 || x.as.number>10000 || y.as.number>10000 || width.as.number>10000 || height.as.number>10000) ho_fail("invalid control geometry");
    GtkWidget *v=native(widget); gtk_fixed_move(GTK_FIXED(gtk_widget_get_parent(v)),v,x.as.number,y.as.number); gtk_widget_set_size_request(v,width.as.number,height.as.number); return ho_void();
}
HValue ho_enabled(HValue widget,HValue enabled) { if(widget.as.object->as.widget.kind==0) ho_fail("enabled requires a control"); gtk_widget_set_sensitive(native(widget),enabled.as.number); return ho_void(); }
HValue ho_run(void) { initialize(); GList *list=gtk_window_list_toplevels(); for(GList *p=list;p;p=p->next) gtk_widget_show_all(p->data); g_list_free(list); gtk_main(); return ho_void(); }
HValue ho_quit(void) { if(gtk_main_level()) gtk_main_quit(); return ho_void(); }
void ho_ui_shutdown(void) { if(retained) { for(guint i=0;i<retained->len;i++) { GtkWidget *v=g_ptr_array_index(retained,i); if(!g_object_get_data(G_OBJECT(v),"hoo-closed")) gtk_widget_destroy(v); } g_ptr_array_free(retained,TRUE); retained=NULL; } }
