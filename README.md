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

### Agree & rank the use cases for the application.

1. What states are connected to state x?
2. What actions can state x take?
3. What is the probability of getting to state x from state y?
4. What is the reward of state x?
5. What is the estimated value of state x?
6. Is state x a terminal state?
7. How far is state x from state y?

## Data Model

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

## Instance Model
4x4 Grid World example used from 'Introduction to Reinforcement Learning'.

Start state is coloured green & end state is coloured blue.
![Instance Model visual](https://raw.githubusercontent.com/UmbrellaRL/environment/refs/heads/dev/instance_model_visual.png)
