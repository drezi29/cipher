from dataclasses import dataclass, asdict
from enum import Enum
from json import dumps


class EncryptionStatus(str, Enum):
    ENCRYPTED = 'encrypted'
    DECRYPTED = 'decrypted'


@dataclass
class Text:
    text: str
    rot_type: int
    status: EncryptionStatus

    @property
    def json(self):
        return dumps(self.__dict__)
