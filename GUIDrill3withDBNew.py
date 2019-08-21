import tkinter
import tkinter as tk
import tkinter.filedialog
from tkinter import *
import os
import sqlite3
from tkinter import filedialog
import shutil
import time

class MainWindow(Frame):
    def __init__(self, master):
        #Frame
        Frame.__init__(self, master)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 600))
        self.master.title('GUIDrill3')
        self.master.config(bg='lavender')

        #Variables   
        self.txtFiles = StringVar()
        self.txtFiles2 = StringVar()

        # Button1 to browse files from source directory
        self.btnBrowse = Button(self.master, text="Source Directory:\nBrowse All Files", width=13, height=2,
                                command=lambda: Files(self))
        self.btnBrowse.grid(row=4, column=2, padx=(20, 100), pady=(100, 0), sticky=S)

        # Entry Box1 for selected file
        self.txtField = Entry(self.master, text=self.txtFiles, font=("Helvetica", 16), fg='black', bg='white', width=37)
        self.txtField.grid(row=4, column=3, padx=(20, 100), pady=(100, 0), sticky=S)

        # Button2 for destination directory
        self.btnBrowse2 = Button(self.master, text="Destination\nDirectory", width=13, height=2,
                                 command=lambda: getFile(self))
        self.btnBrowse2.grid(row=5, column=2, padx=(20, 100), pady=(100, 0), sticky=S)

        # Entry Box2 for destination file path
        self.txtField2 = Entry(self.master, text=self.txtFiles2, font=("Helvetica", 16), fg='black', bg='white',
                               width=37)
        self.txtField2.grid(row=5, column=3, padx=(20, 100), pady=(100, 0), sticky=S)

        # Button3 to browse .txt files
        self.btnBrowseTxt = Button(self.master, text="Move .txt Files", width=13, height=2,
                                   command=lambda: destination(self))
        self.btnBrowseTxt.grid(row=7, column=2, padx=(20, 100), pady=(100, 0), sticky=S)

#select files from source directory and destination directory
def Files(self):
    self.txtFiles.set(filedialog.askdirectory())

def getFile(self):
    self.txtFiles2.set(filedialog.askdirectory())

#To iterate through files
def destination(self):
    self.sourceDirectory = self.txtFiles.get()
    self.destinationDirectory = self.txtFiles2.get()
    self.files = os.listdir(self.sourceDirectory)
    for files in self.files:
        if files.endswith(".txt"):
            self.absolutePath = os.path.join(self.sourceDirectory, files)
            shutil.copy(self.absolutePath, self.destinationDirectory)
    database(self)

#creates database and updates database with .txt files and timestamp
def database(self):
    conn = sqlite3.connect('dbGUIDrill3.db')

    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_txtFiles TEXT)")

    conn.commit()
    conn.close()

    conn = sqlite3.connect('dbGUIDrill3.db')

    with conn:
        cur = conn.cursor()
        #cur.execute("ALTER TABLE tbl_txtFiles ADD col_timeStamp")
        self.files = os.listdir(self.destinationDirectory)
        for files in self.files:
            self.filePath = os.path.join(self.destinationDirectory, files)
            cur.execute("INSERT INTO tbl_txtFiles (col_txtFiles,col_timeStamp) VALUES (?,?)",
                        (files, str(time.ctime(os.path.getmtime(self.filePath))),))
            print(self.filePath, str(time.ctime(os.path.getmtime(self.filePath))))

        conn.commit()
    conn.close()


if __name__ == "__main__":
    root = Tk()
    App = MainWindow(root)
    root.mainloop()
