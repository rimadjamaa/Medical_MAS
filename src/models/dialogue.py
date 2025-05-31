from pydantic import BaseModel
from typing import List

class DialogueOutput(BaseModel):
    intent: str
    symptoms: List[str]
