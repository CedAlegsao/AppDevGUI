import tkinter as tk
from tkinter import ttk, messagebox
import json
import datetime
import math
import random

class UserHome:
    def __init__(self, account):
        self.account = account
        self.window = tk.Tk()
        self.window.title("User Home")
        self.window.geometry("500x400")

        label = ttk.Label(self.window, text="Account Details")
        label.pack(pady=10)

        # Display account details
        details_frame = ttk.Frame(self.window)
        details_frame.pack(padx=20, pady=10)

        ttk.Label(details_frame, text="Account Number:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(details_frame, text=account['accNum']).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(details_frame, text="Account Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(details_frame, text=account['accName']).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(details_frame, text="Account Type:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(details_frame, text=account['accountType']).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(details_frame, text="Gender:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(details_frame, text=account['gender']).grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(details_frame, text="Address:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        ttk.Label(details_frame, text=account['address']).grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(details_frame, text="Balance:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
        self.balance_label = ttk.Label(details_frame, text=account['balance'])
        self.balance_label.grid(row=5, column=1, padx=5, pady=5)

        # Buttons for deposit, withdraw, and transfer fund
        deposit_button = ttk.Button(self.window, text="Deposit", command=self.open_deposit_window)
        deposit_button.pack(side=tk.LEFT, padx=10, pady=10)

        withdraw_button = ttk.Button(self.window, text="Withdraw", command=self.open_withdraw_window)
        withdraw_button.pack(side=tk.LEFT, padx=10, pady=10)

        transfer_button = ttk.Button(self.window, text="Transfer Fund", command=self.open_transfer_window)
        transfer_button.pack(side=tk.LEFT, padx=10, pady=10)

        transfer_button = ttk.Button(self.window, text="Logout", command=self.logout)
        transfer_button.pack(side=tk.LEFT, padx=10, pady=10)

    def logout(self):
        self.window.destroy()

    def update_balance_label(self):
        self.balance_label.config(text=self.account['balance'])

    def save_to_json(self):
        # Load existing data from file
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            # If the file doesn't exist, initialize with empty lists
            data = {"accounts": [], "transactions": []}

        # Update the account in the data
        for acc in data['accounts']:
            if acc['accNum'] == self.account['accNum']:
                acc.update(self.account)
                break

        # Write updated data back to file
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

    def save_recipient_ammount(self, acc_num, amount):
        
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            # If the file doesn't exist, initialize with empty lists
            data = {"accounts": [], "transactions": []}

        # Update the balance of the recipient account
        for account in data['accounts']:
            if account['accNum'] == acc_num:
                account['balance'] += amount
                break

        # Write updated data back to file
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

    def save_transaction(self, title, amount):
        todays_date = datetime.date.today()
        formatted_date = todays_date.strftime("%A, %B %d, %Y")

        # generate transaction number
        digits = [i for i in range(0,10)]
        trans_ref = ""
        for i in range(6):
            index = math.floor(random.random()*10)
            trans_ref += str(digits[index])

        transaction_log = {
            'title': title,
            'Created_By': self.account['accNum'],
            'Transaction_Amount': amount,
            'Transaction_Reference': trans_ref,
            'balance': self.account['balance'],
            'updated_at': formatted_date
        }

        # Load existing data from file
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            # If the file doesn't exist, initialize with empty lists
            data = {"accounts": [], "transactions": []}

        # Append new transaction to transactions list
        data['transactions'].append(transaction_log)

        # Write updated data back to file
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

    def open_deposit_window(self):
        deposit_window = tk.Toplevel(self.window)
        deposit_window.title("Deposit Amount")
        deposit_window.geometry("300x150")

        ttk.Label(deposit_window, text="Enter Deposit Amount:").pack(pady=10)
        deposit_entry = ttk.Entry(deposit_window)
        deposit_entry.pack(pady=10)

        def deposit():
            try:
                amount = float(deposit_entry.get())
                if amount <= 0:
                    messagebox.showerror("Invalid Amount", "Deposit amount must be greater than zero.")
                    return
                self.account['balance'] += amount
                self.update_balance_label()
                self.save_to_json()
                self.save_transaction(title="Deposit", amount=amount)
                messagebox.showinfo("Deposit Successful", f"Deposited {amount} successfully.")
                deposit_window.destroy()
            except ValueError:
                messagebox.showerror("Invalid Amount", "Please enter a valid number.")

        deposit_button = ttk.Button(deposit_window, text="Deposit", command=deposit)
        deposit_button.pack(pady=10)

    def open_withdraw_window(self):
        if self.account['balance'] < 1000:
            messagebox.showinfo("Deposit Error", "Balance less than 1000. Cannot deposit.")
            return
        withdraw_window = tk.Toplevel(self.window)
        withdraw_window.title("Withdraw Amount")
        withdraw_window.geometry("300x150")

        ttk.Label(withdraw_window, text="Enter Withdraw Amount:").pack(pady=10)
        withdraw_entry = ttk.Entry(withdraw_window)
        withdraw_entry.pack(pady=10)

        def withdraw():
            try:
                amount = float(withdraw_entry.get())
                if amount <= 0 or amount > self.account['balance']:
                    messagebox.showerror("Invalid Amount", "Withdraw amount must be greater than zero and less than balance.")
                    return
                self.account['balance'] -= amount
                self.update_balance_label()
                self.save_to_json()
                self.save_transaction(title="Withdraw", amount=amount)
                messagebox.showinfo("Withdraw Successful", f"Withdrew {amount} successfully.")
                withdraw_window.destroy()
            except ValueError:
                messagebox.showerror("Invalid Amount", "Please enter a valid number.")

        withdraw_button = ttk.Button(withdraw_window, text="Withdraw", command=withdraw)
        withdraw_button.pack(pady=10)

    def open_transfer_window(self):
        if self.account['balance'] < 1000:
            messagebox.showinfo("Deposit Error", "Balance less than 1000. Cannot deposit.")
            return
        transfer_window = tk.Toplevel(self.window)
        transfer_window.title("Transfer Fund")
        transfer_window.geometry("400x200")

        ttk.Label(transfer_window, text="Enter Recipient's Account Number:").pack(pady=10)
        recipient_entry = ttk.Entry(transfer_window)
        recipient_entry.pack(pady=10)

        ttk.Label(transfer_window, text="Enter Transfer Amount:").pack(pady=10)
        amount_entry = ttk.Entry(transfer_window)
        amount_entry.pack(pady=10)

        def transfer_fund():
            try:
                recipient_acc_num = recipient_entry.get()
                amount = float(amount_entry.get())

                # Validate recipient account number (for demo purposes)
                # You should have your own validation logic
                if not recipient_acc_num.isdigit() or len(recipient_acc_num) != 6:
                    messagebox.showerror("Invalid Recipient Account Number", "Please enter a valid 6-digit account number.")
                    return

                if amount <= 0 or amount > self.account['balance']:
                    messagebox.showerror("Invalid Amount", "Transfer amount must be greater than zero and less than balance.")
                    return

                # For demo, deduct amount from sender's balance
                self.account['balance'] -= amount
                self.update_balance_label()
                self.save_to_json()
                self.save_recipient_ammount(acc_num=recipient_acc_num, amount=amount)
                self.save_transaction(title=f"Transfer to {recipient_acc_num}", amount=amount)
                messagebox.showinfo("Transfer Successful", f"Transferred {amount} to account {recipient_acc_num} successfully.")
                transfer_window.destroy()

            except ValueError:
                messagebox.showerror("Invalid Amount", "Please enter a valid number.")

        transfer_button = ttk.Button(transfer_window, text="Transfer", command=transfer_fund)
        transfer_button.pack(pady=10)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        account = json.loads(sys.argv[1])
        app = UserHome(account)
        app.window.mainloop()
