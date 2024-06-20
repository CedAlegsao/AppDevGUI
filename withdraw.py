import tkinter as tk

class Withdraw:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Withdraw")

if __name__ == "__main__":
    root = tk.Tk()
    app = Withdraw(root)
    root.mainloop()
