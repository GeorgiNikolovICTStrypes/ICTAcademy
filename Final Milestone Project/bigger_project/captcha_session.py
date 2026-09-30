"""
A class that gives the user n tries to solve a random captcha
"""

import random
from too_many_attempts import TooManyAttemptsError
from math_captcha import MathCaptcha
from scramble_captcha import ScrambleCaptcha
from odd_one_out_captcha import OddOneOutCaptcha
from emoji_captcha import EmojiCaptcha
import time
import tkinter as tk

class CaptchaSession:
    def __init__(self, captcha_types, max_attempts =3):
        self.captcha_types = captcha_types
        self.max_attempts = max_attempts
        self.incorrect = 0

    def start(self, time_limit = None):
        """
        Args:
          time_limit(int) - the time the user is given (in seconds) to solve the captcha
        Starts a captcha in the terminal if time_limit is not None its a timed session
        if the user goes over the limit this captcha is failed.
        The user can attempt to solve a captcha up to max_attempts attempts.

        """
        while self.incorrect<self.max_attempts:
            captcha = random.choice(self.captcha_types)()
            captcha.generate()

            print(captcha.get_prompt())
            started = time.time()
            correct = captcha.check()
            timed_out = time_limit is not None and time.time() - started > time_limit

            if timed_out:
                print(f"Too slow! You had {time_limit} seconds.")
                
            elif correct:
                print("You've passed the captcha!")
                return True
            self.incorrect+=1
            print(f"Wrong! ({self.incorrect}/{self.max_attempts})")
        raise TooManyAttemptsError(self.incorrect)
    
    def start_gui(self):
        """
        Starts a gui captcha session.
        The user is given a captcha and has to solve it.
        The user can attempt to solve a captcha up to max_attempts attempts.
        """
        self.root = tk.Tk()
        self.root.geometry("300x300")

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.label = tk.Label(self.root)
        self.label.pack()

        self.label_result = tk.Label(self.root)
        self.label_result.pack()

        tk.Button(self.root, text = "Submit", command = self.submit).pack()

        self.next_captcha()
        self.root.mainloop()

    def next_captcha(self):
        """
        Gives the user a new captcha, and clears the old tk window.
        """
        self.captcha = random.choice(self.captcha_types)()
        self.captcha.generate()
        self.label.config(text = self.captcha.get_prompt())
        for w in self.input_frame.winfo_children():
            w.destroy()
        self.captcha.display(self.input_frame)

    def submit(self):
        """
        Tis submits the answer and checks it, if correct the captcha is solved and the user is notified
        If incorrect the user gets another try if he can attempt another try else the captcha is failed
        and the user is notified.
        """
        if self.captcha.check(self.captcha.get_answer()):
            self.label_result.config(text = "You passed the captcha!", fg = "green")
            self.root.after(2000, self.root.destroy)
        else:
            self.incorrect+=1
            self.label_result.config(text = f"You have {self.incorrect}/{self.max_attempts} attempts left", fg = "red")
            if self.incorrect>self.max_attempts:
                self.label_result.config(text = "Too many attempts", fg = "crimson")
                self.root.after(2000, self.root.destroy)
            else:
                self.label_result.config(text = "Wrong! Try again!")
                self.next_captcha()
        
if __name__ == '__main__':
    try:
        captcha_session = CaptchaSession([MathCaptcha, ScrambleCaptcha, OddOneOutCaptcha, EmojiCaptcha])
        captcha_session.start_gui()
    except TooManyAttemptsError as e:
        print(f"Access Denied: {e}")