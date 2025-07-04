from main import add
import pytest

def test_empty_string():
    assert add("") == 0

def test_single_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,2") == 3

def test_multiple_numbers():
    assert add("1,2,3,4") == 10

def test_newline_separator():
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3

def test_negative_numbers():
    with pytest.raises(Exception, match="negative numbers not allowed: -2, -3"):
        add("1,-2,-3")