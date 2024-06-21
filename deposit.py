import tkinter as tk
from tkinter import ttk, messagebox
import json
import datetime
import math
import random

class Deposit:
    def __init__(self, parent, accNum):
        self.accNum = accNum
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Deposit")

        self.label = ttk.Label(self.window, text="Enter amount to deposit:")
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.input = ttk.Entry(self.window)
        self.input.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        btn_login = ttk.Button(self.window, text="Deposit", command=self.handleDeposit)
        btn_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def handleDeposit(self):
        amount = self.input.get()

        if amount.isdigit():
            if float(amount) >= 1000:
                self.saveDeposit(float(amount))
            else:
                messagebox.showerror("Error", f"Error: {amount} is less than 1000. To deposit, the amount must be greater than 1000.")
        else:
            messagebox.showerror("Error", f"Error: {amount} is not a number")

    def saveDeposit(self, amount):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("File not Found", "Error: Database file not found!")
            return

        account_found = False

        for account in data['accounts']:
            if account['accNum'] == str(self.accNum):
                account_found = True
                account['balance'] += amount
                current_balance = account['balance']
                break

        if account_found:
            try:
                with open('data.json', 'w') as f:
                    json.dump(data, f, indent=4)
                messagebox.showinfo("Success", f"Successfully deposited {amount} to account {self.accNum}.")
                self.saveTransaction(amount, current_balance)
                self.window.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save data: {e}")
        else:
            messagebox.showerror("Error", "Account not found.")

    def saveTransaction(self, amount, balance):
        todays_date = datetime.date.today()
        formatted_date = todays_date.strftime("%A, %B %d, %Y")

        # generate transaction number
        digits = [i for i in range(0, 10)]
        trans_ref = "".join(str(digits[math.floor(random.random() * 10)]) for _ in range(6))

        transaction = {
            "accNum": self.accNum,
            "title": "Deposit",
            "amount": amount,
            "balance": balance,
            "reference": trans_ref,
            "date": formatted_date
        }

        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "Error: Database not found.")
            return

        if 'transactions' not in data:
            data['transactions'] = []

        data['transactions'].append(transaction)

        try:
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save transaction data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Deposit(root, "893675")  # Replace "893675" with the account number to test
    root.mainloop()
