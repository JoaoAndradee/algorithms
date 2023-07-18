import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(Exception):
        encrypt_message("Message", "Invalid_type")

    with pytest.raises(Exception):
        encrypt_message(12, 12)

    assert encrypt_message("Mensagem", 0) == "megasneM"

    assert encrypt_message("Mensagem", 20) == "megasneM"

    assert encrypt_message("Mensagem", 1) == "M_megasne"

    assert encrypt_message("Mensagem", 2) == "megasn_eM"
