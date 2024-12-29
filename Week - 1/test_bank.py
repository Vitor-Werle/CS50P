import pytest
from bank import value

def main():
    pytest.main(["-v"])


def test_value():
    assert value("hello guys") == "$0"
    assert value("Hey there") == "$20"
    assert value("How are you?") == "$100"

if __name__ == "__main__":
    main()