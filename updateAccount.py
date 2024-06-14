import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Import messagebox directly
import json

class UpdateAccount:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Update Account")
        self.window.geometry("400x400")

        # Account Number Entry
        self.acc_number_label = ttk.Label(self.window, text="Enter Account Number:")
        self.acc_number_label.pack(pady=10)
        
        self.acc_number_entry = ttk.Entry(self.window)
        self.acc_number_entry.pack(pady=5)

        # New Name Entry
        self.new_name_label = ttk.Label(self.window, text="Enter New Name:")
        self.new_name_label.pack(pady=10)
        
        self.new_name_entry = ttk.Entry(self.window)
        self.new_name_entry.pack(pady=5)

        # New Address Entry
        self.new_address_label = ttk.Label(self.window, text="Enter New Address:")
        self.new_address_label.pack(pady=10)
        
        self.new_address_entry = ttk.Entry(self.window)
        self.new_address_entry.pack(pady=5)

        # Update Button
        self.update_button = ttk.Button(self.window, text="Update Account", command=self.update_account)
        self.update_button.pack(pady=10)

    def update_account(self):
        acc_num = self.acc_number_entry.get().strip()
        new_name = self.new_name_entry.get().strip()
        new_address = self.new_address_entry.get().strip()

        # Load data from JSON file
        with open('data.json', 'r') as f:
            data = json.load(f)

        account_found = False
        for account in data['accounts']:
            if account['accNum'] == acc_num:
                if new_name:
                    account['accName'] = new_name
                if new_address:
                    account['address'] = new_address
                account_found = True
                break
        
        if not account_found:
            # Account not found, show error message
            messagebox.showerror("Error", f"Account with number {acc_num} not found.")
            return

        # Write updated data back to file
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

        # Show success message
        messagebox.showinfo("Success", f"Account {acc_num} updated successfully.")
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateAccount(root)
    root.mainloop()
