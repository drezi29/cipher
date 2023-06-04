import os
import shutil
from src.file_handler import FileHandler
from src.memory_buffer import MemoryBuffer, Text
from src.text import EncryptionStatus


class TestFileHandler:
    def setup_method(self):
        os.mkdir('test_files')
        self.buffer = MemoryBuffer()
        self.message = 'Cipher'
        self.message2 = 'Cipher2'
        self.rot = 13
        self.rot2 = 27
        self.status_decrypted = EncryptionStatus.DECRYPTED.value
        self.buffer.add_to_buffer(Text(self.message, self.rot, self.status_decrypted))
        FileHandler.write_to_file('test_files/temp1.json', self.buffer.buffer_to_json())
        self.buffer.clear_buffer()

        self.buffer.add_to_buffer(Text(self.message, self.rot, self.status_decrypted))
        self.buffer.add_to_buffer(Text(self.message2, self.rot2, self.status_decrypted))
        FileHandler.write_to_file('test_files/temp2.json', self.buffer.buffer_to_json())
        self.buffer.clear_buffer()

        self.buffer.add_to_buffer(Text(self.message, self.rot, self.status_decrypted))
        FileHandler.write_to_file('test_files/temp4.json', self.buffer.buffer_to_json())
        self.buffer.clear_buffer()

    def test_is_content_read_as_object_correctly_when_one_element_is_read(self):
        object = FileHandler.read_file('test_files/temp1.json')

        assert len(object) == 1
        assert object[0].text == self.message
        assert object[0].status == self.status_decrypted
        assert object[0].rot_type == self.rot

    def test_is_content_read_as_object_correctly_when_list_of_elements_is_read(self):
        object_list = FileHandler.read_file('test_files/temp2.json')

        assert len(object_list) == 2
        assert object_list[0].text == self.message
        assert object_list[0].status == self.status_decrypted
        assert object_list[0].rot_type == self.rot
        assert object_list[1].text == self.message2
        assert object_list[1].status == self.status_decrypted
        assert object_list[1].rot_type == self.rot2

    def test_is_content_write_correctly_when_saving_one_element_to_new_file(self):
        file_name = 'test_files/temp3.json'
        self.buffer.add_to_buffer(Text(self.message, self.rot, self.status_decrypted))
        FileHandler.write_to_file(file_name, self.buffer.buffer_to_json())
        object_from_file = FileHandler.read_file(file_name)

        assert len(object_from_file) == 1
        assert object_from_file[0].text == self.message
        assert object_from_file[0].status == self.status_decrypted
        assert object_from_file[0].rot_type == self.rot

    def test_is_content_write_correctly_when_saving_many_elements_to_new_file(self):
        file_name = 'test_files/temp3.json'
        self.buffer.add_to_buffer(Text(self.message, self.rot, self.status_decrypted))
        self.buffer.add_to_buffer(Text(self.message2, self.rot2, self.status_decrypted))
        FileHandler.write_to_file(file_name, self.buffer.buffer_to_json())
        object_from_file = FileHandler.read_file(file_name)

        assert len(object_from_file) == 2
        assert object_from_file[0].text == self.message
        assert object_from_file[0].status == self.status_decrypted
        assert object_from_file[0].rot_type == self.rot
        assert object_from_file[1].text == self.message2
        assert object_from_file[1].status == self.status_decrypted
        assert object_from_file[1].rot_type == self.rot2

    def test_is_content_append_correctly_when_saving_to_existing_file(self):
        file_name = 'test_files/temp4.json'
        object_before_saving_to_file = FileHandler.read_file(file_name)
        assert len(object_before_saving_to_file) == 1
        assert object_before_saving_to_file[0].text == self.message
        assert object_before_saving_to_file[0].status == self.status_decrypted
        assert object_before_saving_to_file[0].rot_type == self.rot

        self.buffer.add_to_buffer(Text(self.message2, self.rot2, self.status_decrypted))
        FileHandler.write_to_file(file_name, self.buffer.buffer_to_json())
        object_after_saving_to_file = FileHandler.read_file(file_name)

        assert len(object_after_saving_to_file) == 2
        assert object_after_saving_to_file[0].text == self.message
        assert object_after_saving_to_file[0].status == self.status_decrypted
        assert object_after_saving_to_file[0].rot_type == self.rot
        assert object_after_saving_to_file[1].text == self.message2
        assert object_after_saving_to_file[1].status == self.status_decrypted
        assert object_after_saving_to_file[1].rot_type == self.rot2

    def teardown_method(self):
        shutil.rmtree('test_files')
