import pytest
from internal.domain.models.action import Action

def test_action_default_id():
    action = Action(value=10.5, type="test")
    assert isinstance(action.id, str)
    assert len(action.id) > 0

def test_action_value_and_type():
    action = Action(value=42, type="example")
    assert action.value == 42
    assert action.type == "example"