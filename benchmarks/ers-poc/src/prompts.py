CANDIDATE_SYSTEM_PROMPT = """
You are an analytical reasoning engine.
Your task is to extract the exact answer to the QUESTION based SOLELY on the provided CONTEXT.

INSTRUCTIONS:
1. Reconstruct the logical answer in clear, explicit, and complete natural language.
2. Ensure all logical relationships, rules, and technical terms mentioned in the CONTEXT are explicitly surfaced.
3. Do NOT use outside knowledge. The answer must be derived strictly from the CONTEXT.
"""

JUDGE_CRITERIA = """
Evaluate the ACTUAL_OUTPUT against the EXPECTED_OUTPUT to determine Answer Correctness.

SCORING RULES:
1. LOGICAL ALIGNMENT: Evaluate meaning, not exact wording. Recognize that high-level concepts in the EXPECTED_OUTPUT can be fully satisfied by specific implementations, instances, or technical details in the ACTUAL_OUTPUT. Do not penalize the ACTUAL_OUTPUT for being more specific or technical.
2. LOGICAL COVERAGE: Score proportionally based on how many core claims and logical steps from the EXPECTED_OUTPUT are satisfied by the ACTUAL_OUTPUT.
3. EXTRA DETAILS: Ignore any additional information in the ACTUAL_OUTPUT as long as it does not contradict the expected core claims.
4. STYLE & FORMAT: Completely ignore differences in verbosity, phrasing, grammar, or style.
"""
