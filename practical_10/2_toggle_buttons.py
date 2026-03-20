# Toggle visibility of two buttons

import tkinter as tk

def toggle_visibility():
    if button1.winfo_ismapped():
        button1.pack_forget()
        button2.pack(pady=20)
    else:
        button2.pack_forget()
        button1.pack(pady=20)

root = tk.Tk()
root.geometry("300x200")

button1 = tk.Button(root, text="Button 1", command=toggle_visibility)
button1.pack(pady=20)

button2 = tk.Button(root, text="Button 2", command=toggle_visibility)

root.mainloop()
