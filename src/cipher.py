from text import EncryptionStatus, Text
from custom_exceptions import (
    DecryptionOfDecryptedMessageError,
    EncryptionOfEncryptedMessageError,
)


class Cipher:
    @staticmethod
    def encrypt(text_obj: Text, alphabet: str) -> Text:
        if text_obj.status == EncryptionStatus.ENCRYPTED:
            raise EncryptionOfEncryptedMessageError
        else:
            encrypted_message: str = Cipher.do_shift_in_text(
                text_obj.text, text_obj.rot_type, alphabet
            )
            return Text(
                encrypted_message, text_obj.rot_type, EncryptionStatus.ENCRYPTED.value
            )

    @staticmethod
    def decrypt(text_obj: Text, alphabet: str) -> Text:
        if text_obj.status == EncryptionStatus.DECRYPTED:
            raise DecryptionOfDecryptedMessageError
        else:
            decrypted_message: str = Cipher.do_shift_in_text(
                text_obj.text, -text_obj.rot_type, alphabet
            )
            return Text(
                decrypted_message, text_obj.rot_type, EncryptionStatus.DECRYPTED.value
            )

    @staticmethod
    def do_shift_in_text(text: str, rot_type: int, signs: str) -> str:
        message = ''
        amount_of_signs = len(signs)
        for char in text:
            if char.isupper():
                position: int = signs.find(char)
                message += signs[
                    (position + rot_type + amount_of_signs) % amount_of_signs
                ]
            elif char.islower():
                position: int = signs.find(char.upper())
                message += signs[
                    (position + rot_type + amount_of_signs) % amount_of_signs
                ].lower()
            else:
                message += char
        return message
