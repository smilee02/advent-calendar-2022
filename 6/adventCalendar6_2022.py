fileName = "start-of-packetMarker.txt"

def firstHalf():
    f = open(fileName,"r")
    line = f.readline()

    offset = 4
    for i in range(0,len(line)):
        if len(set(line[i:i+offset])) == len(line[i:i+offset]): #Set é uma lista sem duplicados logo vemos se os tamanhos sao iguais se forem nao existem duplicados
            print(i + offset)
            break
    
def secondHalf():
    f = open(fileName,"r")
    line = f.readline()

    offset = 14
    for i in range(0,len(line)):
        if len(set(line[i:i+offset])) == len(line[i:i+offset]): #Set é uma lista sem duplicados logo vemos se os tamanhos sao iguais se forem nao existem duplicados
            print(i + offset)
            break

#firstHalf()
secondHalf()