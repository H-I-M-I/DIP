import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(image):
    histogram = np.zeros(256, dtype=int)
    height, width = image.shape

    for y in range(height):
        for x in range(width):
            pixel_value = image[y, x]
            histogram[pixel_value] += 1

    return histogram

def calculate_cumulative_histogram(histogram):
    cumulative_histogram = np.zeros(256, dtype=int)
    cumulative_histogram[0] = histogram[0]

    for i in range(1, 256):
        cumulative_histogram[i] = cumulative_histogram[i - 1] + histogram[i]

    return cumulative_histogram

def histogram_equalization(image, cumulative_histogram):
    height, width = image.shape
    equalized_image = np.zeros_like(image)

    total_pixels = height * width
    normalized_cdf = cumulative_histogram * 255 // total_pixels

    for y in range(height):
        for x in range(width):
            pixel_value = image[y, x]
            equalized_pixel = normalized_cdf[pixel_value]
            equalized_image[y, x] = equalized_pixel

    return equalized_image

if __name__ == "__main__":
    input_path = r"input_image/image1.jpeg"  

    input_image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    histogram = calculate_histogram(input_image)

    cumulative_histogram = calculate_cumulative_histogram(histogram)

    equalized_image = histogram_equalization(input_image, cumulative_histogram)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(input_image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Image')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.plot(histogram, color='b')
    plt.title('Histogram (Original)')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plt.subplot(2, 2, 4)
    equalized_histogram = calculate_histogram(equalized_image)
    plt.plot(equalized_histogram, color='r')
    plt.title('Histogram (Equalized)')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()
