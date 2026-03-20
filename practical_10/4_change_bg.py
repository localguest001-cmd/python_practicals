# Change background color using buttons

import tkinter as tk

def change_color_red():
    frame.config(bg="red")

def change_color_green():
    frame.config(bg="green")

def change_color_blue():
    frame.config(bg="blue")

root = tk.Tk()
root.geometry("300x200")

frame = tk.Frame(root, width=200, height=100, bg="white")
frame.pack(pady=20)

button1 = tk.Button(root, text="Red", command=change_color_red)
button1.pack(side="left", padx=10)

button2 = tk.Button(root, text="Green", command=change_color_green)
button2.pack(side="left", padx=10)

button3 = tk.Button(root, text="Blue", command=change_color_blue)
button3.pack(side="left", padx=10)

root.mainloop()
