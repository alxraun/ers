# ERSAR
* name: ers_api_reference
* nature: semantic_graph
* analogue: {`.pyi`, `.d.ts`, ref_assembly}
* extends: `ERS` [protocol]
* role: structural_scaffolding
* usage: {syntax_anchor, hallucination_suppression, vocabulary_bounding}
* goal -> entropy_collapse [probabilistic_guessing -> deterministic_matching]

## THEORY

### ENTROPY_COLLAPSE
* focus: search_space_reduction
* state_a: natural_language -> search_space [infinite] -> ambiguity [max]
* state_b: ersar_in_context -> search_space [formal_constraints] -> ambiguity [zero]
* logic: llm_latent_knowledge == broad_but_blurry
* function: ersar == high_precision_lens
* goal: probabilistic_guessing -> deterministic_matching

### SEMANTIC_RESONANCE
* focus: self_documenting_mechanics
* axiom: symbol_nomenclature == self_documenting_contract
* logic: name_semantics -> triggers -> latent_concept_space
* principle: symbol_activation == conceptual_retrieval
* constraint: prose_explanation == redundant_noise
* benefit: information_density -> max

## DEFINITIONS

### SIGNAL
* focus: the_interface_surface
* visibility: include
* taxonomy: {type_names, method_signatures, arguments, return_types, cli_flags, config_keys, inheritance_hierarchies}

### NOISE
* focus: everything_behind_the_surface
* visibility: exclude
* taxonomy: {implementation_bodies, narrative_docstrings, internal_state, algorithms, usage_examples, prose}

## GENERATION_PATHS

### PATH_A: DETERMINISTIC_EXTRACTION
* status: preferred_if_tooling_exists
* methods: {AST_parsing, {`.pyi`|`.d.ts`|ref_assembly}_generators, compiler_reflection}
* targets: ecosystems_with_standardized_tooling {C#, TypeScript, Rust}
* property: absolute_coverage_guarantee

### PATH_B: LLM_MEDIATED_DISTILLATION
* status: valid_for_unstructured_domains
* methods: {llm_prompt_extraction, semantic_parsing_of_raw_docs}
* targets: ecosystems_lacking_tooling {obscure_configs, prosaic_docs, scattered_markdown, CLI_manpages}
* property: flexibility_over_rigid_syntax

## HEURISTICS

### SYMBOLIC_FIDELITY
* focus: strict_source_isomorphism
* rule: node_id == verbatim_code_symbol [exact_match]
* format: all_code_entities => backticks
* invariant: zero_hallucination_naming

### FORMAT_AGNOSTICISM
* focus: universal_structural_mapping
* rule: ersar_topology applies_to {OOP_classes, REST_endpoints, CLI_commands, YAML_configs, API_routes}
* invariant: target_domain_syntax != barrier_to_graphing

### STRUCTURAL_GLUE
* focus: context_binding
* rule: include_primitives [types, enums, literals] -> essential_for_value_substitution
* rule: use_markdown_headers -> logical_grouping [categories, namespaces]
