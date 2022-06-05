import tkinter as tk
from tkinter import TOP, ttk

class mainapp(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.title = ttk.Label(text='Wikityper', font=('Helvetica', 54))
        self.title.pack(side=TOP)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1920x1080')
    app = mainapp(root)
    app.mainloop()