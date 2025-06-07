from pydantic import BaseModel, Field

from internal.domain.models.state import State
from internal.domain.models.action import Action

import uuid

class Transition(BaseModel):
    id_: str = Field(default_factory=lambda: str(uuid.uuid4()))
    from_: State = Field(alias="from")
    to: State = Field()
    action: Action = Field()
    probability: float = Field(ge=0.0, le=1.0)
