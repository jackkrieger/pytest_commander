import pytest
import time


@pytest.fixture
def myfix():
    print("setup myfix")
    yield
    print("teardown myfix")


def test_one():
    assert True


def test_two(myfix):
    assert not myfix
    assert False


class TestSuite:
    def test_alpha(self):
        time.sleep(10)
        assert 1 != 0

    def test_beta(self):
        time.sleep(10)
        assert 1 is None
