#test
import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.layout()

    def layout(self):
        self.master.title("Shared Power")
        #self.master.geometry("1000x500")
        self.master.maxsize(self.master.winfo_screenwidth(), self.master.winfo_screenheight())
        
        rows = 0
        while rows < 50:
            self.master.rowconfigure(rows, weight=1)
            self.master.columnconfigure(rows, weight=1)
            rows += 1

        self.tabBlock()

    def tabBlock(self):
        style = ttk.Style(self.master)
        style.configure("lefttab.TNotebook", tabposition="wn")
        #style.configure("lefttab.TNotebook", tabmargins="10")
        style.configure("lefttab.TNotebook", padding="10")
        style.configure("TNotebook.Tab", padding="20")

        self.notebook = ttk.Notebook(self.master, style='lefttab.TNotebook')

        tab1 = ttk.Frame(self.notebook, width=500, height=500)
        tab2 = ttk.Frame(self.notebook, width=500, height=500)
        tab3 = ttk.Frame(self.notebook, width=500, height=500)
        tab4 = ttk.Frame(self.notebook, width=500, height=500)
        self.notebook.add(tab1, text=f'{"Search": ^20s}')
        self.notebook.add(tab2, text=f'{"Add New": ^18s}')
        self.notebook.add(tab3, text=f'{"Invoice": ^21s}')
        self.notebook.add(tab4, text=f'{"Profile": ^22s}')

        self.notebook.grid(row=0, column=0, columnspan=5, rowspan=5, sticky="NESW")
    
    def listBlock(self):
        self.listbox = listbox(tab1)

        self.listbox.insert(1, "something")

        self.listbox.grid(row=1, column=1, columnspan=5, rowspan=5, sticky="NESW")



# Define Window
window = tk.Tk() 
app = Application(master=window)
app.mainloop()