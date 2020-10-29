# from tkinter import everything
from tkinter import *

# Create Tk object
root = Tk()

# ------------- First Create Thing------------

# Creating a Label Widget
myLabel1 = Label(root, text='Hello World1')
myLabel2 = Label(root, text='Hello World2')

# You can do it other way
# myLabel = Label(root, 'example').grid(row=0, column=0)


# --------------Next showing thing------------

# Showing it into the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()
