# API_WINDOW

## TYPE_DEFINITIONS
* `Window` == `integer`
* `Buffer` == `integer`
* `Tabpage` == `integer`
* `LuaRef` == `function`
* `Dict` == `table<string, any>`
* `Array` == `any[]`
* `Float` == `number`
* `WinConfigOpts` == `Dict`
* `WinConfigRetOpts` == `Dict`
* `WinTextHeightOpts` == `Dict`
* `WinTextHeightRet` == `Dict`

## API_SIGNATURES

### LIFECYCLE_AND_MANAGEMENT
* `nvim_open_win(buffer: Buffer, enter: boolean, config: WinConfigOpts)` -> `Window`
* `nvim_win_close(window: Window, force: boolean)` -> `void`
* `nvim_win_hide(window: Window)` -> `void`
* `nvim_list_wins()` -> `Window[]`
* `nvim_get_current_win()` -> `Window`
* `nvim_set_current_win(window: Window)` -> `void`
* `nvim_win_is_valid(window: Window)` -> `boolean`

### CONFIGURATION_AND_LAYOUT
* `nvim_win_set_config(window: Window, config: WinConfigOpts)` -> `void`
* `nvim_win_get_config(window: Window)` -> `WinConfigRetOpts`
* `nvim_win_get_width(window: Window)` -> `integer`
* `nvim_win_set_width(window: Window, width: integer)` -> `void`
* `nvim_win_get_height(window: Window)` -> `integer`
* `nvim_win_set_height(window: Window, height: integer)` -> `void`
* `nvim_win_get_position(window: Window)` -> `[row: integer, col: integer]`

### CONTEXT_AND_CURSOR
* `nvim_win_get_cursor(window: Window)` -> `[row: integer, col: integer]`
* `nvim_win_set_cursor(window: Window, pos: [integer, integer])` -> `void`
* `nvim_win_text_height(window: Window, opts: WinTextHeightOpts)` -> `WinTextHeightRet`
* `nvim_win_call(window: Window, fun: LuaRef)` -> `any`
* `nvim_win_get_tabpage(window: Window)` -> `Tabpage`
* `nvim_win_get_number(window: Window)` -> `integer`

### BUFFER_BINDING
* `nvim_win_get_buf(window: Window)` -> `Buffer`
* `nvim_win_set_buf(window: Window, buffer: Buffer)` -> `void`

### VARIABLES_AND_STYLING
* `nvim_win_get_var(window: Window, name: string)` -> `any`
* `nvim_win_set_var(window: Window, name: string, value: any)` -> `void`
* `nvim_win_del_var(window: Window, name: string)` -> `void`
* `nvim_win_set_hl_ns(window: Window, ns_id: integer)` -> `void`

### DEPRECATED_OPTIONS_API
* `nvim_win_get_option(window: Window, name: string)` -> `any`
* `nvim_win_set_option(window: Window, name: string, value: any)` -> `void`

## OPTION_DICTIONARIES

### WinConfigOpts
* `relative`: {`"editor"`, `"win"`, `"cursor"`, `"mouse"`, `"tabline"`, `"laststatus"`, `""`}
* `win`: `Window`
* `anchor`: {`"NW"`, `"NE"`, `"SW"`, `"SE"`}
* `row`: `Float`
* `col`: `Float`
* `bufpos`: `[line: integer, column: integer]`
* `zindex`: `integer`
* `width`: `integer`
* `height`: `integer`
* `split`: {`"left"`, `"right"`, `"above"`, `"below"`}
* `vertical`: `boolean`
* `focusable`: `boolean`
* `external`: `boolean`
* `noautocmd`: `boolean`
* `fixed`: `boolean`
* `hide`: `boolean`
* `mouse`: `boolean`
* `style`: {`"minimal"`, `""`}
* `border`: {`"none"`, `"single"`, `"double"`, `"rounded"`, `"solid"`, `"shadow"`} | `string[]` | `Array<[char: string, hl_group: string]>`
* `title`: `string` | `Array<[text: string, hl_group: string]>`
* `title_pos`: {`"left"`, `"center"`, `"right"`}
* `footer`: `string` | `Array<[text: string, hl_group: string]>`
* `footer_pos`: {`"left"`, `"center"`, `"right"`}
* `_cmdline_offset`: `integer`

### WinConfigRetOpts
* `relative`: `string`
* `win`: `Window`
* `anchor`: `string`
* `row`: `Float`
* `col`: `Float`
* `bufpos`: `[integer, integer]`
* `zindex`: `integer`
* `width`: `integer`
* `height`: `integer`
* `split`: `string`
* `vertical`: `boolean`
* `focusable`: `boolean`
* `external`: `boolean`
* `fixed`: `boolean`
* `hide`: `boolean`
* `mouse`: `boolean`
* `style`: `string`
* `border`: `string | Array<[string, string]>`
* `title`: `Array<[string, string]>`
* `title_pos`: `string`
* `footer`: `Array<[string, string]>`
* `footer_pos`: `string`

### WinTextHeightOpts
* `start_row`: `integer`
* `end_row`: `integer`
* `start_vcol`: `integer`
* `end_vcol`: `integer`
* `max_height`: `integer`

### WinTextHeightRet
* `all`: `integer`
* `fill`: `integer`
* `end_row`: `integer`
* `end_vcol`: `integer`
