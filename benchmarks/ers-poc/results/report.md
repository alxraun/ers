# ERS-PoC Benchmark Report

> **Glossary:**
> * **Compression Ratio (CR):** `(1.0 - (tokens_ers / tokens_source)) * 100.0`
> * **Performance Retention (PR):** `(score_ers / score_source) * 100.0`
> * **Score:** Average accuracy (0.0 to 1.0) awarded by the Judge based on answer correctness with Ground Truth.
> * **Δ (Delta):** `score_ers - score_source`
> * **Simple QA:** Direct fact retrieval.
> * **Complex QA:** Multi-hop reasoning.

---

## Global Leaderboard
| Model | Judge | CR (%) | PR (%) | Score Δ |
| :--- | :--- | :---: | :---: | :---: |
| `openrouter/openai/gpt-oss-20b` | `openai/gpt-5.4` | 72.4 | 93.8 | -0.06 |
| `openrouter/qwen/qwen3-14b` | `openai/gpt-5.4` | 72.4 | 92.1 | -0.07 |
| `openrouter/google/gemma-3-4b-it` | `openai/gpt-5.4` | 72.4 | 89.0 | -0.09 |

---

## Detailed Analysis
### Candidate: `openrouter/google/gemma-3-4b-it`
**Judge:** `openai/gpt-5.4` | **Samples Evaluated:** 240

#### System Metrics
| Metric | Value |
| :--- | :--- |
| **Compression Ratio (CR)** | 72.4% |
| **Performance Retention (PR)** | 89.0% |
| **Score Δ** | -0.09 |
| **Avg Context Size** | 8120 → 2239 tokens (27.6% of original) |

#### Answer Correctness
| Dimension / Slice | Source Score | ERS Score | Δ |
| :--- | :---: | :---: | :---: |
| overall: simple | 0.83 | 0.73 | -0.11 |
| overall: complex | 0.76 | 0.69 | -0.07 |
| overall: avg | 0.80 | 0.71 | -0.09 |
| code: simple | 0.81 | 0.64 | -0.17 |
| code: complex | 0.73 | 0.64 | -0.08 |
| code: avg | 0.77 | 0.64 | -0.13 |
| formal: simple | 0.75 | 0.77 | +0.02 |
| formal: complex | 0.68 | 0.63 | -0.05 |
| formal: avg | 0.71 | 0.70 | -0.01 |
| humanities: simple | 0.91 | 0.78 | -0.13 |
| humanities: complex | 0.82 | 0.74 | -0.08 |
| humanities: avg | 0.86 | 0.76 | -0.11 |
| science: simple | 0.87 | 0.73 | -0.14 |
| science: complex | 0.82 | 0.75 | -0.07 |
| science: avg | 0.84 | 0.74 | -0.10 |

---

### Candidate: `openrouter/openai/gpt-oss-20b`
**Judge:** `openai/gpt-5.4` | **Samples Evaluated:** 240

#### System Metrics
| Metric | Value |
| :--- | :--- |
| **Compression Ratio (CR)** | 72.4% |
| **Performance Retention (PR)** | 93.8% |
| **Score Δ** | -0.06 |
| **Avg Context Size** | 8120 → 2239 tokens (27.6% of original) |

#### Answer Correctness
| Dimension / Slice | Source Score | ERS Score | Δ |
| :--- | :---: | :---: | :---: |
| overall: simple | 0.96 | 0.89 | -0.06 |
| overall: complex | 0.95 | 0.90 | -0.05 |
| overall: avg | 0.95 | 0.90 | -0.06 |
| code: simple | 0.99 | 0.88 | -0.11 |
| code: complex | 0.99 | 0.90 | -0.09 |
| code: avg | 0.99 | 0.89 | -0.10 |
| formal: simple | 0.95 | 0.85 | -0.10 |
| formal: complex | 0.96 | 0.89 | -0.07 |
| formal: avg | 0.95 | 0.87 | -0.08 |
| humanities: simple | 0.97 | 0.91 | -0.06 |
| humanities: complex | 0.96 | 0.90 | -0.05 |
| humanities: avg | 0.96 | 0.91 | -0.05 |
| science: simple | 0.91 | 0.92 | +0.01 |
| science: complex | 0.90 | 0.90 | +0.00 |
| science: avg | 0.91 | 0.91 | +0.01 |

---

### Candidate: `openrouter/qwen/qwen3-14b`
**Judge:** `openai/gpt-5.4` | **Samples Evaluated:** 240

#### System Metrics
| Metric | Value |
| :--- | :--- |
| **Compression Ratio (CR)** | 72.4% |
| **Performance Retention (PR)** | 92.1% |
| **Score Δ** | -0.07 |
| **Avg Context Size** | 8120 → 2239 tokens (27.6% of original) |

#### Answer Correctness
| Dimension / Slice | Source Score | ERS Score | Δ |
| :--- | :---: | :---: | :---: |
| overall: simple | 0.95 | 0.87 | -0.08 |
| overall: complex | 0.94 | 0.87 | -0.07 |
| overall: avg | 0.95 | 0.87 | -0.07 |
| code: simple | 0.97 | 0.86 | -0.11 |
| code: complex | 0.91 | 0.80 | -0.11 |
| code: avg | 0.94 | 0.83 | -0.11 |
| formal: simple | 0.95 | 0.84 | -0.11 |
| formal: complex | 0.96 | 0.85 | -0.11 |
| formal: avg | 0.95 | 0.84 | -0.11 |
| humanities: simple | 0.97 | 0.94 | -0.03 |
| humanities: complex | 0.96 | 0.93 | -0.03 |
| humanities: avg | 0.96 | 0.93 | -0.03 |
| science: simple | 0.93 | 0.85 | -0.07 |
| science: complex | 0.94 | 0.91 | -0.03 |
| science: avg | 0.93 | 0.88 | -0.05 |

---
