"""
Class that implements a Huffman Tree
"""
import heapq
from .node import HuffmanNode
class HuffmanTree:

    def __init__(self, root = None, data = None):
        """
        Args:
          root (HuffmanNode): node thats the root of the huffman tree
          data (string): String to generate the huffman tree from
        Creates a Huffman Tree with the passed root and data.
        If data is passed a new tree is generated from that data.
        """
        self.root = root
        self.codes = {}
        self.data = data
        if self.data:
            self.build_tree(self.data)
        self._get_encoding()
        
    def get_frequency_map(self, data):
        """
        Fills a frequency map which counts how many times each symbol occurs
        """
        self.frequency_map = {} # Could use collections Counter but since i needed ot for this method only i did not see fit to import it
        for symbol in data:
            if symbol not in self.frequency_map:
                self.frequency_map[symbol]=0
            self.frequency_map[symbol]+=1   

    def build_tree(self, data):
        """
        Args:
          data (string): Text data to build the tree from.
        Builds a huffman tree from data, uses a heap to recursively merge nodes until there is 1 left
        """
        self.get_frequency_map(data)
        q = []
        for symbol, frequency in self.frequency_map.items():
            heapq.heappush(q,HuffmanNode(character=symbol, frequency=frequency))
        while len(q)>1:
            left = heapq.heappop(q)
            right = heapq.heappop(q)

            heapq.heappush(q,HuffmanNode(frequency= left.frequency + right.frequency, left = left, right = right))

        self.root = heapq.heappop(q)

    def print_tree(self):
        """
        Prints the tree in pre-order traversal
        """
        print(self.root)
        def helper(temp):
            """
            Small helper function to traverse the tree since we dont want to pass the root in print_tree
            """
            if temp == None:
                return
            print(temp)
            helper(temp.left)
            helper(temp.right)
        helper(self.root)

    def _get_encoding(self):
        """
        Traverses the tree and gets the code for each character go left = add '0' to the code go right and add '1' to the code.
        """
        def help_get_encoding(temp, huff_code):
            """
            Helper func to traverse the tree since we dont want the user to pass temp and huff_code
            """
            if temp == None:
                return
            
            if temp.character:
                self.codes[temp.character] = huff_code

            help_get_encoding(temp.left, huff_code+'0')
            help_get_encoding(temp.right, huff_code+'1')

        help_get_encoding(self.root, '')

    def get_codes(self):
        """
        Returns the huffman code for each character in the text.
        Output: codes (dict) - A dictionary with pairs char: code
        """
        self._get_encoding()
        return self.codes

    def serialize(self):
        """
        Converts the tree to a byte string.
        """
        bits = [] # Here we save the encoding of each of the nodes internal nodes are denoted with 0 while the other nodes are denoted with 1 followed by the char code in binary
        def _serialize_helper(temp):
            if temp is None:
                return
            if temp.character is not None:
                bits.append('1') # add the 1
                char_code = ord(temp.character) if isinstance(temp.character, str) else temp.character # get the char code else if its not a string get the character
                bits.append(f"{char_code:08b}") # convert it to binary
                return 
            
            bits.append('0') # this is an internal node just add 0 and traverse left and right
            _serialize_helper(temp.left)
            _serialize_helper(temp.right)

        
        _serialize_helper(self.root)
        bit_string = "".join(b for b in bits)
        byte_string, _ = self._bitstring_to_bytestring(bit_string)
        return byte_string
        
    @classmethod
    def deserialize(cls, bytes):
        """
        Args:
         bytes(bytestring): Bytestring to build the tree from
        Builds a Huffman Tree from a bytestring
        Output:
         HuffmanTree: returns a new instance of the HuffmanTree class with root set to the root of the deserialized tree.
        """
        bitstring = cls._bytestring_to_bitstring(bytes)
        print(bitstring)
        cursor = 0
        def deserialize_helper():
            nonlocal cursor
            # if the cursor is at the end return 
            if cursor>=len(bitstring):
                return None
            bit = bitstring[cursor]
            cursor+=1
            # if we hit 1 we hit a leaf so just grab that to denote its not an internal node
            # grab the next 8 ones to get the char code in binary and convert it to a char. (since its in binary we need to convert it to int with base 2)
            if bit == '1':
                char_bits = bitstring[cursor:cursor+8]
                cursor+=8
                char = chr(int(char_bits,2))
                return HuffmanNode(character= char)
            else:
                # else its equal to 0 then we just create an empty internal node and we traverse left and right
                node =  HuffmanNode()
                node.left = deserialize_helper()
                node.right = deserialize_helper()
                return node
        # we create a new root and return a new instance with the root set to out deserialized helper output
        root = deserialize_helper()
        return cls(root = root)

    def convert_to_huffman_code(self):
        """
        Returns data fully converted to huffman code.
        Output:
          huffman_code (string): each letter from the original data is now replaced with the corresponding huffman code.
        """
        huffman_code = ""
        for letter in self.data:
            huffman_code+=self.codes[letter]
        return huffman_code

    def convert_to_string(self, bit_str):
        """
        Args:
          bit_str (string): binary string
        Decodes the bit_str using the huffman codes from the huffman_tree
        """
        if self.root == None or not bit_str:
            return ""

        decoded_chars = ""
        current_node = self.root

        for bit in bit_str:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right
            
            if current_node.character is not None:
                decoded_chars += current_node.character
                current_node = self.root

            
        return decoded_chars
    
    @staticmethod
    def _bitstring_to_bytestring(bitstring):
        """
        Args:
          bitstring (string): binary string
        Converts bitstring to a bytestring cosisting of bytes

        """
        padding = 8 - (len(bitstring)%8)
        bitstring+='0'*padding

        byte_string = bytes(int(bitstring[i:i+8],2) for i in range(0,len(bitstring),8))
        return byte_string, padding
    @staticmethod
    def _bytestring_to_bitstring(bytestring):
        """
        Args:
          bytestring (string): byte string
        Converts bytestring to a binarystring consisting of 0s and 1s
        """
        bitstring = "".join(f"{b:08b}" for b in bytestring)
        return bitstring
        
if __name__ == '__main__':
    data = "aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff"
    tree = HuffmanTree(data = data)

    print(tree.serialize())
    tree_deserialized = HuffmanTree.deserialize(b'Y\x8b\x1d\x90\xb0\xd8\xac\xa0\x00')

    print(tree.get_codes())
    print(tree.convert_to_huffman_code())
    print(tree_deserialized.get_codes())


    print(tree.convert_to_string('01100100'))
    