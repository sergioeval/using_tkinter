
from tkinter import *
master = Tk() 
w = Canvas(master, width=1000, height=90) 
w.pack() 
canvas_height=90
canvas_width=1000
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y ) 
mainloop() 
