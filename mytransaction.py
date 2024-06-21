import tkinter as tk
from tkinter import ttk, messagebox
import json

class MyTransaction:
    def __init__(self, parent, accNum):
        self.accNum = accNum
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("My Transactions")

        self.label = ttk.Label(self.window, text=f"Transactions for Account: {self.accNum}")
        self.label.grid(row=0, column=0, padx=20, pady=10)

        self.tree = ttk.Treeview(self.window, columns=("title", "amount", "balance", "reference", "date"), show="headings")
        self.tree.heading("title", text="Title")
        self.tree.heading("amount", text="Amount")
        self.tree.heading("balance", text="Balance")
        self.tree.heading("reference", text="Reference")
        self.tree.heading("date", text="Date")
        self.tree.grid(row=1, column=0, padx=20, pady=10)

        self.load_transactions()

    def load_transactions(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("File not Found", "Error: Database file not found!")
            return

        transactions = data.get("transactions", [])
        for transaction in transactions:
            if transaction["accNum"] == self.accNum:
                self.tree.insert("", tk.END, values=(
                    transaction["title"],
                    transaction["amount"],
                    transaction["balance"],
                    transaction["reference"],
                    transaction["date"]
                ))


if __name__ == "__main__":
    root = tk.Tk()
    app = MyTransaction(root)
    root.mainloop()
