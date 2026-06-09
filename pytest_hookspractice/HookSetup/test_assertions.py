import pytest_check as check

def test_multiple_assertions():
    check.equal(5, 5)

    check.equal(10, 20)

    check.is_true(5 > 1)

    check.is_false(10 > 5)

    print("Test execution continues even after failures")