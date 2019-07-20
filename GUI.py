
import Tkinter 
import FileDialog
import os
import Tkinter as tk
from Tkinter import *
import tkFileDialog
from tkFileDialog import askopenfilename
import sys

import source_code
from source_code import *


window=tk.Tk()
#####################################
#provinding title to the dialog box
#uising geometry func to resize the dialog box

window.title("TEXT ANALYSIS " )
window.geometry("500x400")

label0=tk.Label(text= " Text analytics is the process of drawing meaning out of written communication.")
label0.grid()

###############################################

label=tk.Label(text="Upload the file you want to analyse: " )
label.grid()

#######################################################
#this func help user to search for the the txt files 
def filed():
    root=Tkinter.Tk()
    root.withdraw()
    root.fileName=tkFileDialog.askopenfilename(filetype=(("Text file","*.txt",".pdf"),("All files","*.*")),)
    file_name=root.fileName
    root.title(root.fileName)
    text=open(file_name).read()
    #print file_name
    #print text
    return text

###################################################
def open_display():
    taking=filed()

    display=tk.Text(master=window, height = 70, width=50)
    display.grid()
    display.insert(tk.END,taking)
    
    
########################################################

button1= tk.Button( text="Browse" , command=open_display)
#button1=tk.Button(window, text='Browse', command=DisplayDir(root.fileName)).pack()
button1.grid()

button2=tk.Button(text="Start Analysis",command = source_code.action)
button2.grid()


window.mainloop()


