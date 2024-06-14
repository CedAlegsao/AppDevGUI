import tkinter as tk
from tkinter import ttk, messagebox
import json

class RemoveAccount:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Remove Account")
        self.window.geometry("400x150")

        # Account Number Entry
        self.acc_number_label = ttk.Label(self.window, text="Enter Account Number:")
        self.acc_number_label.pack(pady=10)
        
        self.acc_number_entry = ttk.Entry(self.window)
        self.acc_number_entry.pack(pady=5)

        # Remove Button
        self.remove_button = ttk.Button(self.window, text="Remove Account", command=self.remove_account)
        self.remove_button.pack(pady=10)

    def remove_account(self):
        acc_num = self.acc_number_entry.get().strip()

        # Load data from JSON file
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Find account with matching accNum and remove it
        updated_accounts = [acc for acc in data['accounts'] if acc['accNum'] != acc_num]

        if len(updated_accounts) == len(data['accounts']):
            # Account not found, show error message
            messagebox.showerror("Error", f"Account with number {acc_num} not found.")
            return

        # Update data dictionary
        data['accounts'] = updated_accounts

        # Write updated data back to file
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

        # Show success message
        messagebox.showinfo("Success", f"Account {acc_num} removed successfully.")
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RemoveAccount(root)
    root.mainloop()
