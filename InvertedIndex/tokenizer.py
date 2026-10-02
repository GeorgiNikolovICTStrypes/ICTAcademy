"""
Tokenizer class
  Removes punctuation and stopwords (words from this list:)
"""

class Tokenizer:
    def __init__(self, stop_words = None):
        """
        Args:
          stop_words (set of string): A list of words that get ignored during tokenization
        """
        if stop_words is not None:
            self.stop_words = stop_words
        else:
            self.stop_words = {'is', 'a', 'in', 'on', 'the', 'but', 'at', 'was', 'were','as', 'to', 'for', 'of', 'with', 'and', 'or'}
    
    def show_stop_words(self):
        """
        Shows the list of stopwords
        """
        print(self.stop_words)

    def add_stop_word(self, word):
        """
        Args:
          word (string): word to be added
        Adds the word to the stop list set
        """
        if isinstance(word, str):
            self.stop_words.add(word)

    def remove_stop_word(self, word):
        """
        Args:
          word (string): word to be removed
        Removes the word to the stop list set
        """
        self.stop_words.discard(word)

    @staticmethod
    def _remove_punctuation(text):
        """
        Args:
          text (string): text to replace the non-alphanumeric characters in
        Replaces all non-alphanumeric characters with a whitespace
        """
        ans = ""
        for letter in text:
            if not letter.isalnum():
                ans+=" "
            else:
                ans += letter
        return ans

    def tokenize_text(self, text):
        """
        Args:
          text (string): Text to tokenize
        Tokenize passed text by converting it to lower and removing stopwords and punctuation
        """
        clean = self._remove_punctuation(text).lower()
        tokens = clean.split()
        return [token for token in tokens if token not in self.stop_words]

    def tokenize_file(self, filepath):
        """
        Args:
          filepath (string): Path to a file (.txt)
        Tokenizes the text passed in the file by converting it to lower and removing all stopwords and punctiation
        """
        text = ""
        with open(filepath, 'r',encoding='utf-8') as f:
            text = f.read()
        return self.tokenize_text(text)

if __name__ == '__main__':
    text = "The, quick half-wit {fox{()..}}, jumped over. the Fence/ of pig's\\"
    tokenizer = Tokenizer()
    print(tokenizer.tokenize_file('C:\\Users\\GeorgiNikolov\\Desktop\\Academy\\Python Repo\\ICTAcademy\\File Compressor\\test\\foulder_test.txt'))
    print(tokenizer.tokenize_text(text))