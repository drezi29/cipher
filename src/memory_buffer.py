from json import dumps
from typing import List
from text import Text, EncryptionStatus


class MemoryBuffer:
    def __init__(self) -> None:
        self.__buffer: List[Text] = []

    def add_to_buffer(self, record: Text) -> None:
        self.__buffer.append(record)

    def get_buffer_list(self) -> List[Text]:
        return self.__buffer

    def clear_buffer(self) -> None:
        self.__buffer = []

    def buffer_pop(self) -> Text:
        return self.__buffer.pop()

    def buffer_to_json(self) -> str:
        pass