# LUA_LSP

## TYPE_DEFINITIONS
* `ClientId` == `integer`
* `Buffer` == `integer`
* `Window` == `integer`
* `Method` == `string`
* `LspHandler` == `fun(err: ResponseError?, result: any, ctx: HandlerContext, config?: table)`
* `OffsetEncoding` == {`"utf-8"`, `"utf-16"`, `"utf-32"`}
* `URI` == `string`
* `ClientConfig` == `table` [See CONFIG_DICTIONARIES]
* `LSPAny` == `any`

## CORE_LIFECYCLE_API
* `vim.lsp.start(config: ClientConfig, opts?: table)` -> `ClientId?`
* `vim.lsp.stop_client(client_id: ClientId | ClientId[] | Client[], force?: boolean|integer)` -> `void`
* `vim.lsp.get_client_by_id(client_id: ClientId)` -> `vim.lsp.Client?`
* `vim.lsp.get_clients(filter?: table)` -> `vim.lsp.Client[]`
* `vim.lsp.buf_attach_client(bufnr: Buffer, client_id: ClientId)` -> `boolean`
* `vim.lsp.buf_detach_client(bufnr: Buffer, client_id: ClientId)` -> `void`
* `vim.lsp.buf_is_attached(bufnr: Buffer, client_id: ClientId)` -> `boolean`
* `vim.lsp.enable(name: string | string[], enable?: boolean)` -> `void`
* `vim.lsp.is_enabled(name: string)` -> `boolean`

## BUFFER_OPERATIONS_API (`vim.lsp.buf`)

### NAVIGATION_AND_QUERY
* `declaration(opts?: LocationOpts)` -> `void`
* `definition(opts?: LocationOpts)` -> `void`
* `type_definition(opts?: LocationOpts)` -> `void`
* `implementation(opts?: LocationOpts)` -> `void`
* `references(context?: table, opts?: ListOpts)` -> `void`
* `document_symbol(opts?: ListOpts)` -> `void`
* `workspace_symbol(query?: string, opts?: ListOpts)` -> `void`
* `incoming_calls()` -> `void`
* `outgoing_calls()` -> `void`
* `typehierarchy(kind: "subtypes" | "supertypes")` -> `void`

### INTERACTIVE_FEATURES
* `hover(config?: table)` -> `void`
* `signature_help(config?: table)` -> `void`
* `code_action(opts?: table)` -> `void`
* `rename(new_name?: string, opts?: table)` -> `void`
* `document_highlight()` -> `void`
* `clear_references()` -> `void`
* `selection_range(direction: integer, timeout_ms?: integer)` -> `void`

### EDITING_AND_FORMATTING
* `format(opts?: table)` -> `void`
* `execute_command(command_params: table)` -> `void`

### WORKSPACE_MANAGEMENT
* `add_workspace_folder(path?: string)` -> `void`
* `remove_workspace_folder(path?: string)` -> `void`
* `list_workspace_folders()` -> `string[]`

## CLIENT_OBJECT_METHODS (`vim.lsp.Client`)
* `client:request(method: Method, params?: table, handler?: LspHandler, bufnr?: Buffer)` -> `boolean, request_id?`
* `client:request_sync(method: Method, params: table, timeout_ms?: integer, bufnr?: Buffer)` -> `{err, result}?, error_msg?`
* `client:notify(method: Method, params?: table)` -> `boolean`
* `client:cancel_request(id: integer)` -> `boolean`
* `client:supports_method(method: Method, bufnr?: Buffer)` -> `boolean`
* `client:stop(force?: boolean|integer)` -> `void`
* `client:is_stopped()` -> `boolean`
* `client:on_attach(bufnr: Buffer)` -> `void`
* `client:exec_cmd(command: table, context?: table, handler?: LspHandler)` -> `void`

## PROTOCOL_AND_UTILS
* `vim.lsp.protocol.make_client_capabilities()` -> `table`
* `vim.lsp.protocol.resolve_capabilities(server_capabilities: table)` -> `table`
* `vim.lsp.status()` -> `string` [Aggregated progress]
* `vim.lsp.util.make_position_params(window?: Window, encoding?: OffsetEncoding)` -> `table`
* `vim.lsp.util.make_range_params(window?: Window, encoding?: OffsetEncoding)` -> `table`
* `vim.lsp.util.apply_workspace_edit(edit: table, encoding: OffsetEncoding)` -> `void`
* `vim.lsp.util.apply_text_edits(edits: table, bufnr: Buffer, encoding: OffsetEncoding)` -> `void`

## CONFIG_DICTIONARIES

### ClientConfig
* `cmd`: `string[] | function` [Required]
* `root_dir`: `string?`
* `name`: `string` [Default: `cmd` basename]
* `filetypes`: `string[]?`
* `capabilities`: `table?`
* `handlers`: `table<Method, LspHandler>?`
* `settings`: `table?`
* `init_options`: `table?`
* `on_attach`: `fun(client, bufnr)?`
* `on_init`: `fun(client, result)?`
* `on_exit`: `fun(code, signal, client_id)?`
* `offset_encoding`: `OffsetEncoding?`
* `exit_timeout`: `integer | boolean?`

### LocationOpts
* `on_list`: `fun(list: table)` [Overrides default handler]
* `loclist`: `boolean` [Use location list instead of quickfix]
* `reuse_win`: `boolean` [Jump to existing window if buffer open]

## SYSTEM_EVENTS
* `LspAttach`: {`client_id`} @ `bufnr` => [Client initialized + attached]
* `LspDetach`: {`client_id`} @ `bufnr` => [Just before detachment]
* `LspNotify`: {`client_id`, `method`, `params`} => [Successful notification sent]
* `LspProgress`: {`client_id`, `params`} @ `pattern` == `kind` => [Server progress updates]
* `LspRequest`: {`client_id`, `request_id`, `request`} => [Status: `pending` | `complete` | `cancel`]

## CONSTANTS (`vim.lsp.protocol`)
* `ErrorCodes`: {`ParseError = -32700`, `MethodNotFound = -32601`, `RequestCancelled = -32800`, ...}
* `SymbolKind`: {`File = 1`, `Module = 2`, `Namespace = 3`, `Class = 5`, `Method = 6`, ...}
* `DiagnosticSeverity`: {`Error = 1`, `Warning = 2`, `Information = 3`, `Hint = 4`}
* `MessageType`: {`Error = 1`, `Warning = 2`, `Info = 3`, `Log = 4`}
