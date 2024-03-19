import matplotlib.pyplot as plt
import numpy as np

# White background
image_size = (5, 5)
image = np.ones((image_size[0], image_size[1], 3))

#image to display
fig, ax = plt.subplots(figsize=(5,5))
ax.imshow(image, extent=[0, image_size[1], 0, image_size[0]])

#10x10 grid
ax.set_xticks(np.arange(-0.5, 20, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 20, 1), minor=True)
ax.grid(True, color='white', linewidth=2)

ax.tick_params(which='major', size=0)

# x/y limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_aspect('equal')

plt.show()