# API_HIGHLIGHT

## TYPE_DEFINITIONS
* `HlID` == `integer`
* `NS` == `integer` [0 == global_namespace]
* `Color` == `string | integer` [hex_string: "#RRGGBB", name: "Pink", alias: "fg"|"bg", or integer]
* `RGB` == `integer` [24-bit value]
* `Dict` == `table<string, any>`
* `Array` == `any[]`
* `HlDefinition` == `Dict`
* `GetHlOpts` == `Dict`
* `GetNsOpts` == `Dict`

## API_SIGNATURES

### HIGHLIGHT_DEFINITION_MANAGEMENT
* `nvim_set_hl(ns_id: NS, name: string, val: HlDefinition)` -> `void`
* `nvim_get_hl(ns_id: NS, opts: GetHlOpts)` -> `HlDefinition | table<string, HlDefinition>`
* `nvim_get_hl_id_by_name(name: string)` -> `HlID`

### NAMESPACE_AND_WINDOW_SCOPING
* `nvim_get_hl_ns(opts: GetNsOpts)` -> `NS`
* `nvim_set_hl_ns(ns_id: NS)` -> `void`
* `nvim_set_hl_ns_fast(ns_id: NS)` -> `void` @ [api-fast]
* `nvim_win_set_hl_ns(window: Window, ns_id: NS)` -> `void`

### COLOR_UTILITIES
* `nvim_get_color_by_name(name: string)` -> `RGB`
* `nvim_get_color_map()` -> `table<string, RGB>`

### BUFFER_LAYER_HIGHLIGHTS [LEGACY/DECORATION]
* `nvim_buf_add_highlight(buffer: Buffer, ns_id: NS, hl_group: string, line: integer, col_start: integer, col_end: integer)` -> `NS`
* `nvim_buf_clear_namespace(buffer: Buffer, ns_id: NS, line_start: integer, line_end: integer)` -> `void`

### DEPRECATED_METHODS
* `nvim_get_hl_by_id(hl_id: HlID, rgb: boolean)` -> `Dict` @ [deprecated: 9]
* `nvim_get_hl_by_name(name: string, rgb: boolean)` -> `Dict` @ [deprecated: 9]
* `nvim_buf_clear_highlight(buffer: Buffer, ns_id: NS, line_start: integer, line_end: integer)` -> `void` @ [deprecated: 7]

## OPTION_DICTIONARIES

### HlDefinition
* `fg`: `Color` [foreground_color]
* `bg`: `Color` [background_color]
* `sp`: `Color` [special_color]
* `fg_indexed`: `boolean` [fg_is_terminal_palette_index]
* `bg_indexed`: `boolean` [bg_is_terminal_palette_index]
* `blend`: `integer` [0...100]
* `bold`: `boolean`
* `standout`: `boolean`
* `underline`: `boolean`
* `undercurl`: `boolean`
* `underdouble`: `boolean`
* `underdotted`: `boolean`
* `underdashed`: `boolean`
* `strikethrough`: `boolean`
* `italic`: `boolean`
* `reverse`: `boolean`
* `nocombine`: `boolean` [do_not_combine_with_lower_priority_highlights]
* `link`: `string` [link_to_another_highlight_group]
* `default`: `boolean` [do_not_override_existing_definition]
* `ctermfg`: `integer | string`
* `ctermbg`: `integer | string`
* `cterm`: `table<string, boolean>` [cterm_attributes]
* `force`: `boolean` [force_update_even_if_exists]

### GetHlOpts
* `name`: `string` [target_group_name]
* `id`: `HlID` [target_group_id]
* `link`: `boolean` [default: true, return_link_name_instead_of_resolved_definition]
* `create`: `boolean` [default: true, create_group_if_missing]

### GetNsOpts
* `winid`: `Window` [retrieve_namespace_for_specific_window]

## CONSTANTS [HLF_T]
* `Normal`: {`HLF_NONE`}
* `SpecialKey`: {`HLF_8`}
* `EndOfBuffer`: {`HLF_EOB`}
* `TermCursor`: {`HLF_TERM`}
* `NonText`: {`HLF_AT`}
* `Directory`: {`HLF_D`}
* `ErrorMsg`: {`HLF_E`}
* `IncSearch`: {`HLF_I`}
* `Search`: {`HLF_L`}
* `CurSearch`: {`HLF_LC`}
* `MoreMsg`: {`HLF_M`}
* `ModeMsg`: {`HLF_CM`}
* `LineNr`: {`HLF_N`}
* `CursorLineNr`: {`HLF_CLN`}
* `StatusLine`: {`HLF_S`}
* `StatusLineNC`: {`HLF_SNC`}
* `WinSeparator`: {`HLF_C`}
* `Visual`: {`HLF_V`}
* `Folded`: {`HLF_FL`}
* `DiffAdd`: {`HLF_ADD`}
* `DiffChange`: {`HLF_CHD`}
* `DiffDelete`: {`HLF_DED`}
* `DiffText`: {`HLF_TXD`}
* `SignColumn`: {`HLF_SC`}
* `Pmenu`: {`HLF_PNI`}
* `PmenuSel`: {`HLF_PSI`}
* `NormalFloat`: {`HLF_NFLOAT`}
* `FloatBorder`: {`HLF_BORDER`}
