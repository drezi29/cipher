from dataclasses import dataclass
from enum import Enum


class EncryptionStatus(str, Enum):
    ENCRYPTED = 'encrypted'
    DECRYPTED = 'decrypted'


@dataclass
class Text:
    text: str
    rot_type: int
    status: str
