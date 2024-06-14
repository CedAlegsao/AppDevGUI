import tkinter as tk
from tkinter import ttk
import json
import time
import subprocess

class Login:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Login Account")
        self.window.geometry("500x200")

        label = ttk.Label(self.window, text="Login Account")
        label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # Account number
        acc_num_label = ttk.Label(self.window, text="Account Number:")
        acc_num_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.acc_name_entry = ttk.Entry(self.window)
        self.acc_name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Message
        self.message = tk.Text(self.window, wrap="word", height=3, width=40)
        self.message.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        # Login Button
        login_button = ttk.Button(self.window, text="Login", command=self.account_login)
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

    def account_login(self):
        acc_num = self.acc_name_entry.get()

        # Load data from JSON file
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.message.delete(1.0, tk.END)
            self.message.insert(tk.END, "Error: Data file not found.")
            return

        # Check if account number exists
        account_found = False
        for account in data['accounts']:
            if account['accNum'] == acc_num:
                account_found = True
                self.message.delete(1.0, tk.END)
                self.message.insert(tk.END, f"Login successful for account: {acc_num}")
                break

        if not account_found:
            self.message.delete(1.0, tk.END)
            self.message.insert(tk.END, "Error: Account number not found.")
        else:
            # Close the login window after 2 seconds
            self.window.after(2000, self.open_user_home, account)

    def open_user_home(self, account):
        self.window.destroy()  # Close the login window

        # Open userhome.py and pass account details
        subprocess.Popen(["python", "userhome.py", json.dumps(account)])

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
