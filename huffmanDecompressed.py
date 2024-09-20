from PIL import Image

def compress_image(image, quality=90):

  compressed_image = Image.new('L', image.size)
  image.save(compressed_image, format='PNG', quality=quality)
  return compressed_image

def decompress_image(image):

  decompressed_image = Image.open(image)
  return decompressed_image

if __name__ == '__main__':

  image = Image.open(r'G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Decompression\img2.png')

  compressed_image = compress_image(image)

  compressed_image.save(r'G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Decompression\compressed.png')

  decompressed_image = decompress_image(r'G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Decompression\compressed.png')

  decompressed_image.save(r'G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\Decompression\decompressed.png')
