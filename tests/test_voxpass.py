import pytest
from voxpass import voxpass


@pytest.mark.parametrize("num_vowels, pwd_length", [(0, 0), (1, 3), (3, 9), (50, 150)])
def test_length(num_vowels, pwd_length):
    assert len(voxpass.generate_password(num_vowels)) == pwd_length
