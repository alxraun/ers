# WIKIGEN

## SYSTEM_TOPOLOGY
* `wikigen` : `universal LLM-powered wiki builder`
* `architecture` : {`cli` | `web_ui`} -> `operations` -> {`llm_backends`, `wiki_engine`, `state_manager`, `extractor`} -> `artifact` [obsidian_compatible]

## LLM_BACKEND_LAYER
* `LLMBackend` : `ABC`
    * `complete`(`system`, `user`, `max_tokens`) -> `LLMResponse` {`text`, `input_tokens`, `output_tokens`, `cached`}
    * `estimate_cost_usd`(`input_tokens`, `output_tokens`) -> `float`
* `ClaudeAPIBackend` : `LLMBackend`
    * `complete()` -> {`_prompt_cache` [sha256] -> `LLMResponse`} | {`_wait_for_rate_limit()` -> `_get_client()` -> `anthropic.messages.create()` -> `_check_cost()` -> `LLMResponse`}
    * `_check_cost()` -> {`_warn_usd` -> warn | `_max_usd` -> `CostGuardError`}
* `ClaudeCodeBackend` : `LLMBackend`
    * `complete()` -> {`hashlib.sha256` -> `cache_key` @ `_prompt_cache` -> `LLMResponse`} | {`_find_claude_binary()` -> `subprocess.run` -> `LLMResponse`}
    * `estimate_cost_usd` -> `0.0`
* `OpenAICompatBackend` : `LLMBackend`
    * `complete()` -> {`hashlib.sha256` -> `cache_key` @ `_prompt_cache` -> `LLMResponse`} | {`_get_client()` -> `openai.chat.completions.create` -> `LLMResponse`}
    * `estimate_cost_usd` -> `0.0`
* `create_backend`(`WikiConfig`) -> `LLMBackend`
    * `cfg.llm.backend` -> {`claude-api` -> `ClaudeAPIBackend`, `openai-compat`|`openai`|`ollama`|`openrouter`|`groq` -> `OpenAICompatBackend`, `claude-code`|`claude-cli` -> `ClaudeCodeBackend`}

## OPERATIONS_LAYER
* `run_ingest` : `source_root` -> `artifact`
    * flow: `os.walk` -> `extractor.should_skip_file` -> `extract_text` -> `chunk_content` -> `LLMBackend.complete` -> `_parse_llm_json` -> `write_article` -> `compute_cross_references` -> {`write_folder_index`, `write_master_index`, `write_obsidian_graph`} -> `state.save()`
* `run_lint` : {`WikiConfig`, `WikiState`} -> `LintReport`
    * analysis: {`orphan_pages` [sources == []], `broken_links` [!@ all_slugs], `stale_articles` [{hash | mtime} -> mismatch], `missing_entity_pages` [mentions >= 3 && slug !@ all_slugs]}
    * action: {`_apply_fixes` | `print_report`}
* `run_query` : {`question`, `cfg`, `llm`} -> `answer`
    * flow: `index_path` -> `llm.complete` [identify_slugs] -> `_is_safe_slug` -> `rglob` [fetch_content] -> `llm.complete` [synthesize]
    * side_effect: `!dry_run` => `_save_query_result()`

## WIKI_ENGINE
* `article_generation` : `raw_content` -> `markdown`
    * `write_article` -> `render_article` -> {`_rule_based_summary` [regex: {`.sql`, `.lpd`, `.py`, `.ps1`}] | `LLMCacheEntry`}
    * `render_article` : {`frontmatter`, `breadcrumb`, `notes`, `entities`, `content`, `related`}
* `cross_reference_generation` : `LLMBackend` -> `WikiState`
    * `compute_cross_references` -> {`build_crossref_prompt` -> `LLMBackend.complete` -> `_parse_wikilinks`}
* `index_generation` : {`wiki_root`, `WikiConfig`} -> `wiki_structure`
    * `write_folder_index` -> `folder_index.md`
    * `write_master_index` -> `index.md`
    * `append_log` -> `log.md`
* `obsidian_integration` : {`folders`, `WikiConfig`} -> `graph.json`
    * `write_obsidian_graph` -> {`folder_colors` -> {`_rgb_to_int` | `_hex_to_int`} -> `colorGroups`}

## INFRASTRUCTURE_LAYER
* `extractor` : `file` -> `(label, text)`
    * methods: {`_extract_plain`, `_extract_docx`, `_extract_xlsx`, `_extract_pdf`, `_extract_pptx`, `_extract_eml`, `_extract_vsdx`}
    * utility: {`slugify`, `file_hash`, `content_hash`, `get_file_tag`}
* `WikiState` : {`_wiki_state.json`, `_wiki_llm_cache.json`}
    * `needs_extraction` : {`mtime`, `file_hash`, `wiki_file.exists()`, `incremental`} -> `bool`
    * `needs_summarization` : {`llm_cache_key`, `llm_model`, `_llm_cache`} -> `bool`
    * `update_summarization` -> `LLMCacheEntry` {`summary`, `entities`, `tags`, `topics`, `wikilinks`}
* `WikiConfig` : `yaml.safe_load` -> `composition`
    * components: {`ProjectConfig`, `SourceConfig`, `WikiConfig_Wiki`, `LLMConfig`, `SummarizationConfig`, `CrossRefConfig`, `TaggingConfig`, `ObsidianGroupsConfig`}
* `UI` : `FastAPI`
    * routes: {`GET /` -> dashboard, `POST /ingest` -> ingest, `POST /query` -> query, `GET /lint` -> lint}
* `CLI` : {`init`, `ingest`, `query`, `lint`, `status`, `serve`}
