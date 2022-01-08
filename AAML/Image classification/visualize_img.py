import matplotlib.pyplot as plt
import numpy as np

img = np.random.randint(0, 255, (256,256))
# initialize plot
plt.figure(figsize=(7,7))

print(img.ravel())

# show grayscale image
plt.imshow(img, cmap='gray')
plt.show()
