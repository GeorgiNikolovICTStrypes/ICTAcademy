'''
This module implements the ScrapingSession class.
'''

import os
from scraping_logic.basketball_scraper import NBAScraper
from scraping_logic.quotes_scraper import QuoteScraper
from scraping_logic.book_scraper import BookScraper
from scraping_logic.wordle_scraper import WordleScraper
from saver_logic.txt_saver import TxtSaver
from saver_logic.csv_saver import CSVSaver
from saver_logic.json_saver import JSONSaver
from .menu_exception import InvalidMenuOption

class ScrapingSession:
    """
    A class to manage a web scraping session. Handles user input
    and output, and manages the scraping session.
    """
    def __init__(self):
        self.file_locations = []
        self.data_types = []
        self.sites_scraped_urls = []
        self.curr_scraper = None
        self.curr_saver = None

    def prompt_for_site(self):
        '''
        A function to prompt the user for a site to scrape.
        Displays a menu for the user.
        Output:
          (int) -1 for Exit (if user entered 4)
          (none) None for a valid site to scrape
        '''
        print('What would u like to scrape?')
        print('1. Quotes\n2. Basketball information\n3. Book information\n4. Wordle\n5. Exit')
        choice = None
        while True:
            try:
                choice = int(input("Choose an option from the list (number). "))
                break
            except (ValueError, TypeError):
                print("Please enter a number from the list! ")
                continue
        try:
            if choice == 1:
                self.curr_scraper = QuoteScraper
                self.sites_scraped_urls.append(self.curr_scraper().index_url)
            elif choice == 2:
                self.curr_scraper = NBAScraper
                self.sites_scraped_urls.append(self.curr_scraper().index_url)
            elif choice == 3:
                self.curr_scraper = BookScraper
                self.sites_scraped_urls.append(self.curr_scraper().index_url)
            elif choice == 4:
                self.curr_scraper = WordleScraper
                self.sites_scraped_urls.append(self.curr_scraper().display_url)
            elif choice == 5:
                return -1
            else:
                raise InvalidMenuOption
        except InvalidMenuOption:
            print("Please enter a valid option from the list! ")
            return self.prompt_for_site()

    def prompt_for_function_quotes(self):
        '''
        Prompts the user for a function to scrape from the quotes site. It displays a menu for the user.
        Output:
          (int) -1 for Exit (if user entered 4) or 5 for testing faulty url
          (tuple) (data, fields) for a valid function to scrape
        '''
        print('What information would u like to scrape about quotes?')
        print('1. Authors\n2. Popular Tags\n3. Quotes on page 1-10\n4. Exit\n5. Test faulty url')
        choice = 0
        while True:
            try:
                choice = int(input("Choose an option from the list (number). "))
                break
            except (ValueError, TypeError):
                print("Please enter a number from the list! ")
                continue
        with self.curr_scraper() as scraper:
            try:
                if choice == 1:
                    self.data_types.append('Authors')
                    data = scraper.fetch_authors()
                    return (data, 'Authors')
                elif choice == 2:
                    self.data_types.append('Tags')
                    data = scraper.fetch_top_n_tags()
                    return (data, 'Tags')
                elif choice == 3:
                    self.data_types.append('Quotes')
                    data = scraper.fetch_quotes_for_page()
                    return (data, 'Quotes')
                elif choice == 4:
                    self.sites_scraped_urls.pop()
                    return -1
                elif choice == 5:
                    self.data_types.append('Faulty')
                    data = scraper.test_faulty()
                    # Returns same as exit, because we want the same behaviour as exit.
                    # Future work: we can add a different behaviour for this case, like saving the error to a log file.
                    return -1
                else:
                    raise InvalidMenuOption
            except InvalidMenuOption:
                print("Please enter a valid option from the list! ")
                return self.prompt_for_function_quotes()
            
    def prompt_for_function_books(self):
        '''
        Prompts the user for a function to scrape from the books site. It displays a menu for the user.
        Output:
          (int) -1 for Exit (if user entered 4)
          (tuple) (data, fields) for a valid function to scrape
        '''
        print('What information would u like to scrape about books?')
        print('1. Book info for books with rating [1-5] \n2. Get book categories\n3. Get book titles in a category\n4. Exit')
        choice = 0
        while True:
            try:
                choice = int(input("Choose an option from the list (number). "))
                break
            except ValueError:
                print("Please enter a number from the list! ")
                continue
        with self.curr_scraper() as scraper:
            try:
                if choice == 1:
                    self.data_types.append('Book Info')
                    data = scraper.fetch_info_for_books_with_rating()
                    return (data, ['Book Title', 'Book URL', 'Book Price', 'Book Availability'])
                elif choice == 2:
                    self.data_types.append('Book Categories')
                    data = scraper.fetch_all_categories()
                    return (data, 'Book Categories')
                elif choice == 3:
                    self.data_types.append('Book titles')
                    data = scraper.fetch_books_in_category()
                    return (data, 'Book titles')
                elif choice == 4:
                    self.sites_scraped_urls.pop()
                    return -1
                else:
                    raise InvalidMenuOption
            except InvalidMenuOption:
                print("Please enter a valid option from the list! ")
                return self.prompt_for_function_books()
            
    def prompt_for_function_basketball(self):
        '''
        Prompts the user for a function to scrape from the basketball site. It displays a menu for the user.
        Output:
          (int) -1 for Exit (if user entered 4)
          (tuple) (data, fields) for a valid function to scrape
        '''
        print('What information would u like to scrape about the NBA?')
        print("1. Champions from year to year\n2. Get a team's roster\n3. Get all NBA teams and their abbreviations\n4. Get stats for a player\n5. Exit")
        choice = 0
        while True:
            try:
                choice = int(input("Choose an option from the list (number). "))
                break
            except ValueError, TypeError:
                print("Please enter a number from the list! ")
                continue

        with self.curr_scraper() as scraper:
            try: 
                if choice == 1:
                    self.data_types.append('NBA Champions')
                    data = scraper.fetch_champions_from_to()
                    return (data, 'NBA Champions')
                elif choice == 2:
                    self.data_types.append('Player Names')
                    data = scraper.fetch_current_team_roster()
                    return (data, 'Player Names')
                elif choice == 3:
                    self.data_types.append('Team Names')
                    data = scraper.fetch_teams_with_abbreviations()
                    return (data, ['Team Names', 'Abbreviations'])
                elif choice == 4:
                    self.data_types.append('Player info')
                    data = scraper.fetch_player_info()
                    fields = ['Player Name']
                    fields += ['Career Games', 'Career AVG PPG', 'Career AVG TRB', 'Career AVG AST', 'Career FG%', 'Career FG3%', 'Career FT%', 'Career eFG%']
                    fields += ['Season Games','Season AVG PPG', 'Season AVG TRB', 'Season AVG AST', 'Season FG%', 'Season FG3%', 'Season FT%', 'Season eFG%']
                    return (data, fields)
                elif choice == 5:
                    self.sites_scraped_urls.pop()
                    return -1

                else:
                    raise InvalidMenuOption
                
            except InvalidMenuOption:
                print("Please enter a valid option from the list! ")
                return self.prompt_for_function_basketball()

    def prompt_for_wordle(self):
        '''
        Prompts the user if they would like to play today's wordle.
        Output:
          (int) -1 if the user entered 2 (Exit)
          (tuple) in format (data , fields) if they entered 1
        '''
        print("1. Play today's wordle\n2. Exit")
        choice = 0
        while True:
            try:
                choice = int(input("Choose an option from the list (number). "))
                break
            except ValueError, TypeError:
                print("Please enter a number from the list! ")
                continue

        with self.curr_scraper() as scraper:
            try:
                if choice == 1:
                    self.data_types.append('Wordle Guesses')
                    data = scraper.play_wordle()
                    return (data, ['Guess 1','Guess 2','Guess 3','Guess 4','Guess 5','Guess 6','Answer'])
                elif choice == 5:
                    self.sites_scraped_urls.pop()
                    return -1
                else:
                    raise InvalidMenuOption
            except InvalidMenuOption:
                print("Please enter a valid option from the list! ")
                return self.prompt_for_wordle()

    def prompt_for_save(self):
        '''
        Prompts the user for a file format to save the data. It displays a menu for the user.
        '''
        print("How would you like to save the data?\n1. TXT\n2. CSV\n3. JSON")
        choice = 0
        while True:
            try:
                choice = int(input("Choose an option from the list (number). "))
                break
            except ValueError:
                print("Please enter a number from the list! ")
                continue
        try:
            if choice == 1:
                self.curr_saver = TxtSaver
            elif choice == 2:
                self.curr_saver = CSVSaver
            elif choice == 3:
                self.curr_saver = JSONSaver
            else:
                raise InvalidMenuOption
        except InvalidMenuOption:
            print("Please enter a valid option from the list! ")
            return self.prompt_for_save()

    def prompt_for_file_path(self):
        '''
        Prompts the user for a file path to where they want to save the data.
        '''
        path = input("Please enter the file path where you want to save the data. ")
        name, _ = os.path.splitext(path)
        extension = ""
        if self.curr_saver == TxtSaver:
            extension = "txt"
        elif self.curr_saver == CSVSaver:
            extension = "csv"
        elif self.curr_saver == JSONSaver:
            extension = "json"

        path = name + '.' + extension
        return path

    def start(self):
        """
        Starts a scraping session. It follows the following flow:
        1. Prompts the user for a site to scrape.
        2. Prompts the user for a function to scrape from the site.
        3. Scrapes the data from the site using the selected function.
        4. Prompts the user for a file format to save the data.
        5. Saves the data to the specified file format.
        6. Repeats the process until the user chooses to exit.
        """
        while True:
            
            data = None
            self.curr_scraper = None
            self.curr_saver = None
            ans = self.prompt_for_site()
            if ans == -1:
                break

            if self.curr_scraper == QuoteScraper:
                data_fields = self.prompt_for_function_quotes()
                if data_fields == -1:
                    continue
                
            elif self.curr_scraper == NBAScraper: 
                data_fields = self.prompt_for_function_basketball()
                if data_fields == -1:
                    continue

            elif self.curr_scraper == BookScraper:
                data_fields = self.prompt_for_function_books()
                if data_fields == -1:
                    continue

            elif self.curr_scraper == WordleScraper:
                data_fields = self.prompt_for_wordle()
                if data_fields == -1:
                    continue

            data, fields = data_fields
            print(data)
            if data is None:
                print("The scraper couldnt find any_data. Please try again!")
                self.data_types.pop()
                self.sites_scraped_urls.pop()
                continue
            self.prompt_for_save()
            file_path = self.prompt_for_file_path()
            
            while True:
                try:
                    self.curr_saver().save(data, file_path, fields)
                    self.file_locations.append(file_path)
                    break
                except TypeError:
                    print(f'No data to save')
                except Exception as e:
                    print(f"An error occurred while saving the data: {e}. Please try again.")
                    file_path = self.prompt_for_file_path()

                
                
            print(f'Website scraped: {self.curr_scraper().index_url}\nData types extracted: {self.data_types[-1]}\nNumber of records collected: {len(data)}\nData saved to {file_path}.')
        print(f"Scraping session is over! {len(self.sites_scraped_urls)} URLs were scraped!\nData types extracted: {self.data_types}\nThe sites scraped: {self.sites_scraped_urls}\nThe information was saved to: {self.file_locations}. ")

if __name__ == '__main__':
    sesh = ScrapingSession()
    sesh.start()