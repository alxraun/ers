# API_AUTOCMD

## TYPE_DEFINITIONS
* `AutocmdId` == `integer`
* `AugroupId` == `integer`
* `Buffer` == `integer`
* `Event` == `string | string[]`
* `Pattern` == `string | string[]`
* `Group` == `string | integer`
* `LuaRef` == `function`
* `Callback` == `LuaRef | string`
* `Object` == `any`
* `Dict` == `table<string, any>`

## API_SIGNATURES

### AUTOCMD_LIFECYCLE
* `nvim_create_autocmd(event: Event, opts: CreateAutocmdOpts)` -> `AutocmdId`
* `nvim_del_autocmd(id: AutocmdId)` -> `void`
* `nvim_clear_autocmds(opts: ClearAutocmdOpts)` -> `void`
* `nvim_get_autocmds(opts: GetAutocmdOpts)` -> `AutocmdInfo[]`
* `nvim_exec_autocmds(event: Event, opts: ExecAutocmdOpts)` -> `void`

### AUGROUP_MANAGEMENT
* `nvim_create_augroup(name: string, opts: CreateAugroupOpts)` -> `AugroupId`
* `nvim_del_augroup_by_id(id: AugroupId)` -> `void`
* `nvim_del_augroup_by_name(name: string)` -> `void`

## OPTION_DICTIONARIES

### CreateAutocmdOpts
* `group`: `Group` @[optional]
* `pattern`: `Pattern` @[optional]
* `buffer`: `Buffer` @[optional, !pattern]
* `desc`: `string` @[optional]
* `callback`: `Callback` @[optional, !command]
* `command`: `string` @[optional, !callback]
* `once`: `boolean` @[default: false]
* `nested`: `boolean` @[default: false]

### GetAutocmdOpts
* `group`: `Group | Group[]` @[optional]
* `event`: `Event` @[optional]
* `pattern`: `Pattern` @[optional]
* `buffer`: `Buffer | Buffer[]` @[optional, !pattern]
* `id`: `AutocmdId` @[optional]

### ClearAutocmdOpts
* `group`: `Group` @[optional, nil == "no group"]
* `event`: `Event` @[optional]
* `pattern`: `Pattern` @[optional]
* `buffer`: `Buffer` @[optional, !pattern]

### ExecAutocmdOpts
* `group`: `Group` @[optional]
* `pattern`: `Pattern` @[optional]
* `buffer`: `Buffer` @[optional, !pattern]
* `modeline`: `boolean` @[default: true]
* `data`: `Object` @[arbitrary_payload]

### CreateAugroupOpts
* `clear`: `boolean` @[default: true]

## DATA_STRUCTURES

### AutocmdInfo
* `id`: `AutocmdId` @[if_api_defined]
* `group`: `AugroupId` @[optional]
* `group_name`: `string` @[optional]
* `event`: `string`
* `pattern`: `string`
* `buflocal`: `boolean`
* `buffer`: `Buffer` @[optional]
* `callback`: `Callback` @[optional]
* `command`: `string` @[empty_if_callback_set]
* `desc`: `string` @[optional]
* `once`: `boolean`

### AutocmdCallbackArgs
* `id`: `AutocmdId`
* `event`: `string`
* `group`: `AugroupId | nil`
* `buf`: `Buffer`
* `file`: `string` @[afile]
* `match`: `string` @[amatch]
* `data`: `Object` @[from_nvim_exec_autocmds]

## EVENT_REGISTRY

### BUFFER_LOCAL_EVENTS [win_local == true]
* `BufAdd`, `BufDelete`, `BufEnter`, `BufFilePost`, `BufFilePre`, `BufHidden`, `BufLeave`, `BufModifiedSet`, `BufNew`, `BufNewFile`, `BufReadCmd`, `BufReadPost`, `BufReadPre`, `BufUnload`, `BufWinEnter`, `BufWinLeave`, `BufWipeout`, `BufWriteCmd`, `BufWritePost`, `BufWritePre`
* `CursorHold`, `CursorHoldI`, `CursorMoved`, `CursorMovedC`, `CursorMovedI`
* `FileAppendCmd`, `FileAppendPost`, `FileAppendPre`, `FileChangedRO`, `FileChangedShell`, `FileChangedShellPost`, `FileReadCmd`, `FileReadPost`, `FileReadPre`, `FileType`, `FileWriteCmd`, `FileWritePost`, `FileWritePre`
* `FilterReadPost`, `FilterReadPre`, `FilterWritePost`, `FilterWritePre`
* `InsertChange`, `InsertCharPre`, `InsertEnter`, `InsertLeave`, `InsertLeavePre`
* `RecordingEnter`, `RecordingLeave`, `SearchWrapped`, `ShellFilterPost`
* `TextChanged`, `TextChangedI`, `TextChangedP`, `TextChangedT`, `TextYankPost`
* `WinClosed`, `WinEnter`, `WinLeave`, `WinResized`, `WinScrolled`

### GLOBAL_EVENTS [win_local == false]
* `ChanInfo`, `ChanOpen`, `CmdUndefined`, `CmdlineChanged`, `CmdlineEnter`, `CmdlineLeave`, `CmdlineLeavePre`, `CmdwinEnter`, `CmdwinLeave`
* `ColorScheme`, `ColorSchemePre`, `CompleteChanged`, `CompleteDone`, `CompleteDonePre`
* `DiagnosticChanged`, `DiffUpdated`, `DirChanged`, `DirChangedPre`, `EncodingChanged`, `ExitPre`
* `FocusGained`, `FocusLost`, `FuncUndefined`, `GUIEnter`, `GUIFailed`
* `LspAttach`, `LspDetach`, `LspNotify`, `LspProgress`, `LspRequest`, `LspTokenUpdate`
* `MarkSet`, `MenuPopup`, `ModeChanged`, `OptionSet`, `QuickFixCmdPost`, `QuickFixCmdPre`, `QuitPre`
* `PackChangedPre`, `PackChanged`, `Progress`, `RemoteReply`, `SafeState`, `SessionLoadPost`, `SessionWritePost`, `ShellCmdPost`, `Signal`, `SourceCmd`, `SourcePost`, `SourcePre`, `SpellFileMissing`, `StdinReadPost`, `StdinReadPre`, `SwapExists`, `Syntax`
* `TabClosed`, `TabClosedPre`, `TabEnter`, `TabLeave`, `TabNew`, `TabNewEntered`
* `TermChanged`, `TermClose`, `TermEnter`, `TermLeave`, `TermOpen`, `TermRequest`, `TermResponse`
* `UIEnter`, `UILeave`, `User`, `VimEnter`, `VimLeave`, `VimLeavePre`, `VimResized`, `VimResume`, `VimSuspend`, `WinNewPre`, `WinNew`

### ALIASES
* `BufCreate` -> `BufAdd`
* `BufRead` -> `BufReadPost`
* `BufWrite` -> `BufWritePre`
* `FileEncoding` -> `EncodingChanged`
