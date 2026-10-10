# Hoo Hurts You

**A native compiled programming language whose entire source alphabet is `h`, `o`, and whitespace.**

You can write complete, event-driven desktop applications. You can also stare at a 143-o identifier and question your decisions.

```hoo
hooooooooooooooooooo hoooooooooooooooooooo hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo hoo
```

That program prints `1`. Yes, really.

## What exists

- A handwritten lexer, recursive-descent parser, syntax tree, static type checker, and C code generator.
- Native executables produced by Clang: no Python, Hoo interpreter, browser, or JavaScript is needed to run a compiled application.
- Seven types: signed 64-bit numbers, UTF-8 text, booleans, mutable number lists, native widget handles, callbacks, and `void` function results.
- Named functions, forward calls, recursion, globals, lexical block scopes, conditionals, loops, break/continue, and short-circuit boolean operators.
- Deterministic left-to-right expression evaluation, tracing garbage collection, checked arithmetic, checked indices, and source-located diagnostics.
- Native desktop windows, labels, inputs, multiline editors, buttons, callbacks, file choosers, alerts, custom control geometry, and enable/disable operations.
- UTF-8 file I/O, existence checks, command-line arguments, and macOS `.app` packaging.
- macOS AppKit and Linux GTK 3 desktop runtimes. Console builds can omit the GUI dependency.

## Start hurting

Requirements: Python 3.10+ for the compiler, and Clang for native compilation. On macOS, install Apple's Command Line Tools (`xcode-select --install`). On Debian/Ubuntu, install `clang pkg-config libgtk-3-dev`; GUI tests also use `xvfb`.

From this checkout:

```sh
./hooc run examples/hello.hoo --headless
./hooc run examples/factorial.hoo --headless
./hooc build examples/counter.hoo -o build/counter
./build/counter
```

Build a Finder-launchable macOS application:

```sh
./hooc build examples/counter.hoo -o build/HooCounter.app --app
open build/HooCounter.app
```

Each `--app` output must be a **new** directory. To rebuild, choose a new output name or move the previous bundle first.

A real note application with multiline editing and disk persistence:

```sh
./hooc build examples/notepad.hoo -o build/hoo-notes
./build/hoo-notes ./my-note.txt
```

Without a path argument, Notes uses `~/hoo-note.txt` in the user home directory. The Save button writes the file; Reload reads it. The example does not prompt about unsaved edits. The separate `editor.hoo` example offers native Open and Save As dialogs.

Install the compiler into a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/pip install .
.venv/bin/hooc --version
```

## Why everything looks the same

Count the `o` characters **after** the initial `h`. Their count is the token number. Words are separated by ASCII spaces, tabs, or newlines. There are no punctuation characters, ordinary identifiers, quoted strings, Arabic digits, or comments in Hoo source.

| Word | o count | Meaning |
|---|---:|---|
| `hoo` | 2 | End marker |
| `hooo` | 3 | Declare a variable |
| `hoooo` | 4 | Assign a variable |
| `hooooo` | 5 | Define a function |
| `hoooooo` | 6 | Begin a block |
| `hooooooo` | 7 | Return |
| `h` followed by 64–79 o characters | 64–79 | Hexadecimal digits 0–F inside literals |
| `h` followed by 128–4095 o characters | 128–4095 | Identifiers 0–3967 |

Numbers are terminated sequences of hexadecimal hoo digits. Strings are terminated sequences of UTF-8 bytes, each encoded as two hexadecimal hoo digits. Identifiers occupy a separate word-length range. The grammar is prefix and self-delimiting: you must count correctly, but the compiler does not need to guess.

Read the complete [language specification](docs/language.md), [desktop guide](docs/desktop.md), and [compiler architecture](docs/architecture.md).

## Tools for counting regrets

```sh
./hooc check examples/notepad.hoo
./hooc tokens examples/hello.hoo
./hooc emit examples/factorial.hoo -o build/factorial.c
./hooc format examples/hello.hoo
./hooc build examples/lists.hoo -o build/lists --headless --sanitize
```

`tokens` prints word lengths and meanings with line/column positions. `format` validates and prints one token per line to stdout. `emit` exposes the native compilation input. `CC` selects a compatible compiler binary (a path or executable name, not a shell command).

The optional Python encoders in `hoo.encoding` are for editor integrations, tests, and generating templates. The compiler accepts **only Hoo source**. The checked-in example generator is deterministic:

```sh
python3 tools/generate_examples.py
```

## Verify the compiler

```sh
python3 -m unittest discover -s tests -v
HOO_SANITIZE=1 python3 -m unittest discover -s tests -v
HOO_GUI_TEST=1 python3 -m unittest discover -s tests -v
```

Linux desktop tests run under `xvfb-run -a`. GitHub Actions checks Linux and macOS, installs the package into a fresh virtual environment, executes compiled programs, exercises native controls, and publishes downloadable example artifacts.

## Scope of this first release

This is a working small language and desktop toolkit, with deliberately impractical syntax. The custom compiler frontend and runtime are original; final instruction selection, linking, and operating-system widgets use Clang and the platform toolkit.

Desktop applications target macOS or Linux. There is no Windows GUI backend, module system, generic collection type, exception recovery, networking library, threading, or application sandbox yet. Runtime errors exit with status 70. File writes are direct rather than atomic. Widgets are retained for the application's lifetime; temporary language strings and lists are collected. Compiled macOS bundles are local unsigned builds; distribution signing and notarization are separate work.

MIT licensed. Hoo responsibly.
