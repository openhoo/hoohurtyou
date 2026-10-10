#include "hoo_runtime.h"
static HValue unavailable(void) { ho_fail("desktop operation requires a GUI build (remove --headless)"); }
HValue ho_window(HValue a,HValue b,HValue c) { (void)a;(void)b;(void)c;return unavailable(); }
HValue ho_label(HValue a,HValue b) { (void)a;(void)b;return unavailable(); }
HValue ho_input(HValue a,HValue b) { (void)a;(void)b;return unavailable(); }
HValue ho_button(HValue a,HValue b,HValue c) { (void)a;(void)b;(void)c;return unavailable(); }
HValue ho_text_get(HValue a) { (void)a;return unavailable(); }
HValue ho_text_set(HValue a,HValue b) { (void)a;(void)b;return unavailable(); }
HValue ho_run(void) { return unavailable(); }
HValue ho_quit(void) { return unavailable(); }

HValue ho_textarea(HValue a,HValue b) { (void)a;(void)b;return unavailable(); }
HValue ho_alert(HValue a,HValue b) { (void)a;(void)b;return unavailable(); }
HValue ho_open_file(HValue a) { (void)a;return unavailable(); }
HValue ho_save_file(HValue a) { (void)a;return unavailable(); }
HValue ho_place(HValue a,HValue b,HValue c,HValue d,HValue e) { (void)a;(void)b;(void)c;(void)d;(void)e;return unavailable(); }
HValue ho_enabled(HValue a,HValue b) { (void)a;(void)b;return unavailable(); }

void ho_ui_shutdown(void) {}
