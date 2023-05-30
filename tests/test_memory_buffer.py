from src.memory_buffer import MemoryBuffer, Text
from src.text import EncryptionStatus


def test_shouldBufferSizeReturn1_when_1ElementAdded():
    buffer: MemoryBuffer = MemoryBuffer()
    assert buffer.size() == 0
    text: Text = Text('Cipher', 13, EncryptionStatus.DECRYPTED.value)
    buffer.add_to_buffer(text)
    assert buffer.size() == 1


def test_shouldGetBufferListSize2_when_2ElementsAddes():
    buffer: MemoryBuffer = MemoryBuffer()
    text: Text = Text('Cipher', 13, EncryptionStatus.DECRYPTED.value)
    text2: Text = Text('Cipher2', 13, EncryptionStatus.DECRYPTED.value)
    buffer.add_to_buffer(text)
    buffer.add_to_buffer(text2)
    assert len(buffer.get_buffer_list()) == 2


def test_shouldElementBeTheSame_when_addedToBufferList():
    buffer: MemoryBuffer = MemoryBuffer()
    message: str = 'Cipher'
    text: Text = Text(message, 13, EncryptionStatus.DECRYPTED.value)
    buffer.add_to_buffer(text)
    assert buffer.get_buffer_list()[0] == text
    assert buffer.get_buffer_list()[0].text == message
    assert buffer.get_buffer_list()[0].status == EncryptionStatus.DECRYPTED.value
    assert buffer.get_buffer_list()[0].rot_type == 13


def test_shouldBufferBeEmpty_when_cleared():
    buffer: MemoryBuffer = MemoryBuffer()
    text: Text = Text('Cipher', 13, EncryptionStatus.DECRYPTED.value)
    buffer.add_to_buffer(text)
    assert buffer.size() == 1
    buffer.clear_buffer()
    assert buffer.size() == 0


def test_shouldElementBeTheSame_when_popped():
    buffer: MemoryBuffer = MemoryBuffer()
    text: Text = Text('Cipher', 13, EncryptionStatus.DECRYPTED.value)
    buffer.add_to_buffer(text)
    popped_element: Text = buffer.buffer_pop()
    assert text == popped_element
