from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt 
from PIL import ImageTk, Image 

window = Tk()
#window.geometry('400x250')
window.title('Plotter')

input = StringVar(window)  # Tekst for graf
x0 = StringVar(window) # X0 input
x1 = StringVar(window) # X1 input
x_interval = StringVar(window) # interval steps X input

frame_input = ttk.Frame(window,height=5)
frame_input.grid(row=0)

input_formula = ttk.Entry(frame_input,textvariable=input)
input_formula.grid(row=0,column=1)
label_formula = ttk.Label(frame_input,text='Function')
label_formula.grid(row=0,column=0)

input_x0 = ttk.Entry(frame_input,textvariable=x0)
input_x0.grid(row=1,column=1)
label_x0 = ttk.Label(frame_input,text='X0')
label_x0.grid(row=1,column=0)

input_x1 = ttk.Entry(frame_input,textvariable=x1)
input_x1.grid(row=2,column=1)
label_x1 = ttk.Label(frame_input,text='X1')
label_x1.grid(row=2,column=0)

input_x_interval = ttk.Entry(frame_input,textvariable=x_interval)
input_x_interval.grid(row=3,column=1)
label_x_interval = ttk.Label(frame_input,text='steps')
label_x_interval.grid(row=3,column=0)




def createplot():
    
    tmp_x0 = eval(x0.get())
    tmp_x1 = eval(x1.get())
    tmp_x_interval = eval(x_interval.get())
    
    x = np.arange(tmp_x0,tmp_x1,tmp_x_interval) 
   
    y = eval(input.get())
    
    # Plot the points using matplotlib 
    plt.plot(x, y) 
   # plt.plot(x, y_cos) 
    plt.xlabel('x axis label') 
    plt.ylabel('y axis label') 
    #plt.title('Sine and Cosine') 
    #plt.legend(['Sine', 'Cosine']) 

  
    plt.savefig("data/plot.png",
                facecolor='white',
                bbox_inches="tight",
                pad_inches=0.3,
                transparent=True)
    plt.show()

input_button = ttk.Button(frame_input,text='Create Plot',command=createplot)
input_button.grid(row=0,column=2,rowspan=2)


# running the application 
window.mainloop() 





  