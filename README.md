# Dominant-Colors-Extraction
"Dominant Color Identification Program using K-Means Clustering." The program reads an image, performs clustering on its pixels using the k-means algorithm with a specific number of clusters, and displays both the original image and a representation of the dominant colors in the form of bars.
## Result
<p align="center"><img src="asset/gambar1.jpg" alt="Deskripsi Gambar"></p>


## Features

### Dominant Colors
Here is a brief explanation of each part of the program:

### import library
```swift
import cv2
import numpy as np

```
The script imports the necessary libraries: OpenCV (cv2) for image processing and NumPy (np) for numerical array manipulation.

### Function 'create_bar':
```swift
def create_bar(height, width, color):
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:, :] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)

```
This function creates a colored bar image with specified dimensions and color.
### Load dan Resize Image:
```swift
img = cv2.imread('contoh gambar1.jpg')
img_resized = cv2.resize(img, (400, 300))

```
The script reads an image from a file ('example_image.jpg') and resizes it to (400, 300).

### K-Means Clustering:
```swift
height, width, _ = np.shape(img_resized)
data = np.reshape(img_resized, (height * width, 3))
data = np.float32(data)

number_clusters = 3
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness, labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)

```
The program performs k-means clustering on the pixel data of the resized image.

### Create Bars and Extract RGB Values :
```swift
bars = []
rgb_values = []

for row in centers:
    bar, rgb = create_bar(200, 200, row)
    bars.append(bar)
    rgb_values.append(rgb)
```
Bars representing dominant colors and their corresponding RGB values are created.

### Combine Bars into One Image:
```swift
img_bar = np.hstack(bars)
```
The script combines the created color bars into a single image.

### Display Original Image and Dominant Color Image :
```swift
cv2.imshow('original image', img_resized)
cv2.imshow('dominant color', img_bar)
cv2.waitKey(0)
cv2.destroyAllWindows()

```
The original image and the image with dominant colors are displayed, and the script waits for a key press before closing the windows.
