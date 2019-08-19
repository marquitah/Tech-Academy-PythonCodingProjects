import tkinter
import tkinter.filedialog
from tkinter import *
import os
import sqlite3
from tkinter import filedialog
import shutil


class MainWindow(Frame):
    def __init__ (self, master):
        #Frame
        Frame.__init__(self,master)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 600))
        self.master.title('GUIDrill3')
        self.master.config(bg='lavender')

        #Variables   
        self.txtFiles = StringVar()
        self.txtFiles2 = StringVar()
        
        
        

        
        #select files from source directory            
        def Files(self):
                self.txtFiles = StringVar()
                current_directory = filedialog.askdirectory()
                file_name = ""
                file_path = os.path.join(current_directory,file_name).replace("\\","/")
                print(file_path)


                getFile(self,file_path)

        def getFile(self,file_path):
            self.txtFiles.set(file_path)


            #Entry Box for selected file
            self.txtFiles = Entry(self.master, text=self.txtFiles, font=("Tahoma", 16), fg='black', bg='white',width = 37)
            self.txtFiles.grid(row=4, column=3,padx=(20,100), pady=(100,0), sticky=S)

                        

        #To select destination path
        def destination(self):
            self.txtFiles2 = StringVar()
            selectedFile = filedialog.askdirectory()
            selectedFile2 = ""

            destinationPath = os.path.join(selectedFile,selectedFile2).replace("\\","/")
            print(destinationPath)

            printDestinationPath(self,destinationPath)

        def printDestinationPath(self,destinationPath):
            self.txtFiles2.set(destinationPath)

            #Entry Box for destination file path
            self.txtFiles2 = Entry(self.master, text=self.txtFiles2, font=("Tahoma", 16), fg='black', bg='white',width = 37)
            self.txtFiles2.grid(row=5, column=3,padx=(20,100), pady=(100,0), sticky=S)

            


        #To iterate through .txt files within source directory
        def IterateFiles(self,file_path):
            files = ''
            current_directory = filedialog.askdirectory()
            file_name = ''
            file_path = os.path.join(current_directory,file_name).replace("\\","/")
            for files in os.listdir(file_path):
                if files.endswith('.txt.'):
                    joinPath = (os.path.join(file_path,files))
                    time = (os.path.getmtime(joinPath))
                    print(joinPath,time)

                    
            moveFiles(self,joinPath,time,destinationPath,file_path)
    
        #move files from source directory to destination directory and print to destination directory
        def moveFiles(self,joinPath,time,destinationPath,file_path):
            self.txtFiles3.set(joinPath)
            files = ''
            current_directory = filedialog.askdirectory()
            file_name = ""
            file_path = os.path.join(current_directory,file_name).replace("\\","/")
            destinationPath = os.path.join(selectedFile,selectedFile2).replace("\\","/")
            #path = file_path
            for files in os.listdir(file_path):
                if files.endswith('.txt'):
                    shutil.move(file_path,destinationPath)
                    







        #Button1 to browse files from source directory
        self.btnBrowse = Button(self.master, text="Source Directory:\nBrowse All Files", width=13, height=2, command = lambda: Files(self))
        self.btnBrowse.grid(row=4, column=2,padx=(20,100), pady=(100,0), sticky=S)


        #Entry Box1 for selected file
        self.txtFiles = Entry(self.master, text=self.txtFiles, font=("Tahoma", 16), fg='black', bg='white',width = 37)
        self.txtFiles.grid(row=4, column=3,padx=(20,100), pady=(100,0), sticky=S)


        #Button2 for destination directory
        self.btnBrowse2 = Button(self.master, text="Destination\nDirectory", width=13, height=2, command = lambda: destination(self))
        self.btnBrowse2.grid(row=5, column=2,padx=(20,100), pady=(100,0), sticky=S)

        #Entry Box for destination file path
        self.txtFiles2 = Entry(self.master, text=self.txtFiles2, font=("Tahoma", 16), fg='black', bg='white',width = 37)
        self.txtFiles2.grid(row=5, column=3,padx=(20,100), pady=(100,0), sticky=S)
    

        #Button3 to browse .txt files
        self.btnBrowseTxt = Button(self.master, text="Move .txt Files", width=13, height=2,command = lambda: IterateFiles(self,file_path))
        self.btnBrowseTxt.grid(row=7, column=2,padx=(20,100), pady=(100,0), sticky=S)
        





if __name__ == "__main__":
    root = Tk()
    App = MainWindow(root)
    root.mainloop()
