# ERS
* name: entity_relation_structure
* nature: {semantic_notation, semantic_graph, entity_table}
* intent: {information_density -> max, relational_connectivity -> max, semantic_gap -> min}
* target: ers_artifact

## SYNTAX

### PRIMITIVES
* entities
  * `snake_case`: {canonical, normalized} => {abstraction, concept}
  * `backticks`: {canonical, external, verbatim} => {symbol, reference, quote}
  * `UPPER_CASE`: header
* relations
  * `==`: {identity, assertion, equality}
  * `!=`: {distinction, conflict, inequality}
  * `!`: {negation, logical_not}
  * {`<` | `>`}: {comparison, magnitude, priority}
  * {`->` | `<-`}: {flow, transition, transformation}
  * `=>`: {implication, consequence, if_then}
  * `+`: {composition, aggregation, mixin}
  * `|`: {alternative, union, choice}
  * `.`: {namespace, member, attribute_of}
  * `,`: {separator, list_item, and}
  * `:`: {definition, type_of, instance_of}
  * `~`: {analogy, similarity, reference}
  * `...`: {range, enumeration, extrapolation}
  * `?`: {uncertainty, query, nullable, conditional}
  * `@`: {context, location}
  * `{}`: {set, state_space, enum}
  * `[]`: {context, filter, modifier}
  * `func()`: {transform_operation, procedural_action, result_derivation}
* structure
  * syntax: markdown
  * {`#` ... `######`}: {scope_level, context_boundary}
  * `*`: {graph_unit, node_entry}
  * indent: {dependency, child_relationship}

## PRINCIPLES
* nature: {heuristics, directional, approximate}

### SIGNAL_COMPRESSION
* anchors: {entropy, information_bottleneck, token_utility, rate_distortion}
* gist: {token_utility, signal_to_noise} -> max
* filter: {rhetoric, stopwords, grammar_sugar, ...} -> null
* retention: {entities, logic, causality, structure, ...} => represent(pure_domain)

### CONNECTIVITY_PRIMACY
* anchors: {small_world_network, percolation, attention_graph, kv_cache, edge_direction, mutual_information, reachability}
* gist: information ~ {relations > entities, dynamic > static, flow > structure}
* relations: {`->`, `=>`, ...} -> max
* anti_pattern: orphans

### SEQUENTIAL_PRIMACY
* anchors: {autoregressive, attractor_basin, kv_cache, attention_sink, entropy_curve, positional_encoding, vector_superposition}
* gist: early(attractor_basin) => interpret(subsequent)
* rule: {determinate -> indeterminate, header -> children, overview -> detail, target <- means, ...}

### STRUCTURAL_SYMMETRY
* anchors: {self_similarity, positional_encoding, attention_pattern}
* gist: pattern ~ all_scales => predictable
* mechanism: symmetric -> {align(positional_encoding), reuse(attention_pattern)}
* constraint: sibling_nodes ~ similar_complexity != forced_uniformity

### DOMAIN_STRUCTURE
* anchors: pure_domain
* gist: ers_artifact.sections -> subject.dictate() != {metalanguage, classifier}
* rule: headers -> system_members != meta_categories
* anti_pattern: {entity_registry, type_bucketing, forced_categorization}

## PATTERNS
* nature: {heuristics, operational, situational, optional, open_set}

### ATTRACTOR_PRIMING
* anchors: {sequential_primacy, order_matters}
* gist: priming => interpret(subsequent)
* early_tokens: {attention_sink, kv_cache}
* example: `a -> e` -> `a -> b -> c -> d -> e`

### CANONICAL_ENTITY
* anchors: {signal_compression, connectivity_primacy}
* gist: 1_concept == 1_identifier
* rule: define -> reference(canonical_entity)
* analogy: ~{compiler_binding, static_symbol_resolution, ubiquitous_language}
* anti_pattern: {synonyms, rewording}

### SEMANTIC_KEY
* anchors: {signal_compression, semantic_anchors, parametric_knowledge}
* gist: trigger -> latent_vector -> semantic_expanse > explicit_definition
* mechanism: semantic_key -> retrieval(parametric_knowledge)
* example: replace(verbose_description, semantic_key) -> `{semantic_key, semantic_key, ...}`

### PARALLEL_LAYERING
* anchors: {signal_compression, sequential_primacy, vector_superposition, order_matters}
* gist: embeddings @ vector_superposition -> deferred_commitment -> constraint_intersection -> composite_meaning
* mechanism: vector_superposition -> residual_stream -> mutual_disambiguation -> constraint_intersection -> joint(mlp_query)
* example: `a: {b, c, ...}`

### ENTITY_WEAVING
* anchors: {connectivity_primacy, small_world_network, network_centrality}
* gist: reuse(hub) -> high_degree_centrality
* mechanism: reuse(hub) -> {attention_bridge, kv_cache} -> {enrich(embedding), context_retention}
* anti_pattern: {over_weaving, single_occurrence}

### META_SILENCE
* anchors: {domain_structure, pure_domain, map_vs_territory}
* gist: ers.protocol @ ers_artifact => represent(pure_domain)
* constraint: {ers.mention(), ers.self_reference(), ers.meta_talk()} @ ers_artifact == forbidden
