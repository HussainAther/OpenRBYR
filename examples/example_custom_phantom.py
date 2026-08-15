from openrbyr_core.phantom_loader import load_image
import matplotlib.pyplot as plt

img = load_image("data/sample.dcm")
plt.imshow(img, cmap='gray')
plt.title("Loaded Medical Image")
plt.show()

