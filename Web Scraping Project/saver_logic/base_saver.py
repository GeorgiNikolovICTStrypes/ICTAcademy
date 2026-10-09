'''
Base data saver parent class for the TxtSaver, CSVSaver and JSONSaver
'''
import os

class Saver:
    '''
    Base Saver class for all savers.
    '''
    def save(self, data, file_path, fields = None):
        '''
        Base method for saving data to a file. Implemented by the child classes.
        '''
        raise NotImplementedError

    @staticmethod
    def _transform(data, fields = None):
        '''
        Base method for transforming data to be saved. Implemented by the child classes.
        '''
        raise NotImplementedError

    @staticmethod
    def overwrite_confirmation(file_path, mode):
        """
        Args:
        file_path (string): path to be checked if it exists
        mode (string): the mode in which the file is opened ('a' for append, 'w' for write)
        Checks if this file already exists and prompts the user if they want to overwrite it
        Output:
          (bool): True if the user wants to overwrite/append to the file, False otherwise.
        """
        if os.path.exists(file_path):
            while True:

                if mode == 'w':
                    answer = input(f"Warning! File {file_path} already exists! Are you sure you want to overwrite it? [y/n]")
                else:
                    answer = input(f"Warning! File {file_path} already exists! Are you sure you want to append to it? [y/n]")

                if answer.lower() in ['y','yes']:
                    return True
                if answer.lower() in ['n', 'no']:
                    return False
        return True

    @staticmethod
    def _prompt_for_mode():
        '''
        Prompts the user for a mode to open the file in [a/w] (append, write)
        Output:
          (string): 'a' for append and 'w' for write
        '''
        answer = ''
        while True:
            answer = input("Please enter a valid mode [a/w] (append, write) ")
            if answer.lower() in ['a', 'append']:
                return 'a'
            if answer.lower() in ['w', 'write']:
                return 'w'
