# Button with message box

import tkinter as tk
from tkinter import messagebox

def show_message_box():
    messagebox.showinfo("Message", "Thank you for clicking")

root = tk.Tk()
root.geometry("100x200")

button = tk.Button(root, text="Click Here", command=show_message_box)
button.place(x=20, y=100)

root.mainloop()
