#!/usr/bin/env python3
"""Reproducible construction of the checked-in, exclusively hoo-word examples."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from hoo.encoding import *

ROOT=Path(__file__).resolve().parents[1]/'examples'
def save(name,source): (ROOT/name).write_text(source)
E=expression
save('hello.hoo',program(E('print',text('Hoo, world! 🦉'))))
factorial=function(0,'number',[(0,'number')],if_(E('less',ref(0),integer(2)),return_(integer(1)),return_(E('multiply',ref(0),call(0,E('subtract',ref(0),integer(1)))))))
save('factorial.hoo',program(factorial,E('print',call(0,integer(10)))))
save('lists.hoo',program(let(0,'list',array(integer(2),integer(3),integer(5))),let(1,'number',integer(0)),E('do',E('push',ref(0),integer(7))),while_(E('less',ref(1),E('length',ref(0))),program(E('print',E('get',ref(0),ref(1))),set_(1,E('add',ref(1),integer(1)))))))
# Counter with native labels, editable name, mutable state and two callbacks.
inc=function(0,'void',[],program(set_(0,E('add',ref(0),integer(1))),E('do',E('text_set',ref(2),E('concat',E('concat',E('text_get',ref(3)),text(' says hoo: ')),E('decimal',ref(0)))))))
reset=function(1,'void',[],program(set_(0,integer(0)),E('do',E('text_set',ref(2),text('Count reset. Hoo again.')))))
save('counter.hoo',program(inc,reset,let(0,'number',integer(0)),let(1,'widget',E('window',text('Hoo Hurts You · Counter'),integer(520),integer(320))),let(2,'widget',E('label',ref(1),text('A native desktop app written entirely in hoo.'))),let(3,'widget',E('input',ref(1),text('Hoo enthusiast'))),let(4,'widget',E('button',ref(1),text('Hoo (+1)'),handler(0))),let(5,'widget',E('button',ref(1),text('Reset'),handler(1))),E('do',E('run'))))
# A persistent desktop note: edit, save to an argument-selected UTF-8 file, reload.
save_note=function(0,'void',[],program(E('do',E('write',ref(0),E('text_get',ref(2)))),E('do',E('text_set',ref(3),text('Saved to disk.')))))
reload_note=function(1,'void',[],if_(E('exists',ref(0)),program(E('do',E('text_set',ref(2),E('read',ref(0)))),E('do',E('text_set',ref(3),text('Loaded from disk.')))),E('do',E('text_set',ref(3),text('No saved note yet.')))))
save('notepad.hoo',program(save_note,reload_note,let(0,'text',E('concat',E('home'),text('/hoo-note.txt'))),let(1,'widget',E('window',text('Hoo Notes'),integer(620),integer(480))),let(2,'widget',E('textarea',ref(1),text('Write a note, then press Save.'))),let(3,'widget',E('label',ref(1),text('Notes are saved as UTF-8.'))),let(4,'widget',E('button',ref(1),text('Save'),handler(0))),let(5,'widget',E('button',ref(1),text('Reload'),handler(1))),if_(E('less',integer(0),E('argument_count')),set_(0,E('argument',integer(0)))),E('do',call(1)),E('do',E('run'))))
# Compile+run integration fixture: the UI creates controls, executes the same
# callback that a real click invokes, checks state, writes a marker and exits.
smoke=function(0,'void',[],program(set_(0,E('add',ref(0),integer(1))),E('do',E('text_set',ref(2),E('decimal',ref(0))))))
save('desktop-smoke.hoo',program(smoke,let(0,'number',integer(0)),let(1,'widget',E('window',text('Hoo Desktop Smoke'),integer(400),integer(400))),let(2,'widget',E('label',ref(1),text('0'))),let(3,'widget',E('button',ref(1),text('Increment'),handler(0))),let(4,'widget',E('textarea',ref(1),text('Initial'))),E('do',E('place',ref(4),integer(20),integer(130),integer(360),integer(140))),E('do',E('enabled',ref(4),token('true'))),E('do',E('text_set',ref(4),text('Multiline 🦉\nSecond line'))),E('do',call(0)),E('print',E('text_get',ref(2))),E('print',E('text_get',ref(4)))))
# Multiline editor with native file dialogs. Empty paths mean cancellation.
open_document=function(0,'void',[],program(let(6,'text',E('open_file',ref(1))),if_(E('not',E('equal',ref(6),text(''))),program(set_(0,ref(6)),E('do',E('text_set',ref(2),E('read',ref(0)))),E('do',E('text_set',ref(3),E('concat',text('Opened: '),ref(0))))))))
save_document=function(1,'void',[],program(let(6,'text',E('save_file',ref(1))),if_(E('not',E('equal',ref(6),text(''))),program(set_(0,ref(6)),E('do',E('write',ref(0),E('text_get',ref(2)))),E('do',E('text_set',ref(3),E('concat',text('Saved: '),ref(0))))))))
save('editor.hoo',program(open_document,save_document,let(0,'text',text('')),let(1,'widget',E('window',text('Hoo Editor'),integer(720),integer(520))),let(2,'widget',E('textarea',ref(1),text('Every line of this application is hoo.\nYour document can contain other words.'))),let(3,'widget',E('label',ref(1),text('Open a UTF-8 document, or write and Save As.'))),let(4,'widget',E('button',ref(1),text('Open…'),handler(0))),let(5,'widget',E('button',ref(1),text('Save As…'),handler(1))),E('do',E('place',ref(2),integer(20),integer(20),integer(680),integer(290))),E('do',E('place',ref(3),integer(20),integer(326),integer(680),integer(28))),E('do',E('place',ref(4),integer(20),integer(370),integer(330),integer(36))),E('do',E('place',ref(5),integer(370),integer(370),integer(330),integer(36))),E('do',E('run'))))
