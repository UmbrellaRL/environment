import uuid

from pydantic import BaseModel, Field

# TODO Consider Enum for better validation.
type ActionType = str

class Action(BaseModel):
    id: str = Field(default_factory= lambda: str(uuid.uuid4()))
    value: float
    type: ActionType = Field(alias="type")
