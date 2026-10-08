"""
Exception raised for invalid menu selections
"""
class InvalidMenuOption(Exception):
  
    def __init__(self, message = "Please enter a valid option from the list!"):
        self.message = message
        super().__init__(message)