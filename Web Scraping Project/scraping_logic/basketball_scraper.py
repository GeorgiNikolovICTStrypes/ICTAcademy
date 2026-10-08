'''
A webscraper for the website: basketball-reference.com
'''
from .base_scraper import Scraper
from datetime import datetime

class NBAScraper(Scraper):
    def __init__(self, delay = 5):
        """
        Args:
          delay (int): Delay in seconds between each request
        Initialize a NBAScraper object. Delay is set to atleast 5 due to basketball-reference.com requirements
        """
        nba_age = datetime.now().year - 1947
        self.index_url = 'https://www.basketball-reference.com/'
        self._champions = [None for _ in range(nba_age)]
        self.delay = min(5,delay)
        self.abbreviations = []

    def fetch_champions_from_to(self, from_year = None, to_year = None):
        """
        Args:
          from_year (int): lower bound for year range
          to_year (int): upper bound for year range
        Returns the champions of the NBA in the range [from_year, to_year]. Saves them to an internal array for faster future executions
        Output:
          (list of strings): Team names of champions of the nba
        """
        current_year = datetime.now().year
        
        while from_year is None or not (1946 <= from_year <= current_year):
            try:
                from_year = int(input("Please input a valid from year. The NBA started in 1946. "))
            except ValueError, TypeError:
                 print("Please enter a valid year! ")
                 continue
                            
        
        while to_year is None or not (1946 <= to_year <= current_year):
            try:
                to_year = int(input("Please input a valid to year. We are currently 2026. "))
            except ValueError, TypeError:
                print("Please enter a valid year. ")
                continue

        if to_year<from_year:
            temp = to_year
            to_year = from_year
            from_year = temp

        print(f"Fetching champions from {from_year} to {to_year}. ")

        from_year = current_year - from_year
        to_year = current_year - to_year
        
        if self._champions[0] != None:
            return self._champions[to_year:from_year+1]
        
        start_url = self.index_url+ '/leagues'
        data = self.fetch_data(start_url)
        champions = data.select('td[data-stat="champion"]>a')
        champions = [x.text for x in champions]
        self._champions = champions
        return self._champions[to_year:from_year+1]
    
    def fetch_current_team_roster(self, team = None):
        """
        Args:
          Team (string): Abbreviation of an NBA team.
        Returns the team roster for the current year.
        Output:
          (list of strings): Names of players on the current roster.
        """
        if self.abbreviations == []:
            self.fetch_teams_with_abbreviations()

        while team is None or team not in self.abbreviations:
            team = input("Please enter a valid abbreviation. ")
        curr_url = self.index_url+ f'teams/{team}/{datetime.now().year+1}.html'
        data = self.fetch_data(curr_url)
      
        table = data.find('table', {"id":"roster"})
        player_tags = table.select('td[data-stat="player"]')
        players =  [x.text.replace('\xa0', ' ') for x in player_tags]
        return players

    def fetch_teams_with_abbreviations(self):
        """
        Fetches all full team names and their abbreviations
        Output:
          (list of lists) wherea each string is full_name - abbreviation for each team
        """
        curr_url = self.index_url+'teams'
        data = self.fetch_data(curr_url)
        abb_tags = data.select('th>a')
        team_names = [x.text for x in abb_tags]
       
        abbreviations = [x['href'][7:10] for x in abb_tags]
        self.abbreviations = abbreviations
        
        return [f'{team} - {abb}' for team, abb in zip(team_names, abbreviations)]
        
if __name__ == '__main__':
    with NBAScraper() as scraper:
        print(scraper.fetch_current_team_roster())