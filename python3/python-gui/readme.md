# Tkinter (GUI Programming)

`Tkinter` is a graphical user interface (GUI) module for Python, you can make `desktop apps` with Python. You can make `windows`, `buttons`, `show text` and `images` amongst other things.

Tk and Tkinter apps can run on most `Unix` platforms. This also works on `Windows` and `Mac OS X`.
The module Tkinter is an interface to the Tk GUI toolkit.

## This `readme.md` file contains series of tkinter widget and functionalities

### Base

```py
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
```

![Tkinter Basic Example]()

### Grid Widget

```py
# Creating a Label Widget
myLabel1 = Label(root, text='Hello World1')
myLabel2 = Label(root, text='Hello World2')

# Using grid method(row, columns)
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

# You can do it other way
# myLabel = Label(root, 'example').grid(row=0, column=0)
```

### Button Widget

```py
# Button with label/text 'click me'
myButton = Button(root, text='click me')

# made click disable and override padx and pady for change default button size
myButton = Button(root, text='click me', state=DISABLED, padx=50, pady=40)

# set the command argument and make button interactive
def myClick():
    my_label = Label(root, text="Clicked")
    my_label.pack()

myButton = Button(root, text='click me', command=myClick)
# we cannot use myClick(). Because pass with () parenthesis already call the function,
# that we don't want

# Set fg and bg
myButton = Button(root, text='click me', command=myClick, fg="blue", bg="red")
```

### Entry Widget

```py
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
```
