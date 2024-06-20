import tkinter as tk

class Deposit:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Deposit")

if __name__ == "__main__":
    root = tk.Tk()
    app = Deposit(root)
    root.mainloop()
