# 07/02/2020
# Finite Automata Check

n = 'y'
import re
import sys
from os import system, name
InitialState = []
TerminalStates = []
currentState = 0
patharray = []
alphabets = []
states = []
edges = []

#------------------------------------
# Clear terminal

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        print('\033c')
g = 0
clear()

#------------------------------------
# Check and open text file

while g == 0:
    filename = input("Type the name of your text file : ")
    clear()
    try:
        if filename.endswith('.txt'):
            Input = open(filename)
            lines = Input.readlines()
            Input.close()
            g = 1
        else:
            print("Your file must be a txt file!")
    except IOError:
        print("File not Found!")

#------------------------------------
# deleting line breaks and comments..

i = 0
while i < len(lines):
    txt = lines[i]
    txt = re.sub("(\s)*//.*", "", txt)
    txt = re.sub("\n", "", txt)
    lines[i] = txt
    i = i + 1
    if i == 1 or i == 3:
        if not re.match("^\w*$", txt):
            sys.exit("Number of states or initial state can't be more than one")
    if i > 4:
        if not re.match("^\w*( )\w*( )\w*$", txt):
            sys.exit("The automaton states must be three")

#------------------------------------
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

#----------------------------------------------------------------------------------
# scans user's input and check if it is accepted by automata then print the results

f = 0
while n == 'y': 
    s = input("Enter the word : ")
    while f < len(s):
        if (s[f] in alphabets):
            f = f + 1
        else:
            sys.exit('Not Acceptable String!')
    currentState = InitialState[0]
    del patharray[:]
    patharray.append(currentState)
    for i in range(0, len(s)):
        k = 0
        while k < j:
            if(currentState == edges[k][0] and s[i] == edges[k][1]):
                currentState = edges[k][2]
                patharray.append(currentState)
                k = j
            k = k + 1

    f = 0
    d = 0
    print("The Path is    :", end ="")
    for d in range(len(patharray)): 
    	print(" -> Q",patharray[d], sep ="", end ="")

    if (currentState in TerminalStates):
        print("\nResult\t       : Accepted!")
    else:
        print ("\nResult\t       : Rejected!")
        
    n = input("\nDo you want to continue?(y/n): ")
    clear()