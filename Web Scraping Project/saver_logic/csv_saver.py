from .base_saver import Saver
import csv
from scraping_logic.basketball_scraper import NBAScraper
class CSVSaver(Saver):
    '''
    A class for saving data to a CSV file. Inherits from the base Saver class.
    '''
    @staticmethod
    def _transform(data, fields=None):
        """
        Args:
          data (list): data to be transformed into suitable format
          fields (list): data to be used as a header
        Trasforms the data to be ready for insertion into a csv.file. If data is a list of strings
        each string is put into a list of its own.
        Output:
         data (list of strings)
        """
        if not isinstance(data[0], list):
            data = [[row] for row in data]
            return data
        return data

    def save(self, data, file_path, fields=None):
        """
        Args:
          data (list of lists) or (list of strings): Data to be saved
          file_path (string): Location on where to save the data
          fields (list of strings): Header information about data
        Saves the data to a given file path and displays info if the saving was successful.
        """
        mode = self._prompt_for_mode()
        records = len(data)
        if self.overwrite_confirmation(file_path=file_path, mode = mode):
            with open(file_path, mode, encoding= 'utf-8', newline='') as file:
                data = self._transform(data)
                csv_writer = csv.writer(file)
                if isinstance(fields, str):
                    fields = [fields]
                csv_writer.writerow(fields)
                csv_writer.writerows(data)
        print(f"Data successfuly saved to {file_path}. {records} rows were added. ")

if __name__ == '__main__':

    scraper = NBAScraper
    with scraper() as scr:
        data = scr.fetch_current_team_roster('LAL')
        saver = CSVSaver()
        
