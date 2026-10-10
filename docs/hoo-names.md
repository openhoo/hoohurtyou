# More Hoo: implementation naming and CLI in 0.3.0

Hoo naming now extends into the compiler and runtime. Custom Python functions, methods and classes use only `h` followed by `o`s. Native runtime functions, helper functions, types, enum constants and Objective-C classes do too. Generated application functions, variables, temporaries and GC frame identifiers receive distinct Hoo names.

The native symbols occupy the short-word range; generated symbols start above 128 o characters and use one shared allocator. Function and variable mappings are cached separately, keeping forward calls, callbacks and variable references consistent. Generated names are deterministic.

## Hoo commands

The installed executable is `hoo`. The repository launcher is `./bin/hoo` (also works outside the repository). Commands and flags accept only the Hoo spellings below; English aliases and abbreviated options are rejected.

| Command word | Operation |
|---|---|
| `hoo` | Check types |
| `hooo` | Emit native C |
| `hoooo` | Show tokens |
| `hooooo` | Format |
| `hoooooo` | Build |
| `hooooooo` | Compile and run |

```sh
./bin/hoo hoo examples/counter.hoo
./bin/hoo hooooooo examples/factorial.hoo --hoooo
./bin/hoo hoooooo examples/editor.hoo --hoooooo build/MyHooEditor.app --hooooooo
```

Version 0.3.0 removes English commands, options and the `hooc` executable. Language `.hoo` syntax is unchanged; existing Hoo programs compile without modification.

## Hoo files

| Responsibility | Module / file |
|---|---|
| Native symbol dispatch | `hoo/hoo.py` |
| Static type checker | `hoo/hooo.py` |
| Native code generator | `hoo/hoooo.py` |
| Lexer, parser and AST | `hoo/hooooo.py` |
| Compiler driver | `hoo/hoooooo.py` |
| Word encoders | `hoo/hooooooo.py` |
| Runtime ABI | `hoo/runtime/hoo.h` |
| Core native runtime | `hoo/runtime/hoo.c` |
| macOS runtime | `hoo/runtime/hoo.m` |
| Linux runtime | `hoo/runtime/hooo.c` |
| Console runtime | `hoo/runtime/hoooo.c` |

## Python symbol reference

The Python API intentionally changed in 0.2.0; use these spellings instead of the former descriptive names. Semantic AST tags and diagnostic messages remain readable strings. Python special methods, the C entry point `main`, AppKit delegate selectors and toolkit APIs follow their host platform contracts. Test discovery methods keep their `test_` prefix.

| Role / former name | Hoo symbol | o count |
|---|---|---:|
| `main` | `hoo` | 2 |
| `compile_source` | `hooo` | 3 |
| `build` | `hoooo` | 4 |
| `word` | `hooooo` | 5 |
| `token` | `hoooooo` | 6 |
| `identifier` | `hooooooo` | 7 |
| `integer` | `hoooooooo` | 8 |
| `text` | `hooooooooo` | 9 |
| `expression` | `hoooooooooo` | 10 |
| `ref` | `hooooooooooo` | 11 |
| `handler` | `hoooooooooooo` | 12 |
| `call` | `hooooooooooooo` | 13 |
| `let` | `hoooooooooooooo` | 14 |
| `set_` | `hooooooooooooooo` | 15 |
| `function` | `hoooooooooooooooo` | 16 |
| `return_` | `hooooooooooooooooo` | 17 |
| `if_` | `hoooooooooooooooooo` | 18 |
| `while_` | `hooooooooooooooooooo` | 19 |
| `array` | `hoooooooooooooooooooo` | 20 |
| `program` | `hooooooooooooooooooooo` | 21 |
| `lex` | `hoooooooooooooooooooooo` | 22 |
| `parse` | `hooooooooooooooooooooooo` | 23 |
| `save` | `hoooooooooooooooooooooooo` | 24 |
| `fail` | `hooooooooooooooooooooooooo` | 25 |
| `check` | `hoooooooooooooooooooooooooo` | 26 |
| `expect` | `hooooooooooooooooooooooooooo` | 27 |
| `expr` | `hoooooooooooooooooooooooooooo` | 28 |
| `block` | `hooooooooooooooooooooooooooooo` | 29 |
| `line` | `hoooooooooooooooooooooooooooooo` | 30 |
| `unique` | `hooooooooooooooooooooooooooooooo` | 31 |
| `temp` | `hoooooooooooooooooooooooooooooooo` | 32 |
| `statement` | `hooooooooooooooooooooooooooooooooo` | 33 |
| `emit` | `hoooooooooooooooooooooooooooooooooo` | 34 |
| `peek` | `hooooooooooooooooooooooooooooooooooo` | 35 |
| `take` | `hoooooooooooooooooooooooooooooooooooo` | 36 |
| `need` | `hooooooooooooooooooooooooooooooooooooo` | 37 |
| `name` | `hoooooooooooooooooooooooooooooooooooooo` | 38 |
| `type` | `hooooooooooooooooooooooooooooooooooooooo` | 39 |
| `_expr` | `hoooooooooooooooooooooooooooooooooooooooo` | 40 |
| `cli` | `hooooooooooooooooooooooooooooooooooooooooo` | 41 |
| `reject` | `hoooooooooooooooooooooooooooooooooooooooooo` | 42 |
| `run_hoo` | `hooooooooooooooooooooooooooooooooooooooooooo` | 43 |
| `good` | `hoooooooooooooooooooooooooooooooooooooooooooo` | 44 |
| `failure` | `hooooooooooooooooooooooooooooooooooooooooooooo` | 45 |
| `Checker` | `hoooooooooooooooooooooooooooooooooooooooooooooo` | 46 |
| `Emitter` | `hooooooooooooooooooooooooooooooooooooooooooooooo` | 47 |
| `Token` | `hoooooooooooooooooooooooooooooooooooooooooooooooo` | 48 |
| `HooError` | `hooooooooooooooooooooooooooooooooooooooooooooooooo` | 49 |
| `Node` | `hoooooooooooooooooooooooooooooooooooooooooooooooooo` | 50 |
| `Function` | `hooooooooooooooooooooooooooooooooooooooooooooooooooo` | 51 |
| `Program` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooo` | 52 |
| `Parser` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 53 |
| `variable` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 54 |
| `function_symbol` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 55 |

## Native symbol reference

| Role / former name | Hoo symbol | o count |
|---|---|---:|
| `ho_init` | `hoo` | 2 |
| `ho_shutdown` | `hooo` | 3 |
| `ho_ui_shutdown` | `hoooo` | 4 |
| `ho_location` | `hooooo` | 5 |
| `ho_fail` | `hoooooo` | 6 |
| `ho_alloc` | `hooooooo` | 7 |
| `ho_root` | `hoooooooo` | 8 |
| `ho_frame` | `hooooooooo` | 9 |
| `ho_restore` | `hoooooooooo` | 10 |
| `ho_collect` | `hooooooooooo` | 11 |
| `ho_load` | `hoooooooooooo` | 12 |
| `ho_void` | `hooooooooooooo` | 13 |
| `ho_number` | `hoooooooooooooo` | 14 |
| `ho_boolean` | `hooooooooooooooo` | 15 |
| `ho_callback` | `hoooooooooooooooo` | 16 |
| `ho_text` | `hooooooooooooooooo` | 17 |
| `ho_widget` | `hoooooooooooooooooo` | 18 |
| `ho_array` | `hooooooooooooooooooo` | 19 |
| `ho_add` | `hoooooooooooooooooooo` | 20 |
| `ho_subtract` | `hooooooooooooooooooooo` | 21 |
| `ho_multiply` | `hoooooooooooooooooooooo` | 22 |
| `ho_divide` | `hooooooooooooooooooooooo` | 23 |
| `ho_remainder` | `hoooooooooooooooooooooooo` | 24 |
| `ho_negate` | `hooooooooooooooooooooooooo` | 25 |
| `ho_equal` | `hoooooooooooooooooooooooooo` | 26 |
| `ho_less` | `hooooooooooooooooooooooooooo` | 27 |
| `ho_not` | `hoooooooooooooooooooooooooooo` | 28 |
| `ho_get` | `hooooooooooooooooooooooooooooo` | 29 |
| `ho_length` | `hoooooooooooooooooooooooooooooo` | 30 |
| `ho_push` | `hooooooooooooooooooooooooooooooo` | 31 |
| `ho_put` | `hoooooooooooooooooooooooooooooooo` | 32 |
| `ho_concat` | `hooooooooooooooooooooooooooooooooo` | 33 |
| `ho_decimal` | `hoooooooooooooooooooooooooooooooooo` | 34 |
| `ho_parse_number` | `hooooooooooooooooooooooooooooooooooo` | 35 |
| `ho_read` | `hoooooooooooooooooooooooooooooooooooo` | 36 |
| `ho_write` | `hooooooooooooooooooooooooooooooooooooo` | 37 |
| `ho_exists` | `hoooooooooooooooooooooooooooooooooooooo` | 38 |
| `ho_argument` | `hooooooooooooooooooooooooooooooooooooooo` | 39 |
| `ho_argument_count` | `hoooooooooooooooooooooooooooooooooooooooo` | 40 |
| `ho_home` | `hooooooooooooooooooooooooooooooooooooooooo` | 41 |
| `ho_print` | `hoooooooooooooooooooooooooooooooooooooooooo` | 42 |
| `ho_window` | `hooooooooooooooooooooooooooooooooooooooooooo` | 43 |
| `ho_label` | `hoooooooooooooooooooooooooooooooooooooooooooo` | 44 |
| `ho_input` | `hooooooooooooooooooooooooooooooooooooooooooooo` | 45 |
| `ho_button` | `hoooooooooooooooooooooooooooooooooooooooooooooo` | 46 |
| `ho_text_get` | `hooooooooooooooooooooooooooooooooooooooooooooooo` | 47 |
| `ho_text_set` | `hoooooooooooooooooooooooooooooooooooooooooooooooo` | 48 |
| `ho_textarea` | `hooooooooooooooooooooooooooooooooooooooooooooooooo` | 49 |
| `ho_alert` | `hoooooooooooooooooooooooooooooooooooooooooooooooooo` | 50 |
| `ho_open_file` | `hooooooooooooooooooooooooooooooooooooooooooooooooooo` | 51 |
| `ho_save_file` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooo` | 52 |
| `ho_place` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 53 |
| `ho_enabled` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 54 |
| `ho_run` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 55 |
| `ho_quit` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 56 |
| `string` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 57 |
| `native` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 58 |
| `window` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 59 |
| `row` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 60 |
| `resize` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 61 |
| `object` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 62 |
| `collect` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 63 |
| `divisor` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 64 |
| `index_of` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 65 |
| `utf8` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 66 |
| `initialize` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 67 |
| `dead` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 68 |
| `retain` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 69 |
| `closed` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 70 |
| `invoke` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 71 |
| `destroy_callback` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 72 |
| `parent` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 73 |
| `control` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 74 |
| `choose` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 75 |
| `unavailable` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 76 |
| `HObject` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 77 |
| `HValue` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 78 |
| `HCallback` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 79 |
| `HooWindow` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 80 |
| `HooAction` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 81 |
| `H_VOID` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 82 |
| `H_NUMBER` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 83 |
| `H_BOOLEAN` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 84 |
| `H_TEXT` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 85 |
| `H_LIST` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 86 |
| `H_WIDGET` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 87 |
| `H_CALLBACK` | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 88 |
| `HOO_RUNTIME_H` | `hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo` | 89 |
| Objective-C action selector | `hoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo:` | 120 |

## Compiler options (v0.3.0)

| Flag | Meaning |
|---|---|
| `--hoo` | Help, at the root or on any command |
| `--hooo` | Compiler version (root only) |
| `--hoooo` | Headless runtime (build/run) |
| `--hooooo` | Address and undefined behavior sanitizers (build/run) |
| `--hoooooo hoo` | Output path (required for build, optional for C emission) |
| `--hooooooo` | macOS application bundle (build) |

Paths and application arguments are user data, so they may contain ordinary text. `--` separates application arguments from compiler options. Help descriptions and diagnostics explain the interface in English.
