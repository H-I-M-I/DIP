from PIL import Image
import os

def compress_lzw(data):
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    result = []

    current_code_length = 9  
    code_limit = 1 << current_code_length
    current_code = bytes([data[0]])

    for i in range(1, len(data)):
        current_code += bytes([data[i]])

        if current_code not in dictionary:
            dictionary[current_code] = next_code
            next_code += 1
            result.append(dictionary[current_code[:-1]])

            if next_code >= code_limit and current_code_length < 12:
                current_code_length += 1
                code_limit = 1 << current_code_length

            current_code = bytes([data[i]])

    result.append(dictionary[current_code])

    return result, current_code_length

def decompress_lzw(compressed_data, code_length):
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    result = []

    current_code = compressed_data[0]
    result.append(dictionary[current_code])

    for code in compressed_data[1:]:
        if code not in dictionary:
            entry = dictionary[current_code] + bytes([dictionary[current_code][0]])
        else:
            entry = dictionary[code]

        result.append(entry)

        dictionary[next_code] = dictionary[current_code] + bytes([entry[0]])
        next_code += 1

        if next_code >= 1 << code_length and code_length < 12:
            code_length += 1

        current_code = code

    return b"".join(result)

def gif_compress_decompress(input_path, compressed_output_path, decompressed_output_path):
    img = Image.open(input_path)

    pixel_data = img.tobytes()

    compressed_data, code_length = compress_lzw(pixel_data)

    with open(compressed_output_path, "wb") as compressed_file:
        for code in compressed_data:
            compressed_file.write(code.to_bytes(2, byteorder='big'))

    decompressed_data = decompress_lzw(compressed_data, code_length)

    decompressed_img = Image.frombytes(img.mode, img.size, decompressed_data)

    decompressed_img.save(decompressed_output_path)

if __name__ == "__main__":
    input_path = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\LZW\img1.jpg"
    compressed_output_path = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\LZW\compressed.jpg"
    decompressed_output_path = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\LZW\decompressed.jpg"

    gif_compress_decompress(input_path, compressed_output_path, decompressed_output_path)
    print("\nCompression and decompression complete.")

    original_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(compressed_output_path)

    percentage_saved = ((compressed_size - original_size) / compressed_size) * 100

    compression_ratio =  compressed_size / original_size 

    # print(f"Original Size = {original_size} bytes")
    # print(f"Compressed Size = {compressed_size} bytes")
    print(f"Percentage Saved = {percentage_saved:.2f}%")
    print(f"Compression Ratio = 1 : {compression_ratio:.2f}\n")



















    # A compression ratio of 9:1 means that the compressed data is one-ninth the size of the original data.
    # GIF -->	Lossless  -->	2:1 to 10:1
    # GIF images with a lot of repeated colors are typically more compressible than GIF images with a lot of unique colors.
    # Use a smaller number of colors in your GIF image. This will make the image more compressible.