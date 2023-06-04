import string
from typing import List
from .cipher import Cipher
from .custom_exceptions import InvalidChoice
from .file_handler import FileHandler
from .memory_buffer import MemoryBuffer
from .text import EncryptionStatus, Text


class Manager:
    FOLDER_PATH = 'files/'
    EXTENSION = '.json'

    def __init__(self) -> None:
        self.__is_not_exit = True
        self.__buffer = MemoryBuffer()

    def run(self) -> None:
        """Run loop of the program"""

        while self.__is_not_exit:
            self.__print_menu()
            self.__manage_choosing_option()

    @staticmethod
    def __print_menu() -> None:
        """Print program options as menu"""

        print('------ OPTIONS ------')
        print('[1] Encrypt from file')
        print('[2] Encrypt from text')
        print('[3] Decrypt from file')
        print('[4] Decrypt from text')
        print('[5] Save as file')
        print('[6] Exit')
        print('-' * 21)

    def __manage_choosing_option(self) -> None:
        """Run function selected by user"""

        option: str = input('Choose option: ')
        match option:
            case '1':
                self.__encrypt_from_file()
            case '2':
                self.__encrypt_from_text()
            case '3':
                self.__decrypt_from_file()
            case '4':
                self.__decrypt_from_text()
            case '5':
                self.__save_as_file()
            case '6':
                self.__exit_program()
            case _:
                print(f'Option {option} doesn\'t exist')

    def __exit_program(self) -> None:
        """Exit program with safe exit if records are in buffer"""

        if self.__buffer.size() > 0:
            decision: str = input(
                'There are records not saved in files that will be lost on exit. '
                'Do you want to save result before exit? [Y/N]: '
            )
            if self.__is_confirmed(decision):
                self.__save_as_file()

        print('Thank you for using Cipher!')
        self.__is_not_exit = False

    def __encrypt_from_text(self) -> None:
        """Run encryption for text typed by user"""

        text: str = input('Type the message to be encrypted: ')
        rot: int = Manager.__rot_information()
        text_obj: Text = Text(text, rot, EncryptionStatus.DECRYPTED.value)
        self.__buffer.add_to_buffer(
            Cipher.encrypt(text_obj, Manager.__choose_alphabet(rot))
        )
        self.__ask_to_save()

    def __encrypt_from_file(self) -> None:
        """Run encryption for data loaded from specified file"""

        file_name: str = input(
            'Type the name of the file with the content to be encrypted: '
        )
        messages: List[Text] = FileHandler.read_file(
            self.__prepare_full_path(file_name)
        )
        for message in messages:
            self.__buffer.add_to_buffer(
                Cipher.encrypt(message, Manager.__choose_alphabet(message.rot_type))
            )
        self.__ask_to_save()

    def __decrypt_from_text(self) -> None:
        """Run decryption for text typed by user"""

        text: str = input('Type the message to be decrypted: ')
        rot: int = Manager.__rot_information()
        text_obj: Text = Text(text, rot, EncryptionStatus.ENCRYPTED.value)
        self.__buffer.add_to_buffer(
            Cipher.decrypt(text_obj, Manager.__choose_alphabet(rot))
        )
        self.__ask_to_save()

    def __decrypt_from_file(self) -> None:
        """Run decryption for data loaded from specified file"""

        file_name: str = input(
            'Type the name of the file with the content to be decrypted: '
        )
        messages: List[Text] = FileHandler.read_file(
            self.__prepare_full_path(file_name)
        )
        for message in messages:
            self.__buffer.add_to_buffer(
                Cipher.decrypt(message, Manager.__choose_alphabet(message.rot_type))
            )
        self.__ask_to_save()

    def __save_as_file(self) -> None:
        """Saves all records from memory buffer to file"""

        file_name: str = input(
            'Type the name of the file to which to save the content: '
        )
        FileHandler.write_to_file(
            self.__prepare_full_path(file_name), self.__buffer.buffer_to_json()
        )
        self.__ask_for_cleaning_buffer()

    @staticmethod
    def __rot_information() -> int:
        """Takes rot input from user and validates"""

        print('For rot types to 25 algorithm uses latin alphabet.')
        print(
            'For rot types between 26 and 126 algorithm uses ASCII table known from ROT47 algorithm.'
        )
        invalid_rot: bool = True
        rot: int = 1
        while invalid_rot:
            try:
                rot = int(input('Type rot type (1-126): '))
            except ValueError:
                print('Please enter a integer value between 1 and 126!')
                continue
            if rot < 1 or rot > 126:
                print('The rot value must be in the range 1-126')
            else:
                invalid_rot = False
        return rot

    @staticmethod
    def __choose_alphabet(rot: int) -> str:
        """Returns alphabet for algorithm based on rot. For rot in range 1-25 latin alphabet is returned.
        For rot in range 26-126 ASCII chars from 33 to 126 are returned."""

        if rot < 26:
            return string.ascii_uppercase
        else:
            ascii_rot47: str = ''
            for i in range(33, 127, 1):
                ascii_rot47 += chr(i)
            return ascii_rot47

    def __ask_to_save(self):
        """Ask user for save result in file and saving if user confirm"""

        decision: str = input('Do you want save result to file? [Y/N]: ')
        if self.__is_confirmed(decision):
            self.__save_as_file()

    def __ask_for_cleaning_buffer(self):
        """Ask user for cleaning buffer and clean if user confirm"""

        decision: str = input('Do you want to clear buffer? [Y/N]: ')
        if self.__is_confirmed(decision):
            self.__buffer.clear_buffer()

    @staticmethod
    def __is_confirmed(decision: str) -> bool:
        """Validate user input in Yes/No decision, returns bool"""

        if decision.upper() != 'Y' and decision.upper() != 'N':
            raise InvalidChoice
        elif decision.upper() == 'Y':
            return True
        elif decision.upper() == 'N':
            return False

    def __prepare_full_path(self, file_name: str) -> str:
        return Manager.FOLDER_PATH + file_name + Manager.EXTENSION
