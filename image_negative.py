from PIL import Image
import matplotlib.pyplot as plt

def imageNegative(inputPath, outputPath):

    i_image = Image.open(inputPath)
    width, height = i_image.size
    input_image = i_image.convert("L")

    image_negative = Image.new("L", (width, height))
    pixels = image_negative.load()

    L = 256
    for y in range(height):
        for x in range(width):
            
            r = input_image.getpixel((x, y))
            s = L - 1 - r
            pixels[x, y] = s

    image_negative.save(outputPath)


    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    input_image = Image.open(inputPath)
    output_image = Image.open(outputPath)
    
    axes[0].imshow(input_image, cmap='gray')
    axes[0].set_title('Input Image')
    axes[0].axis('off')

    axes[1].imshow(output_image, cmap='gray')
    axes[1].set_title('Digital Negative Image')
    axes[1].axis('off')
    plt.show()

inputPath = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Histogram\input_image\image1.jpeg"
outputPath = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Histogram\output_image\image1.jpeg"

imageNegative(inputPath, outputPath)



