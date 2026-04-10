# API_TABPAGE

## TYPE_DEFINITIONS
* `Tabpage` == `integer` | `handle`
* `Window` == `integer` | `handle`
* `String` == `string`
* `Object` == `any`
* `Integer` == `number`
* `Boolean` == `boolean`
* `Array` == `any[]`
* `Error` == `pointer` @ [internal_only]

## API_SIGNATURES

### GLOBAL_MANAGEMENT
* `nvim_list_tabpages()` -> `Tabpage[]`
* `nvim_get_current_tabpage()` -> `Tabpage`
* `nvim_set_current_tabpage(tabpage: Tabpage)` -> `void`
    * constraints: [!textlock], [!cmdwin]
* `nvim_win_get_tabpage(window: Window)` -> `Tabpage`
    * usage: `0` => `current_window`

### TABPAGE_PROPERTIES
* `nvim_tabpage_get_number(tabpage: Tabpage)` -> `Integer`
    * usage: `0` => `current_tabpage`
* `nvim_tabpage_is_valid(tabpage: Tabpage)` -> `Boolean`
    * usage: `0` => `current_tabpage`

### WINDOW_MANAGEMENT_IN_TAB
* `nvim_tabpage_list_wins(tabpage: Tabpage)` -> `Window[]`
    * usage: `0` => `current_tabpage`
* `nvim_tabpage_get_win(tabpage: Tabpage)` -> `Window`
    * logic: returns `tp_curwin` for target `tabpage`
    * usage: `0` => `current_tabpage`
* `nvim_tabpage_set_win(tabpage: Tabpage, win: Window)` -> `void`
    * since: 0.10.0
    * constraints: `win` must belong to `tabpage`
    * logic: `tabpage == curtab` => `win_goto(wp)` | `else` => `tp_curwin = wp`

### VARIABLE_SCOPING_(t:)
* `nvim_tabpage_get_var(tabpage: Tabpage, name: String)` -> `Object`
* `nvim_tabpage_set_var(tabpage: Tabpage, name: String, value: Object)` -> `void`
* `nvim_tabpage_del_var(tabpage: Tabpage, name: String)` -> `void`

## INTERNAL_STRUCTURE_MAPPING
* `tabpage_T` {
    * `handle`: `handle_T`
    * `tp_next`: `tabpage_T*`
    * `tp_curwin`: `win_T*`
    * `tp_prevwin`: `win_T*`
    * `tp_firstwin`: `win_T*`
    * `tp_lastwin`: `win_T*`
    * `tp_vars`: `dict_T*` @ [t:_variables]
    * `tp_topframe`: `frame_T*` @ [layout_tree]
}

## DEPRECATED_METHODS_AND_ALIASES
* `tabpage_get_windows(tabpage: Tabpage)` ~ `nvim_tabpage_list_wins`
* `tabpage_get_var(tabpage: Tabpage, name: String)` ~ `nvim_tabpage_get_var`
* `tabpage_set_var(tabpage: Tabpage, name: String, value: Object)` ~ `nvim_tabpage_set_var`
* `tabpage_del_var(tabpage: Tabpage, name: String)` ~ `nvim_tabpage_del_var`
* `tabpage_get_window(tabpage: Tabpage)` ~ `nvim_tabpage_get_win`
* `tabpage_is_valid(tabpage: Tabpage)` ~ `nvim_tabpage_is_valid`
* `vim_get_tabpages()` ~ `nvim_list_tabpages`
* `vim_get_current_tabpage()` ~ `nvim_get_current_tabpage`
* `vim_set_current_tabpage(tabpage: Tabpage)` ~ `nvim_set_current_tabpage`
* `window_get_tabpage(window: Window)` ~ `nvim_win_get_tabpage`

## CONSTANTS_AND_BEHAVIORS
* `TABPAGE_ID_CURRENT` == `0`
* `WINDOW_ID_CURRENT` == `0`
* `handle_persistence` == `true` @ [lifetime_of_tab]
* `order` == `1_indexed_display` | `0_indexed_api_handles`
