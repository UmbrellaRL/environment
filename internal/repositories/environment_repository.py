from typing import Any

from neo4j import Driver

class environment_repository:
    def __init__(self, neo4j_connection: Driver) -> None:
        self.connection: Driver = neo4j_connection

    def add_node(self, label: str, props: dict[str, Any] | None) -> None:
        """
        Adds a node with the specified label and properties to the database.

        This method merges a node with the given label (capitalized) and sets its properties,
        excluding any properties whose values are dictionaries.

        Args:
            label (str): The label for the node to be added.
            props (dict[str, Any] | None): A dictionary of properties to set on the node. 
                Properties with dictionary values are ignored.

        Returns:
            None
        """
        clean_props: dict[str, Any] = {k: v for k, v in (props or {}).items() if not isinstance(v, dict)}

        query: str = f"""
        MERGE(a:{label.capitalize()})
        SET a += $props
        RETURN a
        """
        with self.connection.session() as session:
            result = session.run(query, props=clean_props)
