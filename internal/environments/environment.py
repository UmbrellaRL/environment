from typing import Protocol

from internal.domain.models.state import State

class EnvironmentProtocol(Protocol):
    def reset(self) -> bool: ...

    # TODO For future iterations.
    # def step(self, action: Action) -> State: ...

    def state_space(self) -> list[State]: ...
