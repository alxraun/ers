# LUA_DIAGNOSTIC

## TYPE_DEFINITIONS
* `Namespace` == `integer`
* `Buffer` == `integer`
* `Window` == `integer`
* `Severity` == `1|2|3|4` @see `SEVERITY_ENUM`
* `SeverityFilter` == `Severity | Severity[] | {min: Severity, max: Severity}`
* `Diagnostic` == `table` {`bufnr`, `lnum`, `col`, `end_lnum`, `end_col`, `severity`, `message`, `source`, `code`, `user_data`, `namespace`}
* `DiagnosticSet` == `Omit<Diagnostic, "bufnr"|"namespace">`
* `DiagnosticFilter` == `table` {`ns_id?`, `bufnr?`}
* `GetOpts` == `table` {`namespace?`, `lnum?`, `severity?`, `enabled?`}
* `JumpOpts` == `GetOpts` + {`diagnostic?`, `count?`, `pos?`, `wrap?`, `on_jump?`, `winid?`}
* `Handler` == `table` {`show: fun(ns, bufnr, diags, opts)`, `hide: fun(ns, bufnr)`}

## SEVERITY_ENUM
* `vim.diagnostic.severity.ERROR` == `1`
* `vim.diagnostic.severity.WARN`  == `2`
* `vim.diagnostic.severity.INFO`  == `3`
* `vim.diagnostic.severity.HINT`  == `4`

## API_SIGNATURES

### CORE_OPERATIONS
* `vim.diagnostic.set(namespace: Namespace, bufnr: Buffer, diagnostics: DiagnosticSet[], opts?: Opts)` -> `void`
* `vim.diagnostic.get(bufnr?: Buffer, opts?: GetOpts)` -> `Diagnostic[]`
* `vim.diagnostic.count(bufnr?: Buffer, opts?: GetOpts)` -> `table<Severity, integer>`
* `vim.diagnostic.reset(namespace?: Namespace, bufnr?: Buffer)` -> `void`

### CONFIGURATION_AND_CONTROL
* `vim.diagnostic.config(opts?: Opts, namespace?: Namespace)` -> `Opts|void`
* `vim.diagnostic.enable(enable?: boolean, filter?: DiagnosticFilter)` -> `void`
* `vim.diagnostic.is_enabled(filter?: DiagnosticFilter)` -> `boolean`
* `vim.diagnostic.get_namespace(namespace: Namespace)` -> `NS_Metadata`
* `vim.diagnostic.get_namespaces()` -> `table<Namespace, NS_Metadata>`

### VISUALIZATION_HANDLERS
* `vim.diagnostic.show(namespace?: Namespace, bufnr?: Buffer, diagnostics?: Diagnostic[], opts?: Opts)` -> `void`
* `vim.diagnostic.hide(namespace?: Namespace, bufnr?: Buffer)` -> `void`
* `vim.diagnostic.open_float(opts?: FloatOpts)` -> `[float_bufnr: integer, winid: integer]`
* `vim.diagnostic.status(bufnr?: Buffer)` -> `string` [format: `E:n W:n ...`]

### NAVIGATION
* `vim.diagnostic.jump(opts: JumpOpts)` -> `Diagnostic?`
* `vim.diagnostic.get_next(opts?: JumpOpts)` -> `Diagnostic?`
* `vim.diagnostic.get_prev(opts?: JumpOpts)` -> `Diagnostic?`

### INTEROP_AND_PARSING
* `vim.diagnostic.toqflist(diagnostics: Diagnostic[])` -> `QuickfixItem[]`
* `vim.diagnostic.setqflist(opts?: ListOpts)` -> `void`
* `vim.diagnostic.setloclist(opts?: ListOpts)` -> `void`
* `vim.diagnostic.fromqflist(list: QuickfixItem[], opts?: {merge_lines: boolean})` -> `Diagnostic[]`
* `vim.diagnostic.match(str: string, pat: string, groups: string[], severity_map: table, defaults?: table)` -> `Diagnostic?`

## OPTION_DICTIONARIES

### Opts (Global/Namespace Config)
* `underline`: `boolean | UnderlineOpts | function`
* `virtual_text`: `boolean | VirtualTextOpts | function`
* `virtual_lines`: `boolean | VirtualLinesOpts | function`
* `signs`: `boolean | SignsOpts | function`
* `float`: `boolean | FloatOpts | function`
* `status`: `{text: table<Severity, string>}`
* `update_in_insert`: `boolean`
* `severity_sort`: `boolean | {reverse?: boolean}`
* `jump`: `JumpOpts`

### FloatOpts (Extends `open_floating_preview.Opts`)
* `scope`: {`"line"`, `"buffer"`, `"cursor"`, `"c"`, `"l"`, `"b"`}
* `pos`: `integer | [row, col]`
* `severity_sort`: `boolean | {reverse?: boolean}`
* `severity`: `SeverityFilter`
* `header`: `string | [text, hl_group]`
* `source`: `boolean | "if_many"`
* `format`: `fun(diag: Diagnostic): string?`
* `prefix`: `string | table | fun(diag, i, total): (string, string)`
* `suffix`: `string | table | fun(diag, i, total): (string, string)`
* `bufnr`: `Buffer`
* `focus_id`: `string`

### VirtualTextOpts
* `severity`: `SeverityFilter`
* `current_line`: `boolean`
* `source`: `boolean | "if_many"`
* `spacing`: `integer`
* `prefix`: `string | fun(diag, i, total): string`
* `suffix`: `string | fun(diag): string`
* `format`: `fun(diag: Diagnostic): string?`
* `hl_mode`: {`"replace"`, `"combine"`, `"blend"`}
* `virt_text_pos`: {`"eol"`, `"eol_right_align"`, `"inline"`, `"overlay"`, `"right_align"`}
* `virt_text_win_col`: `integer`
* `virt_text_hide`: `boolean`

### SignsOpts
* `severity`: `SeverityFilter`
* `priority`: `integer` [default: 10]
* `text`: `table<Severity, string>`
* `numhl`: `table<Severity, string>`
* `linehl`: `table<Severity, string>`

## HIGHLIGHT_GROUPS
* `DiagnosticError` / `DiagnosticWarn` / `DiagnosticInfo` / `DiagnosticHint`
* `DiagnosticVirtualText{Severity}`
* `DiagnosticUnderline{Severity}`
* `DiagnosticFloating{Severity}`
* `DiagnosticSign{Severity}`
* `DiagnosticUnnecessary` [via `_tags.unnecessary`]
* `DiagnosticDeprecated` [via `_tags.deprecated`]

## EVENTS
* `DiagnosticChanged` == {`bufnr`: `integer`, `data`: {`diagnostics`: `Diagnostic[]` }}
