# API_EXTMARK

## TYPE_DEFINITIONS
* `Buffer` == `integer` | `0`
* `Namespace` == `integer`
* `ExtmarkId` == `integer`
* `Window` == `integer`
* `LuaRef` == `function`
* `HlGroup` == `string` | `integer`
* `Position` == `[row: integer, col: integer]`
* `ExtmarkRange` == `Position` | `ExtmarkId` | `0` | `-1`
* `VirtTextChunk` == `[text: string, highlight: HlGroup | HlGroup[]]`
* `VirtText` == `VirtTextChunk[]`
* `VirtLine` == `VirtText`
* `VirtLines` == `VirtLine[]`
* `ExtmarkDetails` == `table<string, any>`

## API_SIGNATURES

### NAMESPACE_MANAGEMENT
* `nvim_create_namespace(name: string)` -> `Namespace`
* `nvim_get_namespaces()` -> `table<string, Namespace>`
* `nvim__ns_set(ns_id: Namespace, opts: NsOpts)` -> `void`
* `nvim__ns_get(ns_id: Namespace)` -> `NsOpts`

### EXTMARK_CRUD
* `nvim_buf_set_extmark(buffer: Buffer, ns_id: Namespace, line: integer, col: integer, opts: SetExtmarkOpts)` -> `ExtmarkId`
* `nvim_buf_get_extmark_by_id(buffer: Buffer, ns_id: Namespace, id: ExtmarkId, opts: GetExtmarkOpts)` -> `[row: integer, col: integer, details: ExtmarkDetails?]`
* `nvim_buf_get_extmarks(buffer: Buffer, ns_id: Namespace, start: ExtmarkRange, end: ExtmarkRange, opts: GetExtmarksOpts)` -> `[id: ExtmarkId, row: integer, col: integer, details: ExtmarkDetails?][]`
* `nvim_buf_del_extmark(buffer: Buffer, ns_id: Namespace, id: ExtmarkId)` -> `boolean`
* `nvim_buf_clear_namespace(buffer: Buffer, ns_id: Namespace, line_start: integer, line_end: integer)` -> `void`

### DECORATION_PROVIDER
* `nvim_set_decoration_provider(ns_id: Namespace, opts: DecorProviderOpts)` -> `void`

## OPTION_DICTIONARIES

### SetExtmarkOpts
* `id`: `ExtmarkId` @ [move_existing_if_provided]
* `end_row`: `integer` @ [0_indexed_inclusive]
* `end_col`: `integer` @ [0_indexed_exclusive]
* `hl_group`: `HlGroup | HlGroup[]`
* `hl_eol`: `boolean`
* `virt_text`: `VirtText`
* `virt_text_pos`: {`"eol"`, `"overlay"`, `"right_align"`, `"eol_right_align"`, `"inline"`}
* `virt_text_win_col`: `integer`
* `virt_text_hide`: `boolean`
* `virt_text_repeat_linebreak`: `boolean`
* `hl_mode`: {`"replace"`, `"combine"`, `"blend"`}
* `virt_lines`: `VirtLines`
* `virt_lines_above`: `boolean`
* `virt_lines_leftcol`: `boolean`
* `virt_lines_overflow`: {`"trunc"`, `"scroll"`}
* `ephemeral`: `boolean` @ [requires: nvim_set_decoration_provider]
* `right_gravity`: `boolean` @ [default: true]
* `end_right_gravity`: `boolean` @ [default: false]
* `undo_restore`: `boolean` @ [default: true]
* `invalidate`: `boolean`
* `priority`: `integer` @ [0...65535]
* `strict`: `boolean` @ [default: true]
* `sign_text`: `string` @ [max_length: 2]
* `sign_hl_group`: `HlGroup`
* `number_hl_group`: `HlGroup`
* `line_hl_group`: `HlGroup`
* `cursorline_hl_group`: `HlGroup`
* `conceal`: `string` @ [max_length: 1]
* `conceal_lines`: `string` @ [must_be_empty_string]
* `spell`: `boolean`
* `ui_watched`: `boolean`
* `url`: `string` @ [OSC_8_hyperlink]

### GetExtmarkOpts
* `details`: `boolean`
* `hl_name`: `boolean` @ [default: true]

### GetExtmarksOpts
* `limit`: `integer`
* `details`: `boolean`
* `hl_name`: `boolean` @ [default: true]
* `overlap`: `boolean`
* `type`: {`"highlight"`, `"sign"`, `"virt_text"`, `"virt_lines"`}

### DecorProviderOpts
* `on_start`: `function(name: string, tick: integer)` -> `boolean?`
* `on_buf`: `function(name: string, bufnr: integer, tick: integer)` -> `boolean?`
* `on_win`: `function(name: string, winid: Window, bufnr: integer, toprow: integer, botrow: integer)` -> `boolean?`
* `on_line`: `function(name: string, winid: Window, bufnr: integer, row: integer)` -> `void` @ [deprecated: use_on_range]
* `on_range`: `function(name: string, winid: Window, bufnr: integer, start_row: integer, start_col: integer, end_row: integer, end_col: integer)` -> `boolean | [skip_row: integer, skip_col: integer]`
* `on_end`: `function(name: string, tick: integer)` -> `void`

### NsOpts
* `wins`: `Window[]` @ [scoping_to_specific_windows]

## ENUM_LITERALS

### VirtTextPos
* `kVPosEndOfLine` == `"eol"`
* `kVPosEndOfLineRightAlign` == `"eol_right_align"`
* `kVPosInline` == `"inline"`
* `kVPosOverlay` == `"overlay"`
* `kVPosRightAlign` == `"right_align"`
* `kVPosWinCol` == `"virt_text_win_col"`

### HlMode
* `kHlModeReplace` == `"replace"`
* `kHlModeCombine` == `"combine"`
* `kHlModeBlend` == `"blend"`

### ExtmarkTypeFilter
* `kExtmarkSign` == `"sign"`
* `kExtmarkVirtText` == `"virt_text"`
* `kExtmarkVirtLines` == `"virt_lines"`
* `kExtmarkHighlight` == `"highlight"`
