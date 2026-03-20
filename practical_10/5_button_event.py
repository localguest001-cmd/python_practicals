# Handle button click event

import tkinter as tk

def button_clicked():
    print("Button clicked")

root = tk.Tk()
root.geometry("300x200")

button = tk.Button(root, text="Click me!", command=button_clicked)
button.pack(pady=20)

root.mainloop()
