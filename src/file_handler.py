import os
from custom_exceptions import ReadFileError, CreateFileError,\
    AppendingTextToFileError


class FileHandler:
    FOLDER_PATH = "../files/"

    @staticmethod
    def read_file(file_name: str) -> str:
        """Takes file name, read data from file and return its content"""

        full_path = FileHandler.FOLDER_PATH + file_name
        try:
            with open(full_path, "r") as file:
                file_content = file.read()
                return file_content
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
            with open(full_path, "w") as file:
                file.write(content)
        except IOError:
            raise CreateFileError

    @staticmethod
    def _append_file(full_path: str, content: str):
        """Takes file name and content data, writes data to existing file
        with given name"""

        try:
            with open(full_path, "a") as file:
                file.write("\n" + content)
        except IOError:
            raise AppendingTextToFileError
