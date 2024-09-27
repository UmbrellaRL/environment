import unittest
from unittest.mock import MagicMock

# Assuming the original StateSpace and State classes are imported as follows:
# from state_space_module import StateSpace, State, IState, IAction

class TestStateSpace(unittest.TestCase):

    def setUp(self):
        """Set up common test fixtures"""
        # Mock the actions and states
        self.mock_action1 = MagicMock(spec=IAction)
        self.mock_action2 = MagicMock(spec=IAction)

        # Create state instances
        self.state1 = State(actions=[self.mock_action1], value=0.5, reward=1.0, is_terminal=False)
        self.state2 = State(actions=[self.mock_action2], value=0.75, reward=2.0, is_terminal=True)

        # Create the state space with state indexes as keys
        self.state_space_dict = {1: self.state1, 2: self.state2}
        self.state_space = StateSpace(self.state_space_dict)

    def test_get_state_valid_index(self):
        """Test that get_state method returns the correct state for a valid index."""
        state = self.state_space.get_state(1)
        self.assertEqual(state, self.state1)

    def test_get_state_invalid_index(self):
        """Test that get_state raises a KeyError for an invalid index."""
        with self.assertRaises(KeyError):
            self.state_space.get_state(99)

    def test_number_of_states(self):
        """Test that number_of_states returns the correct count."""
        self.assertEqual(self.state_space.number_of_states(), 2)

class TestState(unittest.TestCase):

    def setUp(self):
        """Set up common test fixtures"""
        # Mock actions
        self.mock_action1 = MagicMock(spec=IAction)
        self.mock_action2 = MagicMock(spec=IAction)

        # Create a test State instance
        self.state = State(actions=[self.mock_action1, self.mock_action2], value=0.5, reward=1.0, is_terminal=False)

    def test_state_attributes(self):
        """Test the State object attributes."""
        self.assertEqual(self.state.value, 0.5)
        self.assertEqual(self.state.reward, 1.0)
        self.assertEqual(self.state.is_terminal, False)
        self.assertEqual(len(self.state.actions), 2)
        self.assertIn(self.mock_action1, self.state.actions)
        self.assertIn(self.mock_action2, self.state.actions)

    def test_state_terminal(self):
        """Test terminal state behavior."""
        terminal_state = State(actions=[], value=0.0, reward=0.0, is_terminal=True)
        self.assertTrue(terminal_state.is_terminal)

if __name__ == '__main__':
    unittest.main()
