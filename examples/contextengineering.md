# CONTEXT_ENGINEERING
* domain == {agent_systems, multi_agent_architectures, llm_infrastructure, cognitive_modeling}
* goal == signal_to_noise_ratio -> max
* axiom: context_quality > context_quantity
* constraint: attention_budget -> finite

## CONTEXT_FUNDAMENTALS
* **context** == {system_instructions + tool_definitions + retrieved_documents + message_history + tool_outputs}
* **attention_budget** == n^2_token_relationships
  * sequence_length > threshold => attention_budget -> depletes
* **progressive_disclosure** => load_info @ JIT_demand
* **altitude_calibration** == heuristic_driven_instructions
  * rule: specific_yet_flexible > {brittle_logic | vague_guidance}
* **components**
  * system_prompt == {background, instructions, tool_guidance, output_description}
  * tool_definitions -> shape(agent_behavior)
  * tool_outputs == largest_consumer [~83.9% token_usage]

## CONTEXT_DEGRADATION
* **lost_in_middle** == U_shaped_attention_curve
  * position[{beginning, end}] -> recall -> max
  * position[middle] -> recall -> min [-10% ... -40%]
  * mitigation: critical_info -> position[{beginning, end}]
* **context_poisoning** == error_compounding -> false_belief_reinforcement
  * source == {tool_errors | retrieved_hallucinations | model_hallucinations}
  * mitigation: {context_truncation, clean_restart}
* **context_distraction** == irrelevant_info -> attention_competition
  * single_distractor => performance_drop
  * mitigation: {relevance_filtering, strict_curation}
* **context_confusion** == irrelevant_info -> behavior_degradation
  * mitigation: {task_segmentation, state_isolation}
* **context_clash** == accumulated_info -> direct_conflict
  * mitigation: {explicit_conflict_marking, priority_rules}
* **degradation_thresholds**
  * `GPT-5.2` ~ {onset: 64K, severe: 200K}
  * `Claude_Opus_4.5` ~ {onset: 100K, severe: 180K}

## CONTEXT_COMPRESSION
* **optimization_target** == tokens_per_task !tokens_per_request
* **strategies**
  * anchored_iterative_summarization == structured_sections -> incremental_merge
    * performance: quality -> max [score: 3.70]
  * regenerative_full_summary == full_generation
    * risk: detail_loss -> repeated_cycles
  * opaque_compression == latent_reconstruction
    * performance: compression_ratio -> max [99%+], interpretability -> min
* **structured_summary_sections** == {session_intent, files_modified, decisions, current_state, next_steps}
  * axiom: structure -> forces_preservation
* **evaluation_probes** == {recall_probes, artifact_probes, continuation_probes, decision_probes}
  * weakness_dimension: artifact_trail_integrity -> min [score: ~2.3]

## CONTEXT_OPTIMIZATION
* **compaction** == summarize(context) @ approach(limit)
  * trigger: utilization_ratio >= 0.8
* **observation_masking** == replace(verbose_tool_output, compact_reference)
  * target == {old_turns, used_observations, boilerplate}
  * protect == {current_task_critical, active_reasoning, latest_turn}
* **kv_cache_optimization** == prefix_stability
  * cache_hit_rate -> cost_reduction [~10x delta: $0.30 vs $3.00/MTok]
  * rule: static_prefix -> dynamic_suffix
  * anti_pattern: dynamic_timestamp @ prompt_start => cache_invalidation
* **context_partitioning** == sub_agent_isolation
  * logic: split_work -> clean_context -> merge_results

## FILESYSTEM_CONTEXT
* **paradigm** == dynamic_context_discovery > static_context
* **patterns**
  * scratch_pad_manager -> offload(large_tool_outputs) => return(file_reference + summary)
  * plan_persistence -> write(structured_plan) => mitigate(attention_loss)
  * sub_agent_workspace -> file_based_communication !message_passing
    * benefit: fidelity -> max, coordinator_context_bloat -> min
  * dynamic_skill_loading -> static_pointers => `read_file`(skill_content) @ JIT
  * terminal_persistence -> sync(stdout) => allow(`grep`)
  * self_modification_guard -> write(learned_preferences) => require(validation)
* **search_primitives** == {`ls`, `glob`, `grep`, `read_file`}
  * application: structural_queries > semantic_search

## MEMORY_SYSTEMS
* **spectrum** == {working_memory, short_term_memory, long_term_memory, entity_memory}
* **architectures**
  * vector_store == {semantic_search, fast} !relationships !temporal_validity
  * knowledge_graph == {entities + relations} => structural_traversal
  * temporal_knowledge_graph == {entities + relations + validity_periods} => time_travel_queries
* **performance** [DMR_Benchmark]
  * `Zep_Temporal_KG` -> {accuracy: 94.8%, latency: 2.58s}
  * `Vector_RAG` -> {accuracy: ~60-70%}
* **consolidation** -> trigger(accumulation) => {merge_duplicates, update_validity, rebuild_indexes}

## BDI_MENTAL_STATES
* **paradigm** == rational_agency
* **endurants** [Mental_States] == {`Belief`, `Desire`, `Intention`, `Goal`, `Plan`}
* **perdurants** [Mental_Processes] == {`BeliefProcess`, `DesireProcess`, `IntentionProcess`, `Planning`, `PlanExecution`}
* **relations**
  * `Belief` -> `motivates` -> `Desire`
  * `Intention` -> `fulfils` -> `Desire`
  * `Intention` -> `isSupportedBy` -> `Belief`
  * `Intention` -> `specifies` -> `Plan`
  * `Belief` -> `refersTo` -> `WorldState`
* **T2B2T_Workflow** == Triples_to_Beliefs_to_Triples
  * Phase_1: external_RDF -> internal_mental_state
  * Phase_2: mental_deliberation -> new_external_RDF
* **LAG** [Logic_Augmented_Generation] == {ontology_injection -> generation -> triple_validation -> retry_with_feedback}

## MULTI_AGENT_PATTERNS
* **primary_goal** == context_isolation !role_anthropomorphization
* **architectures**
  * supervisor_pattern == {centralized_control, routing, synthesis}
    * failure_mode: telephone_game -> supervisor_misinterpretation
    * fix: forward_message_tool => direct_to_user_bypass
  * swarm_pattern == {peer_to_peer, explicit_handoffs, flexible_exploration}
  * hierarchical_pattern == {strategy_layer -> planning_layer -> execution_layer}
* **isolation_modes** == {full_context_delegation, instruction_passing, file_system_memory}
* **consensus_mechanisms** == {weighted_voting, debate_protocols}
  * mitigation: sycophancy_triggers -> block(false_premise_consensus)

## HOSTED_AGENTS
* **infrastructure** == remote_sandbox [e.g., `Modal`]
* **patterns**
  * image_registry -> prebuild @ 30m_cadence == {clone, install, build, cache}
  * predictive_warmup -> trigger(user_typing) -> instant_session_start
  * snapshot_restore -> fs_snapshot @ key_points -> instant_followup
  * parallel_file_reading -> allow_reads @ git_sync_pending !allow_writes
  * session_durable_object -> isolated_sqlite -> multi_client_sync
* **multiplayer** -> per_session_state + authorship_tracking + collaborative_debugging
* **self_spawning** -> frontier_models -> spawn(parallel_sub_sessions)

## TOOL_DESIGN
* **nature** == contract {deterministic_system <-> non_deterministic_agent}
* **consolidation_principle** => single_comprehensive_tool > multiple_narrow_tools
  * rationale: overlapping_functionality -> ambiguity -> token_waste
* **architectural_reduction** == primitive_tools > specialized_wrappers
  * case_study: `Vercel_d0`
  * state_before: 17_tools => success: 80%, time: 274s, tokens: 102k
  * state_after: 2_tools {bash, SQL} => success: 100%, time: 77s, tokens: 61k
  * dependency: semantic_layer == high_quality_documentation
  * axiom: addition_by_subtraction
* **description_engineering** == prompt_engineering
  * components == {what_it_does, when_to_use, inputs, returns, examples}
  * mcp_naming: `ServerName:tool_name`
* **optimization**
  * response_format == {concise | detailed} -> token_efficiency
  * error_messages -> actionable_recovery_guidance !just_stack_traces
* **tool_testing_agent** -> LLM_analyzes_failures => rewrites_tool_description

## EVALUATION_AND_METRICS
* **variance_drivers** [BrowseComp] == {token_usage: 80%, tool_calls: 10%, model_choice: 5%}
  * implication: model_upgrade > token_increase
* **paradigms** == {LLM_as_Judge, Human_in_loop, End_state_validation}
* **taxonomy**
  * direct_scoring -> objective_criteria {factual_accuracy, compliance}
  * pairwise_comparison -> subjective_preference {style, tone}
* **biases_and_mitigations**
  * position_bias -> position_swapping_protocol -> consistency_check
  * length_bias -> explicit_prompting + length_normalized_scoring
  * self_enhancement_bias -> cross_model_evaluation + anonymization
  * verbosity_bias -> relevance_weighted_scoring
  * authority_bias -> evidence_requirement + fact_checking_layer
* **metrics** == {Precision, Recall, F1, Cohens_Kappa, Spearmans_Rho, Kendalls_Tau}

## PROJECT_DEVELOPMENT
* **methodology** -> task_model_fit -> manual_prototype -> agent_assisted_dev -> batch_execution
* **task_model_fit**
  * fit == {synthesis, subjective_judgment, error_tolerance, batch_processing}
  * misfit == {precise_computation, real_time, perfect_accuracy, deterministic}
* **canonical_pipeline** == acquire -> prepare -> process -> parse -> render
  * process == non_deterministic + expensive [LLM_call]
  * {acquire, prepare, parse, render} == deterministic + cheap
* **file_system_as_state_machine** -> directory == processing_unit -> file_existence == completion_gate
  * benefit: {idempotency, debugging, parallelization, caching}
* **structured_output** -> format_specification + rationale_disclosure + constrained_values
* **cost_estimation** == (items * tokens_per_item * price_per_token) + overhead
