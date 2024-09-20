import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def zoom_bilinear(image_path, scale_factor):
    img = Image.open(image_path)
    old_width, old_height = img.size

    new_width = int(old_width * scale_factor)
    new_height = int(old_height * scale_factor)

    new_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    for y in range(new_height):
        for x in range(new_width):

            old_x = x / scale_factor
            old_y = y / scale_factor

            # Get the surrounding pixel coordinates
            x1 = int(old_x)
            y1 = int(old_y)
            x2 = min(x1 + 1, old_width - 1)
            y2 = min(y1 + 1, old_height - 1)

            # Calculate the fractional parts for bilinear interpolation
            alpha = old_x - x1
            beta = old_y - y1

            # Perform bilinear interpolation
            top_left = img.getpixel((x1, y1))
            top_right = img.getpixel((x2, y1))
            bottom_left = img.getpixel((x1, y2))
            bottom_right = img.getpixel((x2, y2))

            new_pixel = tuple(int((1 - alpha) * (1 - beta) * c1 +
                                  alpha * (1 - beta) * c2 +
                                  (1 - alpha) * beta * c3 +
                                  alpha * beta * c4) for c1, c2, c3, c4 in zip(top_left, top_right, bottom_left, bottom_right))

            new_img[y, x] = new_pixel

    new_image = Image.fromarray(new_img)
    return img, new_image

def main():
    input_image_path = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Zooming\input_image\image1.jpg"
    zoom_scale = float(input("Enter the zoom scale factor: "))

    original_img, zoomed_image = zoom_bilinear(input_image_path, zoom_scale)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[1].imshow(original_img)
    axes[1].set_title(f"Zoomed Image (Zoom Factor: {zoom_scale})")
    axes[1].axis("off")

    zoomed_width = int(zoomed_image.width * zoom_scale)
    zoomed_height = int(zoomed_image.height * zoom_scale)
    axes[0].imshow(zoomed_image)
    axes[0].set_title("Original Image")
    axes[0].axis("off")
    axes[0].set_xlim([0, zoomed_width])
    axes[0].set_ylim([zoomed_height, 0])

    plt.tight_layout()
    plt.show()

    output_image_path = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Zooming\output_image\image1.jpg"
    zoomed_image.save(output_image_path)

if __name__ == "__main__":
    main()
