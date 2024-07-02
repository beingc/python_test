import pytest


# 定义一个简单的fixture，返回一个值
@pytest.fixture
def setup():
    print("\nSetup for test")
    yield 10  # yield之后的代码作为清理操作
    print("\nTeardown after test")


# 使用fixture
def test_fixture_example(setup):
    assert setup == 10
