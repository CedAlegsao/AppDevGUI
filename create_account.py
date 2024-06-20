import tkinter as tk
from tkinter import ttk
import math
import random
import json


class CreateAccount:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Create Account")

        label = ttk.Label(self.window, text="Create Account")
        label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        # Account Name
        acc_name_label = ttk.Label(self.window, text="Account Name:")
        acc_name_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.acc_name_entry = ttk.Entry(self.window)
        self.acc_name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Account Type
        account_types = ["Savings", "Checking", "Investment", "Other"]
        selected_account_type = tk.StringVar()
        selected_account_type.set(account_types[0])  # Set default value
        label_account_type = ttk.Label(self.window, text="Account Type:")
        label_account_type.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.dropdown_account_type = ttk.Combobox(self.window, textvariable=selected_account_type, values=account_types, state="readonly", width=27)
        self.dropdown_account_type.grid(row=2, column=1, padx=5, pady=5)

        # Gender
        genders = ["Male", "Female", "Other"]
        selected_gender = tk.StringVar()
        selected_gender.set(genders[0])  # Set default value
        label_gender = ttk.Label(self.window, text="Gender:")
        label_gender.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.dropdown_gender = ttk.Combobox(self.window, textvariable=selected_gender, values=genders, state="readonly", width=27)
        self.dropdown_gender.grid(row=3, column=1, padx=5, pady=5)

        # Address
        label_address = ttk.Label(self.window, text="Address:")
        label_address.grid(row=4, column=0, sticky="ne", padx=5, pady=5)
        self.entry_address = ttk.Entry(self.window, width=30)
        self.entry_address.grid(row=4, column=1, padx=5, pady=5)

        # Message
        self.message = tk.Text(self.window, wrap="word", height=3, width=40)
        self.message.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        # Create Button
        create_button = ttk.Button(self.window, text="Create", command=self.create_account)
        create_button.grid(row=6, column=0)

        btn_back_home = ttk.Button(self.window, text='Cancel', command=self.cancel)
        btn_back_home.grid(row=6, column=1, pady=10, padx=10)


    def create_account(self):
        # get all input data
        acc_name = self.acc_name_entry.get()
        acc_type = self.dropdown_account_type.get()
        gender = self.dropdown_gender.get()
        address = self.entry_address.get()
        balance = 0 # setting the defaul value of balance

        # generate user id using random and math
        digits = [i for i in range(0,10)]
        # generate an account number.
        accNum = ""
        for i in range(6):
            index = math.floor(random.random()*10)
            accNum += str(digits[index])
        
         # Construct account object
        account = {
            'accNum': accNum,
            'accName':acc_name,
            'accountType':acc_type,
            'gender':gender,
            'address':address,
            'balance': balance,
            'isAdmin': False
        }

        # Load existing data from file
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            # If the file doesn't exist, initialize with empty lists
            data = {"accounts": [], "transactions": []}
        
        # Check if the generated account number already exists
        if any(account['accNum'] == acc['accNum'] for acc in data['accounts']):
            self.message.delete(1.0, tk.END)
            self.message.insert(tk.END, "Error: Account number already exists, please try again.")
            return

        # Append new account to the accounts list
        data["accounts"].append(account)
        # Write updated data back to file
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

        # Display success message
        self.message.delete(1.0, tk.END)
        self.message.insert(tk.END, "Account created successfully!")

         # Schedule window destruction after 3000 milliseconds (3 seconds)
        self.window.after(2000, self.window.destroy)


    def cancel(self):
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CreateAccount(root)
    root.mainloop()
