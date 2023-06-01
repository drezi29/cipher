from .text import EncryptionStatus, Text
from .custom_exceptions import (
    DecryptionOfDecryptedMessageError,
    EncryptionOfEncryptedMessageError,
)


class Cipher:
    @staticmethod
    def encrypt(text_obj: Text, alphabet: str) -> Text:
        """Static method that encrypt passed text"""

        if text_obj.status == EncryptionStatus.ENCRYPTED:
            raise EncryptionOfEncryptedMessageError
        else:
            encrypted_message: str = Cipher.__do_shift_in_text(
                text_obj.text, text_obj.rot_type, alphabet
            )
            return Text(
                encrypted_message, text_obj.rot_type, EncryptionStatus.ENCRYPTED.value
            )

    @staticmethod
    def decrypt(text_obj: Text, alphabet: str) -> Text:
        """Static method that decrypt passed text"""

        if text_obj.status == EncryptionStatus.DECRYPTED:
            raise DecryptionOfDecryptedMessageError
        else:
            decrypted_message: str = Cipher.__do_shift_in_text(
                text_obj.text, -text_obj.rot_type, alphabet
            )
            return Text(
                decrypted_message, text_obj.rot_type, EncryptionStatus.DECRYPTED.value
            )

    @staticmethod
    def __do_shift_in_text(text: str, rot_type: int, signs: str) -> str:
        """Method for shifting chars"""

        message: str = ''
        amount_of_signs: int = len(signs)

        if abs(rot_type) > 25:
            for char in text:
                if char not in signs:
                    message += char
                else:
                    position: int = signs.find(char)
                    message += signs[
                        (position + rot_type + amount_of_signs) % amount_of_signs
                    ]
        else:
            for char in text:
                if char.upper() not in signs:
                    message += char
                else:
                    position: int = signs.find(char.upper())
                    shifted_char = signs[
                        (position + rot_type + amount_of_signs) % amount_of_signs
                    ]
                    if char.islower():
                        shifted_char = shifted_char.lower()
                    message += shifted_char
        return message
