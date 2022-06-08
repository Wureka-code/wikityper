import tkinter as tk
from tkinter import TOP, ttk

from matplotlib.figure import Figure
import wikiget
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import graphcreation as grc
import numpy as np 

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
        self.entrypassage = 0 # used to get entrypassage 
        self.passage = 'fortnite testing 123 abc test' #wikiget.getsum()
        self.passagelabel = tk.Message(text=self.passage, font=('helvetica', 24), width=800)
        self.passagelabel.place(relx=.5, rely=.3, anchor='c')
        self.startbutton.destroy()
        self.starttime = time.time()
        self.kpsvar = [] # used for tracking stats
        
        def update(): #updates every 1/10th of a second and checks if the text is finished. if it is finished, displays results.
            
            if self.entrybar.get() is not None:
                self.entrydata = len(self.entrybar.get())
                print(f'DEBUG : {self.entrydata} to get to {len(self.passage)}')
            else:
                self.entrydata = 0

            if self.entrypassage < self.entrydata:
                self.kpsvar.append(self.entrydata - self.entrypassage) 
                self.entrypassage = self.entrydata
                print(f'DEBUG : working entrypassage update. entrypassage is at {self.entrypassage}')
            elif self.kpsvar:
                self.kpsvar.append(self.kpsvar[-1])
                print('DEBUG : kpsvar update no change')
            else:
                self.kpsvar.append(0)
                print('DEBUG : kpsvar append 0')
                

            
            if self.entrypassage == len(self.passage):
                print('DEBUG : successful finish')

                self.endtime = time.time()
                self.finishtime = round(self.endtime - self.starttime, 2)
                self.kps = round(len(self.passage) / self.finishtime, 2)
                
                self.difference = (sum(self.entrybar.get()[i] != self.passage[i] for i in range(len(self.passage))))
                
                self.timelabel = ttk.Label(text=f'Congratulations! you completed this text in {self.finishtime} seconds. your KPS was {self.kps}, and you got {self.difference} letters wrong.')
                
                self.passagelabel.destroy()
                self.timelabel.place(relx=.5, rely=.3, anchor="c")

                # getting mpl graphs ready 
                print(f'DEBUG : entered graph values are {self.kpsvar} and {range(round(self.finishtime))}')
                
                plot = grc.creategraphs(self.kpsvar, range(round(self.finishtime)))
                kpschart = FigureCanvasTkAgg(plot, self)
                kpschart.get_tk_widget().place(relx=.4, rely=.6)
            else:
                self.after(100, update)
            
        self.after(100, update)
    
        
        
        
       

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1920x1080')
    app = mainapp(root)
    app.mainloop()