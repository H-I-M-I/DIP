import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def create_log_transform(inputPath, outputPath):

    input_image = Image.open(inputPath)
    gray_image = input_image.convert('L')
    a = np.array(gray_image)

    height, width = a.shape
    temp = np.zeros_like(a)
    
    c = 1
    L = 255
    for y in range(height):
        for x in range(width):

            r = a[y, x]
            # s = L * np.log(1 + r) / np.log(1 + L)
            s = c * np.log(1 + r)
            temp[y, x] = s

    pixels = temp.astype(np.uint8)

    output_image = Image.fromarray(pixels)
    output_image.save(outputPath)

    
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(a, cmap='gray')
    plt.title('Input Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(pixels, cmap='gray')
    plt.title('Log Transformed Image')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    inputPath = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Histogram\input_image\image1.jpeg"  
    outputPath = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Histogram\output_image\image1.jpeg"

    create_log_transform(inputPath, outputPath)
