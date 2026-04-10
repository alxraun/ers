# API_GLOBAL

## TYPE_DEFINITIONS
* `Object` == `any`
* `Array` == `any[]`
* `Dict` == `table<string, any>`
* `LuaRef` == `function`
* `Boolean` == `boolean`
* `Integer` == `integer`
* `String` == `string`
* `Float` == `number`

## API_SIGNATURES

### LUA_AND_ATOMIC_EXECUTION
* `nvim_exec_lua(code: String, args: Array)` -> `Object`
* `nvim_call_atomic(calls: Array)` -> `Array`

### GLOBAL_VARIABLE_MANAGEMENT (g: and v:)
* `nvim_get_var(name: String)` -> `Object`
* `nvim_set_var(name: String, value: Object)` -> `void`
* `nvim_del_var(name: String)` -> `void`
* `nvim_get_vvar(name: String)` -> `Object`
* `nvim_set_vvar(name: String, value: Object)` -> `void`

### SYSTEM_INFORMATION_AND_RUNTIME
* `nvim_get_api_info()` -> `Array`
* `nvim_set_client_info(name: String, version: Dict, type: String, methods: Dict, attributes: Dict)` -> `void`
* `nvim_list_runtime_paths()` -> `String[]`
* `nvim_get_runtime_file(name: String, all: Boolean)` -> `String[]`
* `nvim_set_current_dir(dir: String)` -> `void`
* `nvim_get_mode()` -> `Dict`
* `nvim_strwidth(text: String)` -> `Integer`
* `nvim_get_chan_info(chan: Integer)` -> `Dict`
* `nvim_list_chans()` -> `Array`
* `nvim_get_proc(pid: Integer)` -> `Object`
* `nvim_get_proc_children(pid: Integer)` -> `Array`

### MESSAGING_AND_OUTPUT
* `nvim_echo(chunks: Array, history: Boolean, opts: Dict)` -> `void`
* `nvim_notify(msg: String, log_level: Integer, opts: Dict)` -> `Object`
* `nvim_out_write(str: String)` -> `void`
* `nvim_err_write(str: String)` -> `void`
* `nvim_err_writeln(str: String)` -> `void`

### CHANNELS_AND_TERMINAL
* `nvim_open_term(buffer: Integer, opts: Dict)` -> `Integer`
* `nvim_chan_send(chan: Integer, data: String)` -> `void`

### CONTEXT_MANAGEMENT
* `nvim_get_context(opts: Dict)` -> `Dict`
* `nvim_load_context(dict: Dict)` -> `Object`

### EVENTS_AND_PUBSUB
* `nvim_subscribe(event: String)` -> `void`
* `nvim_unsubscribe(event: String)` -> `void`

## DEPRECATED_GLOBAL_ALIASES
* `nvim_execute_lua(code: String, args: Array)` -> `Object` @deprecated {use: `nvim_exec_lua`}
* `vim_get_var(name: String)` -> `Object`
* `vim_set_var(name: String, value: Object)` -> `Object`
* `vim_del_var(name: String)` -> `Object`
* `vim_get_vvar(name: String)` -> `Object`
* `vim_strwidth(text: String)` -> `Integer`
* `vim_change_directory(dir: String)` -> `void`
* `vim_list_runtime_paths()` -> `String[]`
* `vim_get_api_info()` -> `Array`
