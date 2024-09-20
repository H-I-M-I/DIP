import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt

def gamma_transform(input_path, output_path, gamma):
    input_image = Image.open(input_path)

    gray_image = input_image.convert('L')
    input_array = np.array(gray_image)

    height, width = input_array.shape
    transformed_array = np.zeros_like(input_array)

    for y in range(height):
        for x in range(width):
            r = input_array[y, x]
            s = 255 * np.power(r / 255.0, gamma)
            transformed_array[y, x] = s

    output_array = transformed_array.astype(np.uint8)

    output_image = Image.fromarray(output_array)
    output_image.save(output_path)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(input_array, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(output_array, cmap='gray')
    plt.title(f'Gamma Transformed Image (Gamma = {gamma})')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    input_path = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Histogram\input_image\image1.jpeg"  
    output_path = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Histogram\output_image\image1.jpeg"
    gamma_value = 1.5 

    gamma_transform(input_path, output_path, gamma_value)
