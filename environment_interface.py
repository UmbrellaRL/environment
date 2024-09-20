# TODO
# determine_next_state_probability_distribution method equivalent done in config tile -> injected into environment factory.

from abc import ABC, abstractmethod
from enum import Enum

from environment.state_space_interface import IState

class IActions(ABC, Enum):
    pass

class IAction(ABC):
    """Abstract Base Class for individual Action within the environment.

    Args:
        ABC (_type_): _description_
    """

class IEnvironment[SI](ABC):

    @abstractmethod
    def step(self, action: IAction) -> ():
        pass

    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def get_state(self, state_index: SI) -> IState:
        pass

    @abstractmethod
    def get_next_states(self, state_index: SI, action: IAction) -> list[SI]:
        pass

    @abstractmethod
    def get_transition_probability(self, state_index: SI, action: A, next_state_index: SI) -> float:
        pass

class IStateTransGraph(ABC):
    pass
