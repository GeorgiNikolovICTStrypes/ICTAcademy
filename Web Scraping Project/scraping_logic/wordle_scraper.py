'''
A webscraper to scrape data for todays wordle
'''

import csv
from datetime import date
from .base_scraper import Scraper
from colorama import Fore

class WordleScraper(Scraper):
    '''
    A webscraper for the site: https://www.nytimes.com/games/wordle/index.html. Inherits from the base Scraper class.
    '''
    def __init__(self):
        '''
        Initializes a WordleScraper object. Loads a list of allowrd words and sets display and index urls.
        '''
        self.display_url = 'https://www.nytimes.com/games/wordle/index.html'
        self.index_url = 'https://www.nytimes.com/svc/wordle/v2/'
        
        with open('wordle_words/word-bank.csv') as file:
            reader = csv.reader(file)
            self.allowed_words =  {row[0] for row in reader}

        with open('wordle_words/valid-words.csv') as file:
            reader = csv.reader(file)
            self.allowed_words.update({row[0] for row in reader})

    def _get_word(self):  
        '''
        Gets the answer to today's wordle.
        Output:
          (string): the answer to today's wordle
        '''      
        today_url = self.index_url + date.today().isoformat() + '.json'
        data = self._fetch_data(today_url)
        wordle_json = data.select_one('p').text
        start = wordle_json.find('solution') + 11 # 8 for the word solution since find returns the start and then we add 3 for ":"
        word = wordle_json[start:start+5]
        return word
    

    def _prompt_for_word(self):
        """
        Prompts the user to enter a word thats 5 letters long and is in the allowed words list
        Output:
          (string): valid word entered by the user.
        """
        word = ''
        while len(word)!=5 or any(not x.isalpha() for x in word) or not word in self.allowed_words:
            word = input("Please enter a valid 5 letter word: ")
            if not word in self.allowed_words:
                print("Word is not allowed!")
            
        return word
    
    def play_wordle(self):
        """
        Plays out a wordle session with today's word as the solution. 
        Output:
          (list of strings): The users guesses + the solution
        """
        solution = self._get_word()
        guesses = []
        print("Welcome to wordle!")
        print("You get 6 tries to guess a 5 letter word")
        print("If a letter is colored green its in the right position, if a letter is colored yellow its in the word but on the wrong position.")
        print("If a letter is colored gray its not in the word.")
        guesses = [''] * 6
        for i in range(6):
            user_word = self._prompt_for_word()
            guesses[i] = user_word
            output_word_with_colors = ''
            if user_word == solution:
                print(f"You've correctly guessed today's wordle! The answer was {solution}, you solved it in {i+1} tries!")
                return [guesses + [solution]]
            for j in range(5):
                if solution[j]==user_word[j]:
                    output_word_with_colors += Fore.LIGHTGREEN_EX + user_word[j] + Fore.RESET
                elif user_word[j] in solution:
                    output_word_with_colors += Fore.LIGHTYELLOW_EX + user_word[j] + Fore.RESET
                else:
                    output_word_with_colors += Fore.LIGHTBLACK_EX + user_word[j] + Fore.RESET
            print(output_word_with_colors)
        print(f'You could not guess the word! The word was: {solution}')
        return [guesses + [solution]]
if __name__ == '__main__':
    with WordleScraper() as scraper:
        print(scraper.play_wordle())