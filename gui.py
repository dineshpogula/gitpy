import Tkinter as git
import sqlite3
import subprocess
import tkMessageBox
from sqlquries import createNewTableGitPathToDB, saveGitPathToDB, retriveStoredDbData, updateGitPath

from Tkinter import *

newline_indent = '\n   '


root = git.Tk()
root.title('Git Commands')

topFrame = Frame(root)
topFrame.pack(side=TOP)

midFrame = Frame(topFrame)
midFrame.pack(side=BOTTOM)

# Accept User input
packageLabel = Label(topFrame, text="Git Path")
packageLabel.pack(side=LEFT)

pathEntry = Entry(topFrame, bd=5, width=50)
pathEntry.pack()

lbl = git.Label(root, text="Empty", bg="black", fg='white')
lbl.pack()


def getPath():
    p = subprocess.Popen("C:\Program Files\Git\git-bash.exe",
                         bufsize=-1,
                         executable=None,
                         stdin=None,
                         stdout=None,
                         stderr=None,
                         preexec_fn=None,
                         close_fds=True,
                         shell=False,
                         cwd="W:/vcs_my23",
                         )

    # lbl.configure(text=pathEntry.get())
    # or
    # lbl["text"] = ent.get()


def clearPath():
    lbl.configure(text="Empty")
    # or
    # lbl["text"] = ent.get()


def callBackFuncCheckBoxOne():
    if CheckVar1.get(): lbl.configure(text="Repo One")
    print (CheckVar1.get())


def callBackFuncCheckBoxTwo():
    if CheckVar2.get(): lbl.configure(text="Repo Two")
    print (CheckVar2.get())


def callSaveeDB():
    saveGitPathToDB(pathEntry.get())
    # sql.retriveStoredDbData()


CheckVar1 = BooleanVar()
CheckVar2 = BooleanVar()

C1 = Checkbutton(midFrame, text="Repo One ", variable=CheckVar1,
                 onvalue=1, offvalue=0, height=5,
                 width=20, command=callBackFuncCheckBoxOne, bd=4)
C2 = Checkbutton(midFrame, text="Repo Two", variable=CheckVar2,
                 onvalue=1, offvalue=0, height=5,
                 width=20, command=callBackFuncCheckBoxTwo, bd=4)

C1.grid(row=0, column=0)
C2.grid(row=0, column=1)

bottomFrame = Frame(root)
bottomFrame.pack()

buttonExecute = git.Button(bottomFrame, text='Execute', width=20, command=lambda: getPath(), bd=5)

buttonCancel = git.Button(bottomFrame, text='Cancel', width=20, command=lambda: clearPath(), bd=5)

buttonSave = git.Button(bottomFrame, text='Save', width=20, command=lambda: callSaveeDB(), bd=5)

buttonUpdate = git.Button(bottomFrame, text='Update', width=20, command=lambda: updateGitPath(pathEntry.get()), bd=5)

buttonSave.pack()
buttonUpdate.pack()
buttonExecute.pack()
buttonCancel.pack()

buttonSave.grid(column=0, row=0, padx=20, pady=20)
buttonUpdate.grid(column=1, row=0, padx=20, pady=20)
buttonExecute.grid(column=0, row=1, padx=20, pady=20)
buttonCancel.grid(column=1, row=1, padx=20, pady=20)

# identical to window.geometry('512x256+16+32')
root.geometry('{}x{}+{}+{}'.format(712, 346, 66, 82))
root.mainloop()
