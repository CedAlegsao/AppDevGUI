import tkinter as tk

class ShowVIP:
    def __init__(self, parent):
        self.window = tk.Toplevel()
        self.window.title("Show VIP Account")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ShowVIP(root)
    app.mainloop()