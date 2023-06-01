from src.memory_buffer import MemoryBuffer, Text
from src.text import EncryptionStatus


class TestBuffer:
    def setup_method(self):
        self.buffer = MemoryBuffer()
        self.text = Text('Cipher', 13, EncryptionStatus.DECRYPTED.value)
        self.text2 = Text('Cipher2', 13, EncryptionStatus.DECRYPTED.value)

    def test_should_buffer_size_return_1_when_1_element_added(self):
        assert self.buffer.size() == 0
        self.buffer.add_to_buffer(self.text)
        assert self.buffer.size() == 1

    def test_should_get_buffer_list_size_2_when_2_elements_addes(self):
        self.buffer.add_to_buffer(self.text)
        self.buffer.add_to_buffer(self.text2)
        assert len(self.buffer.get_buffer_list()) == 2

    def test_should_element_be_the_same_when_added_to_buffer_list(self):
        message = 'Cipher'
        self.buffer.add_to_buffer(self.text)
        assert self.buffer.get_buffer_list()[0] == self.text
        assert self.buffer.get_buffer_list()[0].text == message
        assert (
            self.buffer.get_buffer_list()[0].status == EncryptionStatus.DECRYPTED.value
        )
        assert self.buffer.get_buffer_list()[0].rot_type == 13

    def test_should_buffer_be_empty_when_cleared(self):
        self.buffer.add_to_buffer(self.text)
        assert self.buffer.size() == 1
        self.buffer.clear_buffer()
        assert self.buffer.size() == 0

    def test_should_element_be_the_same_when_popped(self):
        self.buffer.add_to_buffer(self.text)
        popped_element: Text = self.buffer.buffer_pop()
        assert self.text == popped_element
