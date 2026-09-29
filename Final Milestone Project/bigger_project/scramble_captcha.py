"""
A scramble word captcha that is solved if the user deciphers the word.
"""

from captcha import Captcha
import random
class ScrambleCaptcha(Captcha):

    word_list = ['python', 'strypes', 'academy', 'algorithm', 'djikstra', 'flowers', 'seal', 'borzoi']

    def generate(self):
        self.ans = random.choice(self.word_list)
        letters = list(self.ans)
        while True:
            random.shuffle(letters)
            self.scramble = ''.join(letters)
            if self.scramble!= self.ans:
                break

    def get_prompt(self):
        return f"Please unscramble the word: {self.scramble}"

    def check(self):
        answer = input("Please provide the correct word: ")
        return answer == self.ans


if __name__ == '__main__':
    captcha = ScrambleCaptcha()
    captcha.generate()
    print(captcha.get_prompt())
    print(captcha.check())