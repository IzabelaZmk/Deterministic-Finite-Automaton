# 07/02/2020
# Finite Automata Check

n = 'y'
import re
InitialState = []
TerminalStates = []
currentState = 0
alphabets = []
states = []
edges = []
Input = open("dfa.txt")
lines = Input.readlines()
Input.close()

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

while n != 'n': 
    s = input("Enter the word : ")
    currentState = InitialState[0]
    for i in range(0, len(s)):
        k = 0
        while k < j:
            if(currentState == edges[k][0] and s[i] == edges[k][1]):
                currentState = edges[k][2]
                k = j
            k = k + 1
            

    if (currentState in TerminalStates):
        print("accepted")
    else:
        print ("rejected")

    n = input('\n' + 'Do you want to continue?(y/n): ')
