import pytest

# @pytest.fixture(scope="function", autouse=True)
@pytest.fixture(scope="session", autouse=True)
def tc_setup():
    print("launch Bowser")
    print("Login")
    print("Browser Products")
    yield
    print("Logoff")
    print("Close Browser")
