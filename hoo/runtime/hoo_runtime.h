#ifndef HOO_RUNTIME_H
#define HOO_RUNTIME_H
#include <stdint.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>
#include <limits.h>
#include <errno.h>
#include <sys/stat.h>

typedef struct HObject HObject;
typedef struct HValue HValue;
typedef HValue (*HCallback)(void);
enum { H_VOID, H_NUMBER, H_BOOLEAN, H_TEXT, H_LIST, H_WIDGET, H_CALLBACK };
struct HValue { int type; union { int64_t number; HObject *object; HCallback callback; } as; };
struct HObject {
    HObject *next; int marked, type;
    union { char *text; struct { int64_t *data; size_t len, cap; } list;
            struct { void *native; int kind; } widget; } as;
};
void ho_init(int argc, char **argv);
void ho_shutdown(void);
void ho_ui_shutdown(void);
void ho_location(int line, int column);
_Noreturn void ho_fail(const char *message);
void *ho_alloc(size_t bytes);
void ho_root(HValue *value);
size_t ho_frame(void);
void ho_restore(size_t frame);
void ho_collect(void);
HValue ho_load(HValue v);
HValue ho_void(void);
HValue ho_number(int64_t n);
HValue ho_boolean(int b);
HValue ho_callback(HCallback fn);
HValue ho_text(const char *s);
HValue ho_widget(void *native, int kind);
HValue ho_array(size_t count, HValue *values);
HValue ho_add(HValue a,HValue b);
HValue ho_subtract(HValue a,HValue b);
HValue ho_multiply(HValue a,HValue b);
HValue ho_divide(HValue a,HValue b);
HValue ho_remainder(HValue a,HValue b);
HValue ho_negate(HValue a);
HValue ho_equal(HValue a,HValue b);
HValue ho_less(HValue a,HValue b);
HValue ho_not(HValue a);
HValue ho_get(HValue list,HValue index);
HValue ho_length(HValue a);
HValue ho_push(HValue list,HValue a);
HValue ho_put(HValue list,HValue index,HValue a);
HValue ho_concat(HValue a,HValue b);
HValue ho_decimal(HValue a);
HValue ho_parse_number(HValue a);
HValue ho_read(HValue path);
HValue ho_write(HValue path,HValue content);
HValue ho_exists(HValue path);
HValue ho_argument(HValue index);
HValue ho_argument_count(void);
HValue ho_home(void);
void ho_print(HValue a);
HValue ho_window(HValue title,HValue width,HValue height);
HValue ho_label(HValue window,HValue text);
HValue ho_input(HValue window,HValue text);
HValue ho_button(HValue window,HValue text,HValue callback);
HValue ho_text_get(HValue widget);
HValue ho_text_set(HValue widget,HValue text);
HValue ho_textarea(HValue window,HValue text);
HValue ho_alert(HValue window,HValue text);
HValue ho_open_file(HValue window);
HValue ho_save_file(HValue window);
HValue ho_place(HValue widget,HValue x,HValue y,HValue width,HValue height);
HValue ho_enabled(HValue widget,HValue enabled);
HValue ho_run(void);
HValue ho_quit(void);
#endif
