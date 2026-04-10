# API_OPTIONS

## TYPE_DEFINITIONS
* `Buffer` == `integer`
* `Window` == `integer`
* `Object` == `any`
* `Dict` == `table<string, any>`
* `Array` == `any[]`
* `OptionValue` == `string | integer | boolean`
* `OptionInfo` == `Dict`
* `OptionOpts` == `Dict`

## API_SIGNATURES

### CORE_OPTION_VAL_API
* `nvim_get_option_value(name: string, opts: OptionOpts)` -> `OptionValue`
* `nvim_set_option_value(name: string, value: OptionValue, opts: OptionOpts)` -> `void`

### OPTION_METADATA_API
* `nvim_get_option_info2(name: string, opts: OptionOpts)` -> `OptionInfo`
* `nvim_get_all_options_info()` -> `table<string, OptionInfo>`

### DEPRECATED_GLOBAL_API
* `nvim_get_option(name: string)` -> `Object` @deprecated {use: `nvim_get_option_value`}
* `nvim_set_option(name: string, value: Object)` -> `void` @deprecated {use: `nvim_set_option_value`}
* `nvim_get_option_info(name: string)` -> `OptionInfo` @deprecated {use: `nvim_get_option_info2`}

### DEPRECATED_SCOPED_API
* `nvim_buf_get_option(buffer: Buffer, name: string)` -> `Object` @deprecated {use: `nvim_get_option_value`}
* `nvim_buf_set_option(buffer: Buffer, name: string, value: Object)` -> `void` @deprecated {use: `nvim_set_option_value`}
* `nvim_win_get_option(window: Window, name: string)` -> `Object` @deprecated {use: `nvim_get_option_value`}
* `nvim_win_set_option(window: Window, name: string, value: Object)` -> `void` @deprecated {use: `nvim_set_option_value`}

## OPTION_DICTIONARIES

### OptionOpts
* `scope`: {`"global"`, `"local"`} @analogous_to {|:setglobal|, |:setlocal|}
* `win`: `Window` @context {window-local_options}
* `buf`: `integer` @context {buffer-local_options} => {implied_scope: "local"}
* `filetype`: `string` @behavior {triggers: [ftplugin, FileType_autocmds]} @constraints [get_only, !combined_with_other_keys]

### OptionInfo
* `name`: `string` @example `"filetype"`
* `shortname`: `string` @example `"ft"`
* `type`: {`"string"`, `"number"`, `"boolean"`}
* `default`: `OptionValue`
* `was_set`: `boolean`
* `last_set_sid`: `integer`
* `last_set_linenr`: `integer`
* `last_set_chan`: `integer` @note {0_for_local}
* `scope`: {`"global"`, `"win"`, `"buf"`}
* `global_local`: `boolean` @definition {option_has_global_value}
* `commalist`: `boolean` @definition {is_comma_separated_list}
* `flaglist`: `boolean` @definition {is_single_char_flag_list}
* `allows_duplicates`: `boolean` @flag [!kOptFlagNoDup]

## SYSTEM_BEHAVIOR_CONTRACTS

### RESOLUTION_LOGIC
* `nvim_get_option_value` => {
    1. IF `opts.scope` == "local" -> return_local
    2. IF `opts.scope` == "global" -> return_global
    3. IF !`opts.scope` -> return_local_if_exists || return_global
}

### SCOPE_INTERACTION_RULES
* `set_option` + `scope: "local"` + `global-local_option` => {sets_local_value_only}
* `set_option` + `!scope` + `global-local_option` => {sets_both_global_and_local}
* `win` + `buf` keys => {forbidden_in_same_dict}

### INTERNAL_FLAGS [OptFlags]
* `kOptFlagExpand`: {environment_variable_expansion_allowed}
* `kOptFlagSecure`: {prohibited_in_modeline_or_sandbox}
* `kOptFlagUIOption`: {broadcast_to_UI_on_change}
* `kOptFlagRedrAll`: {triggers_full_screen_redraw}
