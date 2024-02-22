# Dominant-Colors-Extraction
"Dominant Color Identification Program using K-Means Clustering." The program reads an image, performs clustering on its pixels using the k-means algorithm with a specific number of clusters, and displays both the original image and a representation of the dominant colors in the form of bars.

## Features

### Dominant Colors
Here is a brief explanation of each part of the program:

### import library
```swift
import cv2
import numpy as np

```

<p align="center">
    <img src="Assets/dominant_colors.jpg">
</p>

By default, **ColorKit** uses an iterative process to determine the dominant colors of an image. But it also supports doing so via a [k-mean clustering algorithm](https://en.wikipedia.org/wiki/K-means_clustering). Choose whichever is more appropriate for your use case.

---
