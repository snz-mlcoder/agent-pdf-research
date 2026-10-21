

from pydantic import BaseModel
from typing import Optional, Literal,List

class Citation(BaseModel):

    text: str
    page_number: int
    source: str

class Answer(BaseModel):
    """
    A class representing an answer with associated citations and confidence level.
    """

    answer: str
    citations: List[Citation]
    confidence: Literal["high", "medium", "low"] = "medium"