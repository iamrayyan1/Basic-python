from tkinter import *

# canvas = widget that is used to draw graphs, plots, images in a window

window = Tk()

canvas = Canvas(window, width = 500, height = 500)
# canvas.create_line(0,0,500,500, fill='blue', width=5)
# canvas.create_line(0,500,500,0, fill='red', width=5)
# canvas.create_rectangle(50,50,250,250, fill='green', width=5)
# canvas.create_polygon(250,0, 500,500, 0,500, fill='yellow', outline='black', width=5)\
# points = [250,0, 500,500, 0,500]
# canvas.create_polygon(points, fill='yellow', outline='black', width=5)
# canvas.create_arc(0,0,500,500,fill="orange", style=PIESLICE, start=90, extent=180)

canvas.create_arc(0,0,500,500, fill="red", extent=180, width=10)
canvas.create_arc(0,0,500,500, fill="white", extent=180, width=10, start=180)
canvas.create_oval(190,190,310,310, fill="White", width=10)

canvas.pack()


window.mainloop()