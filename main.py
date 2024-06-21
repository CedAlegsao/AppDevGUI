import tkinter as tk
from tkinter import ttk, messagebox
import json
import subprocess

root = tk.Tk()
root.title("Login Account")

def checkIsAdmin(account):
    isAdmin = account["isAdmin"]
    accNum = account["accNum"]
    
    if isAdmin:
        messagebox.showinfo("Message", "Logged as Admin.")
        subprocess.Popen(['python', 'adminhome.py', str(accNum)])
    else:
        messagebox.showinfo("Message", "Successfully Logged in to you account.")
        subprocess.Popen(['python', 'userMainMenu.py', str(accNum)])

    root.destroy()

def validated(acc_num):
    #laod the data base
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("File not Found", "Error: Database file not found!")
        return

    account_found = False

    for account in data['accounts']:
        if account['accNum'] == str(acc_num):
            account_found = True
            account_data = account
            
    if not account_found:
        messagebox.showerror("Account number not found", f"Account number {acc_num} is not registered, please contact the admin to register new account.")
    else:
        checkIsAdmin(account_data)

def login():
    
    accNum = input_acc_num.get()

    if accNum.isdigit():
        if len(accNum) != 6:
            messagebox.showerror("Invalid Account Number", "The account number must be 6 digit.")
        else:
            validated(acc_num=accNum)
    else:
        messagebox.showerror("Invalid account number.", "The account number must be 6 digit integer")


label = ttk.Label(text="Account Number")
label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

input_acc_num = ttk.Entry()
input_acc_num.grid(row=1, column=0, columnspan=2, padx=10,pady=10)

btn_login = ttk.Button(text="Login", command=login)
btn_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()