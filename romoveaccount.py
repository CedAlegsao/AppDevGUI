import tkinter as tk

class RemoveAccount:
    def __init__(self, parent):
        self.window = tk.Toplevel()
        self.window.title("Remove Account")

if __name__ == "__main__":
    root = tk.Tk()
    app = RemoveAccount()
    app.mainloop()