import pytest

from bun import Bun


@pytest.fixture
def bun_instance():
    """фикстура создание экземпляра класса Bun"""
    return Bun(name=None, price=None)
