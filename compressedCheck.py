import math
import os

def calculate_rms_difference(input_image_size, compressed_image_size):
    
    rms_difference = math.sqrt((input_image_size - compressed_image_size)**2)

    return rms_difference

input_image_size = os.path.getsize('input_image.jpg')
compressed_image_size = os.path.getsize('compressed_image.jpg')

rms_difference = calculate_rms_difference(input_image_size, compressed_image_size)

if rms_difference == 0:
    print('The image is properly compressed.')
else:
    print('The image is not properly compressed.')
