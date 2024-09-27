# TODO
# determine_next_state_probability_distribution method equivalent done in config tile -> injected into environment factory.

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path

from state_space_interface import IState

@dataclass
class IAction(ABC):
    pass

class IEnvironment[SI](ABC):

    @abstractmethod
    def step(self, action: IAction) -> IState:
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
    def get_transition_probability(self, state_index: SI, action: IAction, next_state_index: SI) -> float:
        pass

class EnvironmentConfig(ABC):
    @abstractmethod
    def from_json(self, path: Path) -> EnvironmentConfig:
        pass

    @abstractmethod
    def validate(self) -> None:
        pass

class IStateTransitionGraph(ABC):
    pass
