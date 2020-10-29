from tkinter import *

# start: create tk object
root = Tk()

# Create function for myButton
def myClick():
    my_label = Label(root, text="Clicked")
    my_label.pack()

# -------------- Create ---------------------
# myButton = Button(root, text='click me', state=DISABLED, padx=50, pady=40)

# to use a function we need to call the function, to doing this we 
# assign command = function_name without parenthesis
myButton = Button(root, text='click me', command=myClick, fg="blue", bg='red')

# fg = foreground color
# bg = background color



# ------------------ show ---------------
myButton.pack()


# end: run mainloop
root.mainloop()
