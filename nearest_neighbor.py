import numpy as np

import matplotlib.pyplot as plt

from PIL import Image

def zoom_nearest_neighbor(image_path, scale_factor):
    
    img = Image.open(image_path)
    
    old_width, old_height = img.size

    new_width = int(old_width * scale_factor)
    
    new_height = int(old_height * scale_factor)

    new_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    for y in range(new_height):
        
        for x in range(new_width):
            
            old_x = int(x / scale_factor)
            
            old_y = int(y / scale_factor)

            new_img[y, x] = img.getpixel((old_x, old_y))

    
    new_image = Image.fromarray(new_img)
    
    return img, new_image

def main():
    
    input_image_path = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Zooming\input_image\image1.jpg"
    
    zoom_scale = float(input("Enter the zoom scale factor: "))

    original_img, zoomed_image = zoom_nearest_neighbor(input_image_path, zoom_scale)
    
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
