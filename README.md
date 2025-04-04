# Design

## Describe the application in detail.

Environment for a reinforcement learning agent.
Environment persisted with Neo4j.
States are represented with nodes.
Node properties describe a state's value & reward.
Relationships describe actions from a state.
Relationship directions describe next states.
Relationship properties describe probabilities of reaching the next state.

## Identify the users of the application (people, systems).

Agent looking for possible actions in a state.
When determining state value function.

## Agree upon the use cases for the application.

 - Persist environment state.
 - Return state properties.

## Rank the importance of the use cases.

 1. Return state properties.
 2. Persist environment state.
