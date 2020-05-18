from pytest import mark
from pytest import fixture

@fixture(scope="module")
def connect_db():
    print("I need to connect to employee database")
    yield
    print("I need to disconnect to employee database")

@mark.fixture_example
def test_first(connect_db):
    print("I am first test to verify employee name against id ")


@mark.fixture_example
def test_second(connect_db):
    print("I am second test to verify employee id against department ")


@mark.fixture_example
def test_third(connect_db):
    print("I am third test to verify employee id against supervisor ")

@mark.fixture_example
def test_fourth():
    print("I dont need db connection")