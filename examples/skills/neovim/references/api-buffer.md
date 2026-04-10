# API_BUFFER

## TYPE_DEFINITIONS
* `Buffer` == `integer`
* `Window` == `integer`
* `LuaRef` == `function`
* `Dict` == `table<string, any>`
* `Array` == `any[]`
* `ExtmarkOpts` == `Dict`
* `ExtmarkFilterOpts` == `Dict`
* `BufAttachOpts` == `Dict`

## API_SIGNATURES

### LIFECYCLE_AND_STATE
* `nvim_create_buf(listed: boolean, scratch: boolean)` -> `Buffer`
* `nvim_buf_delete(buffer: Buffer, opts: {force?: boolean, unload?: boolean})` -> `void`
* `nvim_buf_is_valid(buffer: Buffer)` -> `boolean`
* `nvim_buf_is_loaded(buffer: Buffer)` -> `boolean`
* `nvim_buf_get_name(buffer: Buffer)` -> `string`
* `nvim_buf_set_name(buffer: Buffer, name: string)` -> `void`
* `nvim_buf_get_changedtick(buffer: Buffer)` -> `integer`
* `nvim_buf_line_count(buffer: Buffer)` -> `integer`
* `nvim_list_bufs()` -> `Buffer[]`
* `nvim_get_current_buf()` -> `Buffer`
* `nvim_set_current_buf(buffer: Buffer)` -> `void`

### TEXT_MANIPULATION
* `nvim_buf_get_lines(buffer: Buffer, start: integer, end: integer, strict_indexing: boolean)` -> `string[]`
* `nvim_buf_set_lines(buffer: Buffer, start: integer, end: integer, strict_indexing: boolean, replacement: string[])` -> `void`
* `nvim_buf_get_text(buffer: Buffer, start_row: integer, start_col: integer, end_row: integer, end_col: integer, opts: {})` -> `string[]`
* `nvim_buf_set_text(buffer: Buffer, start_row: integer, start_col: integer, end_row: integer, end_col: integer, replacement: string[])` -> `void`
* `nvim_buf_get_offset(buffer: Buffer, index: integer)` -> `integer`
* `nvim_get_current_line()` -> `string`
* `nvim_set_current_line(line: string)` -> `void`
* `nvim_del_current_line()` -> `void`
* `nvim_paste(data: string, crlf: boolean, phase: integer)` -> `boolean`
* `nvim_put(lines: string[], type: string, after: boolean, follow: boolean)` -> `void`

### EXTMARKS_AND_DECORATION
* `nvim_buf_set_extmark(buffer: Buffer, ns_id: integer, line: integer, col: integer, opts: ExtmarkOpts)` -> `integer`
* `nvim_buf_get_extmark_by_id(buffer: Buffer, ns_id: integer, id: integer, opts: {details?: boolean, hl_name?: boolean})` -> `[row: integer, col: integer, details?: Dict]`
* `nvim_buf_get_extmarks(buffer: Buffer, ns_id: integer, start: any, end: any, opts: ExtmarkFilterOpts)` -> `Array<[id, row, col, details?]>`
* `nvim_buf_del_extmark(buffer: Buffer, ns_id: integer, id: integer)` -> `boolean`
* `nvim_buf_clear_namespace(buffer: Buffer, ns_id: integer, line_start: integer, line_end: integer)` -> `void`

### EVENT_ATTACHMENT
* `nvim_buf_attach(buffer: Buffer, send_buffer: boolean, opts: BufAttachOpts)` -> `boolean`
* `nvim_buf_detach(buffer: Buffer)` -> `boolean`
* `nvim_buf_call(buffer: Buffer, fun: LuaRef)` -> `any`

### VARIABLES_AND_OPTIONS
* `nvim_buf_get_var(buffer: Buffer, name: string)` -> `any`
* `nvim_buf_set_var(buffer: Buffer, name: string, value: any)` -> `void`
* `nvim_buf_del_var(buffer: Buffer, name: string)` -> `void`
* `nvim_buf_get_option(buffer: Buffer, name: string)` -> `any`
* `nvim_buf_set_option(buffer: Buffer, name: string, value: any)` -> `void`

### KEYMAPS_AND_COMMANDS
* `nvim_buf_set_keymap(buffer: Buffer, mode: string, lhs: string, rhs: string, opts: Dict)` -> `void`
* `nvim_buf_get_keymap(buffer: Buffer, mode: string)` -> `Dict[]`
* `nvim_buf_del_keymap(buffer: Buffer, mode: string, lhs: string)` -> `void`
* `nvim_buf_create_user_command(buffer: Buffer, name: string, command: any, opts: Dict)` -> `void`
* `nvim_buf_del_user_command(buffer: Buffer, name: string)` -> `void`
* `nvim_buf_get_commands(buffer: Buffer, opts: Dict)` -> `Dict`

### MARKS
* `nvim_buf_set_mark(buffer: Buffer, name: string, line: integer, col: integer, opts: {})` -> `boolean`
* `nvim_buf_get_mark(buffer: Buffer, name: string)` -> `[row: integer, col: integer]`
* `nvim_buf_del_mark(buffer: Buffer, name: string)` -> `boolean`

### DEPRECATED_HIGHLIGHT_API
* `nvim_buf_add_highlight(buffer: Buffer, ns_id: integer, hl_group: string, line: integer, col_start: integer, col_end: integer)` -> `integer`
* `nvim_buf_clear_highlight(buffer: Buffer, ns_id: integer, line_start: integer, line_end: integer)` -> `void`
* `nvim_buf_set_virtual_text(buffer: Buffer, src_id: integer, line: integer, chunks: Array, opts: Dict)` -> `integer`

## OPTION_DICTIONARIES

### ExtmarkOpts
* `id`: `integer`
* `end_row`: `integer`
* `end_col`: `integer`
* `hl_group`: `string | integer | array`
* `hl_eol`: `boolean`
* `virt_text`: `Array<[text: string, hl_group: string | array]>`
* `virt_text_pos`: {`"eol"`, `"overlay"`, `"right_align"`, `"inline"`, `"eol_right_align"`}
* `virt_text_win_col`: `integer`
* `virt_text_hide`: `boolean`
* `virt_text_repeat_linebreak`: `boolean`
* `hl_mode`: {`"replace"`, `"combine"`, `"blend"`}
* `virt_lines`: `Array<Array<[text, hl_group]>>`
* `virt_lines_above`: `boolean`
* `virt_lines_leftcol`: `boolean`
* `virt_lines_overflow`: {`"trunc"`, `"scroll"`}
* `sign_text`: `string`
* `sign_hl_group`: `string`
* `number_hl_group`: `string`
* `line_hl_group`: `string`
* `cursorline_hl_group`: `string`
* `priority`: `integer`
* `ephemeral`: `boolean`
* `right_gravity`: `boolean`
* `end_right_gravity`: `boolean`
* `undo_restore`: `boolean`
* `invalidate`: `boolean`
* `strict`: `boolean`
* `conceal`: `string`
* `conceal_lines`: `string`
* `spell`: `boolean`
* `ui_watched`: `boolean`
* `url`: `string`

### ExtmarkFilterOpts
* `limit`: `integer`
* `details`: `boolean`
* `hl_name`: `boolean`
* `overlap`: `boolean`
* `type`: {`"highlight"`, `"sign"`, `"virt_text"`, `"virt_lines"`}

### BufAttachOpts
* `on_lines`: `function`
* `on_bytes`: `function`
* `on_changedtick`: `function`
* `on_detach`: `function`
* `on_reload`: `function`
* `utf_sizes`: `boolean`
* `preview`: `boolean`
