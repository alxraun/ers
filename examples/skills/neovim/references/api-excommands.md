# API_EXCOMMANDS

## TYPE_DEFINITIONS
* `Buffer` == `integer`
* `LuaRef` == `function`
* `Object` == `any`
* `Array` == `any[]`
* `Dict` == `table<string, any>`
* `CmdInfo` == `Dict` [structure: `nvim_parse_cmd` return]
* `UserCmdCallbackArgs` == `Dict`
* `UserCmdOpts` == `Dict`
* `ExecOpts` == `Dict`
* `CmdOpts` == `Dict`

## API_SIGNATURES

### COMMAND_REGISTRY
* `nvim_create_user_command(name: string, command: string|LuaRef, opts: UserCmdOpts)` -> `void`
* `nvim_del_user_command(name: string)` -> `void`
* `nvim_buf_create_user_command(buffer: Buffer, name: string, command: string|LuaRef, opts: UserCmdOpts)` -> `void`
* `nvim_buf_del_user_command(buffer: Buffer, name: string)` -> `void`
* `nvim_get_commands(opts: {builtin: boolean})` -> `table<string, Dict>`
* `nvim_buf_get_commands(buffer: Buffer, opts: {builtin: boolean})` -> `table<string, Dict>`

### COMMAND_EXECUTION
* `nvim_cmd(cmd: CmdInfo, opts: CmdOpts)` -> `string`
* `nvim_command(command: string)` -> `void`
* `nvim_exec2(src: string, opts: ExecOpts)` -> `Dict`
* `nvim_parse_cmd(str: string, opts: Dict)` -> `CmdInfo`

### VIMSCRIPT_EVALUATION
* `nvim_eval(expr: string)` -> `Object`
* `nvim_call_function(fn: string, args: Array)` -> `Object`
* `nvim_call_dict_function(dict: Object, fn: string, args: Array)` -> `Object`
* `nvim_parse_expression(expr: string, flags: string, highlight: boolean)` -> `Dict`

## DATA_STRUCTURES

### UserCmdOpts
* `desc`: `string`
* `force`: `boolean` [default: `true`]
* `bang`: `boolean`
* `bar`: `boolean`
* `register`: `boolean`
* `keepscript`: `boolean`
* `preview`: `fun(opts: UserCmdCallbackArgs, ns: integer, buf: Buffer?): integer`
* `complete`: `string` | `fun(ArgLead: string, CmdLine: string, CursorPos: integer): string[]`
* `nargs`: {`0`, `1`, `"*"`, `"?"`, `"+"`}
* `range`: `boolean` | `string` [`"%"`] | `integer` [default_count]
* `count`: `boolean` | `integer` [default_count]
* `addr`: {`"lines"`, `"arguments"`, `"buffers"`, `"loaded_buffers"`, `"windows"`, `"tabs"`, `"quickfix"`, `"other"`}

### UserCmdCallbackArgs
* `name`: `string`
* `args`: `string`
* `fargs`: `string[]`
* `nargs`: `string`
* `bang`: `boolean`
* `line1`: `integer`
* `line2`: `integer`
* `range`: `integer` [0, 1, or 2]
* `count`: `integer`
* `reg`: `string`
* `mods`: `string`
* `smods`: `Dict` [same as `CmdInfo.mods`]

### CmdInfo
* `cmd`: `string`
* `range`: `integer[]` [len 0..2]
* `count`: `integer`
* `reg`: `string`
* `bang`: `boolean`
* `args`: `string[]`
* `addr`: `string`
* `nargs`: `string`
* `nextcmd`: `string`
* `magic`: {`file`: `boolean`, `bar`: `boolean`}
* `mods`:
    * `silent`: `boolean`
    * `emsg_silent`: `boolean`
    * `unsilent`: `boolean`
    * `sandbox`: `boolean`
    * `noautocmd`: `boolean`
    * `browse`: `boolean`
    * `confirm`: `boolean`
    * `hide`: `boolean`
    * `horizontal`: `boolean`
    * `keepalt`: `boolean`
    * `keepjumps`: `boolean`
    * `keepmarks`: `boolean`
    * `keeppatterns`: `boolean`
    * `lockmarks`: `boolean`
    * `noswapfile`: `boolean`
    * `vertical`: `boolean`
    * `tab`: `integer` [-1 if omitted]
    * `verbose`: `integer` [-1 if omitted]
    * `split`: {`"aboveleft"`, `"belowright"`, `"topleft"`, `"botright"`, `""`}
    * `filter`: {`pattern`: `string`, `force`: `boolean`}

### ExecOpts / CmdOpts
* `output`: `boolean` [default: `false`]

## CONSTANTS & ENUMS

### Command_Address_Types
* `lines` == `ADDR_LINES`
* `arg` == `ADDR_ARGUMENTS`
* `buf` == `ADDR_BUFFERS`
* `load` == `ADDR_LOADED_BUFFERS`
* `win` == `ADDR_WINDOWS`
* `tab` == `ADDR_TABS`
* `qf` == `ADDR_QUICKFIX`
* `none` == `ADDR_NONE`

### Completion_Methods
* `arglist`, `augroup`, `buffer`, `color`, `command`, `compiler`, `dir`, `dir_in_path`, `environment`, `event`, `expression`, `file`, `file_in_path`, `filetype`, `function`, `help`, `highlight`, `history`, `keymap`, `locale`, `lua`, `mapclear`, `mapping`, `menu`, `messages`, `option`, `packadd`, `runtime`, `scriptnames`, `shellcmd`, `shellcmdline`, `sign`, `syntax`, `syntime`, `tag`, `tag_listfiles`, `user`, `var`, `custom`, `customlist`

### Parse_Expression_Flags
* `m`: `kExprFlagsMulti` [multiple expressions allowed]
* `E`: `kExprFlagsDisallowEOC` [disallow end-of-command tokens]
* `l`: `kExprFlagsParseLet` [start with lvalues for `:let` or `:for`]
