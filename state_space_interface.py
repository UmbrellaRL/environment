from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class IState(ABC):
    pass

class IStateSpace[SI](ABC):
    @abstractmethod
    def get_state(self, index: SI) -> IState:
        pass
