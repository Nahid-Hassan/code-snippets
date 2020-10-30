from tkinter import *

root = Tk()


# take text input
entry = Entry(root, width=50)
entry.pack()

# index 0, here we set only one box.
entry.insert(0, "Enter your name")

# interactivity of button object
def my_click():
    display_text = "Hello " + entry.get()
    label = Label(root, text=display_text)
    label.pack()


# create button
button = Button(root, text='Enter your name', command=my_click)
button.pack()


root.mainloop()