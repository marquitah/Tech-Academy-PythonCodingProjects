import tkinter
import tkinter.filedialog
from tkinter import *
import os



class ButtonTextWidget(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(400, 400))
        self.master.title('GUI Drill 2')
        self.master.config(bg='lightgreen')

        self.varFilePath = StringVar()

        
        self.lblFilePath = Label(self.master,text='Hit the button for your file path!', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFilePath.grid(row=0, column=0,padx=(50,50), pady=(50,0))
            
        
        self.btnFilePath = Button(self.master, text="Click here!", width=10, height=2, command = lambda: Files(self))
        self.btnFilePath.grid(row=2, column=0, padx=(0,0),pady=(20,0))


def Files(self):
        current_directory = filedialog.askdirectory()
        file_name = ""
        file_path = os.path.join(current_directory,file_name)
        print(file_path)


        getFile(self,file_path)

def getFile(self,file_path):
    self.varFilePath.set(file_path)


    self.txtSearch = Entry(self.master, text = self.varFilePath, font=("Helvetica", 14), fg = 'black', bg = 'white')
    self.txtSearch.grid(row=3, column=0, columnspan = 2, padx=(25,0), pady=(40,0))
        




if __name__ == "__main__":
    root = Tk()
    App = ButtonTextWidget(root)
    root.mainloop()
