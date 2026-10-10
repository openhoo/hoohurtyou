#import <Cocoa/Cocoa.h>
#include "hoo.h"

@interface hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo : NSWindow <NSWindowDelegate>
@property CGFloat nextY;
@property BOOL hooClosed;
@end
@implementation hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
- (BOOL)windowShouldClose:(NSWindow *)sender {
    (void)sender;
    NSUInteger remaining=0;
    for(NSWindow *w in NSApp.windows) if(w!=self && [w isKindOfClass:[hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo class]] && !((hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo*)w).hooClosed) remaining++;
    if(!remaining) [NSApp terminate:nil];
    return YES;
}
- (void)windowWillClose:(NSNotification *)notification { (void)notification; self.hooClosed=YES; }
@end
@interface hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo : NSObject
@property hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo callback;
- (void)hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo:(id)sender;
@end
@implementation hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
- (void)hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo:(id)sender { (void)sender; self.callback(); hooooooooooo(); }
@end
static NSMutableArray *keepAlive;
static NSString *hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo v) {
    NSString *s=[NSString stringWithUTF8String:v.as.object->as.text];
    if(!s) hoooooo("invalid UTF-8 text"); return s;
}
static id hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo w) {
    id n=(__bridge id)w.as.object->as.widget.native;
    hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *owner=w.as.object->as.widget.kind==0 ? n : [(NSView*)n window];
    if(owner.hooClosed) hoooooo("widget belongs to a closed window");
    return n;
}
static hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo w) {
    if(w.as.object->as.widget.kind!=0) hoooooo("control parent must be a window");
    return hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(w);
}
static NSRect hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *w,CGFloat height) {
    w.nextY-=height+12;
    if(w.nextY<12) hoooooo("window is too short for its controls");
    return NSMakeRect(20,w.nextY,w.contentView.bounds.size.width-40,height);
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo title,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo width,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo height) {
    if(width.as.number<160 || height.as.number<100 || width.as.number>10000 || height.as.number>10000) hoooooo("window dimensions must be 160..10000 by 100..10000");
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
    hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *w=[[hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo alloc] initWithContentRect:NSMakeRect(0,0,width.as.number,height.as.number)
        styleMask:NSWindowStyleMaskTitled|NSWindowStyleMaskClosable|NSWindowStyleMaskMiniaturizable|NSWindowStyleMaskResizable backing:NSBackingStoreBuffered defer:NO];
    w.title=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(title); w.nextY=height.as.number-8; w.releasedWhenClosed=NO; w.delegate=w;
    [w center]; [w makeKeyAndOrderFront:nil]; [keepAlive addObject:w];
    return hoooooooooooooooooo((__bridge void*)w,0);
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo parent,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text) {
    hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *w=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(parent); NSTextField *v=[NSTextField labelWithString:hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(text)];
    v.frame=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(w,28); v.autoresizingMask=NSViewWidthSizable|NSViewMinYMargin;
    v.accessibilityLabel=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(text); [w.contentView addSubview:v];
    return hoooooooooooooooooo((__bridge void*)v,1);
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo parent,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text) {
    hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *w=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(parent); NSTextField *v=[[NSTextField alloc] initWithFrame:hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(w,28)];
    v.stringValue=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(text); v.accessibilityLabel=@"Hoo text input";
    v.autoresizingMask=NSViewWidthSizable|NSViewMinYMargin; [w.contentView addSubview:v];
    return hoooooooooooooooooo((__bridge void*)v,2);
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo parent,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo callback) {
    hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *w=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(parent); hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *action=[hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo new]; action.callback=callback.as.callback;
    [keepAlive addObject:action]; NSButton *v=[NSButton buttonWithTitle:hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(text) target:action action:@selector(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo:)];
    v.frame=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(w,32); v.autoresizingMask=NSViewWidthSizable|NSViewMinYMargin;
    [w.contentView addSubview:v]; return hoooooooooooooooooo((__bridge void*)v,3);
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo widget) {
    id v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(widget); int kind=widget.as.object->as.widget.kind;
    if(kind==0 || kind==3) return hooooooooooooooooo([[v title] UTF8String]);
    if(kind==4) return hooooooooooooooooo([[(NSTextView*)v string] UTF8String]);
    return hooooooooooooooooo([[v stringValue] UTF8String]);
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo widget,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text) {
    id v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(widget); int kind=widget.as.object->as.widget.kind;
    if(kind==0 || kind==3) [v setTitle:hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(text)];
    else if(kind==4) [(NSTextView*)v setString:hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(text)];
    else [v setStringValue:hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(text)];
    return hooooooooooooo();
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooooooooooo(void) {
    [NSApp activateIgnoringOtherApps:YES]; [NSApp run]; return hooooooooooooo();
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooooooooooo(void) { [NSApp terminate:nil]; return hooooooooooooo(); }

hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo parent,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text) {
    hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo *w=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(parent); NSScrollView *scroll=[NSTextView scrollableDocumentContentTextView];
    scroll.frame=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(w,140); scroll.autoresizingMask=NSViewWidthSizable|NSViewMinYMargin;
    NSTextView *view=(NSTextView*)scroll.documentView;
    view.richText=NO; view.usesInspectorBar=NO; view.usesRuler=NO; view.importsGraphics=NO; view.allowsUndo=YES; view.string=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(text); view.font=[NSFont systemFontOfSize:14]; view.textColor=[NSColor textColor]; view.backgroundColor=[NSColor textBackgroundColor];
    view.accessibilityLabel=@"Hoo document editor";
    [w.contentView addSubview:scroll]; return hoooooooooooooooooo((__bridge void*)view,4);
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo parent,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo text) {
    (void)hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(parent); NSAlert *alert=[NSAlert new]; alert.messageText=@"Hoo"; alert.informativeText=hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(text);
    [alert runModal]; return hooooooooooooo();
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo parent) {
    (void)hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(parent); NSOpenPanel *panel=[NSOpenPanel openPanel]; panel.canChooseDirectories=NO; panel.allowsMultipleSelection=NO;
    return [panel runModal]==NSModalResponseOK ? hooooooooooooooooo(panel.URL.path.UTF8String) : hooooooooooooooooo("");
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo parent) {
    (void)hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(parent); NSSavePanel *panel=[NSSavePanel savePanel]; panel.nameFieldStringValue=@"hoo-note.txt";
    return [panel runModal]==NSModalResponseOK ? hooooooooooooooooo(panel.URL.path.UTF8String) : hooooooooooooooooo("");
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo widget,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo x,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo y,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo width,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo height) {
    if(widget.as.object->as.widget.kind==0) hoooooo("place requires a control");
    if(x.as.number<0 || y.as.number<0 || width.as.number<1 || height.as.number<1 || x.as.number>10000 || y.as.number>10000 || width.as.number>10000 || height.as.number>10000) hoooooo("invalid control geometry");
    NSView *v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(widget); if(widget.as.object->as.widget.kind==4) v=[(NSTextView*)v enclosingScrollView];
    v.frame=NSMakeRect(x.as.number,v.superview.bounds.size.height-y.as.number-height.as.number,width.as.number,height.as.number);
    return hooooooooooooo();
}
hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoooooooooooooooooooooooooooooooooooooooooooooooooooooo(hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo widget,hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo enabled) {
    id v=hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(widget);
    if(widget.as.object->as.widget.kind==0) hoooooo("enabled requires a control");
    if(widget.as.object->as.widget.kind==4) [(NSTextView*)v setEditable:enabled.as.number];
    else [(NSControl*)v setEnabled:enabled.as.number];
    return hooooooooooooo();
}
void hoooo(void) { for(id obj in keepAlive) if([obj isKindOfClass:[NSWindow class]]) [obj close]; keepAlive=nil; }
