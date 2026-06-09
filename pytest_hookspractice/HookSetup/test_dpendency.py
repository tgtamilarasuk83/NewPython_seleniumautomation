import pytest


@pytest.mark.dependency(name="login_test")
def test_login():
    print("Login test executed")
    assert True


@pytest.mark.dependency(depends=["login_test"])
def test_search_product():
    print("Search product test executed")
    assert True


@pytest.mark.dependency(depends=["login_test"])
def test_add_to_cart():
    print("Add to cart executed")
    assert True


@pytest.mark.dependency(depends=["login_test"])
def test_checkout():
    print("Checkout executed")
    assert True