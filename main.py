from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt 
from PIL import ImageTk, Image 

window = Tk()
#window.geometry('400x250')
window.title('Plotter')

input = StringVar(window)

frame_input = ttk.Frame(window,height=5)
frame_input.grid(row=0)

frame_plot = ttk.Frame(window)
frame_plot.grid(row=1)


# Computes x and y coordinates for 
# points on sine and cosine curves 
x = np.arange(0, 3 * np.pi, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x) 

# Plot the points using matplotlib 
plt.plot(x, y_sin) 
plt.plot(x, y_cos) 
plt.xlabel('x axis label') 
plt.ylabel('y axis label') 
plt.title('Sine and Cosine') 
plt.legend(['Sine', 'Cosine']) 

#plt.show()
plt.savefig("data/plot.png",
            facecolor='white',
            bbox_inches="tight",
            pad_inches=0.3,
            transparent=True)

Input_field = ttk.Entry(frame_input,)
Input_field.grid()

# arranging application parameters 
canvas = Canvas(frame_plot,
                width = 600, 
				height = 600) 

canvas.grid() 

# loading the image 
img = ImageTk.PhotoImage(Image.open("data/plot.png")) 

# arranging image parameters 
# in the application 
canvas.create_image(0,0, anchor = NW, 
				image = img) 

# running the application 
window.mainloop() 





  