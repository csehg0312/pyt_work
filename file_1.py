from tkinter import *

from tkinter import filedialog

#Function for opening the
#file explorer window
def browserFiles():
	filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetypes = (("Text Files" , "*.txt*"), ("all files" , "*.*")))

#Change label contents
	label_file_explorer.configure(text="File Opened:  "+filename)

#Create the root window
window = Tk()

#Set window title
window.title('File Explorer')

#Set window size
window.geometry("750x500")

#Set window background
window.config(background = "white")

#Creating a label 
label_file_explorer = Label(window, text = "File explorer in Python" , width = 100, height = 4, fg = "blue" )

button_explore = Button(window, text = "Browse Files" , command = browseFiles)

button_exit = Button(window, text = "Exit" , command = exit)

label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1, row = 3)

window.mainloop()