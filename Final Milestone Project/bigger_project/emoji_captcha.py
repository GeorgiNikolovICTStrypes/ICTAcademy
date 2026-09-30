"""
An emoji captcha that is solved when the user selects the correct tiles.
"""

from captcha import Captcha
import random
import tkinter as tk

class EmojiCaptcha(Captcha):
    emojis = {"🐈", '🐕', '🐷','🐮','🐎','🍎'}

    def generate(self):
        """
        Generates an emoji captcha by picking 1 emoji from the self.emojis list
        It fills randomly chosen positions with it and fills the rest with the rest of the available
        emojis
        """
        self.target = random.choice(list(self.emojis))
        self.emojis.discard(self.target)

        self.correct = set(random.sample(range(9), random.randint(2,4)))

        self.grid = [self.target if i in self.correct else random.choice(list(self.emojis)) for  i in range(9)]
        print(self.grid)
        
    def get_prompt(self):
        """
        Returns a string that is the prompt of the captcha
        Output: String containing the prompt information
        """
        return f"Select all {self.target}"

    def check(self, answer):
        """
        Args:
          answer(set): A set of selected button indexes
        Checks if the answer is equal to self.correct
        Output: Bool returns true if the answer is equal to the correct buttons.
        """
        print("THIS GOES INTO CHECK: ", answer , self.correct)
        return answer == self.correct

    def display(self, parent):
        """
        Args:
          parent(tk): The main window we display information in
        Displays the captcha question
        """
        self.selected = set()
        self.buttons = []
        grid_frame = tk.Frame(parent)
        grid_frame.pack()
        
        for i, emoji in enumerate(self.grid):
            btn = tk.Button(grid_frame, text = emoji, width = 3, command = lambda i = i: self.toggle(i))
            self.buttons.append(btn)
            btn.grid(row = i//3, column = i%3, padx=2, pady=2)
    
    def toggle(self, i):
        """
        Args:
          i(int): Integer that represents the position of the button in the grid.
        This is the function for all the emoji buttons. When clicked it adds them to the selected set
        If a clicked button is clicked again its then raised and removed from the set.
        """
        if i in self.selected:
            self.selected.remove(i)
            self.buttons[i].config(relief="raised")
        else:
            self.selected.add(i)
            self.buttons[i].config(relief = "sunken")

    def get_answer(self):
        return self.selected
    
if __name__ == '__main__':
    captcha = EmojiCaptcha()
    captcha.generate()
    print(captcha.get_prompt())
