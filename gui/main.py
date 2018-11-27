#test
import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.layout()
        self.login()
    
    def center(self): # Basically edited stackoverflow... XD
        self.master.withdraw()
        self.master.update_idletasks()
        self.x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
        self.y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 2
        self.master.geometry()
        self.master.deiconify()
    
    def login(self): # This is defining the login window on the initial starting page
        self.master.title("Shared Power")
        self.master.geometry("300x100")
        self.master.maxsize(300, 100)
        self.master.minsize(300, 100)

        self.submitButton = ttk.Button(self.master, text="Login", command=self.layout)
        self.submitButton.grid(row=0, column=0)

    def layout(self):
        self.master.title("Shared Power")
        self.master.geometry("500x500")
        self.master.maxsize(self.master.winfo_screenwidth(), self.master.winfo_screenheight())
        self.master.minsize(500, 500)
        self.center()
        
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
    
        self.label1 = ttk.Label(tab1, text="This is a test!")
        self.label1.grid(row=0, column=0)
    
    def listBlock(self):
        self.listbox = listbox(tab1)

        self.listbox.insert(1, "something")

        self.listbox.grid(row=1, column=1, columnspan=5, rowspan=5, sticky="NESW")

# Define Window
window = tk.Tk() 
app = Application(master=window)
app.mainloop()