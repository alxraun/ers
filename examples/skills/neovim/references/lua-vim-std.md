# LUA_VIM_STD

## TYPE_DEFINITIONS
* `Iter` == `table` {metatable: Iter}
* `Iterator` == `fun(): any, any`
* `Path` == `string`
* `Buffer` == `integer`
* `Dict` == `table<string, any>`
* `Array` == `any[]`
* `Marker` == `string | string[] | fun(name: string, path: string): boolean`
* `MarkerList` == `(Marker | Marker[])[]`

## VIM_ITER (Iterator Pipelines)

### CONSTRUCTOR
* `vim.iter(src: table | function | Iter, ...)` -> `Iter`

### CHAINABLE_METHODS
* `Iter:all(pred: fun(...): boolean)` -> `boolean`
* `Iter:any(pred: fun(...): boolean)` -> `boolean`
* `Iter:filter(f: fun(...): boolean)` -> `Iter`
* `Iter:flatten(depth?: integer)` -> `Iter` [array_only]
* `Iter:map(f: fun(...): ...)` -> `Iter`
* `Iter:rev()` -> `Iter` [array_only]
* `Iter:slice(first: integer, last: integer)` -> `Iter` [array_only]
* `Iter:skip(n: integer | fun(...): boolean)` -> `Iter`
* `Iter:rskip(n: integer)` -> `Iter` [array_only]
* `Iter:take(n: integer | fun(...): boolean)` -> `Iter`
* `Iter:unique(key?: fun(...): any)` -> `Iter`
* `Iter:enumerate()` -> `Iter`

### TERMINAL_METHODS
* `Iter:each(f: fun(...))` -> `void`
* `Iter:fold(init: any, f: fun(acc: any, ...): any)` -> `any`
* `Iter:join(delim: string)` -> `string`
* `Iter:last()` -> `any`
* `Iter:next()` -> `any...`
* `Iter:nth(n: integer)` -> `any...`
* `Iter:peek()` -> `any...`
* `Iter:pop()` -> `any` [array_only]
* `Iter:rpeek()` -> `any` [array_only]
* `Iter:find(f: any | fun(...): boolean)` -> `any...`
* `Iter:rfind(f: any | fun(...): boolean)` -> `any...` [array_only]
* `Iter:totable()` -> `Array | Dict`

## VIM_FS (Filesystem Operations)

### PATH_MANIPULATION
* `vim.fs.abspath(path: Path)` -> `Path`
* `vim.fs.basename(file: Path)` -> `Path`
* `vim.fs.dirname(file: Path)` -> `Path`
* `vim.fs.joinpath(...)` -> `Path`
* `vim.fs.normalize(path: Path, opts?: FsNormalizeOpts)` -> `Path`
* `vim.fs.relpath(base: Path, target: Path)` -> `Path?`

### TRAVERSAL_AND_SEARCH
* `vim.fs.dir(path: Path, opts?: FsDirOpts)` -> `Iterator` [yields: name, type]
* `vim.fs.find(names: string | string[] | fun, opts?: FsFindOpts)` -> `Path[]`
* `vim.fs.parents(start: Path)` -> `Iterator` [yields: parent_path]
* `vim.fs.root(source: Buffer | Path, marker: Marker | MarkerList)` -> `Path?`

### DESTRUCTION
* `vim.fs.rm(path: Path, opts?: FsRmOpts)` -> `void`

## VIM_JSON (JSON Serialization)
* `vim.json.decode(str: string, opts?: JsonDecodeOpts)` -> `any`
* `vim.json.encode(obj: any, opts?: JsonEncodeOpts)` -> `string`

## VIM_MPACK (MessagePack Serialization)
* `vim.mpack.decode(str: string)` -> `any`
* `vim.mpack.encode(obj: any)` -> `string`

## VIM_F (Functional Utilities)
* `vim.F.if_nil(...)` -> `any` [returns first non-nil]
* `vim.F.nil_wrap(fn: function)` -> `fun(...): any?`
* `vim.F.npcall(fn: function, ...)` -> `any?`
* `vim.F.ok_or_nil(status: boolean, ...)` -> `any...`
* `vim.F.pack_len(...)` -> `table` {n: integer, [1...n]: any}
* `vim.F.unpack_len(t: table)` -> `any...`

## OPTION_DICTIONARIES

### FsNormalizeOpts
* `expand_env`: `boolean` [default: true]
* `win`: `boolean` [default: os_specific]

### FsDirOpts
* `depth`: `integer` [default: 1]
* `skip`: `fun(dir_name: string): boolean`
* `follow`: `boolean` [default: false]

### FsFindOpts
* `path`: `Path` [default: cwd]
* `upward`: `boolean` [default: false]
* `stop`: `Path`
* `type`: {`"file"`, `"directory"`, `"link"`, `"socket"`, `"char"`, `"block"`, `"fifo"`}
* `limit`: `number` [default: 1]
* `follow`: `boolean` [default: false]

### FsRmOpts
* `recursive`: `boolean`
* `force`: `boolean`

### JsonDecodeOpts
* `luanil`: {`object`: `boolean`, `array`: `boolean`}
* `skip_comments`: `boolean` [default: false]

### JsonEncodeOpts
* `escape_slash`: `boolean` [default: false]
* `indent`: `string` [default: ""]
* `sort_keys`: `boolean` [default: false]
