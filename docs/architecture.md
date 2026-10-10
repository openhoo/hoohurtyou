# Compiler and runtime architecture

## The pipeline

```text
.hoo source (h/o/ASCII whitespace only)
    -> custom scanner -> position-bearing tokens
    -> compile-time import graph -> combined syntax tree
    -> recursive-descent prefix parser -> structured syntax tree
    -> static symbol/type/control-flow analysis
    -> explicit, sequenced C expressions and native functions
    -> Clang + Hoo C runtime + optional AppKit/GTK runtime
    -> native executable / macOS .app
```

The frontend is Python without third-party runtime dependencies. The compiled result is machine code. Calling `hoo hooooooo` compiles into a temporary executable and runs it; it does not interpret the syntax tree.

## Boundaries

- `hooooo.py`: legal alphabet, word lengths, source positions, hexadecimal literals, UTF-8 validation, grammar, AST. No parser generator.
- `hooooooooo.py`: import resolution, dependency order, import-once loading, cycle/size checks and protection against overwriting source dependencies.
- `hooo.py`: function registration, forward declarations, type checking, argument arity, lexical visibility, callback signatures, global prelude and return-path checking.
- `hoooo.py`: sequenced C temporaries, native functions, lexical scope lifetimes, short-circuit branching and GC root registration.
- `hoooooo.py`: native toolchain invocation using argument arrays; staging and atomic executable replacement; macOS bundle metadata.
- `runtime/hoo.c`: tagged values, heap objects, tracing collector, UTF-8 text, lists, checked arithmetic, filesystem and arguments.
- `runtime/hoo.m` / `runtime/hooo.c`: native widgets, native event loops and callbacks.
- `runtime/hoooo.c`: no desktop dependencies; explicit failure if a program uses desktop operations.

## Evaluation and memory

Every expression lowers into a separate C temporary. Function arguments and operator operands evaluate left to right, regardless of C's unspecified argument evaluation order. `and` and `or` emit branches and skip the right operand when possible.

The heap holds text, number lists and widget wrappers. Numbers, booleans, callback pointers and void values are inline tagged values. Generated code registers pointers to live values in a root stack. Each expression temporary is rooted until its statement finishes. Local declarations survive to the end of their lexical block. Globals remain rooted until shutdown. Function arguments remain rooted through the function call.

Collection occurs only at safe statement/loop boundaries after 256 allocations. All objects referenced by roots survive; unreachable text buffers, list storage and wrappers are freed. Numeric lists contain no heap references, so marking does not require recursive list traversal. Functions restore their frame before returning; there is no intervening collection before the caller roots the returned value. Break and continue restore the enclosing iteration's root frame before transferring control.

Toolkit objects have a separate ownership model. Native windows and controls stay owned by their toolkit/runtime until shutdown. Callback targets own native C function pointers rather than dangling lexical captures. Functions used as callbacks are zero-argument `void` functions and can access globals. Widgets from closed windows fail explicitly rather than dereferencing destroyed controls.

## Diagnostics and safety

Lexer/parser/type errors include line and column; the CLI adds the source filename. Runtime statements/operations update the original file, line and column, including operations in imported modules. Arithmetic checks addition, subtraction, multiplication, division, negation and the signed-minimum division edge. List access checks negative and high indices. Files and arguments preserve UTF-8/NUL-free text invariants. A global read performed indirectly during an earlier global initializer fails explicitly if its target is uninitialized.

The runtime is not a security boundary. Compiled applications run with the permissions of the launching user. I/O errors terminate the process. Deep native recursion is limited by the operating system stack.

## Verification

Tests compile and execute programs covering recursion, evaluation order, short circuiting, nested lexical roots, GC under allocation pressure, loop control, mutable lists, filesystem round trips, UTF-8 and runtime failures. AddressSanitizer and UndefinedBehaviorSanitizer are optional compiler flags and are enabled in CI. A native GUI smoke program constructs controls, invokes its callback, reads the changed label, and exits; manual acceptance additionally clicks real native buttons and saves/reloads a note.
