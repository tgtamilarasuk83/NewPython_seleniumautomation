import pytest

@pytest.mark.order(2)
def test_login():
    print("Login")


@pytest.mark.order(1)
def test_search():
    print("Search")


@pytest.mark.order(3)
def test_logout():
    print("Logout")