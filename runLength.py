from PIL import Image
import itertools

def rle_encode(image):
    data = list(image.getdata())
    encoded_data = []
    
    for value, group in itertools.groupby(data):
        run_length = len(list(group))
        encoded_data.append((value, run_length))
    
    return encoded_data

def rle_decode(encoded_data, image_size):
    decoded_data = []
    
    for value, run_length in encoded_data:
        decoded_data.extend([value] * run_length)
    
    decoded_image = Image.new('L', image_size)
    decoded_image.putdata(decoded_data)
    
    return decoded_image

image_path = r'G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Image\Screenshot (7).png'
image = Image.open(image_path)

encoded_data = rle_encode(image)

compressed_size_bits = len(encoded_data) * 8
original_size_bits = image.size[0] * image.size[1] * 16

average_len_bits = compressed_size_bits / original_size_bits

percentage_saved_bits = 100 * (original_size_bits - compressed_size_bits) / original_size_bits

# input_array - compressed_image_array = r.m.s (rms difference of file_size) (compressed and decompressed)
# to check if the image compression is okay or not. if 0, then okay.

print(f'\nAverage code length: {average_len_bits:.2f} bits/pixel')
print(f'Percentage saved: {percentage_saved_bits:.2f}%\n')
