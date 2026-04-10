# NANOCHAT

## data_subsystem

* **fineweb_edu_100b**
  * format == PARQUET
  * shards == 1822
* **tokenizer**
  * implementation: rust_bpe_tiktoken
  * pattern: gpt_4_modified
  * special_tokens == {BOS, USER, ASSISTANT, PYTHON, OUTPUT}
  * split_pattern == `\p{N}{1,2}`
* fineweb_edu_100b -> gpu_batch [nature: pipeline]
  * **data_loader**
    * streaming == TRUE
    * buffer == DEQUE
    * distributed == ddp_sharded
  * **chat_renderer**
    * template == assistant_supervised_only
    * mask_loss == user_tokens_ignored

## model_architecture

* **gpt_core**
  * activation == RELU_SQUARED
  * normalization == rmsnorm_no_param
  * embeddings == rotary_rope
  * logit_softcap == 15.0
  * bias == NONE

### attention_mechanism

* **gqa**
  * type == grouped_query_attention
  * feature: qk_norm
* query_key -> attention_score [nature: rotary_rotation]
  * theta == 10000
  * dtype == BF16

### block_structure

* residual_in -> residual_out [nature: transformer_layer]
  * rmsnorm -> gqa -> add
  * rmsnorm -> mlp_relu2 -> add

## optimization_engine

### hybrid_optimizer

* **muon**
  * target == 2d_matrices
  * method: newton_schulz_5
  * grad -> update [nature: orthogonalization]
    * steps == 5
    * distributed == reduce_scatter_all_gather
* **dist_adamw**
  * target == {embedding, lm_head, 1d_params}
  * sharding == ZERO_2
  * lr_scale == 1/sqrt(d_model)

## inference_runtime

* **engine**
  * component: kv_cache
  * component: tool_repl

### kv_cache_logic

* growth_strategy == 1024_chunk_append
* prefill_b1 -> decode_bn [nature: cache_cloning]

### tool_loop

* assistant_tokens -> python_sandbox [nature: trigger]
  * token_pattern == `[python_start]...[python_end]`
* **execution_sandbox**
  * security == process_isolation
  * limits == {timeout: 5s, ram: 256MB}
  * forbidden == {os, subprocess, shutil, socket}
* sandbox_output -> kv_cache [nature: force_injection]
  * wrapper == `[output_start]...[output_end]`

## evaluation_metrics

* **core_metric**
  * tasks == {MC, SCHEMA, LM}
  * reference: dclm_paper
* **bpb**
  * name == bits_per_byte
  * normalization == token_byte_weighting
  * ignore == special_tokens

## distributed_orchestration

* parallelism == DDP
* precision == TF32_MATMUL + BF16_STORAGE
* rank_n -> rank_0 [nature: report_aggregation]
  * metrics == {bloat, cost, bpb, core}
