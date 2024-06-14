import tkinter as tk
from tkinter import ttk
import json

class Login:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Login Account")
        self.window.geometry("500x500")

        label = ttk.Label(self.window, text="Login Account")
        label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    app.mainloop()