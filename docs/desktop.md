# Building desktop applications in Hoo

An application is a normal Hoo program that creates widgets and enters `run`. Functions used as button callbacks must have no parameters and return `void`. Callback state lives in typed globals.

## Lifecycle

1. Define callback functions (forward calls are also allowed).
2. Declare a contiguous global prelude: state, windows, labels, editors and buttons.
3. Execute setup operations: choose paths, restore files or position controls.
4. Call `run` to dispatch native events.
5. Call `quit` from a callback or close the last application window to exit.

Globals may refer to earlier globals. Function calls made during initialization must not read a global that has not yet been initialized. The runtime detects this case.

Controls default to vertical rows with margins. Multiline editors occupy 140 pixels by default. `place(control,x,y,width,height)` uses coordinates measured from the top-left of the window content area. macOS controls widen with the window. GTK uses fixed geometry; use explicit sizes when designing Linux layouts. Windows need enough height to fit their default control rows before custom placement runs.

`text_get` and `text_set` operate on window titles, labels, single-line inputs, multiline editors and button captions. `enabled` controls editing/interaction. `open_file` and `save_file` return a selected path, or an empty string when cancelled. Check the result before reading/writing. `alert` displays a native modal message.

## Included applications

- `counter.hoo`: editable name, count state, increment/reset callbacks.
- `notepad.hoo`: multiline editor, UTF-8 saving, reload, optional CLI path.
- `editor.hoo`: multiline editor, native Open and Save As file dialogs, status updates and cancellation handling.
- `desktop-smoke.hoo`: automated native-control fixture. It creates controls, calls the same function installed as the button handler, reads its changed label, and exits without entering an event loop.

The ordinary language reference uses English names to explain tokens. Actual `.hoo` files contain exclusively hoo words.

## Packaging

`hoo hoooooo examples/editor.hoo --hoooooo build/HooEditor.app --hooooooo` creates a macOS application bundle containing a native executable and `Info.plist`. It can be launched by Finder or `open`. Use a new output path for each bundle build. Unsigned local bundles do not constitute a signed/notarized distribution package.

Linux output is a native executable linked against GTK 3. A distributor must also provide the relevant GTK runtime packages. `--hoooo` selects the dependency-free console runtime and rejects GUI calls at execution.

The compiler needs Python and Clang. An end user's compiled app does not need Python or the compiler checkout.
