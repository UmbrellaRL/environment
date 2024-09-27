"""Grid World Configuration."""

from enum import Enum

from environment_interface import IActions

class GridWorldActions(IActions, Enum):
    """Grid World Actions."""
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"
