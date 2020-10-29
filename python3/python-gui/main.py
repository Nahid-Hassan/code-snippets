from tkinter import *

# start: create tk object
root = Tk()

# set title
root.title('Tkinter Basic Example')

# -------------- Create Widget---------------------
myLabel = Label(root, text="This a Label")

# ------------------Show Widget---------------
myLabel.pack()


# end: run mainloop
root.mainloop()
