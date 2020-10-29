# Tkinter (GUI Programming)

`Tkinter` is a graphical user interface (GUI) module for Python, you can make `desktop apps` with Python. You can make `windows`, `buttons`, `show text` and `images` amongst other things.

Tk and Tkinter apps can run on most `Unix` platforms. This also works on `Windows` and `Mac OS X`.
The module Tkinter is an interface to the Tk GUI toolkit.

## Base

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
