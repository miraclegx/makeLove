# a simple program to make love files
# cool file name huh :)
import zipfile
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

saveTo = ''
outputName = ''
mainDirectory = ''

def zipAll(directory, outputName):
    with zipfile.ZipFile(outputName, 'w') as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                # Add the file to the zip, preserving the directory structure
                arcname = os.path.relpath(file_path, start=directory)
                zipf.write(file_path, arcname)
    print("zipped the shit :)")

#zipAll(directory,outputName)

def buildLove():
	zipAll(mainDirectory+'/','fuck.zip')
	#rename()

def rename():
	shutil.move(outputName,outputName+'.love')	

def selectDirectory():
	directory = tk.filedialog.askdirectory()
	mainDirectory = directory

root = tk.Tk()
root.geometry('400x400')
root.title('create main.lua')

loveLogo = tk.PhotoImage(file='love.png')
loveImageLabel = tk.Label(text='love Logo').place(x=170,y=10)
#loveImageLabel['image'] = loveLogo

InfoLabel = tk.Label(text='click the button to select the folder').place(x=100,y=70)
selectButton = tk.Button(text='Click Me :)',command=selectDirectory).place(x=150,y=100)

goAheadButton = tk.Button(text='Build Love',command=buildLove).place(x=150,y=200)

root.mainloop()