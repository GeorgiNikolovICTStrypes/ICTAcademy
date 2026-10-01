from HuffmanTree.tree import HuffmanTree
import os

def compress_file(file_path, destination):
    """
    Args:
      file_path(string): A file path to the file you want to compress
      destination(string): The path to the directory where you want to store it!
    Compresses a file in file_path using huffmans algorithm and writes it to destination
    """
    data = ""
    with open(file_path, 'r') as f:
        for line in f.read():
            data += line

    huff_tree = HuffmanTree(data = data)
    binary_data = huff_tree.convert_to_huffman_code()
    body, body_padding = huff_tree._bitstring_to_bytestring(binary_data)
    header = huff_tree.serialize()
    header_len = len(header).to_bytes(2, byteorder='big')
    
    padding_byte = body_padding.to_bytes(1, byteorder='big')
    compressed_data = header_len + header + padding_byte + body
    
    name_of_file = file_path.split('\\')[-1]
    parts = name_of_file.partition('.')
    new_name = parts[0]+parts[1] + 'huff'
    output_path = os.path.join(destination, new_name)
    if _confirm_overwrite(output_path):
        with open(output_path, 'wb') as f:
            f.write(compressed_data)

def decompress_file(file_path, destination):
    """
    Args:
      file_path (string): File path to the file we want to decompress
      destination (string): File path to the directory we want the file to be saved to + its name 
      example: /foulder/file.txt
    Decompresses a file from filepath and saves it to destination
    """
    with open(file_path, 'rb') as file:
        file_bytes = file.read()
    print(file_bytes)
    header_len = int.from_bytes(file_bytes[0:2], byteorder='big')
    print(header_len)
    header_bytes = file_bytes[2:2+header_len]
    padding_count = file_bytes[2+header_len]
    body = file_bytes[2+header_len+1:]
    tree = HuffmanTree.deserialize(header_bytes)
    body_bit_string = tree._bytestring_to_bitstring(body)

    if padding_count>0:
        body_bit_string = body_bit_string[:-padding_count]

    original_text = tree.convert_to_string(body_bit_string)
    if _confirm_overwrite(destination):
        with open(destination, 'w') as file:
            file.write(original_text)

def _confirm_overwrite(output_path):
    """
    Args:
      output_path (string): output_path to be checked if it exists
    Checks if this file already exists and prompts the user if they want to overwrite it
    """
    if os.path.exists(output_path):
        response = input(f"Warning! File {output_path} already exists! Do you wish to overwrite it [y/n]? ")
        return response in ['y', 'YES']
    return True     
# compress_file('C:\\Users\\GeorgiNikolov\\Desktop\\Academy\\Python Repo\\ICTAcademy\\File Compressor\\test.txt', "")
decompress_file('C:\\Users\\GeorgiNikolov\\Desktop\\Academy\\Python Repo\\ICTAcademy\\File Compressor\\test.huff', "test2.txt")