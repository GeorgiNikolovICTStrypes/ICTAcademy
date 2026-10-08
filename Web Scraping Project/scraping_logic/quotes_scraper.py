'''
A webscraper for the website: quotes.toscrape.com
'''
from .base_scraper import Scraper

class QuoteScraper(Scraper):
    def __init__(self):
        self.index_url = "https://quotes.toscrape.com/"
        self._authors = None
        self._tags = None
        self._quotes = [None for _ in range(10)]

    def fetch_authors(self):
        """
        Fetches all authors in the site. Saves results for future queries.
        Output:
          (list of strigns) a list of all authors
        """
        if self._authors:
            return self._authors
        curr_url = self.index_url
        all_authors = set()
        while curr_url:
            data = self.fetch_data(curr_url)
            if data is None:
                print("Scraper couldn't reach the page")
                return None
            authors_on_page = set([x.text for x in data.select('.author')])
            all_authors.update(authors_on_page)

            next_button = data.select_one('li.next > a')
            if next_button:
                curr_url = self.index_url + next_button['href']
            else:
                curr_url = None
        return list(all_authors)

    def fetch_top_n_tags(self,n = None):
        """
        Args:
          n (int) returns top n integers
        Returns top n tags in the site. Saves results for future queries.
        Output:
          (list of strings) list containing tags
        """
        if n is None:
            while True:
                try:
                    n = int(input("Please enter the number for which you want to see the top `number` tags. "))
                    if n>0:
                        break
                except:
                    continue
            
        if self._tags:
            return self._tags[:n]
        data = self.fetch_data(self.index_url)
        if data is None:
            print("Scraper couldn't reach the page")
            return None
        tags = [x.text for x in data.select('a.tag')]
        self._tags = tags
        return tags[:n]

    def fetch_quotes_for_page(self, page = None):
        """
        Args:
          page (int): page to scrape quotes from (in the range 1-10)
        Returns all quotes from a given page. Saves results for future queries.
        Output:
          (list of strings) list containing quotes from page
        """
        
        while not isinstance(page,int) or not (1<=page<=10) or page is None:
            try:
               page =  int(input("Please enter a valid page number in the range from 1-10: "))
            except ValueError, TypeError:
                continue

        if self._quotes[page]:
            return self._quotes[page]
        
        url = self.index_url + f"page/{page}"
        data = self.fetch_data(url)
        if data is None:
            print("Scraper couldn't reach the page")
            return None
        quotes = [x.text for x in data.select('div.quote > span.text')]
        self._quotes[page] = quotes
        return quotes
    
    def test_faulty(self):
        """
        Tests the error handling of the scraper. It tries to fetch data from a non-existing page.
        Output:
          (list of strings) list containing quotes from page
        """
        url = self.index_url + "ewqneiqwiewqi;ebwq"
        data = self.fetch_data(url)
        if data is None:
            print("Scraper couldn't reach the page")
            return None
        quotes = [x.text for x in data.select('div.quote > span.text')]
        return quotes
    
if __name__ == '__main__':
    with QuoteScraper() as scraper:
        print(scraper.test_faulty())
