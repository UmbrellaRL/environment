# TODO Docstring
"""_summary_
"""

from state_space_interface import IStateSpace, IState, IStateProbDist
from environment_interface import IAction

class StateSpace[SI](IStateSpace[SI]):
    # TODO Docstring
    """_summary_
    """
    def __init__(self, state_space: dict[SI, IState]) -> None:
        self._state_space: dict[SI, IState] = state_space

    def get_state(self, index: SI) -> IState: return self._state_space[index]
    
    def number_of_states(self) -> int: return len(self._state_space)

class State(IState):
    # TODO Docstring
    """_summary_

    Args:
        IState (_type_): _description_
    """
    def __init__(
        self,
        actions: list[IAction],
        value: float,
        reward: float,
        is_terminal: bool
    ) -> None:
        self._actions: list[IAction] = actions
        self._value: float = value
        self._reward: float = reward
        self._is_terminal: bool = is_terminal
    
    def get_actions(self) -> list[IAction]: return self._actions
    def get_value(self) -> float: return self._value
    def get_reward(self) -> float: return self._reward
    def is_terminal(self) -> bool: return self._is_terminal

class StateProbDist[SI](IStateProbDist):
    """Probability that a State is achieved following an Action within the 
    Environment.

    State Probability Distribution is a probability distribution of 
    successfully achieving a State following an Action from a State within the 
    Environment.
    """
    
    # raise DeprecationWarning

    def set_probability_distribution_for_state(
        self,
        state_index: SI,
        probability: float
    ) -> None:
        """Set the probability that a State occurs.

        This probability value is for a State occuring following an Action 
        from another State within the Environment.

        Args:
            state_index (StateIndex): State Index for the State occurring.
            probability (float): Probability that a State occurs.
        """
        if not state_index in self:
            raise KeyError(f"State Index {state_index} not within {self.__class__.__name__} for Action.")

        self[state_index] = probability

    def get_state_probability(
        self,
        state_index: SI
    ) -> float:
        """Return the probability of reaching the given State."""
        return self[state_index]
