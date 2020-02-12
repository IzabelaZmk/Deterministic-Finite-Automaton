   # 09/02/2020
   # Finite Automata Gui Check
   # Before start the program
   # Run Python3 then import Tkinter

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import re
import sys
InitialState = []
TerminalStates = []
currentState = 0
pathtext = ""
m = 0
patharray = []
alphabets = []
states = []
edges = []

    # scans user's input and check if it is accepted by automata
def run():
    global m
    f = 0
    s = s_storage.get()
    m = m + 1
    while f < len(s):
        if (s[f] in alphabets):
            f = f + 1
        else:
            messagebox.showerror("Error", "Not Acceptable String You Idiot!")
            sys.exit()

    currentState = InitialState[0]

    del patharray[:]

    pathtext = ""

    patharray.append(currentState)

    pathtext = pathtext + '->Q'
    pathtext = pathtext + currentState

    for i in range(0, len(s)):
        k = 0
        while k < j:
            if(currentState == edges[k][0] and s[i] == edges[k][1]):
                currentState = edges[k][2]
                patharray.append(currentState)
                pathtext = pathtext + '->Q'
                pathtext = pathtext + currentState
                k = j
            k = k + 1

    f = 0
    d = 0

    Label7 = Label(Graphics, text =" ", width = 100)
    Label7.grid(row=1,column=1,sticky = W, columnspan = 10)

    Label6 = Label(Graphics, text = pathtext)
    Label6.grid(row=1,column=1,sticky = W, columnspan = 10)


    if (currentState in TerminalStates):
        Label4 = Label(Graphics, text = "Accepted!")
    else:
        Label4 = Label(Graphics, text = "Rejected!")
    Label4.grid(row=2,column=1,sticky = W, columnspan = 10)



    #------------------------------------------------------
    # initialize interface

Graphics = Tk()
Graphics.title("Deterministic Finite Automaton")
Graphics.geometry("350x100")
Graphics.resizable(1,0)

if ( sys.platform.startswith('win')): 
    Graphics.iconbitmap(r'dfa.ico')
else:
    Graphics.iconbitmap()

Graphics.filename =  filedialog.askopenfilename(initialdir = "",title = "Select file",filetypes = (("txt files","*.txt"),))

#------------------------------------

# Open file and deleting line breaks and comments..

Input = open(Graphics.filename)
lines = Input.readlines()
Input.close()

i = 0
while i < len(lines):
    txt = lines[i]
    txt = re.sub("\n", "", txt)
    txt = re.sub("( )*//.*", "", txt)
    lines[i] = txt
    i = i+1
#------------------------------------------------------
# Greate User interface

Label1 = Label(Graphics, text = "Enter the word\t: ")
Label2 = Label(Graphics, text = "The Path is\t: ")
Label3 = Label(Graphics, text = "Result\t\t: ")
Button1 = Button(Graphics, text = "Answer",command = run)

s_storage = StringVar()
s = Entry(textvariable = s_storage)

Label1.grid(row=0,column=0,sticky = W)
s.grid(row=0,column=1,sticky = W, columnspan = 10)
Label2.grid(row=1,column=0,sticky = W)
Label3.grid(row=2,column=0,sticky = W)
Button1.grid(row=3,column=1,sticky = W, columnspan = 10)

    #------------------------------------------------------

    # create arrays with dictionary data

NumofStates = lines[0]
alphabets = lines[1].split(" ")
InitialState = lines[2].split(" ")
TerminalStates = lines[3].split(" ")

i = 4
j = 0
while i < len(lines):
    edge = lines[i].split(" ")
    edges.append(edge)
    i = i + 1
    j = j + 1


i = 0
while i < len(edges):
    if not(edges[i][0] in states):
        states.append(edges[i][0])
    if not(edges[i][2] in states):
        states.append(edges[i][2])

    i = i + 1

i = 0
#------------------------------------

Graphics.mainloop()