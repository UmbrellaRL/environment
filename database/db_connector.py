from neo4j import GraphDatabase

class Neo4JConnector:
    """
    Neo4JConnector is a utility class for managing connections to a Neo4j database.

    Attributes:
        _driver (neo4j.GraphDatabase.driver): The driver instance used to interact with the Neo4j database.

    Methods:
        __init__(uri: str, user: str, password: str):
            Initializes the Neo4JConnector with the specified connection URI, username, and password.

        close() -> None:
            Closes the connection to the Neo4j database.

        get_session():
            Returns a new session for interacting with the Neo4j database.
    """
    def __init__(self, uri: str, user: str, password: str):
        self._driver = GraphDatabase(uri, auth=(user, password))

    def close(self) -> None:
        self._driver.close()

    def get_session(self):
        return self._driver.session()
