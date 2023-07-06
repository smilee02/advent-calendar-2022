#Meter cada caixa num array
#Ter n arrays para n stacks
#Push e pops dos arrays dependendo da frase
import re
from supplyStacks import stacker
from hashTable import HashTable

fileName = "supplyStacks.txt"

#First Half
#Create the hashtable that will contain the stacks
def createStacks():
    #Pass into lists
    lines = stacker()
    stackerList = []
    stacks = []
    for l in lines: #Stacks of Boxes
        if not l.strip():
            break
        c = l.split(" ")
        stackerList.append(c)


    #Create the number of arrays needed
    x = stackerList.reverse()
    sizeOf = int(len(stackerList[0])/3)
    hashtable = HashTable(sizeOf)
    for n in stackerList[0]: #Number of Stacks
        if n != " " and n != "":
            array = []
            x = int(n)
            hashtable.set_val(x,array)
    #Fill arrays with the boxes from the stacks   
    for n in range(1,len(stackerList)): #The boxes to stack
        count = 1
        for x in stackerList[n]:
        
            x = x.replace("[","")
            x = x.replace("]","")
        
            if x != "":
                array = hashtable.get_val(count)
                if x!="1":
                    array.append(x)
                    hashtable.set_val(count,array)
                count+=1
        
    return hashtable

#For each instructions do this
def readInstructions(line,hashtable):
    crates_to_move, from_stack, to_stack = map(int, re.findall(r"\d+", line))
    crates_to_move, from_stack - 1, to_stack - 1
    stackFrom = hashtable.get_val(from_stack)
    stackTo = hashtable.get_val(to_stack)
    for i in range(0,crates_to_move):#Take one box and place in the stack
        box = stackFrom.pop()
        stackTo.append(box)
    
    hashtable.set_val(from_stack,stackFrom)
    hashtable.set_val(to_stack,stackTo)
    return hashtable

#Get the instructions
def makeInstructions(hashtable):
    lines = []
    with open("supplyStacks.txt", 'r') as f:
        for line in f:
            
            if not line.strip():
                # line is empty
                lines = [line.strip() for line in f]
                break
       
    for line in lines:
        hashtable = readInstructions(line,hashtable)
    
    return hashtable

#Get the top boxes from each stack
def firstTop(hashtable):
    string = ""
    for i in range(1,hashtable.size+1):
        array = hashtable.get_val(i)
        string += array.pop()
       

    return string

def firstHalf():

    stacks = createStacks()
    stacks = makeInstructions(stacks)
    topOfStacks = firstTop(stacks)
    print(topOfStacks)

#9001
def makeInstructions9001(hashtable):
    lines = []
    with open("supplyStacks.txt", 'r') as f:
        for line in f:
            
            if not line.strip():
                # line is empty
                lines = [line.strip() for line in f]
                break
       
    for line in lines:
        hashtable = readInstructions9001(line,hashtable)
    
    return hashtable

#9001
def readInstructions9001(line,hashtable):
    crates_to_move, from_stack, to_stack = map(int, re.findall(r"\d+", line))
    crates_to_move, from_stack - 1, to_stack - 1
    stackFrom = hashtable.get_val(from_stack)
    stackTo = hashtable.get_val(to_stack)
    box = []
    for i in range(0,crates_to_move):
        box.append(stackFrom.pop()) 
    box.reverse() #You will take it from the top to bot so reverse it
    for i in range(0,crates_to_move):
        stackTo.append(box[i])
    hashtable.set_val(from_stack,stackFrom)
    hashtable.set_val(to_stack,stackTo)
    return hashtable

def secondHalf():

    stacks = createStacks()
    stacks = makeInstructions9001(stacks)
    topOfStacks = firstTop(stacks)
    print(topOfStacks)

firstHalf()
secondHalf()
