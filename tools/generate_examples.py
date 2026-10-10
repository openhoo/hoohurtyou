#!/usr/bin/env python3
"""Reproducible construction of the checked-in, exclusively hoo-word examples."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from hoo.hooooooo import *

ROOT=Path(__file__).resolve().parents[1]/'examples'
def hoooooooooooooooooooooooo(name,source):
    path=ROOT/name; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(source)
E=hoooooooooo
hoooooooooooooooooooooooo('hello.hoo',hooooooooooooooooooooo(E('print',hooooooooo('Hoo, world! 🦉'))))
factorial=hoooooooooooooooo(0,'number',[(0,'number')],hoooooooooooooooooo(E('less',hooooooooooo(0),hoooooooo(2)),hooooooooooooooooo(hoooooooo(1)),hooooooooooooooooo(E('multiply',hooooooooooo(0),hooooooooooooo(0,E('subtract',hooooooooooo(0),hoooooooo(1)))))))
hoooooooooooooooooooooooo('factorial.hoo',hooooooooooooooooooooo(factorial,E('print',hooooooooooooo(0,hoooooooo(10)))))
hoooooooooooooooooooooooo('lists.hoo',hooooooooooooooooooooo(hoooooooooooooo(0,'list',hoooooooooooooooooooo(hoooooooo(2),hoooooooo(3),hoooooooo(5))),hoooooooooooooo(1,'number',hoooooooo(0)),E('do',E('push',hooooooooooo(0),hoooooooo(7))),hooooooooooooooooooo(E('less',hooooooooooo(1),E('length',hooooooooooo(0))),hooooooooooooooooooooo(E('print',E('get',hooooooooooo(0),hooooooooooo(1))),hooooooooooooooo(1,E('add',hooooooooooo(1),hoooooooo(1)))))))
# Counter with native labels, editable name, mutable state and two callbacks.
inc=hoooooooooooooooo(0,'void',[],hooooooooooooooooooooo(hooooooooooooooo(0,E('add',hooooooooooo(0),hoooooooo(1))),E('do',E('text_set',hooooooooooo(2),E('concat',E('concat',E('text_get',hooooooooooo(3)),hooooooooo(' says hoo: ')),E('decimal',hooooooooooo(0)))))))
reset=hoooooooooooooooo(1,'void',[],hooooooooooooooooooooo(hooooooooooooooo(0,hoooooooo(0)),E('do',E('text_set',hooooooooooo(2),hooooooooo('Count reset. Hoo again.')))))
hoooooooooooooooooooooooo('counter.hoo',hooooooooooooooooooooo(inc,reset,hoooooooooooooo(0,'number',hoooooooo(0)),hoooooooooooooo(1,'widget',E('window',hooooooooo('Hoo Hurts You · Counter'),hoooooooo(520),hoooooooo(320))),hoooooooooooooo(2,'widget',E('label',hooooooooooo(1),hooooooooo('A native desktop app written entirely in hoo.'))),hoooooooooooooo(3,'widget',E('input',hooooooooooo(1),hooooooooo('Hoo enthusiast'))),hoooooooooooooo(4,'widget',E('button',hooooooooooo(1),hooooooooo('Hoo (+1)'),hoooooooooooo(0))),hoooooooooooooo(5,'widget',E('button',hooooooooooo(1),hooooooooo('Reset'),hoooooooooooo(1))),E('do',E('run'))))
# A persistent desktop note: edit, save to an argument-selected UTF-8 file, reload.
save_note=hoooooooooooooooo(0,'void',[],hooooooooooooooooooooo(E('do',E('write',hooooooooooo(0),E('text_get',hooooooooooo(2)))),E('do',E('text_set',hooooooooooo(3),hooooooooo('Saved to disk.')))))
reload_note=hoooooooooooooooo(1,'void',[],hoooooooooooooooooo(E('exists',hooooooooooo(0)),hooooooooooooooooooooo(E('do',E('text_set',hooooooooooo(2),E('read',hooooooooooo(0)))),E('do',E('text_set',hooooooooooo(3),hooooooooo('Loaded from disk.')))),E('do',E('text_set',hooooooooooo(3),hooooooooo('No saved note yet.')))))
hoooooooooooooooooooooooo('notepad.hoo',hooooooooooooooooooooo(save_note,reload_note,hoooooooooooooo(0,'text',E('concat',E('home'),hooooooooo('/hoo-note.txt'))),hoooooooooooooo(1,'widget',E('window',hooooooooo('Hoo Notes'),hoooooooo(620),hoooooooo(480))),hoooooooooooooo(2,'widget',E('textarea',hooooooooooo(1),hooooooooo('Write a note, then press Save.'))),hoooooooooooooo(3,'widget',E('label',hooooooooooo(1),hooooooooo('Notes are saved as UTF-8.'))),hoooooooooooooo(4,'widget',E('button',hooooooooooo(1),hooooooooo('Save'),hoooooooooooo(0))),hoooooooooooooo(5,'widget',E('button',hooooooooooo(1),hooooooooo('Reload'),hoooooooooooo(1))),hoooooooooooooooooo(E('less',hoooooooo(0),E('argument_count')),hooooooooooooooo(0,E('argument',hoooooooo(0)))),E('do',hooooooooooooo(1)),E('do',E('run'))))
# Compile+run integration fixture: the UI creates controls, executes the same
# callback that a real click invokes, checks state, writes a marker and exits.
smoke=hoooooooooooooooo(0,'void',[],hooooooooooooooooooooo(hooooooooooooooo(0,E('add',hooooooooooo(0),hoooooooo(1))),E('do',E('text_set',hooooooooooo(2),E('decimal',hooooooooooo(0))))))
hoooooooooooooooooooooooo('desktop-smoke.hoo',hooooooooooooooooooooo(smoke,hoooooooooooooo(0,'number',hoooooooo(0)),hoooooooooooooo(1,'widget',E('window',hooooooooo('Hoo Desktop Smoke'),hoooooooo(400),hoooooooo(400))),hoooooooooooooo(2,'widget',E('label',hooooooooooo(1),hooooooooo('0'))),hoooooooooooooo(3,'widget',E('button',hooooooooooo(1),hooooooooo('Increment'),hoooooooooooo(0))),hoooooooooooooo(4,'widget',E('textarea',hooooooooooo(1),hooooooooo('Initial'))),E('do',E('place',hooooooooooo(4),hoooooooo(20),hoooooooo(130),hoooooooo(360),hoooooooo(140))),E('do',E('enabled',hooooooooooo(4),hoooooo('true'))),E('do',E('text_set',hooooooooooo(4),hooooooooo('Multiline 🦉\nSecond line'))),E('do',hooooooooooooo(0)),E('print',E('text_get',hooooooooooo(2))),E('print',E('text_get',hooooooooooo(4)))))
# Multiline editor with native file dialogs. Empty paths mean cancellation.
open_document=hoooooooooooooooo(0,'void',[],hooooooooooooooooooooo(hoooooooooooooo(6,'text',E('open_file',hooooooooooo(1))),hoooooooooooooooooo(E('not',E('equal',hooooooooooo(6),hooooooooo(''))),hooooooooooooooooooooo(hooooooooooooooo(0,hooooooooooo(6)),E('do',E('text_set',hooooooooooo(2),E('read',hooooooooooo(0)))),E('do',E('text_set',hooooooooooo(3),E('concat',hooooooooo('Opened: '),hooooooooooo(0))))))))
save_document=hoooooooooooooooo(1,'void',[],hooooooooooooooooooooo(hoooooooooooooo(6,'text',E('save_file',hooooooooooo(1))),hoooooooooooooooooo(E('not',E('equal',hooooooooooo(6),hooooooooo(''))),hooooooooooooooooooooo(hooooooooooooooo(0,hooooooooooo(6)),E('do',E('write',hooooooooooo(0),E('text_get',hooooooooooo(2)))),E('do',E('text_set',hooooooooooo(3),E('concat',hooooooooo('Saved: '),hooooooooooo(0))))))))
hoooooooooooooooooooooooo('editor.hoo',hooooooooooooooooooooo(open_document,save_document,hoooooooooooooo(0,'text',hooooooooo('')),hoooooooooooooo(1,'widget',E('window',hooooooooo('Hoo Editor'),hoooooooo(720),hoooooooo(520))),hoooooooooooooo(2,'widget',E('textarea',hooooooooooo(1),hooooooooo('Every line of this application is hoo.\nYour document can contain other words.'))),hoooooooooooooo(3,'widget',E('label',hooooooooooo(1),hooooooooo('Open a UTF-8 document, or write and Save As.'))),hoooooooooooooo(4,'widget',E('button',hooooooooooo(1),hooooooooo('Open…'),hoooooooooooo(0))),hoooooooooooooo(5,'widget',E('button',hooooooooooo(1),hooooooooo('Save As…'),hoooooooooooo(1))),E('do',E('place',hooooooooooo(2),hoooooooo(20),hoooooooo(20),hoooooooo(680),hoooooooo(290))),E('do',E('place',hooooooooooo(3),hoooooooo(20),hoooooooo(326),hoooooooo(680),hoooooooo(28))),E('do',E('place',hooooooooooo(4),hoooooooo(20),hoooooooo(370),hoooooooo(330),hoooooooo(36))),E('do',E('place',hooooooooooo(5),hoooooooo(370),hoooooooo(370),hoooooooo(330),hoooooooo(36))),E('do',E('run'))))

# Hoo-only multi-file application: entry, shared state/callbacks and smoke.
hoooooooooooooooooooooooo('hoo/hooo.hoo',hooooooooooooooooooooo(
    hoooooooooooooooo(0,'void',[],hooooooooooooooooooooo(
        hooooooooooooooo(0,E('add',hooooooooooo(0),hoooooooo(1))),
        E('do',E('text_set',hooooooooooo(2),E('decimal',hooooooooooo(0)))))),
    hoooooooooooooooo(1,'void',[],hooooooooooooooooooooo(
        hooooooooooooooo(0,hoooooooo(0)),
        E('do',E('text_set',hooooooooooo(2),E('decimal',hooooooooooo(0)))))),
    hoooooooooooooo(0,'number',hoooooooo(0)),
    hoooooooooooooo(1,'widget',E('window',hooooooooo('Hoo Modules · Counter'),hoooooooo(520),hoooooooo(320))),
    hoooooooooooooo(2,'widget',E('label',hooooooooooo(1),hooooooooo('0')))))
hoooooooooooooooooooooooo('hoo/hoo.hoo',hooooooooooooooooooooo(
    E('import',hooooooooo('hooo.hoo')),
    hoooooooooooooo(3,'widget',E('button',hooooooooooo(1),hooooooooo('Hoo (+1)'),hoooooooooooo(0))),
    hoooooooooooooo(4,'widget',E('button',hooooooooooo(1),hooooooooo('Hoo (reset)'),hoooooooooooo(1))),
    E('do',E('run'))))
hoooooooooooooooooooooooo('hoo/hoooo.hoo',hooooooooooooooooooooo(
    E('import',hooooooooo('hooo.hoo')),
    hoooooooooooooo(3,'widget',E('button',hooooooooooo(1),hooooooooo('Hoo (+1)'),hoooooooooooo(0))),
    hoooooooooooooo(4,'widget',E('button',hooooooooooo(1),hooooooooo('Hoo (reset)'),hoooooooooooo(1))),
    E('do',hooooooooooooo(0)),E('print',E('text_get',hooooooooooo(2))),
    E('do',hooooooooooooo(1)),E('print',E('text_get',hooooooooooo(2)))))
hoooooooooooooooooooooooo('hoo/hooooo.hoo',hooooooooooooooooooooo(
    E('import',hooooooooo('hoooooo.hoo')),E('print',hooooooooooooo(0))))
hoooooooooooooooooooooooo('hoo/hoooooo.hoo',hooooooooooooooooooooo(
    hoooooooooooooooo(0,'number',[],hooooooooooooooooo(hooooooooooo(0))),
    hoooooooooooooo(0,'number',hoooooooo(42))))
