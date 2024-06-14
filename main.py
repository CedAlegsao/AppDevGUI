import tkinter as tk
from tkinter import Button
from create_account import CreateAccount
from login import Login
from displaydata import DisplayAllData
from transactionhistory import TransactionHistory
from showbestaccount import ShowBestAccount
from showVIP import ShowVIP
from romoveaccount import RemoveAccount
from updateAccount import UpdateAccount

# Define buttons with their text and corresponding action
buttons = [
    ("Create Account", CreateAccount),
    ("Login Account", Login),
    ("Display All Account", DisplayAllData),
    ("Transaction History", TransactionHistory),
    ("Show Best Account", ShowBestAccount),
    ("Show VIP", ShowVIP),
    ("Remove Account", RemoveAccount),
    ("Update Account", UpdateAccount)
]

def button_command(action_class):
    action_class(root)

root = tk.Tk()
root.title("Main Menu")

# Calculate screen width and height for centering window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 400
window_height = 400

x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Title label at the top
title_label = tk.Label(root, text="Main Menu", font=("Helvetica", 20))
title_label.grid(row=0, column=0, columnspan=2, pady=20)

button_width = 20
button_height = 1

# Create buttons in a 4x2 grid layout
for i, (btn_text, action_class) in enumerate(buttons):
    button = Button(root, text=btn_text, command=lambda ac=action_class: button_command(ac),
                    width=button_width, height=button_height)
    button.grid(row=i // 2 + 1, column=i % 2, padx=5, pady=5, sticky="nsew")

# Make the grid cells expand equally
for i in range(len(buttons) // 2 + 1):
    root.grid_rowconfigure(i, weight=1)
for j in range(2):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
