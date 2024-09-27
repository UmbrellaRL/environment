"""Grid World Configuration."""

from enum import Enum

from environment import Actions
from environment_interface import IActions

class GridWorldActions(Enum):
    """Grid World Actions."""
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"
