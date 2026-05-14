# DESIGN_PATTERNS

## SOLID
* single_responsibility: {one_reason_to_change, task_encapsulation, cohesive_unit}
* open_closed: {extension_open, modification_closed, abstraction_layer, behavior_inheritance}
* liskov_substitution: {subtype_interchangeability, base_type_contract, behavior_consistency}
* interface_segregation: {fat_interface_splitting, client_specific_methods, dependency_pruning}
* dependency_inversion: {abstraction_reliance, high_low_level_decoupling, detail_independence}

## CREATIONAL
* simple_factory: {instantiation_logic_hiding, object_generation, creation_encapsulation}
* factory_method: {subclass_delegation, instantiation_override, runtime_type_decision}
* abstract_factory: {factory_of_factories, family_of_related_objects, dependency_grouping, theme_consistency}
* builder: {multi_step_creation, avoid_telescoping_constructor, configuration_flavors, step_by_step_assembly}
* prototype: {object_cloning, existing_instance_copy, cost_reduction, state_duplication}
* singleton: {single_instance, global_access_point, private_constructor, resource_coordinator}

## STRUCTURAL
* adapter: {interface_compatibility, wrapper_logic, legacy_integration, translator_role}
* bridge: {composition_over_inheritance, decouple_abstraction_implementation, independent_variation}
* composite: {part_whole_hierarchy, tree_structure, uniform_treatment, nested_objects}
* decorator: {dynamic_behavior_extension, runtime_wrapping, static_inheritance_alternative, srp_adherence}
* facade: {simplified_interface, complex_subsystem_entry, dependency_reduction, entry_point}
* flyweight: {memory_optimization, state_sharing, intrinsic_vs_extrinsic, resource_efficiency}
* proxy: {access_control, placeholder_agent, lazy_initialization, security_shield, remote_representation}

## BEHAVIORAL
* chain_of_responsibility: {request_forwarding, handler_chain, decoupled_sender, successor_logic}
* command: {action_encapsulation, invoker_receiver_decoupling, undo_redo_support, transaction_logging}
* iterator: {sequential_access, container_traversal, underlying_structure_hiding, pointer_logic}
* mediator: {colleague_interaction_control, central_hub, reduced_coupling, communication_encapsulation}
* memento: {state_capture, restoration_undo, rollback_support, encapsulation_preservation}
* observer: {one_to_many_dependency, state_change_notification, publisher_subscriber, event_broadcast}
* visitor: {operation_separation, open_closed_adherence, new_logic_externalization, double_dispatch}
* strategy: {algorithm_runtime_swapping, interchangeable_logic, policy_selection, conditional_logic_removal}
* state: {behavior_change_on_state, finite_state_machine, transition_logic, context_delegation}
* template_method: {algorithm_skeleton, deferred_steps_to_subclasses, structural_invariance, hook_methods}
* interpreter: {grammar_definition, language_expression_evaluation, domain_specific_logic}

## GRASP
* information_expert: {responsibility_assignment, data_owner_logic, encapsulation_max, information_proximity}
* creator: {instance_creation, container_aggregation, initialization_data, recording_responsibility}
* controller: {ui_delegation, use_case_coordination, system_entry_point, workflow_logic}
* low_coupling: {dependency_min, class_independence, change_isolation, reuse_readiness}
* high_cohesion: {focused_responsibilities, logical_unity, complexity_reduction, clarity_max}
* polymorphism: {pluggable_behavior, interface_variation, data_driven_dispatch, switch_statement_removal}
* pure_fabrication: {artificial_class, non_domain_logic, decoupling_helper, cohesion_support}
* indirection: {intermediate_proxy, mediator_role, coupling_severance, link_abstraction}
* protected_variations: {instability_protection, fixed_interface, stable_boundary, variation_encapsulation}

## PRINCIPLES
* dry: {repetition_reduction, single_source_of_truth, knowledge_centralization}
* kiss: {simplicity_priority, clarity_focus, avoid_overengineering}
* yagni: {speculative_coding_removal, immediate_need_focus, complexity_avoidance}
