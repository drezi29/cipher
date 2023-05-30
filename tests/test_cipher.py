import pytest
from src.cipher import Cipher, Text
from src.text import EncryptionStatus
from src.custom_exceptions import (
    DecryptionOfDecryptedMessageError,
    EncryptionOfEncryptedMessageError,
)


def test_shouldHelloMessageBeJgnnq_when_encryptedWithRot2():
    message: Text = Text('Hello', 2, EncryptionStatus.DECRYPTED.value)
    cipher: Cipher = Cipher()
    alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_message: Text = cipher.encrypt(message, alphabet)
    assert encrypted_message.text == 'Jgnnq'


def test_shouldMessageHaveChangedStatus_when_encrypted():
    message: Text = Text('Hello', 2, EncryptionStatus.DECRYPTED.value)
    cipher: Cipher = Cipher()
    alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_message: Text = cipher.encrypt(message, alphabet)
    assert encrypted_message.status != EncryptionStatus.DECRYPTED.value
    assert encrypted_message.status == EncryptionStatus.ENCRYPTED.value


def test_shouldMessageBeTheSame_when_encryptedAndDecrypted():
    message: Text = Text('Hello', 47, EncryptionStatus.DECRYPTED.value)
    cipher: Cipher = Cipher()
    alphabet: str = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    encrypted_message: Text = cipher.encrypt(message, alphabet)
    assert message != encrypted_message
    decrypted_message: Text = cipher.decrypt(encrypted_message, alphabet)
    assert message == decrypted_message


def test_shouldRaiseEncryptionOfEncryptedMessageError_when_encryptionPerformedOnEncryptedMessage():
    message: Text = Text('Jgnnq', 13, EncryptionStatus.ENCRYPTED.value)
    cipher: Cipher = Cipher()
    alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    with pytest.raises(EncryptionOfEncryptedMessageError):
        cipher.encrypt(message, alphabet)


def test_shouldRaiseDecryptionOfDecryptedMessageError_when_decryptionPerformedOnDecryptedMessage():
    message: Text = Text('Hello', 13, EncryptionStatus.DECRYPTED.value)
    cipher: Cipher = Cipher()
    alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    with pytest.raises(DecryptionOfDecryptedMessageError):
        cipher.decrypt(message, alphabet)
