"""
Implementation of a node for a huffman tree
"""

class HuffmanNode:
    def __init__(self, character = None, frequency = 0, left = None, right = None):
        """
        Args:
          character (char): Any kind of symbol (could be none for intermediate nodes)
          frequency (int): The occurances of that symbol
          left (HuffmanNode): Left child of the node
          right (HuffmanNode): Right child of the node
        Constuctor for a huffman node creates a node given a character and a frequency and sets the
        children to left and right. If left or right are None it sets the chilren to None respectively
        """
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right

    def __repr__(self):
        return f"HuffmanNode({self.character}, {self.frequency})"
    
    def __lt__(self, other):
        return self.frequency<other.frequency
    