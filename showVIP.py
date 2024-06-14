import tkinter as tk
from tkinter import ttk
import json

class ShowVIP:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("VIP Accounts")
        self.window.geometry("700x300")

        # Create a Treeview widget to display data
        self.tree = ttk.Treeview(self.window, columns=("Account Number", "Account Name", "Account Type", "Gender", "Address", "Balance"))
        self.tree.heading("#0", text="Category")
        self.tree.column("#0", width=100)
        self.tree.heading("Account Number", text="Account Number")
        self.tree.column("Account Number", width=100)
        self.tree.heading("Account Name", text="Account Name")
        self.tree.column("Account Name", width=100)
        self.tree.heading("Account Type", text="Account Type")
        self.tree.column("Account Type", width=100)
        self.tree.heading("Gender", text="Gender")
        self.tree.column("Gender", width=70)
        self.tree.heading("Address", text="Address")
        self.tree.column("Address", width=100)
        self.tree.heading("Balance", text="Balance")
        self.tree.column("Balance", width=100)

        # Load data from JSON file
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Categorize accounts based on balance
        gold_accounts = []
        silver_accounts = []
        bronze_accounts = []

        for account in data['accounts']:
            if account['balance'] >= 1000000:
                gold_accounts.append(account)
            elif 100000 <= account['balance'] < 1000000:
                silver_accounts.append(account)
            elif account['balance'] < 100000:
                bronze_accounts.append(account)

        # Sort accounts within each category by balance (descending)
        gold_accounts.sort(key=lambda x: x['balance'], reverse=True)
        silver_accounts.sort(key=lambda x: x['balance'], reverse=True)
        bronze_accounts.sort(key=lambda x: x['balance'], reverse=True)

        # Insert data into Treeview starting with Gold category
        self.insert_accounts("Gold", gold_accounts)
        self.insert_accounts("Silver", silver_accounts)
        self.insert_accounts("Bronze", bronze_accounts)

        # Pack Treeview widget
        self.tree.pack(fill=tk.BOTH, expand=True)

    def insert_accounts(self, category, accounts):
        # Insert accounts into Treeview
        for account in accounts:
            self.tree.insert("", "end", text=category, values=(account['accNum'], account['accName'], account['accountType'], account['gender'], account['address'], account['balance']))

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowVIP(root)
    root.mainloop()
