from abc import ABC, abstractmethod
from environment_interface import IAction

class IState(ABC):
    @abstractmethod
    def get_actions(self) -> list[IAction]:
        pass
    @abstractmethod
    def get_value(self) -> float:
        pass
    @abstractmethod
    def get_reward(self) -> float:
        pass
    @abstractmethod
    def is_terminal(self) -> bool:
        pass

class IStateSpace[SI](ABC):
    @abstractmethod
    def get_state(self, index: SI) -> IState:
        pass

class IStateProbDist(ABC):
    pass