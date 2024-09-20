from environment.environment_interface import IEnvironment
from environment.solutions.grid_world import GridWorld

class EnvironmentFactory:
    @staticmethod
    def create_enviornment(name: str) -> iEnvironment:
        match name:
            case "grid_world":
                return GridWorld