import pytest
from twttr import remove_vowels

import pytest

def main():
    pytest.main(["-v"])  # Explique essa parte 

def test_shorten():
    assert remove_vowels("comida") == "cmd"
    assert remove_vowels("Twitter") == "Twttr"

if __name__ == "__main__":
    main()