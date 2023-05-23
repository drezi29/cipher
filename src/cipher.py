from text import EncryptionStatus, Text
from custom_exceptions import DecryptionOfDecryptedMessageError, EncryptionOfEncryptedMessageError

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Cipher:
    @staticmethod
    def encrypt(text_obj: Text) -> Text:
        if text_obj.status == EncryptionStatus.ENCRYPTED:
            raise EncryptionOfEncryptedMessageError
        else:
            encrypted_message: str = ''
            allowed_signs = len(ALPHABET)
            for char in text_obj.text:
                if char.isupper():
                    position: int = ALPHABET.find(char)
                    encrypted_message += ALPHABET[(position + text_obj.rot_type) % allowed_signs]
                elif char.islower():
                    position: int = ALPHABET.find(char.upper())
                    encrypted_message += ALPHABET[(position + text_obj.rot_type) % allowed_signs].lower()
                else:
                    encrypted_message += char
            return Text(encrypted_message, text_obj.rot_type, EncryptionStatus.ENCRYPTED)

    @staticmethod
    def decrypt(text_obj: Text) -> Text:
        if text_obj.status == EncryptionStatus.DECRYPTED:
            raise DecryptionOfDecryptedMessageError
        else:
            decrypted_message: str = ''
            allowed_signs = len(ALPHABET)
            for char in text_obj.text:
                if char.isupper():
                    position: int = ALPHABET.find(char)
                    decrypted_message += ALPHABET[(position - text_obj.rot_type + allowed_signs) % allowed_signs]
                elif char.islower():
                    position: int = ALPHABET.find(char.upper())
                    decrypted_message += ALPHABET[(position - text_obj.rot_type + allowed_signs) % allowed_signs].lower()
                else:
                    decrypted_message += char
            return Text(decrypted_message, text_obj.rot_type, EncryptionStatus.DECRYPTED)
