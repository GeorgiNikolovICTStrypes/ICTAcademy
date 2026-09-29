"""
A class that gives the user n tries to solve a random captcha
"""

import random
from too_many_attempts import TooManyAttemptsError
from math_captcha import MathCaptcha
from scramble_captcha import ScrambleCaptcha
from odd_one_out_captcha import OddOneOutCaptcha
class CaptchaSession:
    def __init__(self, captcha_types, max_attempts =3):
        self.captcha_types = captcha_types
        self.max_attempts = max_attempts
        self.incorrect = 0

    def start(self):
        while self.incorrect<self.max_attempts:
            captcha = random.choice(self.captcha_types)()
            captcha.generate()

            print(captcha.get_prompt())
            if captcha.check():
                print("You've passed the captcha!")
                return True
            self.incorrect+=1
            print(f"Wrong! ({self.incorrect}/{self.max_attempts})")
        raise TooManyAttemptsError(self.incorrect)


if __name__ == '__main__':
    try:
        captcha_session = CaptchaSession([OddOneOutCaptcha, MathCaptcha, ScrambleCaptcha])
        captcha_session.start()
    except TooManyAttemptsError as e:
        print(f"Access Denied: {e}")