"""
An odd one out captcha that is solved if the user picks the correct word
"""

from captcha import Captcha
import random
import tkinter as tk

class OddOneOutCaptcha(Captcha):
    choice_dict = {"animals": ["Cat", "Horse", "Dog", "Cow", "Crocodile", "Bird"],
    "vehichles": ["Car", "Bike", "Boat", "Helicopter", "Airplane"],
    "food": ["Apple", "Soup", "Carrot","Oatmeal", "Toast", "Sandwitch"]}
    
    def generate(self):
        """
        Generates an odd one out captcha by picking 2 categories main and odd. 
        Then picks one odd word from odd and 2 from main and shufles then randomly.
        """
        categories = random.sample(list(self.choice_dict.keys()),2)
        self.odd = random.choice(self.choice_dict[categories[0]])
        self.fodder_words = random.sample(self.choice_dict[categories[1]],2)
        self.all_words = [self.odd]+self.fodder_words
        random.shuffle(self.all_words)

    def get_prompt(self):
        """
        Returns a string that is the prompt of the captcha
        Output: String containing the prompt information
        """
        return "Pick the odd one out {} {} {}".format(*self.all_words)

    def check(self, answer = None):
        """
        Args:
         answer(string): Answer provided by the user
        If answer is None then the user is prompted to provide an answer. If its correct check returns True
        Output: Boolean if answer == self.odd
        """
        if answer is None:
            answer = input("Enter the odd one out (capitalization matters): ")
        return answer == self.odd

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
    captcha = OddOneOutCaptcha()
    captcha.generate()
    print(captcha.get_prompt())
    print(captcha.check())


        
    
    
    