from pydantic import BaseModel, Field

from internal.domain.models.state import State
from internal.domain.models.action import Action
from internal.domain.models.transition import Transition

import uuid

class Environment(BaseModel):
    id_: str = Field(alias="id", default_factory=lambda: str(uuid.uuid4()))
    name: str
    states: list[State]
    actions: list[Action]
    transition: list[Transition]
