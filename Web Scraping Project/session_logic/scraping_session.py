'''
A webscrape session manager class. This class handles the user input and output, and manages the scraping session.
'''
from .menu_exception import InvalidMenuOption
from scraping_logic.basketball_scraper import NBAScraper
from scraping_logic.quotes_scraper import QuoteScraper
from scraping_logic.book_scraper import BookScraper
from saver_logic.txt_saver import TxtSaver
from saver_logic.csv_saver import CSVSaver
from saver_logic.json_saver import JSONSaver
import os

class ScrapingSession:

    def __init__(self):
        self.file_locations = []
        self.data_types = []
        self.sites_scraped_urls = []
        self.curr_scraper = None
        self.curr_saver = None

    def prompt_for_site(self):
        print('What would u like to scrape?')
        print('\n1. Quotes\n2. Basketball information\n3. Book information\n4. Exit')
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
                return -1
            else:
                raise InvalidMenuOption
        except InvalidMenuOption:
            print("Please enter a valid option from the list! ")
            return self.prompt_for_site()

    def prompt_for_function_quotes(self):
        print('What information would u like to scrape about quotes?')
        print('1. Authors\n2. Popular Tags\n3. Quotes on page 1-10\n4. Exit\n5. Test faulty url')
        choice = 0
        while True:
            try:
                choice = int(input("Choose an option from the list (number). "))
                break
            except TypeError:
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
                    return -1
                elif choice == 5:
                    self.data_types.append('Faulty')
                    data = scraper.test_faulty()
                    return -1
                else:
                    raise InvalidMenuOption
            except InvalidMenuOption:
                print("Please enter a valid option from the list! ")
                return self.prompt_for_function_quotes()
            
    def prompt_for_function_books(self):
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
                    return -1
                else:
                    raise InvalidMenuOption
            except InvalidMenuOption:
                print("Please enter a valid option from the list! ")
                return self.prompt_for_function_books()
            

    def prompt_for_function_basketball(self):
        print('What information would u like to scrape about the NBA?')
        print("1. Champions from year to year\n2. Get a team's roster\n3. Get all NBA teams and their abbreviations\n4. Exit")
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
                    return -1

                else:
                    raise InvalidMenuOption
                
            except InvalidMenuOption:
                print("Please enter a valid option from the list! ")
                return self.prompt_for_function_basketball()
            
    def prompt_for_save(self):
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
        self.file_locations.append(path)
        return path

    def start(self):
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
                
            data, fields = data_fields
            self.prompt_for_save()
            file_path = self.prompt_for_file_path()
            self.curr_saver().save(data, file_path, fields)
        print(f"Scraping session is over! {len(self.sites_scraped_urls)} URLs were scraped!\nThe sites scraped are: {self.sites_scraped_urls}\nThe information was saved to: {self.file_locations}. ")

if __name__ == '__main__':
    sesh = ScrapingSession()
    sesh.start()