---
name: neovim
description: Reference for Neovim v0.11+ Lua API and system internals.
license: MIT
---

# Neovim

## Index

### 1. [Buffer API](references/api-buffer.md)
* buffer {lines, vars, marks, options, extmarks, keymaps} => {text_crud, state_storage, event_attachment}
* constraints: [0_indexed], line_end_exclusive, requires: [valid_handle]
* usage: {modifying_text, buffer_local_config, scoping_data, lifecycle_management}

### 2. [Window & Viewport](references/api-window.md)
* window {cursor, viewport, config, buffer, vars, layout} => {view_control, navigation, configuration}
* constraints: [0_indexed], float_config_complexity, z_index_managed
* usage: {positioning_cursor, managing_floating_panels, viewport_scrolling}

### 3. [Tabpage & Layout](references/api-tabpage.md)
* tabpage {wins, layout, vars, handles} => {workspace_org, window_group_management, state_persistence}
* constraints: tab_local_scopes, handle_persistence, [0_indexed_api_handles]
* usage: {switching_contexts, querying_visible_windows}

### 4. [Ex-commands & Registry](references/api-excommands.md)
* command {name, callback, opts, registry, evaluator} => {action_trigger, execution, script_evaluation}
* logic: vimscript_bridge -> lua_function
* usage: {creating_user_commands, executing_vimscript_logic}

### 5. [Autocmds & Events](references/api-autocmd.md)
* event {group, pattern, callback, trigger, registry} => {reactive_programming, lifecycle_hooks, event_dispatching}
* architecture: main_event_loop -> dispatcher
* usage: {buffer_save_hook, lsp_attachment_logic, mode_change_detection}

### 6. [UI & External Protocol](references/api-ui.md)
* ui {grid, message, popup, multigrid, events, options} => {external_rendering, rpc_communication, state_synchronization}
* constraints: [async_only], render_lag_potential
* usage: {gui_development, terminal_multiplexing_integration}

### 7. [Extmarks & Decoration](references/api-extmark.md)
* extmark {namespace, position, virt_text, highlights, signs, provider} => {non_destructive_metadata, ui_overlay, spatial_indexing}
* physics: gravity_logic [left|right], mark_tree_indexing
* usage: {inline_linter_messages, virtual_lines, git_gutter_signs}

### 8. [Highlight & Color](references/api-highlight.md)
* highlight {group, attributes, colors, namespace, priority} => {aesthetic_layer, visual_feedback, theme_management}
* logic: namespace_resolution -> redraw_grid
* usage: {theme_development, syntax_decoration}

### 9. [Keymaps & Keycodes](references/api-keymap.md)
* keymap {lhs, rhs, mode, opts, codes, marks} => {input_redirection, interaction_design, shortcut_management}
* logic: raw_byte_stream -> mapping_resolution
* usage: {binding_shortcuts, translating_keycodes}

### 10. [Options & Settings](references/api-options.md)
* option {global, buffer_local, window_local, meta, scope_logic} => {system_configuration, behavior_control}
* scopes: `o` [global], `bo` [buffer], `wo` [window], `opt` [enhanced_api]
* usage: {configuring_indentation, toggling_ui_features}

### 11. [LSP Client](references/lua-lsp.md)
* lsp {client, rpc, handlers, capabilities, protocol, buf_ops} => {intelligent_ide_features, server_communication, workspace_management}
* bridges: `vim.lsp` -> client_protocol -> `JSON-RPC`
* usage: {goto_definition, code_actions, symbol_search}

### 12. [Treesitter Integration](references/lua-treesitter.md)
* ts {parser, node, query, range, language, tree} => {semantic_parsing, structural_navigation, syntax_awareness}
* constraints: requires_parser_installation, incremental_reparsing
* usage: {advanced_syntax_highlighter, structural_code_refactoring}

### 13. [Diagnostic Framework](references/lua-diagnostic.md)
* diagnostic {severity, lnum, col, namespace, config, handlers} => {feedback_loop, quality_reporting, navigation}
* integration: consumer [UI/gutter] <- producer [LSP/lint]
* usage: {showing_errors, navigating_issues}

### 14. [Lua Standard Lib (Vim Std)](references/lua-vim-std.md)
* vim_std {iter, fs, json, mpack, functional} => {utility_backbone, data_serialization, path_resolution}
* module: `vim.iter`, `vim.fs`, `vim.json`, `vim.mpack`, `vim.F`
* usage: {array_manipulation, path_resolution, data_serialization}

### 15. [Global System](references/api-global.md)
* global {lua_exec, vars, channels, proc, runtime, messaging, context} => {system_bridge, environment_awareness, state_control}
* scopes: `g` [user], `v` [vim_engine]
* usage: {cross_plugin_communication, runtime_environment_queries, system_messaging}
