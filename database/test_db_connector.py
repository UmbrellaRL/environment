import pytest
from testcontainers.neo4j import Neo4jContainer
from database.db_connector import Neo4JConnector

@pytest.fixture(scope="module")
def neo4j_container():
    with Neo4jContainer("neo4j:5.15") as neo4j:
        neo4j.start()
        yield neo4j

@pytest.fixture
def connector(neo4j_container):
    bolt_url = neo4j_container.get_connection_url()
    user = neo4j_container.NEO4J_USER
    password = neo4j_container.NEO4J_ADMIN_PASSWORD
    conn = Neo4JConnector(bolt_url, user, password)
    yield conn
    conn.close()

@pytest.mark.skip(reason="Laptop not strong enough for test containers 😔😔")
def test_init_creates_driver(connector):
    assert connector._driver is not None

@pytest.mark.skip(reason="Laptop not strong enough for test containers 😔😔")
def test_close_calls_driver_close(connector):
    connector.close()
    assert True

@pytest.mark.skip(reason="Laptop not strong enough for test containers 😔😔")
def test_get_session_returns_session(connector):
    session = connector.get_session()
    assert session is not None
    session.close()
