import tkinter as tk
from tkinter import ttk
import json

class ShowBestAccount:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Show Best Accounts")
        self.window.geometry("700x300")

        # Create a Treeview widget to display sorted accounts
        self.tree = ttk.Treeview(self.window, columns=("Account Number", "Account Name", "Account Type", "Gender", "Address", "Balance"))
        self.tree.heading("#0", text="ID")
        self.tree.column("#0", width=20)
        self.tree.heading("Account Number", text="Account Number")
        self.tree.column("Account Number", width=85)
        self.tree.heading("Account Name", text="Account Name")
        self.tree.column("Account Name", width=85)
        self.tree.heading("Account Type", text="Account Type")
        self.tree.column("Account Type", width=85)
        self.tree.heading("Gender", text="Gender")
        self.tree.column("Gender", width=50)
        self.tree.heading("Address", text="Address")
        self.tree.column("Address", width=50)
        self.tree.heading("Balance", text="Balance")
        self.tree.column("Balance", width=80)
        
        # Configure Treeview to expand and fill
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Load data from JSON file
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Sort accounts by balance (descending order)
        sorted_accounts = sorted(data['accounts'], key=lambda x: x['balance'], reverse=True)

        # Display sorted accounts in Treeview
        for idx, account in enumerate(sorted_accounts, start=1):
            self.tree.insert("", "end", text=f"{idx}", values=(
                account['accNum'],
                account['accName'],
                account['accountType'],
                account['gender'],
                account['address'],
                account['balance']
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowBestAccounts(root)
    root.mainloop()
