"""
Environment type for a reinforcement learning problem.

Environment type is a mapping from a State Index to the State's possible Actions.
"""
from enum import Enum
from dataclasses import dataclass

from environment_interface import IAction, IStateTransitionGraph
from state_space_interface import IStateSpace, IState

# TODO Might not need this here.
class Actions(Enum):
    pass

@dataclass
class Action(IAction):
    # TODO Doc string.
    """Action available within the Environment.
    """
    name: Actions
    value: float

class Environment[SI]:
    def __init__(self, state_space: IStateSpace[SI], state_transition_graph: IStateTransitionGraph) -> None:
        self._state_space: IStateSpace[SI] = state_space
        self._graph: IStateTransitionGraph = state_transition_graph

    def step(self, action: IAction) -> IState:
        """Perform Action in Environment.

        Args:
            self (_type_): _description_
        """
        pass

    def render(self) -> None:
        """Plot the current state of the Environment.
        """
        pass

    def get_state_space(self) -> IStateSpace[SI]: return self._state_space

class StateTransititionGraph[SI](IStateTransitionGraph):
    """State Transition Graph.
    
    Possible to go from State A to State B within the Environment with specific
    Actions.
    This graph class describes those transitions.
    """
    def __init__(self, state_transition_graph: dict[SI, dict[IAction, dict[SI, float]]]) -> None:
        self._graph = state_transition_graph
    
    def get_next_states(
        self,
        index: SI,
        action: IAction
    ) -> dict[SI, float]:
        """Return which States may occur following Action
        with their probabilities of occuring.

        Method used by agents with knowledge of their environment.
        This value is determined by the environment.

        Args:
            self (_type_): _description_
        """
        return self._graph[index][action]

    def get_state_transition_probability(
        self,
        state_index: SI,
        action: IAction,
        next_state_index: SI
    ) -> float:
        """Return the probability of successfully transitioning from one State 
        to another State after following an Action within the Environment.

        Args:
            current_state_index (SI): State Index of the current State the 
            Agent is making an Action within.
            action (A): Action being made by the Agent.
            next_state_index (SI): State Index of the next State the Agent will 
            be in after following Action.

        Returns:
            float: Percentage probability of the next State occuring.
        """
        return self._graph[state_index][action][next_state_index] 
