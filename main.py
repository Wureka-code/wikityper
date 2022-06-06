import tkinter as tk
from tkinter import TOP, ttk
import wikiget
import time

class mainapp(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.passage = ''

        self.title = ttk.Label(text='Wikityper', font=('Helvetica', 54))
        self.title.pack(side=TOP)
        
        #main bar used for entry
        self.entrybar = ttk.Entry()
        self.entrybar.place(relx=.5, rely=.5, anchor='c', width=800)

        self.startbutton = ttk.Button(command=lambda : self.startgame(), text='start')
        self.startbutton.place(relx=.5, rely=.3, anchor='c')

        
    
    def startgame(self):
        # define variables 
        self.entrypassage = None # used to get entrypassage 
        self.passage = wikiget.getsum()
        self.passagelabel = tk.Message(text=self.passage, font=('helvetica', 24), width=800)
        self.passagelabel.place(relx=.5, rely=.3, anchor='c')
        self.startbutton.destroy()
        self.starttime = time.time()
        
        def update(): #updates every 1/10th of a second and checks if the text is finished. if it is finished, displays results.
            self.entrypassage = self.entrybar.get() 
            print(self.entrypassage)
            if self.entrypassage == self.passage:
                self.endtime = time.time()
                self.finishtime = round(self.endtime - self.starttime, 2)
                self.kps = round(len(self.passage) / self.finishtime, 2)
                
                self.timelabel = ttk.Label(text=f'Congratulations! you completed this text in {self.finishtime} seconds. your KPS was {self.kps}')
                
                self.passagelabel.destroy()
                self.timelabel.place(relx=.5, rely=.3, anchor="c")
            else:
                self.after(100, update)
        self.after(100, update)
    
        
        
        
       

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1920x1080')
    app = mainapp(root)
    app.mainloop()