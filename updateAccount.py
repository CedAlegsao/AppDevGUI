import tkinter as tk

class UpdateAccount:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Update Accont")

if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateAccount(root)
    app.mainloop()