from typing import Any, Dict, List
from .text import Text
from dataclasses import asdict


class MemoryBuffer:
    def __init__(self) -> None:
        self.__buffer: List[Text] = []

    def add_to_buffer(self, record: Text) -> None:
        """Add record to buffer"""

        self.__buffer.append(record)

    def get_buffer_list(self) -> List[Text]:
        """Returns full buffer list"""

        return self.__buffer

    def clear_buffer(self) -> None:
        """Makes buffer empty"""
        self.__buffer.clear()

    def buffer_pop(self) -> Text:
        """Take the last element of buffer"""

        return self.__buffer.pop()

    def buffer_to_json(self) -> List[Dict[str, Any]]:
        """Converts buffer records to json format"""

        return [asdict(record) for record in self.__buffer]

    def size(self) -> int:
        """Returns amount of elements in buffer"""

        return len(self.__buffer)
