import uuid
import pytest
from internal.domain.models.state import State

def test_state_default_values():
    state = State(reward=10.0)
    uuid_obj = uuid.UUID(state.id)
    assert isinstance(state.id, str)
    assert isinstance(uuid_obj, uuid.UUID)
    assert state.reward == 10.0
    assert state.is_terminal is False

def test_state_custom_values():
    custom_id = "123e4567-e89b-12d3-a456-426614174000"
    state = State(id=custom_id, reward=5.5, is_terminal=True)
    assert state.id == custom_id
    assert state.reward == 5.5
    assert state.is_terminal is True

def test_state_invalid_uuid_raises_error():
    with pytest.raises(ValueError):
        uuid.UUID("not-a-uuid")

def test_state_negative_reward():
    state = State(reward=-1.0)
    assert state.reward == -1.0
    assert isinstance(state.id, str)
    assert state.is_terminal is False

def test_state_multiple_instances_unique_ids():
    state1 = State(reward=1.0)
    state2 = State(reward=2.0)
    assert state1.id != state2.id
    assert isinstance(uuid.UUID(state1.id), uuid.UUID)
    assert isinstance(uuid.UUID(state2.id), uuid.UUID)

def test_state_repr_and_str():
    state = State(reward=3.0)
    assert "State" in repr(state)
    assert "reward=3.0" in str(state)
