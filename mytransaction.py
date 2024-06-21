import tkinter as tk

class MyTransaction:
    def __init__(self, parent, accNum):
        self.accNum = accNum
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("MyTransaction")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyTransaction(root)
    root.mainloop()
