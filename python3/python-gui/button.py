from tkinter import *

# start: create tk object
root = Tk()

# -------------- Create ---------------------
myButton = Button(root, text='click me', state=DISABLED, padx=50, pady=40)


# ------------------ show ---------------
myButton.pack()


# end: run mainloop
root.mainloop()