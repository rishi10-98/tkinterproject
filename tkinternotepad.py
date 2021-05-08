from tkinter import *
import tkinter.messagebox as tmsg
import os
from tkinter.filedialog import askopenfilename,asksaveasfile 
 ### all commands 
def newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    textspace.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("all files","*.*"),("text document","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file))
        textspace.delete(1.0,END)
        f=open(file,"r")
        textspace.insert(1.0,f.read())
        f.close()
def savefile():
    global file
    if file==None:
        file=asksaveasfile(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("all files","*.*"),("text document","*.txt")])
def exitfile():
    root.destroy()
def cutfile():
    textspace.event_generate("<<Cut>>")
def copyfile():
    textspace.event_generate("<<Copy>>")
def pastefile():
    textspace.event_generate("<<Paste>>")
def aboutfile():
    tmsg.showinfo("Notepad","Notepad by creative hub")

if __name__=='__main__':
    root=Tk()
    root.title("NOTEPAD")
    root.geometry("690x550")
    root.wm_iconbitmap("icon.ico")
    textspace=Text(root,font=14)
    file=None
    textspace.pack(expand=True,fill=BOTH)
    menubar=Menu(root)
      #file_icons
    new_icon=PhotoImage(file='icons2/icons2/new.png')
    open_icon=PhotoImage(file='icons2/icons2/open.png')
    save_icon=PhotoImage(file='icons2/icons2/save.png')
    exit_icon=PhotoImage(file='icons2/icons2/exit.png')

       #FILEMENU
    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_command(label="New",image=new_icon,compound=LEFT,command=newfile,accelerator='Ctrl+N')
    filemenu.add_command(label="Open",image=open_icon,compound=LEFT,command=openfile,accelerator='Ctrl+O')
    filemenu.add_command(label="Save",image=save_icon,compound=LEFT,command=savefile,accelerator='Ctrl+S')
    filemenu.add_command(label="Exit",image=exit_icon,compound=LEFT,command=exitfile,accelerator='Ctrl+Q')
    menubar.add_cascade(label="File",menu=filemenu)
      #edit_icon
    copy_icon=PhotoImage(file='icons2/icons2/copy.png')
    cut_icon=PhotoImage(file='icons2/icons2/cut.png')
    paste_icon=PhotoImage(file='icons2/icons2/paste.png')
    root.config(menu=menubar)
     #EDITMENU
    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label="Cut",image=cut_icon,compound=LEFT,command=cutfile,accelerator="Ctrl+X")
    editmenu.add_command(label="Copy",image=copy_icon,compound=LEFT,command=copyfile,accelerator="Ctrl+C")
    editmenu.add_command(label="Paste",image=paste_icon,compound=LEFT,command=pastefile,accelerator="Ctrl+V")
    menubar.add_cascade(label="Edit",menu=editmenu)
    root.config(menu=menubar)
     #HELPMENU
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label="About Notepad",command=aboutfile)
    menubar.add_cascade(label="Help",menu=helpmenu)
    root.config(menu=menubar)
     #adding scrollbar
    scroll=Scrollbar(textspace)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textspace.yview)
    textspace.config(yscrollcommand=scroll.set)
    root.mainloop()