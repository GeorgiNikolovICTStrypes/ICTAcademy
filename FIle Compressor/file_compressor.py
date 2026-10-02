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
    # Open a file and save the data to a string
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.read():
            data += line
    # Create an instance of the HuffmanTree Class
    huff_tree = HuffmanTree(data = data)
    # Convert the data using the huffman codes for each character to a binary string
    binary_data = huff_tree.convert_to_huffman_code()
    # convert the binary data to a bytestring and return the num of bits needed for padding (used when decompressed)
    body, body_padding = huff_tree.bitstring_to_bytestring(binary_data)
    # header = serialization of the tree
    header = huff_tree.serializeutf()
    # as the header len could get quite large we encode it into 2 bytes.
    header_len = len(header).to_bytes(2, byteorder='big')
    # this padding byte signals how many padding bits we used
    # since its a number between 0 and 7 we can encode it in 1 byte
    padding_byte = body_padding.to_bytes(1, byteorder='big')
    # glue it all together
    compressed_data = header_len + header + padding_byte + body

    # get the name of the file and add .huff extension
    name_of_file = file_path.split('\\')[-1]
    new_name = name_of_file + '.huff'

    # create path to destination and open a file in write binary and write the data to it
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
    # gets the file_bytes from the given file_path
    with open(file_path, 'rb') as file:
        file_bytes = file.read()
    # the structure is 2 bytes for header_len, then the header, then the padding_count 1 byte, then the body
    header_len = int.from_bytes(file_bytes[0:2], byteorder='big')
    
    header_bytes = file_bytes[2:2+header_len]
    padding_count = file_bytes[2+header_len]
    body = file_bytes[2+header_len+1:]
    # deserializes the header to recreate a huffmantree to use for decoding
    tree = HuffmanTree.deserializeutf(header_bytes)
    # converts the body to bits and remove the padding bits
    body_bit_string = tree.bytestring_to_bitstring(body)

    if padding_count>0:
        body_bit_string = body_bit_string[:-padding_count]
    # original text is converted to string using the huffman codes and the binary body
    original_text = tree.convert_to_string(body_bit_string)
    # ask the user if they want ot overwrite and write to it using utf-8 encoding to the destination files
    if _confirm_overwrite(destination):
        with open(destination, 'w', encoding='utf-8') as file:
            file.write(original_text)

def compress_foulder(source, target = None):
    """
    Args:
      source (string): source filepath
      target (string): target filepath, default = None
    Compresses a fouder to an archived one by mirroring the source dir structure and compresses the files in the dirs
    Outputs: None
    """
    if target is None: # if the target is not passed a new one is created with the same name + _archived suffix
        target = f"{source}_archived"

    for root, _ , files in os.walk(source): # for each root dir, subdirs and files
        rel_path = os.path.relpath(root, source) # caulcuate the rel path from root dir to source
        # A new dir is created for each subdir in source
        if rel_path == ".": # root == source <-> rel_path == "."
            target_directory = target
        else:
            target_directory = os.path.join(target,rel_path)  

        os.makedirs(target_directory, exist_ok=True)
        print(target_directory)
        # For every file
        for file in files:
            # The path is from curr dir + file
            source_file_path = os.path.join(root, file)
            # The new file is named file.huff and the dir is target_dir. we compress it and send it there.
            
            compress_file(source_file_path, target_directory)


def decompress_foulder(source, target = None):
    """
    Args:
      source (string): filepath to a foulder to unzip
      target (string): name of the new foulder.
    Creates a foulder with the same structure. Files from source are decompressed and put into target location
    Outputs: None
    """
    if target is None:
        # If no name is passed
        if source.endswith("archived"):
            target = source[:-len("archived")]
        # target  = sourcename - (archived if there is) + restored
        target+='restored'
    # for each directory, _, files when walking from source downwards
    for root, _, files in os.walk(source):
        # The relative path from the curr_dir to start
        rel_path = os.path.relpath(root, source)
        # if we are in the same dir current_target_directory = target
        if rel_path == ".":
            target_dir = target
        else:
            # current_target_directory = target + rel_path so the path to get from source to target + relative path.
            # To mirror the Source structure
            # Target = Fouder
            # relpath = path to the subfoulder.
            target_dir = os.path.join(target, rel_path)
        # create the folder return true if it exists
        os.makedirs(target_dir, exist_ok= True)

        for file in files:
            # Path to source = root directory + file
            source_file_path = os.path.join(root, file)
            # remove the .huff suffix to reveal the true file extension
            target_file_name = file[:-5]
            # the path is equal to current_target_Dir + target_file_name
            target_file_path = os.path.join(target_dir, target_file_name)
            # call decompress_file on source_file_path, target_file_path
            decompress_file(source_file_path, target_file_path)   

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

