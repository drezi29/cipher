class Manager:
    def __init__(self):
        self.__is_not_exit = True

    def loop(self):
        while self.__is_not_exit:
            self.__print_menu()
            self.__manage_choosing_option()

    @staticmethod
    def __print_menu() -> None:
        '''Print program options as menu'''

        print('------ OPTIONS ------')
        print('[1] Decrypt from file')
        print('[2] Decrypt from text')
        print('[3] Encrypt from file')
        print('[4] Encrypt from text')
        print('[5] Save as file')
        print('[6] Exit')
        print('-' * 21)

    def __manage_choosing_option(self):
        option = input('Choose option: ')
        match option:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                self.__exit_program()
            case _:
                print(f'Option {option} doesn\'t exist')

    def __exit_program(self) -> None:
        print('Thank you for using Cipher!')
        self.__is_not_exit = False
