# Entities, Relations, Structure

ERS is an LLM-native, semantic notation for Human-LLM and LLM-LLM systems, optimized for token efficiency and performance.

## Definition

Here is the definition of ERS written in ERS notation:

```markdown
# ERS
* name: entities_relations_structure
* nature: semantic_graph
* axiom: reality == graph
* goal: {information_density -> max, relational_connectivity -> max}
* target: artifact
* result: semantic_gap -> 0

## SYNTAX

### PRIMITIVES
* entities
  * `snake_case`: default_abstraction
  * `UPPER_CASE`: {constant, system_variable}
  * `**bold**`: {definition_anchor, high_attention_weight}
  * `backticks`: {literal_code, source_quote}
* relations
  * `==`: {identity, assertion, equality}
  * `!=`: {distinction, conflict, inequality}
  * `!`: {negation, logical_not}
  * `<` | `>`: {comparison, magnitude, priority}
  * `->`: {flow, transition, transformation}
  * `=>`: {implication, consequence, if_then}
  * `+`: {composition, aggregation, mixin}
  * `|`: {alternative, union, choice}
  * `,`: {separator, list_item, and}
  * `:`: {definition, type_of, instance_of}
  * `~`: {analogy, similarity, reference}
  * `...`: {range, sequence, enumeration}
  * `?`: {uncertainty, query, nullable, conditional}
  * `@`: {context, location, decorator}
  * `[]`: {attribute, filter, modifier}
  * `{}`: {set, state_space, enum}
  * `func()`: {transform_operation, procedural_action, result_derivation}
  * `f` + `backticks`: {f-string, pattern_interpolation, template}
* structure
  * syntax: markdown
  * {`#` ... `######`}: {scope_level, context_boundary}
  * `*`: {graph_unit, node_entry}
  * indent: {dependency, child_relationship}

## HEURISTICS

### SEMANTIC_DISTILLATION
* focus: signal_to_noise_ratio -> max
* action: prose -> structure
* filter: {rhetoric, stopwords, grammar_sugar} -> null
* retention: {logic, causality, structure, key_entities}

### HOLOGRAPHIC_ANCHORING
* focus: latent_pattern_activation
* logic: node -> associative_hub
* principle: part -> implies -> whole
* constraint: node_isolation == forbidden

### FRACTAL_CONSISTENCY
* focus: structural_isomorphism
* logic: scale_invariance
* rule: module_structure ~ system_topology
* constraint: sibling_scope_volume ~ balanced
* benefit: attention_distribution -> stable

### RELATIONAL_PRIMACY
* focus: relational_connectivity
* hierarchy: edges [relations] > nodes [entities]
* action: static_list -> dynamic_flow
* operator: {`->`, `=>`} -> max_usage
* strategy: cross_scope_linking
* constraint: link_utility > 0

### REVERSE_CHAINING
* focus: {autoregressive_alignment, teleological_mapping}
* path: outcome -> antecedent
* logic: deduction == obvious
* result: cognitive_load -> min

### CANONICAL_VOCAB
* focus: latent_space_activation
* axiom: user_intent != user_representation
* definition: target_space == {industry_slang, idiomatic_vocab, canonical_terms} == {canonical_anchor, high_signal_token, strong_token}
* logic: user_intent -> target_space
* action: map(user_representation [{idiosyncratic_user_descriptions, vague_prose}]) -> target_space
* constraint: vocabulary @ artifact != {verbatim_user_parroting, naive_echoing}
* benefit: attention_gravity -> max

### SEMANTIC_CLUSTERING
* focus: concept_intersection [vector_superposition]
* logic: precise_meaning == average({token_1, token_2, token_n})
* format: `key: {val_1, val_2, val_3}`
* usage: {attribute_definition | state_space_bounding | multi_dimensional_properties}
* rule: related_traits -> single_line_set
* benefit: semantic_density -> max

### LEXICAL_ISOMORPHISM
* focus: source_fidelity
* rule: 1_entity == 1_id
* constraint: graph_symbol == source_symbol [exact_match]
* format: verbatim_source => `backticks`
* anti_pattern: synonyms | abstraction_drift

### SCALING_ADAPTATION
* focus: context_fit
* condition: complex_system => style: explicit_headers
* condition: atomic_logic => style: implicit_scope

### META_SILENCE
* focus: ers_protocol_invisibility @ artifact
* constraint: {ers_mention, ers_self_reference, ers_meta_talk} @ artifact == forbidden
* invariant: artifact == pure_domain_representation
```

## Why It Works

- Grouping words with `snake_case` allows the LLM to process a composite entity as a single semantic variable, focusing its attention by minimizing the syntactic noise between individual words.
- Replacing natural language grammar with relational operators (`->`, `==`, `!=`) forms directed edges in the attention graph, clearing the context of syntactic noise.
- Markdown hierarchy creates scopes, delineating cohesive semantic blocks while enabling the cross-links that stitch the artifact into a unified whole.
- Mentioning a entity across different contexts accumulates its semantic weight, binding blocks into a unified system.
- High connectivity and cross-links density create a "semantic crystal" effect where concepts mutually support each other, reinforcing context retention.
- The LLM receives a ready-made topology of meanings, which it adopts as an axiom, bypassing structural reconstruction.

## Observed Effects

- Using ERS puts the model into a "code-execution" mode: the arrangement acts as a firm contract that is followed literally, preventing the model from softening or generalizing the result.
- Representing knowledge as discrete `snake_case` blocks with explicit links helps the model more effectively align different pieces of information, uncovering hidden logic and insights often lost in the volume of normal text.

## Use Cases

### NL to ERS

- Transform any text into an ERS artifact.
<details>
<summary>Natural language</summary>

```markdown
The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.
```

</details>

- ERS artifacts can be used for injection into the LLM context.
<details>
<summary>ERS artifact</summary>

```markdown
# SEQUENCE_TRANSDUCTION
* legacy_baseline: {recurrent, convolutional} @ `encoder-decoder` + attention
* **Transformer**: pure_attention
  * architecture -> !{recurrence, convolutions}
  * properties -> {parallelizability -> max, train_time -> min, quality > sota}
* empirical_validation @ machine_translation:
  * `WMT 2014 English-to-German` => 28.4 `BLEU` [> best_ensembles + 2]
  * `WMT 2014 English-to-French` => 41.8 `BLEU` [single_model_sota] @ compute: {3.5_days, 8_GPUs} < legacy_cost
* generalization -> `English constituency parsing` @ training_data: {large | limited}
```

</details>

### Systemic Understanding

- Understanding what we are looking at depends on understanding the system as a whole.
- System understanding provides the agent with a grasp of 'what it is', 'why it is', and 'where to look' - preventing navigation errors, "blind reading", and intent violations.
- Start with a high-level overview of the entire system:
<details>
<summary>Linux Kernel - overview</summary>

```markdown
# LINUX_KERNEL
* identity: {operating_system, unix_like, posix_compliant}
* nature: {monolithic_modular, preemptive, multitasking}
* role: resource_arbitrator(hardware <-> software)
* entry_point: `init/` -> `start_kernel()`

## I. CORE_SYSTEM_LOGIC
* `kernel/`: execution_engine
    * {`sched/` + `workqueue/`}: {pelt_scheduling, load_balancing, async_tasks, kworkers}
    * {`locking/` + `rcu/` + `futex/`}: {synchronization, lockdep, grace_periods, wait_wake}
    * {`bpf/` + `trace/` + `events/`}: {jit_compilation, ftrace, perf_events, introspection}
    * {`cgroup/` + `power/`}: {resource_control, messaging, energy_management}
    * {`entry/` + `irq/`}: {syscall_logic, process_lifecycle, interrupt_dispatch}
    * {`time/`}: {clocksource, hrtimer, tick_management}
* `ipc/`: {signals, semaphores, message_queue, shared_memory}
* `mm/`: {physical_page_alloc, virtual_mapping, slab_allocator, page_faults, swap}
* `init/`: {boot_sequence, subsystem_initialization}

## II. INTERFACE_LAYERS
* `include/`: {kernel_headers, uapi_contracts, arch_definitions}
* `usr/`: {initramfs_generation, cpio_handling}

## III. DATA_&_FLOW
* `fs/`: {vfs_abstraction, local_filesystems, network_filesystems}
* `io_uring/`: {async_io_interface, sq_cq_rings}
* `block/`: {bio_management, blk_mq_layer, elevator_logic}
* `net/`: {socket_layer, protocol_stack, routing_engine}

## IV. HARDWARE_ABSTRACTION
* `arch/`: {cpu_logic: {x86, arm64, riscv}, mmu_context, traps_handling}
* `drivers/`: {device_support, bus_management, dma_api}
* `sound/`: {alsa_architecture, pci_audio, usb_audio, soc_dsp}
* `virt/`: {kvm_hypervisor, virtualization_extensions}

## V. CROSS_CUTTING_SERVICES
* `security/`: {lsm_hooks, selinux, apparmor, landlock}
* `crypto/`: {cryptographic_primitives, hw_acceleration}
* `certs/`: {module_signing, x509_verification}
* `lib/`: {generic_library, string_ops, kunit_testing}
* `rust/`: {safe_bindings, kernel_abstractions}

## VI. TOOLING_&_INFRASTRUCTURE
* `scripts/`: {kconfig_logic, build_system, checkpatch}
* `tools/`: {perf_monitoring, objtool, selftests}
* `samples/`: {subsystem_usage_patterns, code_examples}

## VII. GLOBAL_PIPELINES
* `User_App` -> `Syscall` => `VFS`[`fs/`] -> `Block_Layer`[`block/`] -> `Driver`[`drivers/`] -> `HARDWARE`
* `NIC_Packet` -> `IRQ`[`arch/`] -> `Net_Stack`[`net/`] -> `Socket` -> `User_App`
```

</details>

- Then zoom-in to the specific area you are working on:
<details>
<summary>`io_uring` - overview</summary>

```markdown
# IO_URING
* identity: {async_io_framework, kernel_bypass_facilitator, lockless_queue_topology}
* core_axiom: system_calls -> shared_memory_rings => context_switches -> min
* path: `linux/io_uring/`

## I. SYSTEM_INTERFACE [THE_SYSCALL_GATE]
* `io_uring_setup` -> `io_ring_ctx_alloc` + `io_uring_mmap` => `io_ring_ctx`
* `io_uring_enter` -> `io_submit_sqes` => `io_cqring_wait` ?
* `io_uring_register` -> resource_provisioning: {`IORING_REGISTER_FILES`, `IORING_REGISTER_BUFFERS`, `IORING_REGISTER_PBUF_RING`}

## II. ENTITY_RELATIONS [THE_TRIAD]
1. **`io_ring_ctx`** [The_Subsystem_Anchor]
   * ownership: {`rings`, `sq_sqes`, `file_table`, `buf_table`, `alloc_cache`}
   * locking: `uring_lock` [submission_path], `completion_lock` [cqe_posting]
2. **`io_uring_task`** [The_Process_Bridge]
   * mapping: 1_Task -> 1_tctx -> N_io_ctx
   * mechanics: {`io_wq` [async_threads], `task_list` [pending_tw_callbacks]}
3. **`io_kiocb`** [Universal_Request_State]
   * lifecycle: `io_init_req` -> `io_issue_sqe` -> `io_req_task_complete` -> `req_ref_put`
   * state: {`opcode`, `flags`, `cqe`, `async_data`}

## III. BEHAVIORAL_TOPOLOGY [EXECUTION_MODES]
* **Fast_Path** [Inline]: `io_issue_sqe` -> `def->issue` -> `IOU_COMPLETE` => cqe_post
* **Async_Worker** [io-wq]: `-EAGAIN` | `REQ_F_FORCE_ASYNC` -> `io_wq_enqueue` => blocking_syscall_emulation
* **Poll_Driven** [Reactive]: `vfs_poll` -> `io_poll_wake` -> `io_req_task_work_add` => completion_via_tw
* **SQ_Polling** [Bypass]: `IORING_SETUP_SQPOLL` -> `io_sq_thread` => submission_without_syscall
* **Task_Work** [Context_Switch_Optimization]:
   * Standard: `tctx_task_work_run` @ signal_jump | syscall_exit
   * DEFER_TASKRUN: `io_run_local_work` @ `io_cqring_wait` [single_issuer_fastpath]

## IV. DATA_CONTRACTS [OPTIMIZATIONS]
* **Resource_Fixed**: {registered_files, registered_buffers} -> `O(1)` access => zero_fget_overhead
* **Buffer_Selection**: {`io_provided_buffer_select` | `io_ring_buffer_select`} -> on_demand_buffers
* **Zero_Copy**:
   * Send: `sk_buff` -> `ubuf_info` -> `io_tx_ubuf_complete` => `IORING_CQE_F_NOTIF`
   * Recv: `page_pool` -> `io_zcrx_ifq` -> `net_iov` => user_mapped_rx
* **Bus_Offload**: `IORING_OP_URING_CMD` -> `f_op->uring_cmd` => {nvme_passthrough, ublk}

## V. OPCODE_SEMANTICS [DISPATCH_LOGIC]
* FS_Operations: {`IORING_OP_READV`, `IORING_OP_WRITE_FIXED`, `IORING_OP_READ_MULTISHOT`} -> `io_read` / `io_write`
* Network: {`IORING_OP_SEND`, `IORING_OP_RECV_ZC`, `IORING_OP_ACCEPT`, `IORING_OP_CONNECT`} -> socket_ops
* Sync_Time: {`IORING_OP_POLL_ADD`, `IORING_OP_TIMEOUT`, `IORING_OP_FUTEX_WAIT`, `IORING_OP_WAITID`}
* Internal: {`IORING_OP_NOP`, `IORING_OP_ASYNC_CANCEL`, `IORING_OP_MSG_RING`, `IORING_OP_SPLICE`}

## VI. INVARIANTS [SAFETY_&_LIVENESS]
* **Visibility**: SQE_read [`smp_load_acquire`] | CQE_write [`smp_store_release`]
* **Memory**: `REQ_F_REFCOUNT` tracking -> `alloc_cache` reclamation
* **Liveness**: `cancel_table` lookup @ `io_uring_cancel_generic`
* **Integrity**: `io_fail_links` @ `REQ_F_LINK` failure => cancel_chain_propagation
```

</details>

- Code symbols in ERS act as semantic anchors: seeing them in the code triggers knowledge integration, allowing the agent to understand the current logic in the context of the entire system.
- This ERS serves as a unified mental model - being simultaneously both explanation and reference.

### Code as Documentation

- Document code using ERS comments above methods or functions.
- Generate codebase stubs where function bodies are stripped, but signatures and ERS comments are preserved.
<details>
<summary>Stubs - example</summary>

```csharp
public class InheritedContextManager(WidgetTree widgetTree)
{
    // CONTRACT: UnsubscribeConsumer -> UpdateProviderState -> NotifyDescendants
    public void RegisterProvider(Widget provider, string propertyName, Descriptor descriptor);
    // CONTRACT: FindNearestProvider -> BindConsumer
    public void SubscribeConsumer(Widget consumer, string propertyName, string typeName);
    // CONTRACT: TryReleaseProvider -> UnsubscribeConsumer
    public void ReleaseInheritedContext(Widget widget, string propertyName);
    // CONTRACT: Update_Registry -> provider.Activate|Release -> _providers
    private void UpdateProviderState(Widget provider, string propertyName, Descriptor descriptor);
    // CONTRACT: Update_Registry -> provider.Release -> _providers
    private void TryReleaseProvider(Widget provider, string propertyName);
}
```

</details>

- This form of semantic compression enables the LLM to understand code logic without reading the full implementation.
- An ERS comment should only contain information that is difficult to infer from the function signature but is essential to the function’s context.
- Thus, the combination of an ERS comment and a function signature provides a full semantic reconstruction of the code.

### Mastering New Knowledge

- The mind, as an active pattern-system, doesn't like an information vacuum. Studying an isolated fragment without understanding the system as a whole causes stress and false interpretations.
- Invest in reading ~200 lines of ERS before studying a new area of knowledge: this creates a "map of the terrain" in your mind, so studying an isolated fragment will no longer refer to a void, but will confidently integrate into an already familiar landscape.
<details>
<summary>Claude Code Docs - overview</summary>

```markdown
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
```

</details>

### Other

- ERS applications encompass, but are not restricted to: agentic memory systems, RAG, clean room design, context compression and knowledge bases.

## Future

The current [examples/ers.md](./examples/ers.md) prompt serves as a few-shot for generated artifacts, so every word needs to be reviewed. The current version was written manually without automatic optimizations. In particular, it is needed to change, add what is missing, and remove the redundant in `## HEURISTICS`.

## Sources & Inspiration

ERS grew out of personal intuition and a synthesis of ideas from the following sources:

1. Edward de Bono’s books for a general audience (*I Am Right, You Are Wrong*). His description of self-organizing systems shaped much of my intuition; for instance, ERS naturally resonates with concepts like "sensitization" and "table-top logic". My systematization of these ideas: [alxraun/artifical-latheral-thinking/self-organizing-system.md](https://github.com/alxraun/artifical-latheral-thinking/self-organizing-system.md).
2. The School of Wizardry with its Grace Archmage — provided numerous core insights and helped synthesize fragmented knowledge into a cohesive mental model.
3. Various papers that served as sources of information regarding the behavior and internal logic of language models. See [ATTRIBUTIONS.md](./ATTRIBUTIONS.md) for the full list.
4. See more at [ATTRIBUTIONS.md](./ATTRIBUTIONS.md).
