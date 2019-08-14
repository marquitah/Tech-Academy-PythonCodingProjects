import tkinter
from tkinter import *


class guiDrill(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(656, 225))
        self.master.title('Check files')
        self.master.configure(bg='lightgray')

        self.varFirstLine = StringVar()
        self.varSecondLine = StringVar()

        self.btnBrowse = Button(self.master, text="Browse...", font=("Tahoma", 12), width=15, height=1)
        self.btnBrowse.grid(row=1, column=0,padx=(30,0),pady=(55,0))

        self.btnBrowse = Button(self.master, text="Browse...", font=("Tahoma", 12), width=15, height=1)
        self.btnBrowse.grid(row=2, column=0,padx=(30,0),pady=(15,0))


        self.btnCheckforfiles = Button(self.master, text="Check for files...", font=("Tahoma", 12), width=15, height=2)
        self.btnCheckforfiles.grid(row=4, column=0,padx=(30,0),pady=(15,0))



        self.txtName = Entry(self.master, text=self.varFirstLine, font=("Tahoma", 16), fg='black', bg='white', width = 37)
        self.txtName.grid(row=1, column=1, padx=(30,0), pady=(55,0))

        self.txtName = Entry(self.master, text=self.varSecondLine, font=("Tahoma", 16), fg='black', bg='white', width = 37)
        self.txtName.grid(row=2, column=1, padx=(30,0), pady=(15,0))



        self.btnCloseProgram = Button(self.master, text="Close Program", font=("Tahoma", 12), width=15, height=2)
        self.btnCloseProgram.grid(row=4, column=1,padx=(298,0),pady=(15,0))









if __name__ == "__main__":
    root = Tk()
    App = guiDrill(root)
    root.mainloop()
