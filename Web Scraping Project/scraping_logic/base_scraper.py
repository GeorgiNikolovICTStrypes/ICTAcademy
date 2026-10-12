'''
Base scraper class
'''

import requests
import bs4

class Scraper:
    '''
    Base class for all scrapers. Transforms the data fetched from a url into a soup object.
    Makes the scraper objects context managers to ensure that the session is closed after use.
    '''
    def __init__(self):
        '''
        Initialize an empty Scraper Object.
        '''
        self.index_url = None
        self.session = None

    def connect(self):
        """
        Starts a requests session that is used between different get calls.
        """
        self.session = requests.sessions.Session()

    def disconnect(self):
        """
        Disconnects from the current sesison
        """
        if self.session: 
            self.session.close()

    def _fetch_data(self, url):
        """
        Args:
          url (string): A string containing the url to scrape from
        Sends a get request using the connection and handles errors.
        Output:
          Soup object containing the data scraped from url
        """
        try:
           response =  self.session.get(url)
           response.encoding = 'utf-8'
           response.raise_for_status()
        except requests.RequestException as e:
            print(f'Failed to fetch data from {url}: {e}')
            return None
        return bs4.BeautifulSoup(response.text, 'lxml')

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.disconnect()