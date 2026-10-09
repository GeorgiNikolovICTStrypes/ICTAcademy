'''
Custom exception class for handling invalid menu options in the application.
'''
class InvalidMenuOption(Exception):
    """
    Exception raised for invalid menu selections
    """
    def __init__(self, message = "Please enter a valid option from the list!"):
        self.message = message
        super().__init__(message)