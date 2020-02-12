# 07/02/2020
# Finite Automata Check

n = 'y'
import re
import sys
InitialState = []
TerminalStates = []
currentState = 0
patharray = []
alphabets = []
states = []
edges = []

g = 0
print('\033c')

while g == 0:
    filename = input("Open Point File : ")
    print('\033c')
    if filename.endswith('.txt'):
        Input = open(filename)
        lines = Input.readlines()
        Input.close()
        g = 1
    else:
        print("Your file must be a txt file!")

# deleting line breaks and comments..
i = 0
while i < len(lines):
    txt = lines[i]
    txt = re.sub("\n", "", txt)
    txt = re.sub("( )*//.*", "", txt)
    lines[i] = txt
    i = i+1
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
#------------------------------------

# scans user's input and check if it is accepted by automata
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
    print('\033c')