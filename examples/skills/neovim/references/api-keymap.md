# API_KEYMAP

## TYPE_DEFINITIONS
* `Buffer` == `integer`
* `LuaRef` == `function`
* `Dict` == `table<string, any>`
* `Array` == `any[]`
* `KeymapOpts` == `Dict`
* `KeymapRet` == `Dict`
* `MarkOpts` == `Dict`

## API_SIGNATURES

### GLOBAL_KEYMAPS
* `nvim_set_keymap(mode: string, lhs: string, rhs: string, opts: KeymapOpts)` -> `void`
* `nvim_get_keymap(mode: string)` -> `Array<KeymapRet>`
* `nvim_del_keymap(mode: string, lhs: string)` -> `void`

### BUFFER_KEYMAPS
* `nvim_buf_set_keymap(buffer: Buffer, mode: string, lhs: string, rhs: string, opts: KeymapOpts)` -> `void`
* `nvim_buf_get_keymap(buffer: Buffer, mode: string)` -> `Array<KeymapRet>`
* `nvim_buf_del_keymap(buffer: Buffer, mode: string, lhs: string)` -> `void`

### INPUT_AND_KEYCODES
* `nvim_feedkeys(keys: string, mode: string, escape_ks: boolean)` -> `void`
* `nvim_input(keys: string)` -> `integer`
* `nvim_input_mouse(button: string, action: string, modifier: string, grid: integer, row: integer, col: integer)` -> `void`
* `nvim_replace_termcodes(str: string, from_part: boolean, do_lt: boolean, special: boolean)` -> `string`

### MARKS
* `nvim_set_mark(name: string, line: integer, col: integer, opts: MarkOpts)` -> `boolean`
* `nvim_get_mark(name: string, opts: MarkOpts)` -> `[row: integer, col: integer, buffer: Buffer, buffername: string]`
* `nvim_del_mark(name: string)` -> `boolean`
* `nvim_buf_set_mark(buffer: Buffer, name: string, line: integer, col: integer, opts: MarkOpts)` -> `boolean`
* `nvim_buf_get_mark(buffer: Buffer, name: string)` -> `[row: integer, col: integer]`
* `nvim_buf_del_mark(buffer: Buffer, name: string)` -> `boolean`

## OPTION_DICTIONARIES

### KeymapOpts
* `nowait`: `boolean`
* `noremap`: `boolean`
* `silent`: `boolean`
* `script`: `boolean`
* `expr`: `boolean`
* `unique`: `boolean`
* `callback`: `LuaRef`
* `desc`: `string`
* `replace_keycodes`: `boolean`

### KeymapRet
* `lhs`: `string`
* `lhsraw`: `string`
* `lhsrawalt`: `string`
* `rhs`: `string`
* `callback`: `LuaRef`
* `desc`: `string`
* `noremap`: `integer`
* `script`: `integer`
* `expr`: `integer`
* `silent`: `integer`
* `sid`: `integer`
* `scriptversion`: `integer`
* `lnum`: `integer`
* `buffer`: `integer`
* `nowait`: `integer`
* `replace_keycodes`: `integer`
* `mode`: `string`
* `abbr`: `integer`
* `mode_bits`: `integer`

### FeedkeysMode
* `m`: {remap_keys, default}
* `n`: {do_not_remap}
* `t`: {handle_as_typed}
* `i`: {insert_mode_behavior}
* `x`: {execute_commands_sync}
* `!`: {do_not_end_insert}
* `L`: {low_level_input}

### MouseButton
* `button`: {`"left"`, `"right"`, `"middle"`, `"wheel"`, `"move"`, `"x1"`, `"x2"`}

### MouseAction
* `action`: {`"press"`, `"drag"`, `"release"`, `"up"`, `"down"`, `"left"`, `"right"`}
