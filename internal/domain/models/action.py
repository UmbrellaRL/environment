from pydantic import BaseModel, Field
from internal.domain.models.state import State

class Action(BaseModel):
    value: float
    from_: State = Field(alias="from")
    to: State
