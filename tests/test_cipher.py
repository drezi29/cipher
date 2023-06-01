import pytest
import string
from src.cipher import Cipher, Text
from src.text import EncryptionStatus
from src.custom_exceptions import (
    DecryptionOfDecryptedMessageError,
    EncryptionOfEncryptedMessageError,
)


class TestCipher:
    def setup_method(self):
        self.message = Text('Hello', 2, EncryptionStatus.DECRYPTED.value)
        self.cipher = Cipher()
        self.alphabet = string.ascii_uppercase
        self.full_alphabet = ''.join([chr(i) for i in range(33, 127)])

    def test_should_hello_message_be_jgnnq_when_encrypted_with_rot2(self):
        encrypted_message = self.cipher.encrypt(self.message, self.alphabet)
        assert encrypted_message.text == 'Jgnnq'

    def test_should_message_have_changed_status_when_encrypted(self):
        encrypted_message: Text = self.cipher.encrypt(self.message, self.alphabet)
        assert encrypted_message.status != EncryptionStatus.DECRYPTED.value
        assert encrypted_message.status == EncryptionStatus.ENCRYPTED.value

    def test_should_message_be_the_same_when_encrypted_and_decrypted(self):
        message = Text('Hello', 47, EncryptionStatus.DECRYPTED.value)
        encrypted_message = self.cipher.encrypt(message, self.full_alphabet)
        assert message != encrypted_message
        decrypted_message = self.cipher.decrypt(encrypted_message, self.full_alphabet)
        assert message == decrypted_message

    def test_should_raise_encryption_of_encrypted_message_error_when_encryption_performed_on_encrypted_message(
        self,
    ):
        message = Text('Jgnnq', 13, EncryptionStatus.ENCRYPTED.value)
        with pytest.raises(EncryptionOfEncryptedMessageError):
            self.cipher.encrypt(message, self.alphabet)

    def test_should_raise_decryption_of_decrypted_message_error_when_decryption_performed_on_decrypted_message(
        self,
    ):
        message = Text('Hello', 13, EncryptionStatus.DECRYPTED.value)
        with pytest.raises(DecryptionOfDecryptedMessageError):
            self.cipher.decrypt(message, self.alphabet)
