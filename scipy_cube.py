from PIL import Image
import numpy as np
from scipy import ndimage

img = np.array(Image.open('img/rubiks_cube.png'), dtype=np.float32)
img_filtered = ndimage.gaussian_filter(img, sigma=[3, 3, 0])

Image.fromarray(img_filtered.astype(np.uint8)).show()
