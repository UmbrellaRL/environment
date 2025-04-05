# Design

## Domain understanding

### Describe the application in detail.

- Environment for a reinforcement learning agent.
- Environment persisted with Neo4j.
- States are represented with nodes.
- Node properties describe a state's value & reward.
- Relationships describe actions from a state.
- Relationship directions describe next states.
- Relationship properties describe probabilities of reaching the next state.

### Identify the users of the application (people, systems).

Agent looking for possible actions in a state.
When determining state value function.

### Agree upon the use cases for the application.

 - Persist environment state.
 - Return state properties.

### Rank the importance of the use cases.

 1. Return state properties.
 2. Persist environment state.

## Data Model
--- describe labels, relationships & properties.

State (Node)
Label: _state_index_
Properties:
    - estimated_return: float
    - reward: float
    - is_terminal: bool

Action (Relationship)
Label: _action_name_
Properties:
    - probability: float    (probability that the next state is successfully reached)

![Data Model visual](https://raw.githubusercontent.com/UmbrellaRL/environment/refs/heads/dev/data_model_visual.png)

