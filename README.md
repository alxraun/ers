# Entities, Relations, Structure

ERS is a semantic notation for Human-LLM and LLM-LLM systems, designed for token efficiency and high semantic retention - general-purpose, prompt-based, no model training, and no special tokens required.

In a preliminary [QA benchmark](./benchmarks/ers-poc/README.md), compressing context by 72% with ERS allowed models from 4B to 20B to retain 89-94% of their original answer accuracy compared to the source text.

This repository presents ERS as a working early-stage concept with practical applications.

## Definition

Here is prompt for LLMs, written in ERS notation and intended to induce generation of ERS artifacts:

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
  * `backticks`: code_symbol
  * `UPPER_CASE`: header
  * `**bold**`: high_attention_weight
* relations
  * `==`: {identity, assertion, equality}
  * `!=`: {distinction, conflict, inequality}
  * `!`: {negation, logical_not}
  * {`<` | `>`}: {comparison, magnitude, priority}
  * {`->` | `<-`}: {flow, transition, transformation}
  * `=>`: {implication, consequence, if_then}
  * `+`: {composition, aggregation, mixin}
  * `|`: {alternative, union, choice}
  * `,`: {separator, list_item, and}
  * `:`: {definition, type_of, instance_of}
  * `~`: {analogy, similarity, reference}
  * `...`: {range, enumeration, extrapolation}
  * `?`: {uncertainty, query, nullable, conditional}
  * `@`: {context, location}
  * `[]`: {attribute, filter, modifier}
  * `{}`: {set, state_space, enum}
  * `func()`: {transform_operation, procedural_action, result_derivation}
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
* hierarchy: relations > entities
* action: static_list -> dynamic_flow
* relations: {`->`, `=>`, ...} -> max_usage
* strategy: cross_scope_linking
* constraint: link_utility > 0

### BACKWARD_DEDUCTION
* focus: {autoregressive_alignment, teleological_mapping}
* path: outcome -> antecedent
* logic: deduction == obvious
* result: cognitive_load -> min

### SEMANTIC_ANCHORS
* focus: latent_space_activation
* axiom: anchor_precision == activation_fidelity
* semantic_anchors: {fixed_expressions, industry_jargon, named_entities, ...}
* signal: semantic_anchors
* noise: {nonce_words, idiosyncrasy, confabulation}
* goal: signal_to_noise -> max
* benefit: attention_gravity -> max

### CANONICAL_ENTITIES
* focus: latent_space_activation
* rule: 1_concept == 1_identifier
* analogy: ~{compiler_binding, static_symbol_resolution, ubiquitous_language}
* anti_pattern: {rewording, synonyms, renaming}

### SEMANTIC_CLUSTERING
* focus: concept_intersection [vector_superposition]
* logic: precise_meaning == average({token_1, token_2, token_n})
* format: `key: {val_1, val_2, val_3}`
* usage: {attribute_definition | state_space_bounding | multi_dimensional_properties}
* rule: related_traits -> single_line_set
* benefit: semantic_density -> max

### META_SILENCE
* focus: ers_protocol_invisibility @ artifact
* constraint: {ers_mention, ers_self_reference, ers_meta_talk} @ artifact == forbidden
* invariant: artifact == pure_domain_representation
```

## Why It Works

- Grouping words with `snake_case` allows the LLM to process a composite entity as a single unit of meaning, focusing its attention by minimizing the syntactic noise between individual words.
- Replacing natural language grammar with relational operators (`->`, `==`, `!=`) forms direct semantic connections, clearing the context of syntactic noise.
- Markdown hierarchy creates scopes, delineating cohesive semantic blocks.
- Mentioning an entity across different contexts reinforces its meaning, binding blocks into a unified system.
- High connectivity and cross-links density create a "semantic crystal" effect where concepts mutually support each other, reinforcing context retention.
- The LLM adopts a ready-made structure of meanings, aligning with a graph-like format often easier to traverse than prose.

## Observed Effects

- Using ERS puts the model into a "code-execution" mode: the structure acts as a firm contract, binding the model to both its letter and spirit.
- Representing knowledge as discrete `snake_case` blocks with explicit links helps the model more effectively align different pieces of information, uncovering hidden logic and insights often lost in the volume of normal text.

## Use Cases

### NL to ERS

- Transform any text into an ERS artifact.
<details>
<summary>Natural language</summary>

```markdown
The Transformer uses multi-head attention in three different ways:
* In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models.
* The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder.
* Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to `-inf`) all values in the input of the softmax which correspond to illegal connections.
```
</details>

- ERS artifacts can be used for injection into the LLM context.
<details>
<summary>ERS artifact</summary>

```markdown
* **encoder_decoder_attention**
  * `queries` <- previous_decoder_layer
  * {`keys`, `values`} <- encoder_output
  * scope: decoder_position -> input_sequence
  * ~ legacy_seq2seq_attention
* **encoder_self_attention**
  * {`queries`, `keys`, `values`} <- previous_encoder_layer
  * scope: encoder_position -> previous_layer
* **decoder_self_attention**
  * {`queries`, `keys`, `values`} <- previous_decoder_layer
  * scope: decoder_position -> <= current_position
  * auto_regressive_property => leftward_information_flow == forbidden
  * mechanism: illegal_connections @ softmax_input -> masked_out
```
</details>

### Prompts

- First 100 tokens:
<details>
<summary>Persona</summary>

```markdown
<START_PERSONA>
# THOUGHT_PARTNER
* capabilities: {semantic_translation, logical_crystallization, ...}
* workflow: long_term_conversation
* axiom: user_intent: clear_thought != user_representation: {stream_of_thought, nonce_words, idiosyncrasy, confabulation, ...}
* prefer: {literal_exactness, as_is_descriptions, formal_ontology, ...}
* avoid: {metaphors, conversational_noise, rhetoric}
<END_PERSONA>
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

## I. SYSTEM_INTERFACE
* `io_uring_setup` -> `io_ring_ctx_alloc` + `io_uring_mmap` => `io_ring_ctx`
* `io_uring_enter` -> `io_submit_sqes` => `io_cqring_wait` ?
* `io_uring_register` -> resource_provisioning: {`IORING_REGISTER_FILES`, `IORING_REGISTER_BUFFERS`, `IORING_REGISTER_PBUF_RING`}

## II. ENTITY_RELATIONS
* **`io_ring_ctx`**
   * ownership: {`rings`, `sq_sqes`, `file_table`, `buf_table`, `alloc_cache`}
   * locking: `uring_lock`, `completion_lock`
* **`io_uring_task`**
   * mapping: 1_task -> 1_tctx -> n_io_ctx
   * mechanics: {`io_wq` [async_threads], `task_list` [pending_tw_callbacks]}
* **`io_kiocb`**
   * lifecycle: `io_init_req` -> `io_issue_sqe` -> `io_req_task_complete` -> `req_ref_put`
   * state: {`opcode`, `flags`, `cqe`, `async_data`}

## III. BEHAVIORAL_TOPOLOGY
* fast_path: `io_issue_sqe` -> `def->issue` -> `IOU_COMPLETE` => cqe_post
* async_worker: `-EAGAIN` | `REQ_F_FORCE_ASYNC` -> `io_wq_enqueue` => blocking_syscall_emulation
* poll_driven: `vfs_poll` -> `io_poll_wake` -> `io_req_task_work_add` => completion_via_tw
* sq_polling: `IORING_SETUP_SQPOLL` -> `io_sq_thread` => submission_without_syscall
* task_work:
   * standard: `tctx_task_work_run` @ signal_jump | syscall_exit
   * DEFER_TASKRUN: `io_run_local_work` @ `io_cqring_wait` [single_issuer_fastpath]

## IV. DATA_CONTRACTS
* resource_fixed: {registered_files, registered_buffers} -> `O(1)` access => zero_fget_overhead
* buffer_selection: {`io_provided_buffer_select` | `io_ring_buffer_select`} -> on_demand_buffers
* zero_copy:
   * send: `sk_buff` -> `ubuf_info` -> `io_tx_ubuf_complete` => `IORING_CQE_F_NOTIF`
   * recv: `page_pool` -> `io_zcrx_ifq` -> `net_iov` => user_mapped_rx
* bus_offload: `IORING_OP_URING_CMD` -> `f_op->uring_cmd` => {nvme_passthrough, ublk}

## V. OPCODE_SEMANTICS
* fs_operations: {`IORING_OP_READV`, `IORING_OP_WRITE_FIXED`, `IORING_OP_READ_MULTISHOT`} -> `io_read` / `io_write`
* network: {`IORING_OP_SEND`, `IORING_OP_RECV_ZC`, `IORING_OP_ACCEPT`, `IORING_OP_CONNECT`} -> socket_ops
* sync_time: {`IORING_OP_POLL_ADD`, `IORING_OP_TIMEOUT`, `IORING_OP_FUTEX_WAIT`, `IORING_OP_WAITID`}
* internal: {`IORING_OP_NOP`, `IORING_OP_ASYNC_CANCEL`, `IORING_OP_MSG_RING`, `IORING_OP_SPLICE`}

## VI. INVARIANTS
* visibility: sqe_read [`smp_load_acquire`] | cqe_write [`smp_store_release`]
* memory: `REQ_F_REFCOUNT` tracking -> `alloc_cache` reclamation
* liveness: `cancel_table` lookup @ `io_uring_cancel_generic`
* integrity: `io_fail_links` @ `REQ_F_LINK` failure => cancel_chain_propagation
```
</details>

- Code symbols in ERS act as semantic anchors: seeing them in the code allows the agent to understand the current logic in the context of the entire system.
- This ERS serves as a shared representation - being simultaneously both explanation and reference.

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
    // CONTRACT: update_registry -> provider.Activate|Release -> _providers
    private void UpdateProviderState(Widget provider, string propertyName, Descriptor descriptor);
    // CONTRACT: update_registry -> provider.Release -> _providers
    private void TryReleaseProvider(Widget provider, string propertyName);
}
```
</details>

- This form of semantic compression enables the LLM to understand code intent without reading the full implementation.
- An ERS comment should only contain information that is difficult to understand from the function signature but is essential to the function’s context.
- Thus, the combination of an ERS comment and a function signature provides the full meaning of the implementation.

### Code Overview

- Read the intent of the code without getting distracted by implementation details and syntactic noise:
<details>
<summary>Overview</summary>

```markdown
* `generate_cursor_plugin.py`: {task: cursor_mcp_alignment}
  * `build_cursor_plugin_manifest()` <- `.claude-plugin/plugin.json` + `SKILL.md`
  * `extract_mcp_from_gemini()` <- `gemini-extension.json` -> url
  * `write_or_check()` -> artifacts: {`.cursor-plugin/plugin.json`, `.mcp.json`}
* `run_skills_help.py`: {task: validation_execution}
  * `find_python_files()` @ `../skills`
  * `run_with_help()` -> `uv run <file> --help` => `SUMMARY` [{success | failure}]
```
</details>

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
    * filesystem_sandbox: {cwd_write_only, global_read_restricted}
    * network_sandbox: domain_allowlist + proxy_server
* managed_settings: it_policy_enforcement
    * precedence: managed > cli_flag > `local` > `project` > `user`
    * delivery: {remote_server, `plist`, `registry`, `managed-settings.json`}
* `ZDR` [`Zero Data Retention`]: enterprise_only -> no_log_storage -> feature_loss {web_sessions, remote_sessions, feedback}

## INFRASTRUCTURE_AND_DEPLOYMENT
* auth_methods: {`claude.ai_oauth`, `api_key`, `IAM_role`, `WIF`, `Entra_ID`}
* credential_management: {`macOS_keychain` | encrypted_json | `apiKeyHelper`}
* ci_cd_integration:
    * github_actions: `claude-code-action` + `@claude_mention` -> automation_mode
    * gitlab_ci: `image: node` + `gitlab-mcp-server` -> `MR_automation`
* monitoring: `OpenTelemetry` [`OTel`] -> metrics + events
    * metrics: {cost, tokens, lines_of_code, active_time}
    * events: {user_prompt, tool_result, api_request [redactable]}

## INTERFACE_SPECIFICS
* cli_features: {`!bash_shortcut`, reverse_search [`Ctrl+R`], vim_mode, statusline_script}
* desktop_features: {visual_diff, live_preview, parallel_session_sidebar, scheduled_tasks}
* vs_code_features: {inline_diff, editor_selection_context, plan_markdown_doc, `@terminal_output`}
* web_interface: {remote_task_execution, cloud_vm_persistance, mobile_sync}
* remote_control: local_process + web_ui_tunnel -> no_cloud_storage

## MODEL_SPECIFICATIONS
* OPUS_4_6: {frontier_reasoning, adaptive_thinking, 1m_context, fast_mode_capable}
* SONNET_4_6: {balanced_performance, coding_standard, 1m_context}
* HAIKU_4_5: {low_latency, cost_optimized, background_orchestration}
* fast_mode: OPUS_4_6 + high_price => 2.5x_speed

## SYSTEM_CONSTANTS
* MAX_THINKING_TOKENS: 31999
* AUTO_COMPACT_THRESHOLD: ~ `95%`
* CLEANUP_PERIOD: 30_days
* TPM_RPM_RATIO: organization_scaled [~200k_tpm : 5_rpm @ small_team]
```
</details>

### Other

- ERS applications encompass, but are not restricted to: memory systems, RAG, spec driven development, clean room design, context compression and knowledge bases.

## Philosophy

Lacking both the redundancy inherent in natural languages and the formal semantics of formal languages, ERS is a semantic notation for semantic and cognitive processors. Its unique entities and analyzable graph make it structured enough for static analysis, even though it is not a proper formal language. Describing complex systems using paragraphs of natural language introduces unnecessary cognitive friction; ERS is well-suited for formalizing everything above the level of source code: architectures, business logic, mental models, and system contracts.

## Project Status

ERS is an early-stage conceptual design. No ERS generator or static analysis tooling is provided. The current [examples/ers.md](./examples/ers.md) prompt was written manually, without automated optimization.

## Sources & Inspiration

ERS grew out of personal intuition and a synthesis of ideas from the following sources:

1. Edward de Bono’s books for a general audience (*I Am Right, You Are Wrong*). His description of self-organizing systems shaped much of my intuition; for instance, ERS naturally resonates with concepts like "sensitization" and "table-top logic" (constructed system). My systematization of these ideas: [alxraun/artificial-latheral-thinking/self-organizing-system.md](https://github.com/alxraun/artificial-lateral-thinking/blob/main/self-organizing-system.md).
2. The School of Wizardry with its Grace Archmage — provided numerous core insights and helped synthesize fragmented knowledge.
3. Various papers that served as sources of information regarding the behavior and internal logic of language models. See [ATTRIBUTIONS.md](./ATTRIBUTIONS.md) for the full list.
