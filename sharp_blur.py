import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('img9.jpg', cv2.IMREAD_GRAYSCALE)

rows, cols = image.shape

# Fourier Transform
f_transform = np.zeros((rows, cols), dtype=np.complex128)
for u in range(rows):
    for v in range(cols):
        sum_val = 0
        for x in range(rows):
            for y in range(cols):
                pixel_value = image[x, y]
                angle = 2 * np.pi * ((u * x / rows) + (v * y / cols))
                sum_val += pixel_value * (np.cos(angle) - 1j * np.sin(angle))
        f_transform[u, v] = sum_val

cutoff_frequency = 20

center_row, center_col = rows // 2, cols // 2

# Apply an ideal low-pass filter for smoothing
ideal_low_pass = np.zeros((rows, cols), dtype=np.float64)
for u in range(rows):
    for v in range(cols):
        distance = np.sqrt((u - center_row) ** 2 + (v - center_col) ** 2)
        if distance <= cutoff_frequency:
            ideal_low_pass[u, v] = 1

# Apply a Gaussian low-pass filter for smoothing
sigma = 2.0
x, y = np.meshgrid(np.linspace(-1, 1, cols), np.linspace(-1, 1, rows))
gaussian_kernel = np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
gaussian_kernel /= np.sum(gaussian_kernel)

# Apply an ideal high-pass filter for sharpening
ideal_high_pass = np.zeros((rows, cols), dtype=np.float64)
for u in range(rows):
    for v in range(cols):
        distance = np.sqrt((u - center_row) ** 2 + (v - center_col) ** 2)
        if distance > cutoff_frequency:
            ideal_high_pass[u, v] = 1

# Convolve the Fourier Transform with the filters
smoothed_f_transform_ideal = f_transform * ideal_low_pass
smoothed_f_transform_gaussian = f_transform * gaussian_kernel
sharpened_f_transform = f_transform * ideal_high_pass

# Inverse Fourier Transform
smoothed_image_ideal = np.zeros((rows, cols), dtype=np.uint8)
smoothed_image_gaussian = np.zeros((rows, cols), dtype=np.uint8)
sharpened_image = np.zeros((rows, cols), dtype=np.uint8)

for x in range(rows):
    for y in range(cols):
        smoothed_sum_ideal = 0
        smoothed_sum_gaussian = 0
        sharpened_sum = 0
        for u in range(rows):
            for v in range(cols):
                angle = 2 * np.pi * ((u * x / rows) + (v * y / cols))
                smoothed_sum_ideal += smoothed_f_transform_ideal[u, v].real * (np.cos(angle) + 1)
                smoothed_sum_gaussian += smoothed_f_transform_gaussian[u, v].real * (np.cos(angle) + 1)
                sharpened_sum += sharpened_f_transform[u, v].real * (np.cos(angle) + 1)
        
        smoothed_image_ideal[x, y] = np.uint8(smoothed_sum_ideal)
        smoothed_image_gaussian[x, y] = np.uint8(smoothed_sum_gaussian)
        sharpened_image[x, y] = np.uint8(sharpened_sum)

# Display all four images in two rows
plt.figure(figsize=(15, 10))

# Original Image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Smoothed Image (Ideal LPF)
plt.subplot(2, 2, 2)
plt.imshow(smoothed_image_ideal, cmap='gray')
plt.title('Smoothed Image (Ideal LPF)')
plt.axis('off')

plt.tight_layout()
plt.show()
