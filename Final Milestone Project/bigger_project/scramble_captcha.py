"""
A scramble word captcha that is solved if the user deciphers the word.
"""

from captcha import Captcha
import random
import tkinter as tk

class ScrambleCaptcha(Captcha):

    word_list = ['python', 'strypes', 'academy', 'algorithm', 'djikstra', 'flowers', 'seal', 'borzoi']

    def generate(self):
        """
        Generates a Scramble captcha by chosing a word from the self.word_list and shuffling its letters randomly
        It shuffles until they are not equal to ensure that the word and the scrambled version are not the same
        """
        self.ans = random.choice(self.word_list)
        letters = list(self.ans)
        while True:
            random.shuffle(letters)
            self.scramble = ''.join(letters)
            if self.scramble!= self.ans:
                break

    def get_prompt(self):
        """
        Returns a string that is the prompt of the captcha
        Output: String containing the prompt information
        """
        return f"Please unscramble the word: {self.scramble}"

    def check(self, answer = None):
        """
        Args:
          answer(string): Answer provided by the user
        If answer is None then the user is prompted to provide an answer. If its correct check returns True
        Output: Boolean if answer == self.ans
        """        
        if answer is None:
            answer = input("Please provide the correct word: ")
        return answer == self.ans
    
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


if __name__ == '__main__':
    captcha = ScrambleCaptcha()
    captcha.generate()
    print(captcha.get_prompt())
    print(captcha.check())