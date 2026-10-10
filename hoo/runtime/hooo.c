#include <gtk/gtk.h>
#include "hoo.h"
static int ready,windows;
static GPtrArray *retained;
static void hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(void) {
    if(!ready) { if(!gtk_init_check(NULL,NULL)) hoooooo("cannot connect to desktop display"); ready=1; retained=g_ptr_array_new_with_free_func(g_object_unref); }
}
static void hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(GtkWidget *widget,gpointer data) { (void)data; g_object_set_data(G_OBJECT(widget),"hoo-closed",GINT_TO_POINTER(1)); }
static void hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(GtkWidget *widget) { g_object_ref_sink(widget); g_ptr_array_add(retained,widget); g_signal_connect(widget,"destroy",G_CALLBACK(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo),NULL); }
static void hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(GtkWidget *widget,gpointer data) { (void)widget;(void)data; if(--windows==0 && gtk_main_level()) gtk_main_quit(); }
static void hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(GtkWidget *widget,gpointer data) { (void)widget; hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *fn=data; (*fn)(); hooooooooooo(); }
static void hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(gpointer data,GClosure *closure) { (void)closure; free(data); }
static GtkWidget *hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo w) { GtkWidget *v=w.as.object->as.widget.native; if(g_object_get_data(G_OBJECT(v),"hoo-closed")) hoooooo("widget belongs to a closed window"); return v; }
static GtkWidget *hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo w) { if(w.as.object->as.widget.kind!=0) hoooooo("control parent must be a window"); return g_object_get_data(G_OBJECT(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(w)),"hoo-fixed"); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo title,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo width,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo height) {
    if(width.as.number<160 || height.as.number<100 || width.as.number>10000 || height.as.number>10000) hoooooo("invalid window dimensions");
    hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(); GtkWidget *w=gtk_window_new(GTK_WINDOW_TOPLEVEL); hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(w);
    gtk_window_set_title(GTK_WINDOW(w),title.as.object->as.text); gtk_window_set_default_size(GTK_WINDOW(w),width.as.number,height.as.number);
    GtkWidget *fixed=gtk_fixed_new(); gtk_container_add(GTK_CONTAINER(w),fixed);
    g_object_set_data(G_OBJECT(w),"hoo-fixed",fixed); g_object_set_data(G_OBJECT(fixed),"hoo-width",GINT_TO_POINTER((int)width.as.number));
    g_object_set_data(G_OBJECT(fixed),"hoo-next",GINT_TO_POINTER(20));
    g_signal_connect(w,"destroy",G_CALLBACK(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo),NULL); windows++; return hoooooooooooooooooo(w,0);
}
static hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo window,GtkWidget *v,int kind,int height) {
    GtkWidget *fixed=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(window); int y=GPOINTER_TO_INT(g_object_get_data(G_OBJECT(fixed),"hoo-next"));
    int width=GPOINTER_TO_INT(g_object_get_data(G_OBJECT(fixed),"hoo-width"));
    hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(v); gtk_widget_set_size_request(v,width-40,height); gtk_fixed_put(GTK_FIXED(fixed),v,20,y);
    g_object_set_data(G_OBJECT(fixed),"hoo-next",GINT_TO_POINTER(y+height+12)); return hoooooooooooooooooo(v,kind);
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo window,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text) { GtkWidget *v=gtk_label_new(text.as.object->as.text); gtk_label_set_xalign(GTK_LABEL(v),0); return hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(window,v,1,28); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo window,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text) { GtkWidget *v=gtk_entry_new(); gtk_entry_set_text(GTK_ENTRY(v),text.as.object->as.text); return hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(window,v,2,28); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo window,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo callback) { GtkWidget *v=gtk_button_new_with_label(text.as.object->as.text); hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *fn=hooooooo(sizeof(*fn)); *fn=callback.as.callback; g_signal_connect_data(v,"clicked",G_CALLBACK(hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo),fn,destroy_callback,0); return hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(window,v,3,32); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo window,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text) {
    GtkWidget *scroll=gtk_scrolled_window_new(NULL,NULL),*view=gtk_text_view_new();
    gtk_text_view_set_wrap_mode(GTK_TEXT_VIEW(view),GTK_WRAP_WORD_CHAR);
    gtk_text_buffer_set_text(gtk_text_view_get_buffer(GTK_TEXT_VIEW(view)),text.as.object->as.text,-1);
    gtk_container_add(GTK_CONTAINER(scroll),view); g_object_set_data(G_OBJECT(scroll),"hoo-textview",view);
    return hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(window,scroll,4,140);
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo widget) {
    GtkWidget *v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(widget); const char *s;
    switch(widget.as.object->as.widget.kind) {
        case 0:s=gtk_window_get_title(GTK_WINDOW(v));break; case 1:s=gtk_label_get_text(GTK_LABEL(v));break;
        case 2:s=gtk_entry_get_text(GTK_ENTRY(v));break; case 3:s=gtk_button_get_label(GTK_BUTTON(v));break;
        default: { GtkTextBuffer *buffer=gtk_text_view_get_buffer(g_object_get_data(G_OBJECT(v),"hoo-textview"));
            GtkTextIter start,end; gtk_text_buffer_get_bounds(buffer,&start,&end); char *content=gtk_text_buffer_get_text(buffer,&start,&end,FALSE);
            hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo value=hooooooooooooooooo(content); g_free(content); return value;
        }
    }
    return hooooooooooooooooo(s ? s : "");
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo widget,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text) {
    GtkWidget *v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(widget); const char *s=text.as.object->as.text;
    switch(widget.as.object->as.widget.kind) {
        case 0:gtk_window_set_title(GTK_WINDOW(v),s);break; case 1:gtk_label_set_text(GTK_LABEL(v),s);break;
        case 2:gtk_entry_set_text(GTK_ENTRY(v),s);break; case 3:gtk_button_set_label(GTK_BUTTON(v),s);break;
        default:gtk_text_buffer_set_text(gtk_text_view_get_buffer(g_object_get_data(G_OBJECT(v),"hoo-textview")),s,-1);
    }
    return hooooooooooooo();
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo window,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text) {
    (void)hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(window); GtkWidget *dialog=gtk_message_dialog_new(GTK_WINDOW(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(window)),GTK_DIALOG_MODAL,GTK_MESSAGE_INFO,GTK_BUTTONS_OK,"%s",text.as.object->as.text);
    gtk_dialog_run(GTK_DIALOG(dialog)); gtk_widget_destroy(dialog); return hooooooooooooo();
}
static hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo window,int save) {
    (void)hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(window); GtkWidget *dialog=gtk_file_chooser_dialog_new(save ? "Save Hoo File" : "Open Hoo File",GTK_WINDOW(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(window)),save ? GTK_FILE_CHOOSER_ACTION_SAVE : GTK_FILE_CHOOSER_ACTION_OPEN,"Cancel",GTK_RESPONSE_CANCEL,save ? "Save" : "Open",GTK_RESPONSE_ACCEPT,NULL);
    if(save) gtk_file_chooser_set_do_overwrite_confirmation(GTK_FILE_CHOOSER(dialog),TRUE);
    hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo result;
    if(gtk_dialog_run(GTK_DIALOG(dialog))==GTK_RESPONSE_ACCEPT) { char *path=gtk_file_chooser_get_filename(GTK_FILE_CHOOSER(dialog)); result=hooooooooooooooooo(path); g_free(path); }
    else result=hooooooooooooooooo("");
    gtk_widget_destroy(dialog); return result;
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo window) { return hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(window,0); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo window) { return hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(window,1); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo widget,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo x,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo y,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo width,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo height) {
    if(widget.as.object->as.widget.kind==0) hoooooo("place requires a control");
    if(x.as.number<0 || y.as.number<0 || width.as.number<1 || height.as.number<1 || x.as.number>10000 || y.as.number>10000 || width.as.number>10000 || height.as.number>10000) hoooooo("invalid control geometry");
    GtkWidget *v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(widget); gtk_fixed_move(GTK_FIXED(gtk_widget_get_parent(v)),v,x.as.number,y.as.number); gtk_widget_set_size_request(v,width.as.number,height.as.number); return hooooooooooooo();
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo widget,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo enabled) { if(widget.as.object->as.widget.kind==0) hoooooo("enabled requires a control"); gtk_widget_set_sensitive(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(widget),enabled.as.number); return hooooooooooooo(); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooooooooooo(void) { hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(); GList *list=gtk_window_list_toplevels(); for(GList *p=list;p;p=p->next) gtk_widget_show_all(p->data); g_list_free(list); gtk_main(); return hooooooooooooo(); }
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooooooooooo(void) { if(gtk_main_level()) gtk_main_quit(); return hooooooooooooo(); }
void hoooo(void) { if(retained) { for(guint i=0;i<retained->len;i++) { GtkWidget *v=g_ptr_array_index(retained,i); if(!g_object_get_data(G_OBJECT(v),"hoo-closed")) gtk_widget_destroy(v); } g_ptr_array_free(retained,TRUE); retained=NULL; } }
