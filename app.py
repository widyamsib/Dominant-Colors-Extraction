import cv2
import numpy as np

def create_bar(height: int, width: int, color: list) -> np.ndarray | tuple:
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:, :] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)

# Load gambar dan perkecil ukuran
img = cv2.imread('contoh gambar1.jpg')
img_resized = cv2.resize(img, (400, 300))  # Ganti ukuran sesuai kebutuhan

height, width, _ = np.shape(img_resized)

data = np.reshape(img_resized, (height * width, 3))
data = np.float32(data)

number_clusters = 3
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness, labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)

bars = []
rgb_values = []

for row in centers:
    bar, rgb = create_bar(200, 200, row)
    bars.append(bar)
    rgb_values.append(rgb)

img_bar = np.hstack(bars)

cv2.imshow('original image', img_resized)
cv2.imshow('dominant color', img_bar)
cv2.waitKey(0)
cv2.destroyAllWindows()
