# ERS_RAG

## ARCHITECTURE_TOPOLOGY
* ers_db: ers_artifacts @ lexical_isomorphism
* vector_db: canonical_entity_embeddings
* llm_extractor: {query_parsing, entity_guessing}
* llm_generator: {reasoning, answer_synthesis}
* search_engine: exact_string_match

## PIPELINE_DYNAMICS

### 1. INDEXING_PHASE
* extract_entities(ers_db) => canonical_entities
* embed(canonical_entities) => vector_db
* state: vector_db == isolated_entity_vectors != {document_vectors, relational_vectors}

### 2. QUERY_ROUTING_PHASE
* extract_entities(user_query) @ llm_extractor => guessed_entities
* logic: natural_language -> potential_semantic_anchors

### 3. ENTITY_RESOLUTION_PHASE
* embed(guessed_entities) -> guessed_vectors
* cosine_similarity(guessed_vectors, vector_db) => similarity_scores
* filter_top_k(similarity_scores, threshold) => resolved_entities
* logic: vector_db == semantic_spellchecker => mapping(guessed_entities -> canonical_entities)

### 4. GRAPH_TRAVERSAL_PHASE
* exact_match(resolved_entities, ers_db) @ search_engine => matched_ers_lines
* logic: ers_line == causal_chain => line_extraction

### 5. CONTEXT_ASSEMBLY_PHASE
* merge(matched_ers_lines) => jit_ers_artifact == {query_specific, semantic_topology}

### 6. GENERATION_PHASE
* generate_answer(jit_ers_artifact, user_query) => final_response
