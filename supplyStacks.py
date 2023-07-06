#Transform the Supply stack exists into possible readable

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def replace(s,ch,index):
    return s[:index] + ch + s[index + 1:]


def stacker():
    f = open("supplyStacks.txt", "r")
    lines = f.read().splitlines()
    stacker = []
    stacks = []
    for l in lines: #Stacks of Boxes
        if not l.strip():
            break
        stacker.append(l)

    for x in stacker:
        l = find(x,"]")
        for j in range(0,len(l)):
            x = replace(x,".",l[j]+1)

        for i in range(0,len(x)):
        
            if x[i+1:i+4]=="   ":

                x = x.replace("    ","[1].")
        x = x.replace("."," ")
        stacks.append(x)

    return stacks