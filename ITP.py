#Made by Sebastián HC Username: Animalsebas
import tkinter
import tkinter.font
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename
import img2pdf
import os
def Process():
    Tk().withdraw()
    listPages = filedialog.askopenfilenames(title = "Select files", filetypes = (("jpeg files","*.jpg"), ("all files", "*.*")))
    images = []
    for i in listPages:
        print(i)
        images.append(i)
    pdfFilename = filedialog.asksaveasfilename(parent=window, initialdir=os.getcwd(), title="Save as", filetypes= (("pdf files", "*.pdf"), ("all files", "*.*")), defaultextension = ".pdf")
    pdfFilename = str(pdfFilename)
    with open(pdfFilename,"wb") as f:
        f.write(img2pdf.convert(images))
#Main window
window = tkinter.Tk()
window.geometry("600x480")
window.title("Image to PDF")
window.configure(background = "light gray")
window.resizable(False, False)
program_version = tkinter.Label(window, text = "Version Pre-Alpha", font = "Arial 15")
program_version.pack(side = tkinter.BOTTOM)
#Title Label
title = tkinter.Label(window, text = "Image to PDF", bg = "gray", font = "Arial 30")
title.pack(fill = tkinter.X)
#Programmer Label
made_by = tkinter.Label(window, text = "Made by SHC Software on Python", font = "Arial 15")
made_by.pack(side = tkinter.BOTTOM)
#Image Button
button_Image = tkinter.Button(window, text = "Select Images \n and Convert", font = "Arial 20", command = Process)
button_Image.configure(width = 13, height = 2)
button_Image.place(x = 190, y = 160)
window.mainloop()
