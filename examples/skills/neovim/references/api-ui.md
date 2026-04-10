# API_UI

## TYPE_DEFINITIONS
* `Window` == `integer`
* `Buffer` == `integer`
* `Tabpage` == `integer`
* `Object` == `any`
* `Dict` == `table<string, any>`
* `Array` == `any[]`
* `Integer` == `integer`
* `Float` == `number`
* `Boolean` == `boolean`
* `String` == `string`
* `Color` == `integer` (24-bit RGB or 0-255 terminal index)
* `HlAttrs` == `Dict` (Highlight attributes)

## RPC_METHODS (Client -> Nvim)
* `nvim_ui_attach(width: Integer, height: Integer, options: Dict)` -> `void`
* `nvim_ui_detach()` -> `void`
* `nvim_ui_try_resize(width: Integer, height: Integer)` -> `void`
* `nvim_ui_set_option(name: String, value: Object)` -> `void`
* `nvim_ui_try_resize_grid(grid: Integer, width: Integer, height: Integer)` -> `void`
* `nvim_ui_pum_set_height(height: Integer)` -> `void`
* `nvim_ui_pum_set_bounds(width: Float, height: Float, row: Float, col: Float)` -> `void`
* `nvim_ui_set_focus(gained: Boolean)` -> `void`
* `nvim_ui_send(content: String)` -> `void`
* `nvim_ui_term_event(event: String, value: Object)` -> `void`
* `nvim_list_uis()` -> `Array`
* `nvim_select_popupmenu_item(item: Integer, insert: Boolean, finish: Boolean, opts: Dict)` -> `void`
* `nvim_eval_statusline(str: String, opts: Dict)` -> `Dict`

## UI_OPTIONS (nvim_ui_attach)
* `rgb`: `Boolean` (default: `true`) => 24-bit RGB colors
* `override`: `Boolean` (default: `false`) => Force capability activation
* `ext_cmdline`: `Boolean` => Externalize command line
* `ext_popupmenu`: `Boolean` => Externalize completion menu
* `ext_tabline`: `Boolean` => Externalize tabline
* `ext_wildmenu`: `Boolean` => Externalize wildmenu
* `ext_messages`: `Boolean` => Externalize messages (implies `ext_linegrid`, `ext_cmdline`)
* `ext_linegrid`: `Boolean` => Use grid-based events (replaces legacy `put`)
* `ext_multigrid`: `Boolean` => Per-window grids (implies `ext_linegrid`)
* `ext_hlstate`: `Boolean` => Detailed highlight state (implies `ext_linegrid`)
* `ext_termcolors`: `Boolean` => Use external default colors
* `term_name`: `String` => Sets `'term'`
* `term_colors`: `Integer` => Sets `'t_Co'`
* `stdin_fd`: `Integer` => Read buffer 1 from specific FD
* `stdin_tty`: `Boolean` => Stdin is TTY
* `stdout_tty`: `Boolean` => Stdout is TTY

## REDRAW_EVENTS (Nvim -> Client Notification)
*Method: `redraw`, Params: `Array<[event_name: String, ...args]>`*

### GLOBAL_EVENTS
* `["set_title", title: String]`
* `["set_icon", icon: String]`
* `["mode_info_set", cursor_style_enabled: Boolean, mode_info: Array]`
* `["option_set", name: String, value: Object]`
* `["chdir", path: String]`
* `["mode_change", mode: String, mode_idx: Integer]`
* `["mouse_on"]`
* `["mouse_off"]`
* `["busy_start"]`
* `["busy_stop"]`
* `["suspend"]`
* `["update_menu"]`
* `["bell"]`
* `["visual_bell"]`
* `["flush"]`
* `["ui_send", content: String]`

### LINEGRID_EVENTS (ext_linegrid == true)
* `["grid_resize", grid: Integer, width: Integer, height: Integer]`
* `["default_colors_set", rgb_fg: Color, rgb_bg: Color, rgb_sp: Color, cterm_fg: Integer, cterm_bg: Integer]`
* `["hl_attr_define", id: Integer, rgb_attrs: HlAttrs, cterm_attrs: HlAttrs, info: Array]`
* `["hl_group_set", name: String, id: Integer]`
* `["grid_line", grid: Integer, row: Integer, col_start: Integer, cells: Array<[text: String, hl_id: Integer?, repeat: Integer?]>, wrap: Boolean]`
* `["grid_clear", grid: Integer]`
* `["grid_cursor_goto", grid: Integer, row: Integer, col: Integer]`
* `["grid_scroll", grid: Integer, top: Integer, bot: Integer, left: Integer, right: Integer, rows: Integer, cols: Integer]`
* `["grid_destroy", grid: Integer]`

### MULTIGRID_EVENTS (ext_multigrid == true)
* `["win_pos", grid: Integer, win: Window, start_row: Integer, start_col: Integer, width: Integer, height: Integer]`
* `["win_float_pos", grid: Integer, win: Window, anchor: String, anchor_grid: Integer, row: Float, col: Float, focusable: Boolean, zindex: Integer, compindex: Integer, screen_row: Integer, screen_col: Integer]`
* `["win_external_pos", grid: Integer, win: Window]`
* `["win_hide", grid: Integer]`
* `["win_close", grid: Integer]`
* `["win_viewport", grid: Integer, win: Window, topline: Integer, botline: Integer, curline: Integer, curcol: Integer, line_count: Integer, scroll_delta: Integer]`
* `["win_viewport_margins", grid: Integer, win: Window, top: Integer, bottom: Integer, left: Integer, right: Integer]`
* `["win_extmark", grid: Integer, win: Window, ns_id: Integer, mark_id: Integer, row: Integer, col: Integer]`
* `["msg_set_pos", grid: Integer, row: Integer, scrolled: Boolean, sep_char: String, zindex: Integer, compindex: Integer]`

### CMDLINE_EVENTS (ext_cmdline == true)
* `["cmdline_show", content: Array<[hl_id: Integer, text: String]>, pos: Integer, firstc: String, prompt: String, indent: Integer, level: Integer, hl_id: Integer]`
* `["cmdline_pos", pos: Integer, level: Integer]`
* `["cmdline_special_char", c: String, shift: Boolean, level: Integer]`
* `["cmdline_hide", level: Integer, abort: Boolean]`
* `["cmdline_block_show", lines: Array<Array<[hl_id: Integer, text: String]>>]`
* `["cmdline_block_append", line: Array<[hl_id: Integer, text: String]>]`
* `["cmdline_block_hide"]`

### POPUPMENU_EVENTS (ext_popupmenu == true)
* `["popupmenu_show", items: Array<[word: String, kind: String, menu: String, info: String]>, selected: Integer, row: Integer, col: Integer, grid: Integer]`
* `["popupmenu_select", selected: Integer]`
* `["popupmenu_hide"]`

### TABLINE_EVENTS (ext_tabline == true)
* `["tabline_update", curtab: Tabpage, tabs: Array<Dict>, curbuf: Buffer, buffers: Array<Dict>]`

### MESSAGE_EVENTS (ext_messages == true)
* `["msg_show", kind: String, content: Array<[hl_id: Integer, text: String]>, replace_last: Boolean, history: Boolean, append: Boolean, msg_id: Object]`
* `["msg_clear"]`
* `["msg_showmode", content: Array]`
* `["msg_showcmd", content: Array]`
* `["msg_ruler", content: Array]`
* `["msg_history_show", entries: Array<[kind: String, content: Array, append: Boolean]>, prev_cmd: Boolean]`
* `["msg_history_clear"]`

### LEGACY_GRID_EVENTS (ext_linegrid == false)
* `["resize", width: Integer, height: Integer]`
* `["clear"]`
* `["eol_clear"]`
* `["cursor_goto", row: Integer, col: Integer]`
* `["update_fg", color: Color]`
* `["update_bg", color: Color]`
* `["update_sp", color: Color]`
* `["highlight_set", attrs: HlAttrs]`
* `["put", text: String]`
* `["set_scroll_region", top: Integer, bot: Integer, left: Integer, right: Integer]`
* `["scroll", count: Integer]`

## DATA_STRUCTURES

### HlAttrs
* `foreground`: `Integer`
* `background`: `Integer`
* `special`: `Integer`
* `reverse`: `Boolean`
* `italic`: `Boolean`
* `bold`: `Boolean`
* `strikethrough`: `Boolean`
* `underline`: `Boolean`
* `undercurl`: `Boolean`
* `underdouble`: `Boolean`
* `underdotted`: `Boolean`
* `underdashed`: `Boolean`
* `altfont`: `Boolean`
* `blend`: `Integer` (0-100)
* `url`: `String`

### ModeInfo
* `cursor_shape`: {`"block"`, `"horizontal"`, `"vertical"`}
* `cell_percentage`: `Integer`
* `blinkwait`: `Integer`
* `blinkon`: `Integer`
* `blinkoff`: `Integer`
* `attr_id`: `Integer`
* `attr_id_lm`: `Integer`
* `short_name`: `String`
* `name`: `String`

## SPECIAL_EVENTS
* `["error_exit", status: Integer]` => Server exit notification.
