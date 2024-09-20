import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('edge3.jpeg')

# vertical prewitt
mask = np.array([[-1, 0, 1],
                 [-1, 0, 1],
                 [-1, 0, 1]])

result = cv2.filter2D(image, -1, mask)

plt.figure(figsize=(15, 10)) 
plt.subplot(1, 2, 1)
plt.title('Input Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Output Image')
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

plt.show()

