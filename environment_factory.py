from environment_interface import IEnvironment
from solutions.grid_world import GridWorld

class EnvironmentFactory:
    @staticmethod
    def create_enviornment(state_config) -> IEnvironment:
        # TODO Docstring
        """_summary_

        Args:
            name (str): _description_

        Returns:
            IEnvironment: _description_
        """