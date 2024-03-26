import matplotlib.pyplot as plt
import numpy as np
import random
import textwrap
import matplotlib.patches as patches

#function to hide the grid so user cant see it till they are ready to start.
def hideWindow(event):
    global startScreen
    global startText
    if startScreen and startText:
        startScreen.remove() 
        startText.remove()
        fig.canvas.draw() 
        fig.canvas.mpl_disconnect(cid)
    startScreen = None
    startText = None
    
#White background
image_size = (5, 5)
image = np.ones((image_size[0], image_size[1], 3))

#Image to display
fig, ax = plt.subplots(figsize=(12, 8))
fig.patch.set_facecolor('#89CFF0')
ax.imshow(image, extent=[0, image_size[1], 0, image_size[0]])

#20x20 grid
ax.set_xticks(np.arange(-0.5, 20, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 20, 1), minor=True)
ax.grid(True, color='white', linewidth=3)
ax.tick_params(which='minor', size=0)

#Remove tick labels and marks
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_yticks([])

#X/Y limits
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_aspect('equal')

# Create a start screen that covers the whole plot
# Allows the grid to be hidden for initial start
startScreen = patches.Rectangle((-5, -5), 30, 30, color='skyblue', alpha=1.0, zorder=10, label='Click to start')
ax.add_patch(startScreen)
startText = ax.text(10, 10, 'Start', color='black', fontsize=20, fontweight='bold', ha='center', va='center', zorder=11)
cid = fig.canvas.mpl_connect('button_press_event', hideWindow)

#Title and random number generation for unique symbol
plt.title("Find the Odd One Out", color='Black', fontsize=30, fontweight='bold')
searchItem_x = random.randint(2, 19)
searchItem_y = random.randint(2, 19)

#Adding directions to the left
label_x_position = -5 
label_y_position = 19 
ax.text(label_x_position, label_y_position, 'Directions', fontsize=20, fontweight='bold', ha='center', va='center', rotation='horizontal')

#description/directions.
label_text = "This game is about finding out how fast you can find the odd object out. As the levels progress, you will see that it gets more difficult. There will be increasing 2D animations to distract you and thus making it increasingly more difficult to complete the challenge. Good Luck! Have fun!"
wrap = textwrap.TextWrapper(width=20)  
wrapped_label = wrap.fill(text=label_text)
label_x_position = -5 
label_y_position = 13
ax.text(label_x_position, label_y_position, wrapped_label, fontsize=12, ha='center', va='center', rotation='horizontal')


#Hex codes for hearts and clubs
clubSymbol = '\u2663'
heartSymbol = '\u2665'

#Random plot generator - search for the club
for i in range(1, 20):
    for j in range(1, 20):
        if i == searchItem_x and j == searchItem_y:
            ax.text(i, j, clubSymbol, fontsize=15, ha='center', va='center', color='gray')
        else:
            ax.text(i, j, heartSymbol, fontsize=15, ha='center', va='center', color='black')

#mouse clicks
def objectFound(click):
    #range for click detection
    tolerance = 0.3
    if abs(click.xdata - searchItem_x) < tolerance and abs(click.ydata - searchItem_y) < tolerance:
        print("Element Found!")    
        #Adding directions to the right
      
#connect the click event to the onclick function
fig.canvas.mpl_connect('button_press_event', objectFound)

plt.show()