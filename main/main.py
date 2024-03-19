import matplotlib.pyplot as plt
import numpy as np
import random

# White background
image_size = (5, 5)
image = np.ones((image_size[0], image_size[1], 3))

#image to display
fig, ax = plt.subplots(figsize=(12,8))
fig.patch.set_facecolor('white')
ax.imshow(image, extent=[0, image_size[1], 0, image_size[0]])

#20x20 grid
ax.set_xticks(np.arange(-0.5, 20, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 20, 1), minor=True)
ax.grid(True, color='white', linewidth=3)
ax.tick_params(which='minor', size=0)

#this gets rid of the hashmarks and the numbers, doesnt allow for cursor tracking however. 
# ax.set_xticklabels([])
# ax.set_yticklabels([])
# ax.set_xticks([])
# ax.set_yticks([])

# x/y limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_aspect('equal')

# title, and random number generation for unique symbol
plt.title("CS464 - Odd One Out", color='Red', fontsize=30)
searchItem_x = random.randint(2, 19)
searchItem_y = random.randint(2, 19)
#hex codes for hearts and clubs
clubSymbol = '\u2663'
heartSymbol = '\u2665'

#random plot generator - search for the club.
for i in range(1,20):
    for j in range(1,20):
        if i == searchItem_x and j == searchItem_y:
            ax.text(i, j, clubSymbol, fontsize=15, ha='center', va='center', color='red')
        else:
            ax.text(i, j, heartSymbol, fontsize=15, ha='center', va='center', color='black')

plt.show()