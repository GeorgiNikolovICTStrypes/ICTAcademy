from base_scraper import Scraper
from datetime import datetime
import time
class NBAScraper(Scraper):
    def __init__(self, delay = 5):
        """
        Args:
          delay (int): Delay in seconds between each request
        Initialize a NBAScraper object. Delay is set to atleast 5 due to basketball-reference.com requirements
        """
        self.index_url = 'https://www.basketball-reference.com/'
        self._champions = []
        self.delay = min(5,delay)
        self.abbreviations = []

    def fetch_champions_from_to(self):
        """
        Args:
          from_year (int): lower bound for year range
          to_year (int): upper bound for year range
        Returns the champions of the NBA in the range [from_year, to_year]. Saves them to an internal array for faster future executions
        Output:
          (list of strings): Team names of champions of the nba
        """
        if self._champions != []:
            return self._champions
        start_url = self.index_url+ f'/leagues/NBA_{datetime.now().year}_standings.html'
        while start_url:
            data = self.fetch_data(start_url)
            champion_p = data.find(lambda tag: tag.name == 'p' and tag.find('strong'))
            champion_name = champion_p.find('a')
            self._champions.append(champion_name.text)

            prev = data.select_one('a.button2.prev')
            
            if prev:
                start_url = self.index_url + prev['href']
            else:
                start_url = None
            time.sleep(self.delay)
        return self._champions
    
    def fetch_current_team_roster(self, team):
        """
        Args:
          Team (string): Abbreviation of an NBA team.
        Returns the team roster for the current year.
        Output:
          (list of strings): Names of players on the current roster.
        """
        if self.abbreviations == []:
            self.fetch_teams_with_abbreviations()

        while team not in self.abbreviations:
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
        [[team,abb] for team, abb in zip(team_names, abbreviations)]
        return [f'{team} - {abb}' for team, abb in zip(team_names, abbreviations)]
        
if __name__ == '__main__':
    with NBAScraper() as scraper:
        print(scraper.fetch_teams_with_abbreviations())