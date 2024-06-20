import tkinter as tk

class TransferFund:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("TransferFund")

if __name__ == "__main__":
    root = tk.Tk()
    app = TransferFund(root)
    root.mainloop()
