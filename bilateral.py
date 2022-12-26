import numpy as np
from PIL import Image
import filt

# Gaussian convolution applied at a pixel in an image

img = np.array(Image.open('./img/rubiks_cube.png'), dtype=np.float32)
Image.fromarray(img.astype(np.uint8)).show()
#exit()
img_filtered = np.asarray(filt.gaussian(img, 3))
Image.fromarray(img_filtered.astype(np.uint8)).show()
