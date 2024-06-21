import tkinter as tk
from tkinter import  ttk, messagebox
import json
import math
import random
import datetime

class TransferFund:
    def __init__(self, parent, accNum):
        self.accNum = accNum
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("TransferFund")

        self.label = ttk.Label(self.window, text="Enter reciever account number:")
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.reciever_accNum = ttk.Entry(self.window)
        self.reciever_accNum.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.label = ttk.Label(self.window, text="Enter amount to transfer:")
        self.label.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

        self.amount_to_trans = ttk.Entry(self.window)
        self.amount_to_trans.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        btn_login = ttk.Button(self.window, text="Transfer", command=self.handleTranferFund)
        btn_login.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    def handleTranferFund(self):
        reciever_accNum = self.reciever_accNum.get()
        amount_to_trans = self.amount_to_trans.get()

        if len(reciever_accNum) == 6 and reciever_accNum.isdigit():
            if len(amount_to_trans) > 0 and float(amount_to_trans) >= 1000:
                self.saveTransferFund(reciever_accNum, amount_to_trans)
            else:
                messagebox.showerror("Error", f"Error: Ammount({amount_to_trans}) to transfer must be greater than 1000.")
                self.window.destroy()
        else:
            messagebox.showerror("Error", "Error: Please check the reviever account number and try again.")
            self.window.destroy()

    def saveTransferFund(self, reciever_accNum, amount_to_trans):

        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("File not Found", "Error: Database file not found!")
            return

        reciever_acc_found = False

        for account in data['accounts']:
            if account['accNum'] == str(reciever_accNum):
                reciever_acc_found = True
                account['balance'] += float(amount_to_trans)
                break
                
        if reciever_acc_found:
            acc_found = False

            for account in data['accounts']:
                if account['accNum'] == str(self.accNum):
                    acc_found = True
                    account['balance'] -= float(amount_to_trans)
                    new_user_balance = account['balance']
                    break

            if acc_found:
                try:
                    with open('data.json', 'w') as f:
                        json.dump(data, f, indent=4)
                    messagebox.showinfo("Success", f"Successfully tranfered {amount_to_trans} to account {reciever_accNum}.")
                    self.saveTransaction(reciever_accNum, amount_to_trans, new_user_balance)
                    self.window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save data: {e}")
        else:
            messagebox.showerror("Error", "Error: Receiver account number not found.")

    def saveTransaction(self, reciever_accNum, amount_to_trans, new_user_balance):

        todays_date = datetime.date.today()
        formatted_date = todays_date.strftime("%A, %B %d, %Y")

        # generate transaction number
        digits = [i for i in range(0, 10)]
        trans_ref = "".join(str(digits[math.floor(random.random() * 10)]) for _ in range(6))

        transaction = {
            "accNum": self.accNum,
            "title": f"Tranfer to {reciever_accNum}",
            "amount": amount_to_trans,
            "balance": float(new_user_balance),
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
    app = TransferFund(root)
    root.mainloop()
