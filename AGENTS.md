# Hoo contributor instructions

- Preserve the language invariant: `.hoo` files contain only `h`, `o` and ASCII whitespace; words are `h` followed by at least two `o`s.
- Frontend parsing and lexing stay handwritten. Do not add a parser generator or a second accepted source language.
- Update the word table, grammar, static signatures, all three runtime backends, examples and specification together when adding syntax/builtins.
- Preserve deterministic left-to-right evaluation, short-circuit operators, checked arithmetic and GC root lifetimes across calls, returns, break and continue.
- Run `python3 -m unittest discover -s tests -v` for compiler changes. Use `HOO_SANITIZE=1` for changes to generated code, runtime or root lifetime handling.
- GUI smoke tests require `HOO_GUI_TEST=1`; use `xvfb-run -a` on Linux. Do not describe smoke's direct callback call as a physical button-click test.
- Generate examples with `python3 tools/generate_examples.py` and check reproducibility.
- Keep binaries, bundles and test output under ignored `build/`; keep real credentials out of this project.

- Custom compiler/runtime callables, classes and generated native identifiers use Hoo spellings. Keep the naming reference in `docs/hoo-names.md` synchronized. Host entry points/protocol methods and test discovery names keep their required spellings.
