"""
A math captcha that is solved if the user solves the given equation
"""
from captcha import Captcha
import random
import tkinter as tk

class MathCaptcha(Captcha):
    def generate(self):
        """
        Generates 2 random numvers and an operation and sets self.ands to the
        evaluation of the string a op b
        """
        self.a = random.randint(-1000,1000)
        self.b = random.randint(-1000,1000)
        self.operation = random.choice(['-', '+', '*', '/'])
        self.ans = eval(f"{self.a} {self.operation} {self.b}")

    def get_prompt(self):
        """
        Returns a string that is the prompt of the captcha
        Output: String containing the prompt information
        """
        return f"Please solve this problem: {self.a} {self.operation} {self.b}"

    def check(self,answer = None):
        """
        Args:
          answer(string): Answer provided by the user
        If answer is None then the user is prompted to provide an answer. If its correct check returns True
        Output: Boolean if answer == self.ans
        """
        if answer is None:
            answer = input("Please provide an answer (if its division just provide it rounded to the nearest integer): ")
        try:
            return int(answer.strip()) == self.ans
        except ValueError:
            return False 
        
    def display(self, parent):
        """
        Args:
          parent(tk) A windows to which we add a tk.Entry object where the user can type in their answer.
        """
        self.entry = tk.Entry(parent)
        self.entry.pack()

    def get_answer(self):
        """
        Fetches the string from tk.Entry object in self.entry
        Output: String from tk.Entry obj
        """
        return self.entry.get()
        
if __name__ == "__main__":
    captcha = MathCaptcha()
    captcha.generate()
    print(captcha.get_prompt())
    print(captcha.check())
