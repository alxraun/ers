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
  * {`#` ... `######`} : {scope_level, context_boundary}
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
