from .base_saver import Saver
from scraping_logic.book_scraper import BookScraper

class TxtSaver(Saver):
    @staticmethod
    def _transform(data, fields = None):
        """
        Args:
          data (list): data to be transformed into suitable format
          fields (list): fields to be used as header (not in TxtSaver._transform)
        Trasforms the data to be ready for insertion into a txt.file. If data is a list of lists it concatenates
        The rows of data into strings.
        Output:
         data (list of strings)
        """
        if isinstance(data[0], (list, tuple)):
           return [" ".join(x) for x in data]
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
        data = self._transform(data)
        
        if self.overwrite_confirmation(file_path=file_path):
            with open(file=file_path, mode = mode, encoding='utf-8') as file:
                if fields is not None and isinstance(fields, (list, tuple)):
                    fields = " ".join(fields)
                   
                file.write(fields + '\n')
                
                file.writelines([x + '\n' for x in data])
            print(f"Data successfuly saved to {file_path}. {records} record were added. ")

if __name__ == '__main__':
    scraper = BookScraper
    with scraper() as scr:
        data = scr.fetch_info_for_books_with_rating(6)

        saver = TxtSaver()
        saver.save(data, 'C:\\Users\\GeorgiNikolov\\Desktop\\Academy\\Python Repo\\ICTAcademy\\Web Scraping Project\\test_save.txt', ['categories', 'ppop', 'waewaea'])

