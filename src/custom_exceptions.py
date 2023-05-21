class ReadFileError(Exception):
    '''Raised for IOError while reading a file'''

    def __str__(self):
        return "File doesn\'t exist or there is problem with reading this file"


class CreateFileError(Exception):
    '''Raised for IOError while creating new file'''

    def __str__(self):
        return "Problem while creating new file appeared"


class AppendingTextToFileError(Exception):
    '''Raised for IOError while appending text to existing file'''

    def __str__(self):
        return "Problem while appending text to existing file appeared"
