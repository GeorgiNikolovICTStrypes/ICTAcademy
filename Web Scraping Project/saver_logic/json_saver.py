
from .base_saver import Saver
import json
from scraping_logic.quotes_scraper import QuoteScraper

class JSONSaver(Saver):
    @staticmethod
    def _transform(data, fields=None):
        """
        Args:
          data (list): data to be transformed into suitable format
          fields (list): data to be used as a header
        Trasforms the data to be ready for insertion into a csv.file. If data is a list of lists
        each list is converted to a dict with the structure field: feature for field in fields and feature in a row of data.
        Output:
         data (list of strings)
        """
        if isinstance(data[0], (list, tuple)):
            return [dict(zip(fields, row)) for row in data]
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
        if self.overwrite_confirmation(file_path):
            data = self._transform(data, fields)
            with open(file_path, mode, encoding= 'utf-8') as file:
                json.dump(data, file, indent = 2)
        print(f"Data successfuly saved to {file_path}. {records} records were added. ")

if __name__  == '__main__':
   
    scraper2 = QuoteScraper
    with scraper2() as scr:
        data = scr.fetch_authors()
        saver = JSONSaver()
        