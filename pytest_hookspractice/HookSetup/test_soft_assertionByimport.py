class SoftAssert:
    def __init__(self):
        self.errors = []

    def assert_equal(self, actual, expected, msg=""):
        if actual != expected:
            self.errors.append(
                f"Expected {expected}, Actual {actual}. {msg}"
            )

    def assert_all(self):
        if self.errors:
            raise AssertionError("\n".join(self.errors))


def test_example():
    soft = SoftAssert()

    soft.assert_equal(5, 10, "First Check")
    soft.assert_equal(20, 30, "Second Check")
    soft.assert_equal("A", "B", "Third Check")

    print("Execution continues")

    soft.assert_all()