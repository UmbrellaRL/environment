import pytest
from unittest.mock import MagicMock
from neo4j import Driver
from internal.repositories.environment_repository import environment_repository

@pytest.fixture
def mock_driver():
    return MagicMock(spec=Driver)

@pytest.fixture
def repo(mock_driver: MagicMock):
    return environment_repository(mock_driver)

def test_add_node_merges_node_and_sets_properties(repo: environment_repository, mock_driver: MagicMock):
    mock_session = MagicMock()
    mock_driver.session.return_value.__enter__.return_value = mock_session

    label = "testlabel"
    props = {"name": "env1", "value": 42, "ignore": {"nested": "dict"}}
    expected_props = {"name": "env1", "value": 42}

    repo.add_node(label, props)

    query = """
        MERGE(a:Testlabel)
        SET a += $props
        RETURN a
        """
    mock_session.run.assert_called_once_with(query, props=expected_props)

def test_add_node_with_none_props(repo: environment_repository, mock_driver: MagicMock):
    mock_session = MagicMock()
    mock_driver.session.return_value.__enter__.return_value = mock_session

    label = "empty"
    repo.add_node(label, None)

    query = """
        MERGE(a:Empty)
        SET a += $props
        RETURN a
        """
    mock_session.run.assert_called_once_with(query, props={})

def test_add_node_ignores_dict_values(repo: environment_repository, mock_driver: MagicMock):
    mock_session = MagicMock()
    mock_driver.session.return_value.__enter__.return_value = mock_session

    label = "dictlabel"
    props = {"a": 1, "b": {"should": "ignore"}, "c": 2}
    expected_props = {"a": 1, "c": 2}

    repo.add_node(label, props)

    query = """
        MERGE(a:Dictlabel)
        SET a += $props
        RETURN a
        """
    mock_session.run.assert_called_once_with(query, props=expected_props)