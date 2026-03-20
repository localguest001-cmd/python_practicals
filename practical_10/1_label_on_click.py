# Display label on button click

import tkinter as tk

def display_label():
    label.config(text="Hello, World!")

root = tk.Tk()
root.geometry("300x200")

button = tk.Button(root, text="Click me!", command=display_label)
button.pack(pady=20)

label = tk.Label(root, text="")
label.pack()

root.mainloop()
