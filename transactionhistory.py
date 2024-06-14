import tkinter as tk
from tkinter import ttk
import json

class TransactionHistory:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Transaction History")
        self.window.geometry("700x300")  # Set window size

        # Create a Treeview widget to display transaction data
        self.tree = ttk.Treeview(self.window, columns=("Title", "Created By", "Amount", "Reference", "Balance", "Date"))
        self.tree.heading("#0", text="ID")
        self.tree.column("#0", width=50)
        self.tree.heading("Title", text="Title")
        self.tree.column("Title", width=100)
        self.tree.heading("Created By", text="Created By")
        self.tree.column("Created By", width=100)
        self.tree.heading("Amount", text="Amount")
        self.tree.column("Amount", width=80)
        self.tree.heading("Reference", text="Reference")
        self.tree.column("Reference", width=100)
        self.tree.heading("Balance", text="Balance")
        self.tree.column("Balance", width=80)
        self.tree.heading("Date", text="Date")
        self.tree.column("Date", width=150)
        
        # Configure Treeview to expand and fill
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Load transaction data from JSON file
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Display transactions in Treeview
        for idx, transaction in enumerate(data['transactions'], start=1):
            self.tree.insert("", "end", text=f"{idx}", values=(
                transaction['title'],
                transaction['Created_By'],
                transaction['Transaction_Amount'],
                transaction['Transaction_Reference'],
                transaction['balance'],
                transaction['updated_at']
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = TransactionHistory(root)
    root.mainloop()
