import tkinter as tk
from tkinter import ttk, messagebox
import json
import sys

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

root = tk.Tk()
root.title("User Home")

label = ttk.Label(root, text="User Main Menu")
label.pack(padx=20, pady=20)

# Fetch account data when the app starts
account_details = accData(accNum)
if account_details:
    text_display = tk.Text(root, height=10, width=40)
    text_display.insert(tk.END, account_details)
    text_display.pack(pady=10)

# Exit button
btn_exit = ttk.Button(root, text="Logout", command=root.destroy)
btn_exit.pack(pady=10)

root.mainloop()
