from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = "abcdef"
    key = 3
    expected = "cba_fed"
    assert encrypt_message(message, key) == expected

    message = "abcdef"
    key = 4
    expected = "fe_dcba"
    assert encrypt_message(message, key) == expected

    message = "abcdef"
    key = 9
    expected = "fedcba"
    assert encrypt_message(message, key) == expected

    message = "fedcba"
    key = -1
    expected = "abcdef"
    assert encrypt_message(message, key) == expected

    # dois meios de se fazer a mesma coisa
    message = 6
    key = 3
    expected = "tipo inválido para message"
    with pytest.raises(TypeError) as excinfo:
        encrypt_message(message, key)

    assert str(excinfo.value) == expected

    message = "abcdef"
    key = "abcdef"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message, key)
