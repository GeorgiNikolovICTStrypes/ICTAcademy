'''
A webscraper for the website: quotes.toscrape.com
'''
from base_scraper import Scraper

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
            authors_on_page = set([x.text for x in data.select('.author')])
            all_authors.update(authors_on_page)

            next_button = data.select_one('li.next > a')
            if next_button:
                curr_url = self.index_url + next_button['href']
            else:
                curr_url = None
        return list(all_authors)

    def fetch_top_n_tags(self,n):
        """
        Args:
          n (int) returns top n integers
        Returns top n tags in the site. Saves results for future queries.
        Output:
          (list of strings) list containing tags
        """
        if self._tags:
            return self._tags[:n]
        data = self.fetch_data(self.index_url)
        tags = [x.text for x in data.select('a.tag')]
        self._tags = tags
        return tags[:n]

    def fetch_quotes_for_page(self, page):
        """
        Args:
          page (int): page to scrape quotes from (in the range 1-10)
        Returns all quotes from a given page. Saves results for future queries.
        Output:
          (list of strings) list containing quotes from page
        """
        while not (1<=page<=10):
            try:
               page =  int(input("please enter a valid page number in the range from 1-10: "))
            except:
                continue

        if self._quotes[page]:
            return self._quotes[page]
        
        url = self.index_url + f"page/{page}"
        data = self.fetch_data(url)
        quotes = [x.text for x in data.select('div.quote > span.text')]
        self._quotes[page] = quotes
        return quotes
        
if __name__ == '__main__':
    with QuoteScraper() as scraper:
        print(scraper.fetch_quotes_for_page(100))
