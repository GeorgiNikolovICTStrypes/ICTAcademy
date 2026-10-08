'''
Base data saver parent class for the TxtSaver, CSVSaver and JSONSaver
'''
import os

class Saver:

    def save(self, data, file_path, fields = None):
        raise NotImplementedError
    
    @staticmethod
    def _transform(data, fields = None):
        raise NotImplementedError
    
    @staticmethod
    def overwrite_confirmation(file_path):
        """
        Args:
        file_path (string): path to be checked if it exists
        Checks if this file already exists and prompts the user if they want to overwrite it
        """
        if os.path.exists(file_path):
            while True:
                answer = input(f"Warning! File {file_path} already exists! Are you sure you want to overwrite it? [y/n]")
                if answer.lower() in ['y','yes']:
                    return True
                if answer.lower() in ['n', 'no']:
                    return False
        return True
    
    @staticmethod
    def _prompt_for_mode():
        answer = ''
        while True:
            answer = input("Please enter a valid mode [a/w] (append, write) ")
            if answer.lower() in ['a', 'append']:
                return 'a'
            if answer.lower() in ['w', 'write']:
                return 'w'