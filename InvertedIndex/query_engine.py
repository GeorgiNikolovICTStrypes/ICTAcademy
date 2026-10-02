"""
This is a query_engine class to query the inverted_index
"""

from inverted_index import InvertedIndex
from tokenizer import Tokenizer
class QueryEngine:
    def __init__(self, index):
        self.index = index

    def or_query(self, *words):
        """
        Args:
          words (iterable of strings): Words to be queried
        Executes an AND query on an InverseIndex object using all words in words
        Output:
          (set) of all ids that satistfy the query
        """
        ans = set()
        for word in words:
            ans.update(self.index.lookup_word(word))
        return ans

    def and_query(self,*words):
        """
        Args:
          words (iterable of strings): Words to be queried
        Executes an AND query on an InverseIndex object using all words in words
        Output:
          (set) of all ids that satistfy the query
        """
        ans = self.index.get_file_ids()
        for word in words:
            ans = ans.intersection(self.index.lookup_word(word))
        return ans

    def not_query(self, *words):
        """
        Args:
          words (iterable of strings): Words to be queried
        Executes a NOT query on an InverseIndex object using word
        Output:
          (set) of all ids that satistfy the query
        """
        containing_words = set()
        for word in words:
            containing_words.update(self.index.lookup_word(word))
        
        all_ids = self.index.get_file_ids()
        return all_ids-containing_words

tokenizer = Tokenizer()
inverted_index = InvertedIndex(tokenizer=tokenizer)
inverted_index.add_file('C:\\Users\\GeorgiNikolov\\Desktop\\Academy\\Python Repo\\ICTAcademy\\File Compressor\\test\\foulder_test.txt')
inverted_index.add_file('C:\\Users\\GeorgiNikolov\\Desktop\\Academy\\Python Repo\\ICTAcademy\\File Compressor\\test\\test_sub_dir\\subdir_test.txt')
inverted_index.print_index()
qe = QueryEngine(inverted_index)
print(qe.not_query('kopur', 'magdanoz'))