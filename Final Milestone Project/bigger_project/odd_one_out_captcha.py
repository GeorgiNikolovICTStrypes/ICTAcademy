"""
An odd one out captcha that is solved if the user picks the correct word
"""

from captcha import Captcha
import random 

class OddOneOutCaptcha(Captcha):
    choice_dict = {"animals": ["Cat", "Horse", "Dog", "Cow", "Crocodile", "Bird"],
    "vehichles": ["Car", "Bike", "Boat", "Helicopter", "Airplane"],
    "food": ["Apple", "Soup", "Carrot","Oatmeal", "Toast", "Sandwitch"]}
    
    def generate(self):
        categories = random.sample(list(self.choice_dict.keys()),2)
        self.odd = random.choice(self.choice_dict[categories[0]])
        self.fodder_words = random.sample(self.choice_dict[categories[1]],2)
        self.all_words = [self.odd]+self.fodder_words
        random.shuffle(self.all_words)

    def get_prompt(self):
        return "Pick the odd one out {} {} {}".format(*self.all_words)

    def check(self):
        answer = input("Enter the odd one out (capitalization matters): ")
        return answer == self.odd

if __name__ == "__main__":
    captcha = OddOneOutCaptcha()
    captcha.generate()
    print(captcha.get_prompt())
    print(captcha.check())


        
    
    
    