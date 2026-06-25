# ERSC
* name: ers_code
* extends: ers
* goal: cognitive_replacement == reading_code -> traversing_graph

## DEFINITIONS
* abstraction_level

### SIGNAL
* focus: {observable, intent, contracts, ...}
  * filter: include
  * covers:
    * {api_signatures, type_definitions, interfaces, inheritance, generics, ...}
    * {lifecycle_flows, state_transitions, event_reactions, call_chains, ...}
    * {pre_conditions, post_conditions, invariants, side_effects, data_guarantees, ...}

### NOISE
* focus: {execution, implementation, ...}
  * filter: exclude
  * covers:
    * {algorithms, loops, math_operations, step_by_step_instructions, ...}
    * {temp_vars, internal_counters, hidden_buffers, loop_indices, ...}
    * {boilerplate, syntax_sugar, language_overhead, debug_traces, ...}

## PRINCIPLES
* inherits: ers.principles
* nature: {heuristics, operational, situational}

### SIGNAL_EXTRACTION
* anchors: signal_to_noise
* gist: {ersc, code} -> {signal, intent} != {noise, implementation}

### SOURCE_ANCHORING
* anchors: symbolic_fidelity
* gist: entity == {code_symbol @ codebase} => {`backticks`, verbatim, exact}
* benefit: {zero_hallucination, traceability}
* anti_pattern: paraphrase

### SYMBOLIC_COMPRESSION
* anchors: abstraction_scale
* gist: snake_case == group_compression
* constraint: snake_case -> decompose(`backticks`) @ zoom_in

### FLOW_PRIMACY
* gist: behavioral_flow > static_structure @ information_utility
* logic: {flow -> reconstruct(structure) => low_entropy} != {structure -> reconstruct(flow) => high_entropy}
* compression: flow => {critical_path + system_intent == 100%}
