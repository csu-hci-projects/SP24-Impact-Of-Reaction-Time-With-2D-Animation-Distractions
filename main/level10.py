import matplotlib.pyplot as plt
import numpy as np
import random
import textwrap
import matplotlib.patches as patches
import time
from matplotlib.animation import FuncAnimation
import sys
from matplotlib.patches import Circle

def createCircle(ax, x_pos, y_pos):
    circle = Circle((x_pos, y_pos), 0.5, color='black', fill=True)
    ax.add_patch(circle)
    return circle

def init():
    global circles, velocities, ax
    circles = []
    velocities = []
    for _ in range(10):
        x_pos = random.uniform(1, 19)
        y_pos = random.uniform(1, 19)
        circles.append(createCircle(ax, x_pos, y_pos))
        velocities.append((random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)))
    return circles

def move2D(frame):
    for circle, velocity in zip(circles, velocities):
        x, y = circle.center
        vx, vy = velocity
        x_new = x + vx
        y_new = y + vy

        if not (0 <= x_new <= 20):
            vx = -vx
            x_new = x + vx
        if not (0 <= y_new <= 20):
            vy = -vy
            y_new = y + vy

        circle.set_center((x_new, y_new))
        
        index = circles.index(circle)
        velocities[index] = (vx, vy)

    return circles

#function to hide the grid so user cant see it till they are ready to start.
def hideWindow(event):
    global startScreen
    global startText
    global startTime
    global ani
    global found
    if startScreen and startText:
        found = False
        startScreen.remove() 
        startText.remove()
        found = True
        fig.canvas.draw() 
        fig.canvas.mpl_disconnect(cid)
        startTime = time.time()
        ani = FuncAnimation(fig, move2D, frames=np.linspace(0, 20, 100), init_func=init, blit=True, interval=20)
    startScreen = None
    startText = None

userID = 00
#White background
image_size = (5, 5)
image = np.ones((image_size[0], image_size[1], 3))

#Image to display
fig, ax = plt.subplots(figsize=(12, 8))
fig.patch.set_facecolor('#b3c7f7')
ax.imshow(image, extent=[0, image_size[1], 0, image_size[0]])

#20x20 grid
ax.set_xticks(np.arange(-0.5, 20, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 20, 1), minor=True)
ax.grid(True, color='#b3c7f7', linewidth=3)
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
startScreen = patches.Rectangle((-5, -5), 30, 30, color='#b3c7f7', alpha=1.0, zorder=10, label='Click to start')
ax.add_patch(startScreen)
startText = ax.text(10, 10, 'Start', color='black', fontsize=20, fontweight='bold', ha='center', va='center', zorder=11)
# Creating FuncAnimation
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
label_x_position = 24 
label_y_position = 19 
ax.text(label_x_position, label_y_position, "Time (sec): ", fontsize=20, fontweight='bold', color="black", ha='center', va='center', rotation='horizontal') 

#Hex codes for hearts and clubs
clubSymbol = '\u2663'
heartSymbol = '\u2665'

#Random plot generator - search for the club
for i in range(1, 20):
    for j in range(1, 20):
        if i == searchItem_x and j == searchItem_y:
            ax.text(i, j, clubSymbol, fontsize=15, ha='center', va='center', color='black')
        else:
            ax.text(i, j, heartSymbol, fontsize=15, ha='center', va='center', color='black')
            
#mouse clicks
#start = time.time()
def objectFound(click):
    #range for click detection
    tolerance = 0.3
    if abs(click.xdata - searchItem_x) < tolerance and abs(click.ydata - searchItem_y) < tolerance:
        end = time.time()
        totalTime = end - startTime
        formattedTime = format(totalTime, '.2f')
        with open('level10.txt', 'w') as file:
            file.write(formattedTime)
        print("Element Found in:", formattedTime, "seconds!")   
        time_x_position = 24 
        time_y_position = 17 
        ax.text(time_x_position, time_y_position, formattedTime, fontsize=20, fontweight='bold', color='black', ha='center', va='center', rotation='horizontal')    
        #hide screen after completion
        startScreen = patches.Rectangle((-5, -5), 30, 30, color='#b3c7f7', alpha=1.0, zorder=10, label='Click to start')
        ax.add_patch(startScreen)
        found = False
        startText = ax.text(10, 10, 'Congrats! Level Complete!', color='black', fontsize=20, fontweight='bold', ha='center', va='center', zorder=11)
        cid = fig.canvas.mpl_connect('button_press_event', hideWindow)
        fig.canvas.draw()
#connect the click event to the onclick function
fig.canvas.mpl_connect('button_press_event', objectFound)

plt.show()