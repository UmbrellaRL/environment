# TODO Docstring
"""_summary_
"""
from dataclasses import dataclass

from state_space_interface import IStateSpace, IState
from environment_interface import IAction

class StateSpace[SI](IStateSpace[SI]):
    # TODO Docstring
    """_summary_
    """
    def __init__(self, state_space: dict[SI, IState]) -> None:
        self._state_space: dict[SI, IState] = state_space

    def get_state(self, index: SI) -> IState: return self._state_space[index]
    
    def number_of_states(self) -> int: return len(self._state_space)

@dataclass
class State(IState):
    # TODO Docstring
    """_summary_

    Args:
        IState (_type_): _description_
    """
    actions: list[IAction]
    value: float
    reward: float
    is_terminal: bool
