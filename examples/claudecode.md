# CLAUDE_CODE

## SYSTEM_TOPOLOGY
* claude_code: agentic_coding_environment + {CLI, desktop_app, vs_code_extension, jetbrains_plugin, web_interface, slack_integration}
* claude_code -> architecture: agentic_loop + tool_harness + context_manager
* agentic_loop: gather_context -> take_action -> verify_results -> iterate | stop
* execution_environment: {local_machine, anthropic_cloud_vm, remote_control}
* account_tier: {pro, max, team_standard, team_premium, enterprise, api_console}
* model_provider: {anthropic_1p, amazon_bedrock, google_vertex_ai, microsoft_foundry}

## CORE_AGENTIC_LOOP
* user_prompt -> claude_code => thought_block [extended_thinking] -> tool_use -> tool_output -> iteration
* extended_thinking: adaptive_reasoning + effort_level {low, medium, high}
* effort_level : OPUS_4_6 | SONNET_4_6 => thinking_token_allocation -> dynamic
* built_in_tools:
    * file_ops: {`Read`, `Edit`, `Write`, `NotebookEdit`}
    * discovery: {`Glob`, `Grep`, `LS`}
    * execution: {`Bash`, `Task`}
    * web: {`WebFetch`, `WebSearch`, `Chrome`}
    * orchestration: {`Agent`, `AskUserQuestion`, `CronCreate`, `TaskList`}
* `Bash` @ local: login_shell !persistent_env_vars, working_directory == persistent
* verify_results: {tests, lint, build, visual_preview, chrome_automation}

## CONTEXT_MANAGEMENT
* context_window: {200k, 1m} [model_dependent]
* context_usage -> auto_compaction @ 95%_capacity => conversation_summary
* `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` -> compaction_trigger
* compaction_preservation: `CLAUDE.md` + `MEMORY.md` + recent_code_snippets + key_decisions
* token_optimization: prompt_caching + subagent_delegation + skill_lazy_loading + `/clear`
* input_augmentation:
    * `@file_mention`: fuzzy_search -> file_content -> context
    * image_paste: visual_reasoning -> ui_implementation | bug_diagnosis
    * terminal_output: pipe | `@terminal:name` -> context

## MEMORY_SYSTEM
* memory : `CLAUDE.md` + `MEMORY.md` + `.claude/rules/`
* `CLAUDE.md`: {project_conventions, build_commands, test_patterns} -> human_written
    * loading_logic: recursive_upward_traversal + lazy_subdirectory_discovery
    * imports: `@path/to/file` -> recursive_expansion [max_depth: 5]
* auto_memory: `MEMORY.md` + topic_files -> agent_written
    * logic: incremental_learning -> persistent_knowledge [cross_session]
    * threshold: first_200_lines -> eager_load, topic_files -> on_demand_read
* `.claude/rules/`: path_specific_instructions -> yaml_frontmatter [`paths: []`] => conditional_injection

## EXTENSIONS_ENGINE
* skill: `SKILL.md` + frontmatter + markdown_instructions
    * logic: reusable_workflow | domain_knowledge
    * trigger: user_invocation [`/name`] | model_invocation [description_match]
    * injection: `!backticks_command` -> pre_processing_output -> context
* subagent: isolated_context_loop -> summary_return
    * specialization: {`Explore`, `Plan`, general-purpose, custom}
    * isolation: {context_only, worktree}
    * worktree: git_worktree -> filesystem_isolation -> parallel_task
* agent_team [experimental]: team_lead + teammates + shared_task_list
    * communication: mailbox + p2p_messaging + broadcast
    * topology: independent_context_windows -> high_token_usage
* mcp: model_context_protocol -> external_tool_integration
    * transport: {stdio, http, sse}
    * capabilities: {tools, resources, prompts, list_changed_notifications}
    * scaling: `ToolSearch` -> on_demand_schema_loading
* hook: deterministic_script @ lifecycle_event
    * events: {`SessionStart`, `PreToolUse`, `PostToolUse`, `Stop`, `ConfigChange`, `Notification`}
    * logic: `PreToolUse` + exit_2 => block_action
    * types: {command, http, prompt, agent}
* plugin: package {skills, agents, hooks, mcp, lsp}
    * namespace: `plugin_name:component_name`
    * marketplace: `marketplace.json` -> distribution_catalog

## SECURITY_AND_GOVERNANCE
* permission_system: `deny` > `ask` > `allow`
    * scope: `Bash(pattern *)`, `Read(path)`, `WebFetch(domain)`, `Skill(name)`
    * mode: {`default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`}
* sandboxing: os_level_isolation {`Seatbelt` @ macOS, `bubblewrap` @ Linux}
    * filesystem_sandbox: cwd_write_only, global_read_restricted
    * network_sandbox: domain_allowlist + proxy_server
* managed_settings: it_policy_enforcement
    * precedence: managed > cli_flag > `local` > `project` > `user`
    * delivery: {remote_server, `plist`, `registry`, `managed-settings.json`}
* `ZDR` [Zero Data Retention]: enterprise_only -> no_log_storage -> feature_loss {web_sessions, remote_sessions, feedback}

## INFRASTRUCTURE_AND_DEPLOYMENT
* auth_methods: {`claude.ai_oauth`, `api_key`, `IAM_role`, `WIF`, `Entra_ID`}
* credential_management: `macOS_keychain` | encrypted_json | `apiKeyHelper`
* ci_cd_integration:
    * github_actions: `claude-code-action` + `@claude_mention` -> automation_mode
    * gitlab_ci: `image: node` + `gitlab-mcp-server` -> `MR_automation`
* monitoring: `OpenTelemetry` [`OTel`] -> metrics + events
    * metrics: cost, tokens, lines_of_code, active_time
    * events: user_prompt, tool_result, api_request [redactable]

## INTERFACE_SPECIFICS
* cli_features: `!bash_shortcut`, reverse_search [Ctrl+R], vim_mode, statusline_script
* desktop_features: visual_diff, live_preview, parallel_session_sidebar, scheduled_tasks
* vs_code_features: inline_diff, editor_selection_context, plan_markdown_doc, `@terminal_output`
* web_interface: remote_task_execution, cloud_vm_persistance, mobile_sync
* remote_control: local_process + web_ui_tunnel -> no_cloud_storage

## MODEL_SPECIFICATIONS
* OPUS_4_6: frontier_reasoning, adaptive_thinking, 1m_context, fast_mode_capable
* SONNET_4_6: balanced_performance, coding_standard, 1m_context
* HAIKU_4_5: low_latency, cost_optimized, background_orchestration
* fast_mode: OPUS_4_6 + high_price => 2.5x_speed

## SYSTEM_CONSTANTS
* MAX_THINKING_TOKENS: 31999
* AUTO_COMPACT_THRESHOLD: ~ `95%`
* CLEANUP_PERIOD: 30_days
* TPM_RPM_RATIO: organization_scaled [~200k_TPM : 5_RPM @ small_team]
