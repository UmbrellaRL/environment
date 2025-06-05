from pydantic import BaseModel

class State(BaseModel):
    index: int
    estimated_return: float
    reward: float
    is_terminal: bool