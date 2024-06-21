import tkinter as tk
from tkinter import ttk, messagebox
import json
import sys

from withdraw import Withdraw
from deposit import Deposit
from transfer_fund import TransferFund
from mytransaction import MyTransaction

# Read account number from command-line argument
if len(sys.argv) > 1:
    accNum = sys.argv[1]
else:
    messagebox.showerror("Error", "Invalid Access to this page, Please log in properly.")
    sys.exit(1)

def accData(accNum):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Database Not Found", "Error: Database not found, Please Contact the Admin.")
        sys.exit(1)

    for account in data['accounts']:
        if account['accNum'] == accNum:
            # Construct account details string
            account_details = ""
            for key, value in account.items():
                account_details += f"{key}: {value}\n"
            return account_details

    messagebox.showerror("Account Not Found", f"Account number {accNum} not found in database. Try contacting the admin for you to register your own account")
    sys.exit(1)

def Logout():
    root.destroy()

def handleCommands(cmd, accNum):
    if cmd == Logout:
        Logout()
    elif cmd == refreshData:
        refreshData()
    else:
        cmd(root, accNum)

def refreshData():
    account_details = accData(accNum)
    if account_details:
        text_display.delete(1.0, tk.END)  # Clear the current content
        text_display.insert(tk.END, account_details)  # Insert the refreshed content

root = tk.Tk()
root.title("User Home")

label = ttk.Label(root, text="User Main Menu")
label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Fetch account data when the app starts
account_details = accData(accNum)
text_display = tk.Text(root, height=10, width=40)
if account_details:
    text_display.insert(tk.END, account_details)
text_display.grid(row=1, column=0, columnspan=2, pady=10)

# Buttons layout
buttons = [
    ('Deposit Amount', Deposit),
    ('Withdraw Amount', Withdraw),
    ('Transfer Fund', TransferFund),
    ('My Transaction', MyTransaction),
    ('Logout', Logout),
    ('Refresh', refreshData)  # Add the refresh button
]

# Create buttons in a 2x3 grid layout (add extra row for Refresh button)
for i, (text, command) in enumerate(buttons):
    row = i // 2 + 2
    col = i % 2
    btn = ttk.Button(root, text=text, command=lambda cmd=command: handleCommands(cmd, accNum) if cmd != refreshData else cmd())
    btn.grid(row=row, column=col, padx=10, pady=10)

root.mainloop()
