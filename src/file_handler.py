import os
from json import dump, dumps, load, loads
from typing import Any, Dict, List
from .custom_exceptions import (
    AppendingTextToFileError,
    CreateFileError,
    InvalidRotStatus,
    InvalidTextStatus,
    ReadFileError,
)
from .text import EncryptionStatus, Text


class FileHandler:
    @staticmethod
    def read_file(full_path: str) -> List[Text]:
        """Takes file name, read data from file and return its content as Text object list"""

        #
        try:
            with open(full_path, 'r') as file:
                file_content: str = file.read()
                data: List[Any] = loads(file_content)
                text_objects: List[Text] = [
                    Text(**item)
                    for item in data
                    if FileHandler.__validate_record(Text(**item))
                ]
                return text_objects
        except IOError:
            raise ReadFileError

    @staticmethod
    def write_to_file(full_path: str, content: List[Dict[str, Any]]):
        """Takes file name and content data that needs to be written to file,
        decides if file needs to be created or data needs to be appended
        to the existing one"""

        # full_path: str = FileHandler.FOLDER_PATH + file_name + FileHandler.EXTENSION
        if os.path.isfile(full_path):
            FileHandler._append_file(full_path, content)
        else:
            FileHandler._create_file(full_path, content)

    @staticmethod
    def _create_file(full_path: str, content: List[Dict[str, Any]]):
        """Takes file name and content data, writes data to new file"""

        try:
            with open(full_path, 'w') as file:
                file.write(dumps(content))
        except IOError:
            raise CreateFileError

    @staticmethod
    def _append_file(full_path: str, content: str):
        """Takes file name and content data, writes data to existing file
        with given name"""

        try:
            with open(full_path, 'r+') as file:
                file_data = load(file)
                file_data.append(*content)
                file.seek(0)
                dump(file_data, file)
        except IOError:
            raise AppendingTextToFileError

    @staticmethod
    def __validate_record(record: Text) -> bool:
        """Checks if text from file contains correct status and rot type"""

        if (
            record.status != EncryptionStatus.ENCRYPTED.value
            and record.status != EncryptionStatus.DECRYPTED.value
        ):
            raise InvalidTextStatus
        if record.rot_type < 1 or record.rot_type > 126:
            raise InvalidRotStatus
        return True
