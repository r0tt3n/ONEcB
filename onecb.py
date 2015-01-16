### ONEcB - One Click Backup v1.0 by G.C. Gerba
import sys
import os
import shutil
from tkinter import *
import tkinter.messagebox
gui = Tk()
gui.geometry('200x100')
gui.title("ONEcB")
path = '~'
destination = str(os.getcwd()) +  str("/backup")
source = os.path.expanduser(path)
photo = PhotoImage(file="onecb.gif")
label = Label(image=photo).place(x=35, y=5)
def copyhome():
    if os.name == 'posix' or os.name == 'nt':
        try:
            shutil.copytree(source, destination)
            tkinter.messagebox.showinfo("Success!", "Files were successfully copied")
        except:
            tkinter.messagebox.showerror("Error", "Permission Denied\nor folder alredy exists")
    else:
        print("Unrecognized OS")
copy = Button(text="Copy to USB", command=copyhome)
copy.place(x=20,y=60)
guiexit = Button(text="Exit", command=gui.quit)
guiexit.place(x=130,y=60)
gui.mainloop()

### TODO:
### real world test.
