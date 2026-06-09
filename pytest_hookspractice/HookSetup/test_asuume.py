import pytest

def test_soft_assertions():

    pytest.assume(5 == 10)

    pytest.assume(20 == 30)

    pytest.assume("Google" == "Google")

    pytest.assume(100 > 200)

    print("Execution continues after failed assumptions")