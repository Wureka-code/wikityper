import tkinter as tk
from tkinter import TOP, ttk
import wikiget

class mainapp(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.title = ttk.Label(text='Wikityper', font=('Helvetica', 54))
        self.title.pack(side=TOP)
        
        #main bar used for entry
        self.entrybar = ttk.Entry()
        self.entrybar.place(relx=.5, rely=.5, anchor='c', width=800)

        self.startbutton = ttk.Button(command=lambda : self.startgame(), text='start')
        self.startbutton.place(relx=.5, rely=.3, anchor='c')
    
    def startgame(self):
        passage = wikiget.getsum()
        self.passagelabel = tk.Message(text=passage, font=('helvetica', 24), width=800)
        self.passagelabel.place(relx=.5, rely=.3, anchor='c')
        self.startbutton.destroy()
        

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1920x1080')
    app = mainapp(root)
    app.mainloop()