from main import add
import pytest

def test_empty_string():
    assert add("") == 0
