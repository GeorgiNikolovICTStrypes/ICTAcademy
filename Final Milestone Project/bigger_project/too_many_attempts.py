"""
A custom exception class
"""

class TooManyAttemptsError(Exception):
    def __init__(self, attempts):
        self.attempts = attempts
        super().__init__(f"You failed the captcha {self.attempts} times you are locked out.")