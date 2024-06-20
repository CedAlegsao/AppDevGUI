import tkinter as tk
from tkinter import ttk, messagebox

import sys

# Read account number from command-line argument
if len(sys.argv) > 1:
    accNum = sys.argv[1]
else:
    messagebox.showerror("Error", "Invalid Access to this page, Please loggin properly.")


root = tk.Tk()
root.title("User Home")
# Use accNum in your user home interface

label = ttk.Label(root, text=f"Welcome to User Home!\nLogged in with Account Number: {accNum}", font=("Helvetica", 20))
label.pack(padx=20, pady=20)

root.mainloop()
