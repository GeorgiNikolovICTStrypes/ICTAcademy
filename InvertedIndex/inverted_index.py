"""
Class implementing the inverted index data structure
"""

from tokenizer import Tokenizer
from collections import defaultdict

class InvertedIndex:

    def __init__(self, tokenizer, files = None):
        """
        Args:
          tokenizer (Tokenizer): Tokenizer to use to tokenize the files
          files (list of strings): List of filepaths
        Initializes an InvertedIndex object with passed tokenizer
        If files are passed it filles self.index otherwise its empty
        """
        self.index = defaultdict(set)
        self.tokenizer = tokenizer
        self.documents = {}
        self._id_counter = 0
        if files is not None:
            for file in files:
                self.add_file(file_path=file)

    def add_file(self, file_path):
        """
        Args:
          file_path (string): A file path
        Add document to InvertedIndex instance
        """
        self.documents[self._id_counter] = file_path
        tokens = self.tokenizer.tokenize_file(file_path)
        for token in tokens:
            self.index[token].add(self._id_counter)
        self._id_counter +=1
        
    def lookup_word(self, word):
        """
        Args:
          word (string): word to lookup
        Using the index it first converts word to correct format and then looks up which files contain it.
        If word is in the format word1_g_word2 where _g_ is some non alphanumeric character only the ids of the documents where
        word1 is found will be returned.
        Returns:
        A set of all documents where word is found
        """
        clean_word = self.tokenizer.tokenize_text(word)
        if not clean_word:
            return set()
        return self.index.get(clean_word[0], set())

    def print_index(self):
        """
        Prints the index of the InvertedIndex object
        """
        print(self.index.items())

    def get_file_ids(self):
        """
        Returns the id of all documents in the instance
        Output:
          (set) of all ids of documents in the InvertedIndex instance
        """
        return set(self.documents.keys())

    def get_name_from_file_ids(self, file_ids):
        """
        Returns the file paths to all documents given file_ids
        Output:
          (set) a set of filenames
        """
        ans = set()
        for file_id in file_ids:
            ans.add(self.documents[file_id])
        return ans


if __name__ == '__main__':
    tokenizer = Tokenizer()
    inverted_index = InvertedIndex(tokenizer=tokenizer)
    inverted_index.add_file('C:\\Users\\GeorgiNikolov\\Desktop\\Academy\\Python Repo\\ICTAcademy\\File Compressor\\test\\foulder_test.txt')
    inverted_index.add_file('C:\\Users\\GeorgiNikolov\\Desktop\\Academy\\Python Repo\\ICTAcademy\\File Compressor\\test\\foulder_test.txt')
    print(inverted_index.lookup_word('the'))
    inverted_index.print_index()
    print(inverted_index.get_file_ids())
    print(inverted_index.get_name_from_file_ids([0]))