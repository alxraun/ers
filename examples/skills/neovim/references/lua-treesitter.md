# LUA_TREESITTER

## TYPE_DEFINITIONS
* `TSNode` == `userdata` [Tree-sitter node reference]
* `TSTree` == `userdata` [Parsed syntax tree]
* `TSQuery` == `userdata` [Compiled query object]
* `TSParser` == `userdata` [Low-level parser instance]
* `TSQueryCursor` == `userdata` [Query execution state]
* `TSQueryMatch` == `userdata` [Single pattern match result]
* `LanguageTree` == `table` [Nvim wrapper for nested parsers]
* `Range4` == `[start_row: integer, start_col: integer, end_row: integer, end_col: integer]`
* `Range6` == `[start_row: integer, start_col: integer, start_byte: integer, end_row: integer, end_col: integer, end_byte: integer]`
* `TSMetadata` == `table<integer|string, any>` [Directives/Predicates metadata]
* `TSCallbackNameOn` == {`"on_bytes"`, `"on_changedtree"`, `"on_child_added"`, `"on_child_removed"`, `"on_detach"`}

## CORE_API_SIGNATURES (`vim.treesitter`)

### PARSER_FACTORY
* `get_parser(bufnr: integer?, lang: string?, opts: table?)` -> `LanguageTree`
* `get_string_parser(str: string, lang: string, opts: table?)` -> `LanguageTree`
* `_create_parser(bufnr: integer, lang: string, opts: table?)` -> `LanguageTree`

### NODE_OPERATIONS
* `get_node(opts: table?)` -> `TSNode?`
* `get_node_text(node: TSNode, source: integer|string, opts: table?)` -> `string`
* `get_range(node: TSNode, source: integer|string?, metadata: TSMetadata?)` -> `Range6`
* `get_node_range(node_or_range: TSNode|Range4)` -> `integer, integer, integer, integer` [srow, scol, erow, ecol]
* `is_ancestor(dest: TSNode, source: TSNode)` -> `boolean`
* `is_in_node_range(node: TSNode, line: integer, col: integer)` -> `boolean`
* `node_contains(node: TSNode, range: Range4|Range6)` -> `boolean`

### HIGHLIGHT_AND_UI
* `start(bufnr: integer?, lang: string?)` -> `void`
* `stop(bufnr: integer?)` -> `void`
* `get_captures_at_pos(bufnr: integer, row: integer, col: integer)` -> `table[]`
* `get_captures_at_cursor(winnr: integer?)` -> `string[]`
* `inspect_tree(opts: table?)` -> `void`
* `foldexpr(lnum: integer?)` -> `string`

## QUERY_API (`vim.treesitter.query`)

### COMPILATION_AND_RETRIEVAL
* `parse(lang: string, query: string)` -> `vim.treesitter.Query`
* `get(lang: string, query_name: string)` -> `vim.treesitter.Query?`
* `set(lang: string, query_name: string, text: string)` -> `void`
* `get_files(lang: string, query_name: string, is_included: boolean?)` -> `string[]`

### EXECUTION_ITERATORS
* `Query:iter_captures(node: TSNode, source: integer|string, start_row: integer?, end_row: integer?, opts: table?)` -> `fun(): integer, TSNode, TSMetadata, TSQueryMatch, TSTree`
* `Query:iter_matches(node: TSNode, source: integer|string, start: integer?, stop: integer?, opts: table?)` -> `fun(): integer, table<integer, TSNode[]>, TSMetadata, TSTree`

### EXTENSION_API
* `add_predicate(name: string, handler: function, opts: table|boolean?)` -> `void`
* `add_directive(name: string, handler: function, opts: table|boolean?)` -> `void`
* `list_directives()` -> `string[]`
* `list_predicates()` -> `string[]`
* `lint(buf: integer, opts: table?)` -> `void`
* `omnifunc(findstart: 0|1, base: string)` -> `table|integer`

## LANGUAGE_API (`vim.treesitter.language`)

* `add(lang: string, opts: table?)` -> `boolean, string?`
* `inspect(lang: string)` -> `TSLangInfo`
* `register(lang: string, filetype: string|string[])` -> `void`
* `get_lang(filetype: string)` -> `string?`
* `get_filetypes(lang: string)` -> `string[]`

## CLASS_METHODS

### `LanguageTree` [API_SURFACE]
* `parse(range: boolean|Range4|Range4[]?, on_parse: function?)` -> `table<integer, TSTree>?`
* `invalidate(reload: boolean?)` -> `void`
* `trees()` -> `table<integer, TSTree>`
* `lang()` -> `string`
* `children()` -> `table<string, LanguageTree>`
* `parent()` -> `LanguageTree?`
* `source()` -> `integer|string`
* `is_valid(exclude_children: boolean?, range: Range4|Range4[]?)` -> `boolean`
* `for_each_tree(fn: fun(tree: TSTree, ltree: LanguageTree))` -> `void`
* `register_cbs(cbs: table<TSCallbackNameOn, function>, recursive: boolean?)` -> `void`
* `contains(range: Range4)` -> `boolean`
* `tree_for_range(range: Range4, opts: table?)` -> `TSTree?`
* `node_for_range(range: Range4, opts: table?)` -> `TSNode?`
* `named_node_for_range(range: Range4, opts: table?)` -> `TSNode?`
* `language_for_range(range: Range4)` -> `LanguageTree`
* `destroy()` -> `void`

### `TSNode` [USERDATA_METHODS]
* `parent()` -> `TSNode?`
* `next_sibling()`, `prev_sibling()` -> `TSNode?`
* `next_named_sibling()`, `prev_named_sibling()` -> `TSNode?`
* `child(index: integer)` -> `TSNode?`
* `named_child(index: integer)` -> `TSNode?`
* `child_count()`, `named_child_count()` -> `integer`
* `named_children()` -> `TSNode[]`
* `child_with_descendant(descendant: TSNode)` -> `TSNode?`
* `iter_children()` -> `fun(): TSNode, string` [node, field_name]
* `field(name: string)` -> `TSNode[]`
* `start()`, `end_()` -> `integer, integer, integer` [row, col, byte]
* `range(include_bytes: boolean)` -> `integer...` [Range4 | Range6]
* `type()` -> `string`
* `symbol()` -> `integer`
* `named()`, `missing()`, `extra()`, `has_changes()`, `has_error()` -> `boolean`
* `sexpr()`, `id()` -> `string`
* `tree()` -> `TSTree`
* `byte_length()` -> `integer`
* `equal(node: TSNode)` -> `boolean`
* `descendant_for_range(srow, scol, erow, ecol)` -> `TSNode?`
* `named_descendant_for_range(srow, scol, erow, ecol)` -> `TSNode?`

### `TSTree` [USERDATA_METHODS]
* `root()` -> `TSNode`
* `copy()` -> `TSTree`
* `included_ranges(include_bytes: boolean)` -> `Range4[] | Range6[]`
* `edit(...)` -> `TSTree` [Internal_Update]

### `TSQuery` [USERDATA_METHODS]
* `inspect()` -> `TSQueryInfo`
* `disable_capture(name: string)` -> `void`
* `disable_pattern(index: integer)` -> `void`

## STRUCTURAL_CONSTANTS
* `vim.treesitter.language_version` == `integer` [Current_ABI]
* `vim.treesitter.minimum_language_version` == `integer` [Min_Compatible_ABI]

## CONFIG_DICTIONARIES

### `get_node.Opts`
* `bufnr`: `integer`
* `pos`: `[row: integer, col: integer]`
* `lang`: `string`
* `ignore_injections`: `boolean` [default: true]
* `include_anonymous`: `boolean` [default: false]

### `TSLangInfo`
* `abi_version`: `integer`
* `state_count`: `integer`
* `fields`: `string[]`
* `symbols`: `table<string, boolean>`
* `supertypes`: `table<string, string[]>`
* `_wasm`: `boolean`
* `metadata`: `{ major_version: integer, minor_version: integer, patch_version: integer }`
