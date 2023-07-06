from hashTable import HashTable
def numberOfDirs():
    num = 0
    for i in range(0,len(lines)):
        if "ls" in lines[i] and "$" in lines[i-1]:
            
            num += 1
    return num

fileName = "noSpaceLeft.txt"
dirs = 0

with open(fileName, 'r') as f:
    lines = f.read().splitlines()
    directories = []
    dirs = numberOfDirs()
    folders = HashTable(dirs)

    #Files and Dirs for every Directory
    for i in range(0,len(lines)):
        if "ls" in lines[i] and "$" in lines[i-1]:
            x = lines[i-1].split("cd ")[1]
            directories.append(x)
            files = []
            for j in range(i+1,len(lines)):
                if "$" in lines[j]:
                    break
                files.append(lines[j])
            
            folders.set_val(x,files)
    
    sizes = HashTable(dirs)

    #Get initial size without subdirs
    for x in directories:
        folder = folders.get_val(x)
        weight = []
        sum = 0
        for j in folder:
            str =j.split(" ")
            if str[0] != "dir":
                sum += int(str[0])
            elif str[0] == "dir":
                weight.append(str[1])
        weight.append(sum)
        sizes.set_val(x,weight)

#Recursivamente
            
    

                


