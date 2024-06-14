import tkinter as tk
from create_account import CreateAccount
from login import Login
from displaydata import DisplayAllData

buttons = [
    ("Create Account", "CreateAccount"),
    ("Login Account", "LoginAccount"),
    ("Display All Account", "DisplayAllAccounts"),
    ("Transaction History", ""),
    ("Show Best Account", ""),
    ("Show VIP", ""),
    ("Remove Account", ""),
    ("Update Account", "")
]

def button_command(action):
    if action == "CreateAccount":
        CreateAccount(root)
    elif action == "LoginAccount":
        Login(root)
    elif action == "DisplayAllAccounts":
        DisplayAllData(root)

root = tk.Tk()
root.title("Final Python Project-python")

button_width = 20
button_height = 1

for i in range(4):  # 4 rows
    for j in range(2):  # 2 columns
        index = i * 2 + j
        if index < len(buttons):
            btn_text, action = buttons[index]
            button = tk.Button(root, text=btn_text, command=lambda a=action: button_command(a),
                               width=button_width, height=button_height)
            button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

# Make the grid cells expand equally
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
for j in range(2):
    root.grid_columnconfigure(j, weight=1)


root.mainloop()
