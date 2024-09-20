from PIL import Image
import numpy as np

def calculate_rmse(original_path, decompressed_path):
    original_img = Image.open(original_path)
    decompressed_img = Image.open(decompressed_path)

    original_pixels = np.array(original_img)
    decompressed_pixels = np.array(decompressed_img)

    mse = np.mean((original_pixels - decompressed_pixels) ** 2)
    rmse = np.sqrt(mse)

    return rmse

if __name__ == "__main__":
    original_path = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\LZW\img2.png"
    decompressed_path = r"G:\Academic\3rdYear\3-2_term\Current_term\DIP_lab\LZW\decompressed.png"

    rmse = calculate_rmse(original_path, decompressed_path)
    print(f"\nRMSE: {rmse}\n")
