#%%Buttons

import tkinter as tk 
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop() 

##%%Canvas 

from tkinter import *
master = Tk() 
w = Canvas(master, width=1000, height=90) 
w.pack() 
canvas_height=90
canvas_width=1000
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y ) 
mainloop() 

#%%