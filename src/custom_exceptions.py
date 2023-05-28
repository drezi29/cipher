class ReadFileError(Exception):
    """Raised for IOError while reading a file"""

    def __str__(self):
        return 'File doesn\'t exist or there is problem with reading this file'


class CreateFileError(Exception):
    """Raised for IOError while creating new file"""

    def __str__(self):
        return 'Problem while creating new file appeared'


class AppendingTextToFileError(Exception):
    """Raised for IOError while appending text to existing file"""

    def __str__(self):
        return 'Problem while appending text to existing file appeared'


class DecryptionOfDecryptedMessageError(Exception):
    """Raised when for decrypted text decryption operation is selected"""

    def __str__(self):
        return 'Attempting to decrypt an decrypted message'


class EncryptionOfEncryptedMessageError(Exception):
    """Raised when for encrypted text encryption operation is selected"""

    def __str__(self):
        return 'Attempting to encrypt an encrypted message'


class InvalidTextStatus(Exception):
    """Raised when status of record from file is other than encrypted or decrypted"""

    def __str__(self):
        return 'Invalid status. Status should be "encrypted" or "decrypted"'


class InvalidChoice(Exception):
    """Raised when user type invalid value"""

    def __str__(self):
        return 'Invalid choice'
