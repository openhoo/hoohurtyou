#import <Cocoa/Cocoa.h>
#include "hoo_runtime.h"

@interface HooWindow : NSWindow <NSWindowDelegate>
@property CGFloat nextY;
@property BOOL hooClosed;
@end
@implementation HooWindow
- (BOOL)windowShouldClose:(NSWindow *)sender {
    (void)sender;
    NSUInteger remaining=0;
    for(NSWindow *w in NSApp.windows) if(w!=self && [w isKindOfClass:[HooWindow class]] && !((HooWindow*)w).hooClosed) remaining++;
    if(!remaining) [NSApp terminate:nil];
    return YES;
}
- (void)windowWillClose:(NSNotification *)notification { (void)notification; self.hooClosed=YES; }
@end
@interface HooAction : NSObject
@property HCallback callback;
- (void)invoke:(id)sender;
@end
@implementation HooAction
- (void)invoke:(id)sender { (void)sender; self.callback(); ho_collect(); }
@end
static NSMutableArray *keepAlive;
static NSString *string(HValue v) {
    NSString *s=[NSString stringWithUTF8String:v.as.object->as.text];
    if(!s) ho_fail("invalid UTF-8 text"); return s;
}
static id native(HValue w) {
    id n=(__bridge id)w.as.object->as.widget.native;
    HooWindow *owner=w.as.object->as.widget.kind==0 ? n : [(NSView*)n window];
    if(owner.hooClosed) ho_fail("widget belongs to a closed window");
    return n;
}
static HooWindow *window(HValue w) {
    if(w.as.object->as.widget.kind!=0) ho_fail("control parent must be a window");
    return native(w);
}
static NSRect row(HooWindow *w,CGFloat height) {
    w.nextY-=height+12;
    if(w.nextY<12) ho_fail("window is too short for its controls");
    return NSMakeRect(20,w.nextY,w.contentView.bounds.size.width-40,height);
}
HValue ho_window(HValue title,HValue width,HValue height) {
    if(width.as.number<160 || height.as.number<100 || width.as.number>10000 || height.as.number>10000) ho_fail("window dimensions must be 160..10000 by 100..10000");
    [NSApplication sharedApplication]; [NSApp setActivationPolicy:NSApplicationActivationPolicyRegular];
    if(!keepAlive) {
        keepAlive=[NSMutableArray new];
        NSMenu *bar=[NSMenu new]; NSMenuItem *appItem=[NSMenuItem new]; [bar addItem:appItem];
        NSMenu *appMenu=[NSMenu new]; [appMenu addItemWithTitle:@"Quit Hoo" action:@selector(terminate:) keyEquivalent:@"q"]; appItem.submenu=appMenu;
        NSMenuItem *editItem=[NSMenuItem new]; editItem.title=@"Edit"; [bar addItem:editItem]; NSMenu *edit=[NSMenu new];
        [edit addItemWithTitle:@"Undo" action:@selector(undo:) keyEquivalent:@"z"];
        [edit addItemWithTitle:@"Cut" action:@selector(cut:) keyEquivalent:@"x"];
        [edit addItemWithTitle:@"Copy" action:@selector(copy:) keyEquivalent:@"c"];
        [edit addItemWithTitle:@"Paste" action:@selector(paste:) keyEquivalent:@"v"];
        [edit addItemWithTitle:@"Select All" action:@selector(selectAll:) keyEquivalent:@"a"];
        editItem.submenu=edit; NSApp.mainMenu=bar;
    }
    HooWindow *w=[[HooWindow alloc] initWithContentRect:NSMakeRect(0,0,width.as.number,height.as.number)
        styleMask:NSWindowStyleMaskTitled|NSWindowStyleMaskClosable|NSWindowStyleMaskMiniaturizable|NSWindowStyleMaskResizable backing:NSBackingStoreBuffered defer:NO];
    w.title=string(title); w.nextY=height.as.number-8; w.releasedWhenClosed=NO; w.delegate=w;
    [w center]; [w makeKeyAndOrderFront:nil]; [keepAlive addObject:w];
    return ho_widget((__bridge void*)w,0);
}
HValue ho_label(HValue parent,HValue text) {
    HooWindow *w=window(parent); NSTextField *v=[NSTextField labelWithString:string(text)];
    v.frame=row(w,28); v.autoresizingMask=NSViewWidthSizable|NSViewMinYMargin;
    v.accessibilityLabel=string(text); [w.contentView addSubview:v];
    return ho_widget((__bridge void*)v,1);
}
HValue ho_input(HValue parent,HValue text) {
    HooWindow *w=window(parent); NSTextField *v=[[NSTextField alloc] initWithFrame:row(w,28)];
    v.stringValue=string(text); v.accessibilityLabel=@"Hoo text input";
    v.autoresizingMask=NSViewWidthSizable|NSViewMinYMargin; [w.contentView addSubview:v];
    return ho_widget((__bridge void*)v,2);
}
HValue ho_button(HValue parent,HValue text,HValue callback) {
    HooWindow *w=window(parent); HooAction *action=[HooAction new]; action.callback=callback.as.callback;
    [keepAlive addObject:action]; NSButton *v=[NSButton buttonWithTitle:string(text) target:action action:@selector(invoke:)];
    v.frame=row(w,32); v.autoresizingMask=NSViewWidthSizable|NSViewMinYMargin;
    [w.contentView addSubview:v]; return ho_widget((__bridge void*)v,3);
}
HValue ho_text_get(HValue widget) {
    id v=native(widget); int kind=widget.as.object->as.widget.kind;
    if(kind==0 || kind==3) return ho_text([[v title] UTF8String]);
    if(kind==4) return ho_text([[(NSTextView*)v string] UTF8String]);
    return ho_text([[v stringValue] UTF8String]);
}
HValue ho_text_set(HValue widget,HValue text) {
    id v=native(widget); int kind=widget.as.object->as.widget.kind;
    if(kind==0 || kind==3) [v setTitle:string(text)];
    else if(kind==4) [(NSTextView*)v setString:string(text)];
    else [v setStringValue:string(text)];
    return ho_void();
}
HValue ho_run(void) {
    [NSApp activateIgnoringOtherApps:YES]; [NSApp run]; return ho_void();
}
HValue ho_quit(void) { [NSApp terminate:nil]; return ho_void(); }

HValue ho_textarea(HValue parent,HValue text) {
    HooWindow *w=window(parent); NSScrollView *scroll=[NSTextView scrollableDocumentContentTextView];
    scroll.frame=row(w,140); scroll.autoresizingMask=NSViewWidthSizable|NSViewMinYMargin;
    NSTextView *view=(NSTextView*)scroll.documentView;
    view.richText=NO; view.usesInspectorBar=NO; view.usesRuler=NO; view.importsGraphics=NO; view.allowsUndo=YES; view.string=string(text); view.font=[NSFont systemFontOfSize:14]; view.textColor=[NSColor textColor]; view.backgroundColor=[NSColor textBackgroundColor];
    view.accessibilityLabel=@"Hoo document editor";
    [w.contentView addSubview:scroll]; return ho_widget((__bridge void*)view,4);
}
HValue ho_alert(HValue parent,HValue text) {
    (void)window(parent); NSAlert *alert=[NSAlert new]; alert.messageText=@"Hoo"; alert.informativeText=string(text);
    [alert runModal]; return ho_void();
}
HValue ho_open_file(HValue parent) {
    (void)window(parent); NSOpenPanel *panel=[NSOpenPanel openPanel]; panel.canChooseDirectories=NO; panel.allowsMultipleSelection=NO;
    return [panel runModal]==NSModalResponseOK ? ho_text(panel.URL.path.UTF8String) : ho_text("");
}
HValue ho_save_file(HValue parent) {
    (void)window(parent); NSSavePanel *panel=[NSSavePanel savePanel]; panel.nameFieldStringValue=@"hoo-note.txt";
    return [panel runModal]==NSModalResponseOK ? ho_text(panel.URL.path.UTF8String) : ho_text("");
}
HValue ho_place(HValue widget,HValue x,HValue y,HValue width,HValue height) {
    if(widget.as.object->as.widget.kind==0) ho_fail("place requires a control");
    if(x.as.number<0 || y.as.number<0 || width.as.number<1 || height.as.number<1 || x.as.number>10000 || y.as.number>10000 || width.as.number>10000 || height.as.number>10000) ho_fail("invalid control geometry");
    NSView *v=native(widget); if(widget.as.object->as.widget.kind==4) v=[(NSTextView*)v enclosingScrollView];
    v.frame=NSMakeRect(x.as.number,v.superview.bounds.size.height-y.as.number-height.as.number,width.as.number,height.as.number);
    return ho_void();
}
HValue ho_enabled(HValue widget,HValue enabled) {
    id v=native(widget);
    if(widget.as.object->as.widget.kind==0) ho_fail("enabled requires a control");
    if(widget.as.object->as.widget.kind==4) [(NSTextView*)v setEditable:enabled.as.number];
    else [(NSControl*)v setEnabled:enabled.as.number];
    return ho_void();
}
void ho_ui_shutdown(void) { for(id obj in keepAlive) if([obj isKindOfClass:[NSWindow class]]) [obj close]; keepAlive=nil; }
