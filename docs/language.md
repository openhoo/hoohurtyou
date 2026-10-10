# The Hoo language specification (0.5.0)

This document uses English metasyntax to explain the grammar. **None of those English names are accepted in source.** Every token below is an `h` followed by exactly the indicated number of `o` characters. For example, `end` means `hoo`.

## Lexical law

Source contains only ASCII `h`, ASCII `o`, and ASCII whitespace (space, tab, CR, LF). Each word must match `hoo+`; adjacent words need whitespace. There are no comments. Tokens retain 1-based line/column positions. A word may contain at most 4095 `o`s.

Token lengths 64–79 encode hexadecimal digits 0–F inside literals. Lengths 128–4095 encode identifiers 0–3967. Other unassigned lengths are reserved. An identifier has a numeric identity, but its source representation is still exclusively one long hoo word.

## Grammar

All expressions are prefix; operator precedence does not exist. Fixed-arity expressions consume exactly the required number of following expressions. Functions, literals, calls, arrays and control blocks use explicit `end` markers.

```text
program      = import* (function | statement)*
import       = import string (HEX HEX)* end
function     = function IDENT result-type (IDENT value-type)* body statement* end
statement    = let IDENT value-type expression
             | set IDENT expression
             | return expression? end
             | if expression body statement* (else statement*)? end
             | while expression body statement* end
             | do expression
             | print expression
             | break | continue
expression   = integer HEX+ end
             | string (HEX HEX)* end
             | true | false
             | ref IDENT
             | handler IDENT
             | call IDENT expression* end
             | array expression* end
             | OPERATOR expression{arity}
result-type  = void | value-type
value-type   = number | text | boolean | list | widget | callback
```

Function parameters have no punctuation or separator; `body` terminates the signature. A return always ends with `end`, including a bare void return. `if` and `while` require the `body` word. `else` begins its own block without an additional `body`. Calls and arrays end with `end`, including empty calls and empty lists.

## Compile-time imports

`import` is the word with 85 o characters. It must be followed by a literal encoded text path and appear before functions or statements. The path is encoded using the ordinary Hoo string syntax: source still contains only Hoo words. Imported filenames match `hoo+.hoo`; directory components match `hoo+`. Examples of decoded paths are `hooo.hoo` and `hoo/hoooo.hoo`.

Paths resolve relative to the importing file. Absolute paths, `..`, non-Hoo names and symlinks resolving outside the entry file's directory tree are rejected. Imported files pass through the same handwritten lexer and parser. Imports are compile-time dependencies and are bundled into one native executable; no source files are needed at runtime.

Dependencies are visited in source order, depth first, and each canonical file is loaded once. An imported module may contain imports, functions and global declarations; it cannot contain top-level executable statements. Imported globals initialize before the importing file's globals. Functions and globals share one compilation namespace, and duplicate identifiers are rejected. There are no private exports or namespace qualifiers in this version. Functions can call functions in other modules and native callbacks can reference imported functions.

Import cycles fail with a dependency chain and the importing source position. The graph allows at most 256 files including the entry and at most 64 files along one dependency chain. Compiler and runtime errors preserve the original file, line and column. Output paths cannot overwrite any loaded source file.

The CLI supplies the origin path automatically. Python integrations pass it as the second argument to `hoo.hoooooo.hooo(source, path)` or as `hoo=path` to `hoo.hoooooo.hoooo(source, output, ...)`. In-memory compilation without a path continues to work for programs without imports. The `hooooo` formatter validates dependencies and formats only the entry file; `hoooo` displays the entry file's tokens.

## Types and scope

- `number`: signed 64-bit integer; no floats or implicit conversions. Integer literals encode 0..9223372036854775807. Negative values use `negate`; the signed minimum can be expressed as `subtract (negate MAX) 1` in metasyntax.
- `text`: immutable, valid UTF-8 without NUL bytes. `length` counts Unicode code points, rather than UTF-8 bytes or grapheme clusters.
- `boolean`: true/false; conditions require this type.
- `list`: mutable ordered numbers. Assignment shares the same list; `push` and `put` mutate shared storage. Indexing is zero-based.
- `widget`: opaque native window/control handle. Widget-specific misuse is checked at runtime.
- `callback`: pointer to a zero-parameter void function. Use `handler IDENT` to create one; it is not a closure.
- `void`: function result and effectful builtin result. It cannot be a variable or parameter type.

Functions and variables occupy separate identifier namespaces. Function calls may be forward or recursive. Globals are a contiguous declaration prelude in the top-level statement stream. Functions may appear anywhere at top level; nested function definitions are not legal. Global initializer expressions see earlier globals. Functions see globals and their own parameters/locals. If a global initializer calls a function that reads a later global, execution fails with an initialization diagnostic.

Variable shadowing is forbidden. `if` branches and loop bodies introduce lexical scopes. Branch locals do not escape. Loops reevaluate their conditions. `break` and `continue` target the nearest loop. Parameters may use the same identifier as a global and take precedence within that function; other local shadowing is rejected.

Every non-void function needs a return on every statically checked fallthrough path. Returning in both arms of an `if` establishes that property. The checker conservatively assumes a loop may finish. A statement following an unconditional return, break, continue, or an if whose two branches return is rejected as unreachable.

## Literals without ordinary characters

To encode an integer, convert it to hexadecimal, replace each digit D with a word containing `64 + D` o characters, then wrap those words with `integer` and `end` tokens. Integers need 1–16 hex digits and must fit the positive signed range. Leading zeroes are allowed.

To encode a string, first obtain its UTF-8 bytes. Encode each byte as two hex digits, replace those digits with the same 64–79 word-length encoding, and wrap with `string` and `end`. Empty strings are allowed. An odd number of digits, NUL or invalid UTF-8 is rejected.

Example in explanatory notation: `print integer HEX1 end` prints 1. Its actual Hoo source is the short example in the README. `hoo.hooooooo` can emit exact words for editor integrations; it is not an alternate compiler input language.

## Complete word table

| o count | Meaning |
|---:|---|
| 2 | `end` |
| 3 | `let` |
| 4 | `set` |
| 5 | `function` |
| 6 | `body` |
| 7 | `return` |
| 8 | `void` |
| 9 | `number` |
| 10 | `text` |
| 11 | `boolean` |
| 12 | `list` |
| 13 | `widget` |
| 14 | `callback` |
| 15 | `if` |
| 16 | `else` |
| 17 | `while` |
| 18 | `do` |
| 19 | `print` |
| 20 | `integer` |
| 21 | `string` |
| 22 | `true` |
| 23 | `false` |
| 24 | `ref` |
| 25 | `call` |
| 26 | `add` |
| 27 | `subtract` |
| 28 | `multiply` |
| 29 | `divide` |
| 30 | `remainder` |
| 31 | `equal` |
| 32 | `less` |
| 33 | `not` |
| 34 | `and` |
| 35 | `or` |
| 36 | `array` |
| 37 | `get` |
| 38 | `length` |
| 39 | `handler` |
| 40 | `concat` |
| 41 | `decimal` |
| 42 | `read` |
| 43 | `write` |
| 44 | `window` |
| 45 | `label` |
| 46 | `input` |
| 47 | `button` |
| 48 | `text_get` |
| 49 | `text_set` |
| 50 | `run` |
| 51 | `quit` |
| 52 | `push` |
| 53 | `put` |
| 54 | `argument` |
| 55 | `argument_count` |
| 56 | `negate` |
| 57 | `break` |
| 58 | `continue` |
| 59 | `parse_number` |
| 60 | `exists` |
| 61 | `textarea` |
| 62 | `alert` |
| 80 | `open_file` |
| 81 | `save_file` |
| 82 | `place` |
| 83 | `enabled` |
| 84 | `home` |
| 85 | `import` |
| 86 | `slice` |
| 87 | `code` |
| 88 | `character` |
| 89 | `find` |
| 90 | `random` |
| 91 | `clock` |
| 92 | `canvas` |
| 93 | `fill` |
| 94 | `clear` |
| 95 | `paint` |
| 96 | `timer` |
| 97 | `key` |
| 98 | `pixel` |

## Builtin expression signatures

`equal(a,b)` accepts two matching scalar types (number, text or boolean); text equality compares UTF-8 contents. `length(a)` accepts text or list and returns number. `array` consumes zero or more numbers and returns a list. `and`/`or` short circuit. All other operands and function arguments evaluate left to right.

| Operation | Arguments in order | Result |
|---|---|---|
| `add` | number, number | number |
| `subtract` | number, number | number |
| `multiply` | number, number | number |
| `divide` | number, number | number |
| `remainder` | number, number | number |
| `less` | number, number | boolean |
| `not` | boolean | boolean |
| `and` | boolean, boolean | boolean |
| `or` | boolean, boolean | boolean |
| `negate` | number | number |
| `get` | list, number | number |
| `concat` | text, text | text |
| `decimal` | number | text |
| `read` | text | text |
| `write` | text, text | void |
| `window` | text, number, number | widget |
| `label` | widget, text | widget |
| `input` | widget, text | widget |
| `button` | widget, text, callback | widget |
| `text_get` | widget | text |
| `text_set` | widget, text | void |
| `run` | none | void |
| `quit` | none | void |
| `push` | list, number | void |
| `put` | list, number, number | void |
| `argument` | number | text |
| `textarea` | widget, text | widget |
| `alert` | widget, text | void |
| `open_file` | widget | text |
| `save_file` | widget | text |
| `place` | widget, number, number, number, number | void |
| `enabled` | widget, boolean | void |
| `home` | none | text |
| `argument_count` | none | number |
| `parse_number` | text | number |
| `exists` | text | boolean |
| `slice` | text, start, count | text |
| `code` | text, index | number |
| `character` | number | text |
| `find` | text, needle | number |
| `random` | limit | number |
| `clock` | none | number |
| `canvas` | widget, width, height | widget |
| `fill` | canvas, x, y, width, height, color | void |
| `clear` | canvas, color | void |
| `paint` | canvas, x, y, text, color | void |
| `timer` | milliseconds, callback | void |
| `key` | canvas | text |
| `pixel` | canvas, x, y | number |

`print` is a statement accepting a scalar and appending a newline. `do` is a statement evaluating and discarding any expression result.

`divide` truncates toward zero. `remainder` follows signed C integer remainder after overflow/zero checks. Arithmetic overflow is a runtime error, not wraparound. `parse_number` accepts decimal text, including an optional sign and leading ASCII whitespace; trailing junk, empty input and out-of-range values fail.

`home` returns the UTF-8 user home path from the HOME environment variable. File operations work on UTF-8 text. `write` replaces file contents. `read` rejects NUL and invalid UTF-8. `exists` checks the filesystem path. `argument(0)` is the first argument after the executable name, and `argument_count` excludes the executable name. Out-of-range argument access fails.

`slice`, `code` and `find` index Unicode code points, matching `length`. `slice(text,start,count)` fails if the range passes the end; `code` returns the code point at an index; `find` returns the first code-point index of a needle or -1. `character` builds one-code-point text and rejects NUL, surrogates and values above U+10FFFF. `random(limit)` returns a uniformly distributed number in `0..limit-1` from a per-process xorshift generator without modulo bias; it is not cryptographic. `clock` returns monotonic milliseconds for measuring elapsed time; its origin is unspecified.

Desktop operations are explained in [the desktop guide](desktop.md). `open_file`/`save_file` return empty text on cancellation. `place` uses top-left coordinates. Window dimensions are 160..10000 by 100..10000 pixels; placement dimensions are 1..10000, and positions are 0..10000. Controls use default rows until explicitly positioned. `enabled` requires a control rather than a window. `run` enters the event loop; closing the last window or `quit` ends the app. macOS terminates immediately; GTK leaves its main loop and allows following statements to execute. Portable programs should make `run` their final statement.

## Canvas, timers and keyboard (0.5.0)

`canvas(window,width,height)` adds a 1..4096 by 1..4096 pixel framebuffer control in the next layout row and gives it keyboard focus. Colors are numbers `0xRRGGBB` (0..16777215). `fill` draws a rectangle clipped to the canvas; `clear` fills it; `paint` draws text with Hoo's built-in 5×7 bitmap font at 2× scale (12 pixels per character, 14 pixels high). Lowercase letters are drawn as uppercase; characters outside ASCII 32..95 are drawn as `?`. Drawing coordinates may lie partially or completely outside the canvas but must be within -100000..100000; `pixel` must be inside and returns the stored color, so drawing is deterministic and testable on every backend.

`key(canvas)` dequeues the next key pressed while the canvas had focus and returns empty text when the queue is empty. Named keys are `left`, `right`, `up`, `down`, `space`, `enter`, `escape`, `backspace` and `tab`; other keys return their lowercase character. The queue keeps the latest 64 keys. Clicking a canvas focuses it.

`timer(milliseconds,callback)` schedules a repeating 1..3600000 ms callback on the native event loop after `run` begins. Timers cannot be cancelled; use state in globals to ignore ticks, or `quit`. Callback execution is single-threaded and never overlaps. Console builds reject canvases and timers at runtime.

`print` flushes standard output after every line, so piped and redirected desktop programs show output immediately.

## Failures and limits

Compile-time failures return CLI status 1. Runtime failures print the original source file (when available), line and column and exit 70. There is no exception recovery. Parser expression nesting is limited to 200 levels. Native recursion uses the platform stack. Functions, globals and locals are limited by the identifier space, compilation resources and process memory.
