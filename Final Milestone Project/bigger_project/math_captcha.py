"""
A math captcha that is solved if the user solves the given equation
"""
from captcha import Captcha
import random
class MathCaptcha(Captcha):
    def generate(self):
        self.a = random.randint(-1000,1000)
        self.b = random.randint(-1000,1000)
        self.operation = random.choice(['-', '+', '*', '/'])
        self.ans = eval(f"{self.a} {self.operation} {self.b}")

    def get_prompt(self):
        return f"Please solve this problem: {self.a} {self.operation} {self.b}"

    def check(self):
        answer = input("Please provide an answer (if its division just provide it rounded to the nearest integer): ")
        try:
            return int(answer.strip()) == self.ans
        except ValueError:
            return False 

if __name__ == "__main__":
    captcha = MathCaptcha()
    captcha.generate()
    print(captcha.get_prompt())
    print(captcha.check())
