from PIL import Image

def nearest_neighbor_interpolation(image, new_width, new_height):
    width, height = image.size
    scale_x = width / new_width
    scale_y = height / new_height

    output_image = Image.new("L", (new_width, new_height)) 

    for y in range(new_height):
        for x in range(new_width):
            src_x = int(x * scale_x)
            src_y = int(y * scale_y)

            pixel_color = image.getpixel((src_x, src_y))
            grayscale_intensity = int(0.299 * pixel_color[0] + 0.587 * pixel_color[1] + 0.114 * pixel_color[2])
            output_image.putpixel((x, y), grayscale_intensity)

    return output_image

if __name__ == "__main__":
    input_image = Image.open(r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Shrink_Image\input_image\image1.jpeg") 
    new_width = 200
    new_height = 150

    output_image = nearest_neighbor_interpolation(input_image, new_width, new_height)

    output_image.save(r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Shrink_Image\output_image\image1.jpeg") 
