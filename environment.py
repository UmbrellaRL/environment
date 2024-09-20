"""
Environment type for a reinforcement learning problem.

Environment type is a mapping from a State Index to the State's possible Actions.
"""

from environment_interface import IActions, IAction, IStateTransGraph
from state_space_interface import IStateSpace, IState

# TODO Might not need this here.
class Actions(IActions):
    pass

class Action(IAction):
    # TODO Doc string.
    """Actions available within the Environment.

    Args:
        IAction (_type_): _description_
    """
    def __init__(self, name: str, value: float) -> None:
        self.name = name
        self.value = value

class Environment[SI]:
    def __init__(self, state_space: IStateSpace[SI], state_trans_graph: IStateTransGraph) -> None:
        self._state_space: IStateSpace[SI] = state_space
        self._state_transitions: IStateTransGraph = state_trans_graph

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

    def get_next_states(
        self,
        state_index: SI,
        action: A
    ) -> StateProbabilityDistribution[SI]:
        """Return which States may occur following Action
        with their probabilities of occuring.

        Method used by agents with knowledge of their environment.
        This value is determined by the environment.

        Args:
            self (_type_): _description_
        """
        return self.get_state_actions(current_state_index) \
            .get_state_probability_distribution(action)

    def get_state_transition_probability(
        self,
        current_state_index: SI,
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
        
        return self.get_state_actions(current_state_index) \
            .get_state_probability_distribution(action) \
                .get_state_probability(next_state_index)

    def get_state_space(self) -> IStateSpace[SI]: return self._state_space

class StateTransGraph(IStateTransGraph):
    """State Transition Graph.
    
    Possible to go from State A to State B within the Environment with specific
    Actions.
    This graph class describes those transitions.
    """
    def __init__(self, state_transition_graph: dict[IState, dict[IAction, IState]]) -> None:
        self._graph = state_transition_graph