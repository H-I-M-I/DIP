# DIP
Digital Image Processing 

## Contents

1. Image Compression and Decompression
   - Implemented multiple compression algorithms to reduce image file sizes:
     - Huffman Encoding: Applied Huffman coding to compress images using a binary tree-based technique.
     - Run-Length Encoding (RLE): Explored run-length encoding for compressing repeated sequences of pixels.
   - Decompression:
     - Implemented Huffman Decoding* to restore compressed images back to their original form.

2. Histogram Operations 
   - Worked on image intensity transformations and enhancements:
     - Image Negative: Inverted pixel values to create negative images.
     - Histogram Equalization: Improved image contrast by redistributing intensity levels.
     - Log Transformation: Applied logarithmic transformations for contrast enhancement.
     - Gamma Transformation: Enhanced image brightness by adjusting gamma values.

3. LZW Algorithm 
   - Implemented the Lempel-Ziv-Welch (LZW) algorithm for lossless image compression, ensuring no data loss while reducing image size.

4. Masking  
   - Explored various filtering techniques through masking:
     - Sharpening: Enhanced edges and fine details in images using sharpening filters.
     - Blurring: Applied blur filters to reduce noise and soften images.

5. Image Segmentation  
   - Implemented methods to divide an image into distinct regions:
     - Edge Detection: Used algorithms such as Canny, Sobel, and Prewitt to detect sharp changes in intensity that correspond to object boundaries.
     - Line Detection: Implemented Hough Transform to detect straight lines in images.
     - **Point Detection**: Identified distinct points or small features in an image.

6. Image Shrinking and Zooming  
   - Explored different resizing techniques:
     - Bilinear Interpolation: Used bilinear interpolation for smooth image zooming.
     - Nearest Neighbor Interpolation: Implemented nearest neighbor interpolation for simple image zooming with a focus on speed.
     - Image Shrinking: Reduced the size of images while preserving key features.

## How to Run

Each topic has its own script. To run the code:
1. Clone this repository.
2. Navigate to the corresponding folder for each lab task.
3. Execute the Python scripts using your preferred environment.

```bash
git clone <repository-link>
cd <specific-folder>
python <script-name>.py
```
