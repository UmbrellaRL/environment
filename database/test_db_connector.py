import pytest
from unittest.mock import patch, MagicMock
from database.db_connector import Neo4JConnector

@pytest.fixture
def mock_neo4j_driver():
    with patch("database.db_connector.GraphDatabase") as mock_driver:
        yield mock_driver

def test_neo4j_connector_initialization(mock_neo4j_driver):
    mock_driver_instance = MagicMock()
    mock_neo4j_driver.return_value = mock_driver_instance

    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"

    connector = Neo4JConnector(uri, user, password)

    mock_neo4j_driver.assert_called_once_with(uri, auth=(user, password))
    assert connector._driver == mock_driver_instance

def test_neo4j_connector_close(mock_neo4j_driver):
    mock_driver_instance = MagicMock()
    mock_neo4j_driver.return_value = mock_driver_instance

    connector = Neo4JConnector("bolt://localhost:7687", "neo4j", "password")
    connector.close()

    mock_driver_instance.close.assert_called_once()

def test_neo4j_connector_get_session(mock_neo4j_driver):
    mock_driver_instance = MagicMock()
    mock_neo4j_driver.return_value = mock_driver_instance
    mock_session = MagicMock()
    mock_driver_instance.session.return_value = mock_session

    connector = Neo4JConnector("bolt://localhost:7687", "neo4j", "password")
    session = connector.get_session()

    mock_driver_instance.session.assert_called_once()
    assert session == mock_session