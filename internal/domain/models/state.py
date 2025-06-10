from pydantic import BaseModel, Field

import uuid

class State(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    reward: float
    is_terminal: bool = False
