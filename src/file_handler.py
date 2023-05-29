import os
from json import loads
from typing import List
from custom_exceptions import (
    AppendingTextToFileError,
    CreateFileError,
    InvalidRotStatus,
    InvalidTextStatus,
    ReadFileError,
)
from text import EncryptionStatus, Text


class FileHandler:
    FOLDER_PATH = '../files/'

    @staticmethod
    def read_file(file_name: str) -> List[Text]:
        """Takes file name, read data from file and return its content as Text object list"""

        full_path = FileHandler.FOLDER_PATH + file_name
        try:
            with open(full_path, 'r') as file:
                file_content: str = file.read()
                data = loads(file_content)

                messages_as_text_objects: List[Text] = []
                for item in data:
                    text = Text(**item)
                    FileHandler.__validate_record(text)
                    messages_as_text_objects.append(text)
                return messages_as_text_objects
        except IOError:
            raise ReadFileError

    @staticmethod
    def write_to_file(file_name: str, content: str):
        """Takes file name and content data that needs to be written to file,
        decides if file needs to be created or data needs to be appended
        to the existing one"""

        full_path = FileHandler.FOLDER_PATH + file_name
        if os.path.isfile(full_path):
            FileHandler._append_file(full_path, content)
        else:
            FileHandler._create_file(full_path, content)

    @staticmethod
    def _create_file(full_path: str, content: str):
        """Takes file name and content data, writes data to new file"""
        try:
            with open(full_path, 'w') as file:
                file.write(content)
        except IOError:
            raise CreateFileError

    @staticmethod
    def _append_file(full_path: str, content: str):
        """Takes file name and content data, writes data to existing file
        with given name"""

        try:
            with open(full_path, 'a') as file:
                file.write('\n' + content)
        except IOError:
            raise AppendingTextToFileError

    @staticmethod
    def __validate_record(record: Text) -> None:
        """Checks if text from file contains correct status and rot type"""

        if (
            record.status != EncryptionStatus.ENCRYPTED.value
            and record.status != EncryptionStatus.DECRYPTED.value
        ):
            raise InvalidTextStatus
        if record.rot_type < 1 or record.rot_type > 126:
            raise InvalidRotStatus
