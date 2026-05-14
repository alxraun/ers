from typing import Literal, Optional
from pydantic import BaseModel

class QuestionRecord(BaseModel):
    domain: str
    sample_id: str
    source: str
    ers_artifact: str
    question_id: str
    question_type: str
    question: str
    answer: str

    @property
    def identity_tuple(self):
        return (self.domain, self.sample_id, self.question_id)

class GenerationItem(BaseModel):
    domain: str
    sample_id: str
    question_id: str
    context_type: Literal["source", "ers"]
    actual_output: str
    finish_reason: str
    latency_ms: float
    prompt_tokens: int
    completion_tokens: int
    cost: float
    model_id: Optional[str] = None

    @property
    def identity_tuple(self):
        return (self.domain, self.sample_id, self.question_id)

class EvaluationItem(BaseModel):
    domain: str
    sample_id: str
    question_id: str
    context_type: Literal["source", "ers"]
    score: float
    reason: str
    candidate_id: Optional[str] = None
    judge_id: Optional[str] = None

    @property
    def identity_tuple(self):
        return (self.domain, self.sample_id, self.question_id)
