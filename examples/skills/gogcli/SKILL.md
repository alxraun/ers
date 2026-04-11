---
name: gogcli
description: A CLI tool (gogcli / gog) for working with Google Workspace. It lets you manage Gmail, Calendar, Drive, Docs, and more - send/read emails, handle files, events, and tasks.
license: MIT
---

# GOGCLI

## SYSTEM_PRIMITIVES

### TYPES
* `DATETIME` == {`RFC3339`, `RFC3339Nano`, `YYYY-MM-DDTHH:MM[:SS]`, `YYYY-MM-DD HH:MM[:SS]`, `YYYY-MM-DDTHH:MM:SS-0800`}
* `DATE` == `YYYY-MM-DD`
* `RELATIVE_TIME` == {`now`, `today`, `tomorrow`, `yesterday`, `monday`...`sunday`, `next monday`...}
* `DURATION` == `time.ParseDuration` [e.g., `24h`, `15m`]
* `OUTPUT_FORMAT` == {`table`, `json`, `plain`}
* `G_SERVICE` == {`gmail`, `calendar`, `classroom`, `drive`, `docs`, `contacts`, `tasks`, `sheets`, `people`, `groups`}

### GLOBAL_FLAGS
* `--color`: {`auto`, `always`, `never`} [default: `auto`]
* `--json`: `bool` -> force `OUTPUT_FORMAT` == `json`
* `--plain`: `bool` -> force `OUTPUT_FORMAT` == `plain` [tsv]
* `--force`: `bool` -> skip_destructive_confirmations
* `--no-input`: `bool` -> fail_if_prompt_required
* `--version`: `bool`
* `--client`: `string` -> select_oauth_client
* `--out` | `--output`: `path`
* `--out-dir` | `--output-dir`: `path`

### ENV_VARS
* `GOG_COLOR`: {`auto`, `always`, `never`}
* `GOG_JSON`: `1`
* `GOG_PLAIN`: `1`
* `GOG_ACCOUNT`: `email` | `alias`
* `GOG_CLIENT`: `string` -> override `config.json:account_clients`
* `GOG_KEYRING_PASSWORD`: `string`
* `GOG_KEYRING_BACKEND`: {`auto`, `keychain`, `file`}
* `GOG_TIMEZONE`: `IANA_NAME` | `UTC` | `local`
* `GOG_ENABLE_COMMANDS`: `csv` [e.g., `calendar,tasks`]
* `GOG_CALENDAR_WEEKDAY`: `1` -> defaults `--weekday`

## STATE_AND_CONFIG

### CONFIG_JSON
* path == `$(os.UserConfigDir())/gogcli/config.json`
* format == `JSON5`
* keys:
  * `keyring_backend`: {`auto`, `keychain`, `file`}
  * `default_timezone`: `string`
  * `account_aliases`: `map[string]string`
  * `account_clients`: `map[string]string`
  * `client_domains`: `map[string]string`

### CREDENTIALS
* path_default == `$(os.UserConfigDir())/gogcli/credentials.json`
* path_named == `$(os.UserConfigDir())/gogcli/credentials-<client>.json`
* keyring_key == `token:<client>:<email>` [legacy: `token:<email>` -> auto-migrated]

### INTERNAL_STATE
* `gmail_watch` == `$(os.UserConfigDir())/gogcli/state/gmail-watch/<account>.json`
  * schema:
    * `account`: `string`
    * `topic`: `string`
    * `labels`: `[]string`
    * `historyId`: `string`
    * `expirationMs`: `int`
    * `providerExpirationMs`: `int`
    * `renewAfterMs`: `int`
    * `updatedAtMs`: `int`
    * `hook`: `struct`
      * `url`: `string`
      * `token`: `string`
      * `includeBody`: `bool`
      * `maxBytes`: `int`

## COMMAND_SURFACE

### `gog`
* `version`

### `gog config`
* `get` -> `<key>`
* `keys`
* `list`
* `path`
* `set` -> `<key> <value>`
* `unset` -> `<key>`

### `gog auth`
* `credentials` -> `[<credentials.json|->]`
* `credentials list`
* `add` -> `<email>`
  * `--services`: {`user`, `all`, `G_SERVICE`...}
  * `--readonly`: `bool`
  * `--drive-scope`: {`full`, `readonly`, `file`}
  * `--gmail-scope`: {`full`, `readonly`}
  * `--extra-scopes`: `csv`
  * `--manual`: `bool`
  * `--remote`: `bool`
  * `--step`: {`1`, `2`}
  * `--auth-url`: `url`
  * `--listen-addr`: `host[:port]`
  * `--redirect-host`: `host`
  * `--timeout`: `DURATION`
  * `--force-consent`: `bool`
* `services` -> `[--markdown]`
* `manage` -> `[--services ...] [--listen-addr ...] [--redirect-host ...]`
* `keep` -> `<email> --key <service-account.json>`
* `list`
* `status`
* `remove` -> `<email>`
* `alias`
  * `list`
  * `set` -> `<alias> <email>`
  * `unset` -> `<alias>`
* `tokens`
  * `list`
  * `delete` -> `<email>`

### `gog drive`
* `ls` -> `[--all | --parent ID] [--max N] [--page TOKEN] [--query Q] [--[no-]all-drives]`
* `search` -> `<text> [--raw-query] [--max N] [--page TOKEN] [--[no-]all-drives]`
* `get` -> `<fileId>`
* `download` -> `<fileId> [--out PATH] [--format F]`
* `upload` -> `<localPath> [--name N] [--parent ID] [--convert] [--convert-to {doc,sheet,slides}]`
* `mkdir` -> `<name> [--parent ID]`
* `delete` -> `<fileId> [--permanent]`
* `move` -> `<fileId> --parent ID`
* `rename` -> `<fileId> <newName>`
* `share` -> `<fileId> --to {anyone,user,domain} [--email addr] [--domain example.com] [--role {reader,writer}] [--discoverable]`
* `permissions` -> `<fileId> [--max N] [--page TOKEN]`
* `unshare` -> `<fileId> <permissionId>`
* `url` -> `<fileIds...>`
* `drives` -> `[--max N] [--page TOKEN] [--query Q]`

### `gog docs`
* `sed` -> `<DOC_ID> [<expression>]`
  * `-f`: `file` -> read_expressions
  * `-p`: `bool` -> paste_mode
  * `--dry-run` | `-n`: `bool`
  * `-a`: `account`
  * `--tab`: `string` -> target_sheet
* `clear` -> `<DOC_ID>`
* `edit` -> `<DOC_ID>`
* `get` -> `<DOC_ID>`
* `images list` -> `<DOC_ID>`
* `structure` -> `<DOC_ID> [--tab name]`
* `cat` -> `<DOC_ID> [-N]`
* `export` -> `<DOC_ID>`
  * `--format`: {`pdf`, `docx`, `txt`, `md`, `html`}
  * `--out`: `path`

### `gog slides`
* `create-from-template` -> `<templateId> <title>`
  * `--replace`: `KV` -> e.g., `key=value`
  * `--replacements`: `file.json`
  * `--exact`: `bool` -> disable `{{}}` wrapping
  * `--parent`: `folderId`
* `export` -> `<presentationId>`
  * `--format`: {`pdf`, `pptx`}
  * `--out`: `path`

### `gog sheets`
* `export` -> `<spreadsheetId>`
  * `--format`: {`pdf`, `xlsx`, `csv`}
  * `--out`: `path`

### `gog calendar`
* `calendars` -> `[--max N] [--json]`
* `acl` -> `<calendarId>`
* `events` -> `<calendarId> [--cal ID_OR_NAME] [--calendars CSV] [--all] [--from DATETIME|RELATIVE_TIME] [--to DATETIME|RELATIVE_TIME] [--max N] [--page TOKEN] [--query Q] [--weekday]`
* `event` | `get` -> `<calendarId> <eventId>`
* `create` -> `<calendarId> --summary S --from DATETIME --to DATETIME [--description D] [--location L] [--attendees a@b.com,...] [--all-day] [--event-type TYPE]`
* `update` -> `<calendarId> <eventId> [--summary S] [--from DATETIME] [--to DATETIME] [--description D] [--location L] [--attendees ...] [--add-attendee ...] [--all-day] [--event-type TYPE]`
* `delete` -> `<calendarId> <eventId>`
* `freebusy` -> `[calendarIds] [--cal ID_OR_NAME] [--calendars CSV] [--all] --from DATETIME --to DATETIME`
* `conflicts` -> `[--cal ID_OR_NAME] [--calendars CSV] [--all] [--from DATETIME|RELATIVE_TIME] [--to DATETIME|RELATIVE_TIME] [--today|--week|--days N]`
* `respond` -> `<calendarId> <eventId> --status {accepted,declined,tentative} [--send-updates {all,none,externalOnly}]`

### `gog gmail`
* `search` -> `<query> [--max N] [--page TOKEN]`
* `messages search` -> `<query> [--max N] [--page TOKEN] [--include-body]`
* `thread get` -> `<threadId> [--download]`
* `thread modify` -> `<threadId> [--add ...] [--remove ...]`
* `get` -> `<messageId> [--format {full,metadata,raw}] [--headers ...]`
* `attachment` -> `<messageId> <attachmentId> [--out PATH] [--name NAME]`
* `url` -> `<threadIds...>`
* `labels`
  * `list`
  * `get` -> `<labelIdOrName>`
  * `create` -> `<name>`
  * `rename` -> `<labelIdOrName> <newName>`
  * `modify` -> `<threadIds...> [--add ...] [--remove ...]`
* `send`
  * `--to`: `csv_emails`
  * `--subject`: `string`
  * `--body`: `string`
  * `--body-html`: `string`
  * `--cc`: `csv_emails`
  * `--bcc`: `csv_emails`
  * `--reply-to-message-id`: `string`
  * `--reply-to`: `email`
  * `--attach`: `path...`
  * `--track`: `bool` -> inject_tracking_pixel
  * `--track-split`: `bool` -> send_separately_per_recipient
* `drafts`
  * `list` -> `[--max N] [--page TOKEN]`
  * `get` -> `<draftId> [--download]`
  * `create` -> `[flags ~ send]`
  * `update` -> `<draftId> [flags ~ send]`
  * `send` -> `<draftId>`
  * `delete` -> `<draftId>`
* `watch`
  * `start` -> `--topic <gcp-topic> [--label <idOrName>...] [--ttl <sec|DURATION>]`
  * `status`
  * `renew` -> `[--ttl <sec|DURATION>]`
  * `stop`
  * `serve`
    * `--bind`: `ip` [default: `127.0.0.1`]
    * `--port`: `int` [default: `8788`]
    * `--path`: `string` [default: `/gmail-pubsub`]
    * `--verify-oidc`: `bool`
    * `--oidc-email`: `email`
    * `--oidc-audience`: `string`
    * `--token`: `string`
    * `--hook-url`: `url`
    * `--hook-token`: `string`
    * `--fetch-delay`: `DURATION` [default: `3s`]
    * `--include-body`: `bool`
    * `--max-bytes`: `int` [default: `20000`]
    * `--exclude-labels`: `csv` [default: `SPAM,TRASH`]
    * `--history-types`: `csv` {`messageAdded`, `messageDeleted`, `labelAdded`, `labelRemoved`} [default: `messageAdded`]
    * `--save-hook`: `bool`
* `history` -> `--since <historyId> [--max N] [--page TOKEN]`
* `autoreply` -> `<query>`
  * `--body-file`: `path`
  * `--label`: `string` -> dedupe_label
  * `--archive`: `bool`
  * `--mark-read`: `bool`
* `track`
  * `setup` -> `--worker-url <url> [--worker-name <name>] [--db-name <name>] [--worker-dir <path>] [--deploy]`
  * `opens` -> `[<tracking_id> | --to <email>]`
  * `status`

### `gog chat`
* `spaces`
  * `list` -> `[--max N] [--page TOKEN]`
  * `find` -> `<displayName> [--max N]`
  * `create` -> `<displayName> [--member email,...]`
* `messages`
  * `list` -> `<space> [--max N] [--page TOKEN] [--order ORDER] [--thread THREAD] [--unread]`
  * `send` -> `<space> --text TEXT [--thread THREAD]`
* `threads list` -> `<space> [--max N] [--page TOKEN]`
* `dm`
  * `space` -> `<email>`
  * `send` -> `<email> --text TEXT [--thread THREAD]`

### `gog tasks`
* `lists` -> `[--max N] [--page TOKEN]`
* `lists create` -> `<title>`
* `list` -> `<tasklistId> [--max N] [--page TOKEN]`
* `get` -> `<tasklistId> <taskId>`
* `add` -> `<tasklistId> --title T [--notes N] [--due DATE|DATETIME] [--repeat {daily,weekly,monthly,yearly}] [--repeat-count N] [--repeat-until DATETIME] [--parent ID] [--previous ID]`
* `update` -> `<tasklistId> <taskId> [--title T] [--notes N] [--due DATE|DATETIME] [--status {needsAction,completed}]`
* `done` -> `<tasklistId> <taskId>`
* `undo` -> `<tasklistId> <taskId>`
* `delete` -> `<tasklistId> <taskId>`
* `clear` -> `<tasklistId>`

### `gog contacts`
* `search` -> `<query> [--max N]`
* `list` -> `[--max N] [--page TOKEN]`
* `get` -> `<people/...|email> [--json]`
* `create` -> `--given NAME [--family NAME] [--email addr] [--phone num] [--relation type=person]`
* `update` -> `<people/...>`
  * `--given`: `string`
  * `--family`: `string`
  * `--email`: `email`
  * `--phone`: `string`
  * `--birthday`: `DATE`
  * `--notes`: `string`
  * `--relation`: `string`
  * `--from-file`: `path` | `-` -> update_from_json
  * `--ignore-etag`: `bool` -> force_overwrite
* `delete` -> `<people/...>`
* `directory list` -> `[--max N] [--page TOKEN]`
* `directory search` -> `<query> [--max N] [--page TOKEN]`
* `other list` -> `[--max N] [--page TOKEN]`
* `other search` -> `<query> [--max N]`

### `gog people`
* `me`
* `get` -> `<people/...|userId>`
* `search` -> `<query> [--max N] [--page TOKEN]`
* `relations` -> `[<people/...|userId>] [--type TYPE]`

### `gog classroom`
* `courses`
  * `[list]` -> `[--state ...] [--max N] [--page TOKEN]`
  * `get` -> `<courseId>`
  * `create` -> `--name NAME [--owner me] [--state ACTIVE|...]`
  * `update` -> `<courseId> [--name ...] [--state ...]`
  * `delete` -> `<courseId>`
  * `archive` -> `<courseId>`
  * `unarchive` -> `<courseId>`
  * `join` -> `<courseId> [--role {student,teacher}] [--user me]`
  * `leave` -> `<courseId> [--role {student,teacher}] [--user me]`
  * `url` -> `<courseId...>`
* `students` -> `[<courseId>] [--max N] [--page TOKEN]`
  * `get` -> `<courseId> <userId>`
  * `add` -> `<courseId> <userId> [--enrollment-code CODE]`
  * `remove` -> `<courseId> <userId>`
* `teachers` -> `[<courseId>] [--max N] [--page TOKEN]`
  * `get` -> `<courseId> <userId>`
  * `add` -> `<courseId> <userId>`
  * `remove` -> `<courseId> <userId>`
* `roster` -> `<courseId> [--students] [--teachers]`
* `coursework` -> `[<courseId>] [--state ...] [--topic TOPIC_ID] [--scan-pages N] [--max N] [--page TOKEN]`
  * `get` -> `<courseId> <courseworkId>`
  * `create` -> `<courseId> --title TITLE [--type ASSIGNMENT|...]`
  * `update` -> `<courseId> <courseworkId> [--title ...]`
  * `delete` -> `<courseId> <courseworkId>`
  * `assignees` -> `<courseId> <courseworkId> [--mode ...] [--add-student ...]`
* `materials` -> `[<courseId>] [--state ...] [--topic TOPIC_ID] [--scan-pages N] [--max N] [--page TOKEN]`
  * `get` -> `<courseId> <materialId>`
  * `create` -> `<courseId> --title TITLE`
  * `update` -> `<courseId> <materialId> [--title ...]`
  * `delete` -> `<courseId> <materialId>`
* `submissions` -> `<courseId> <courseworkId> [--state ...] [--max N] [--page TOKEN]`
  * `get` -> `<courseId> <courseworkId> <submissionId>`
  * `turn-in` -> `<courseId> <courseworkId> <submissionId>`
  * `reclaim` -> `<courseId> <courseworkId> <submissionId>`
  * `return` -> `<courseId> <courseworkId> <submissionId>`
  * `grade` -> `<courseId> <courseworkId> <submissionId> [--draft N] [--assigned N]`
* `announcements` -> `[<courseId>] [--state ...] [--max N] [--page TOKEN]`
  * `get` -> `<courseId> <announcementId>`
  * `create` -> `<courseId> --text TEXT`
  * `update` -> `<courseId> <announcementId> [--text ...]`
  * `delete` -> `<courseId> <announcementId>`
  * `assignees` -> `<courseId> <announcementId> [--mode ...]`
* `topics` -> `[<courseId>] [--max N] [--page TOKEN]`
  * `get` -> `<courseId> <topicId>`
  * `create` -> `<courseId> --name NAME`
  * `update` -> `<courseId> <topicId> --name NAME`
  * `delete` -> `<courseId> <topicId>`
* `invitations` -> `[--course ID] [--user ID]`
  * `get` -> `<invitationId>`
  * `create` -> `<courseId> <userId> --role {STUDENT,TEACHER,OWNER}`
  * `accept` -> `<invitationId>`
  * `delete` -> `<invitationId>`
* `guardians` -> `<studentId> [--max N] [--page TOKEN]`
  * `get` -> `<studentId> <guardianId>`
  * `delete` -> `<studentId> <guardianId>`
* `guardian-invitations` -> `<studentId> [--state ...] [--max N] [--page TOKEN]`
  * `get` -> `<studentId> <invitationId>`
  * `create` -> `<studentId> --email EMAIL`
* `profile` -> `[userId]`

### `gog time`
* `now` -> `[--timezone TZ]`

## DSL_SURFACE

### `SEDMAT` [Docs Formatting]
* syntax: `s/pattern/replacement/flags`
* inline_flags [brace_syntax]:
  * `{b}`: `bold`
  * `{i}`: `italic`
  * `{_}`: `underline`
  * `{-}`: `strikethrough`
  * `{#}`: `code`
  * `{^}`: `superscript`
  * `{,}`: `subscript`
  * `{w}`: `smallcaps`
* properties [brace_syntax]:
  * `{c=val}`: `color`
  * `{z=val}`: `bg`
  * `{f=val}`: `font`
  * `{s=val}`: `size`
  * `{u=val}`: `url`
  * `{h=val}`: `heading` {1-6, t, s}
  * `{a=val}`: `align` {left, center, right}
  * `{l=val}`: `leading`
  * `{n=val}`: `indent`
  * `{o=val}`: `opacity`
  * `{k=val}`: `kerning`
  * `{p=b,a}`: `spacing` [before,after]
* commands:
  * `d`: `delete` -> `N,Md`
  * `a`: `append` -> `a/pattern/text/`
  * `i`: `insert` -> `i/pattern/text/`
  * `y`: `transliterate`
* paragraphs:
  * `N`: `target_line_N`
  * `N,M`: `range`
  * `$`: `last`
