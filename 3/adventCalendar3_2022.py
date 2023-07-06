def common_rucksack(frstComp,scndComp):
    first = set(frstComp)
    second = set(scndComp)
    if len(first.intersection(second)) > 0:
        return(first.intersection(second).pop()) #To get the value of the intersection
    else:
        return 0


priority = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def firstHalf():
    f = open("ruckSack.txt", "r")
    lines = f.readlines()
    total = 0
    for x in lines:
      size = len(x)
      mid = int(size/2)
      arr1 = x[0:mid]
      arr2 = x[mid:size]
      common = common_rucksack(arr1,arr2)
     
      total += priority.index(common)+1
    print(total)

#1,2,3 the elves, first,second the rucksacks
def common_rucksack_by_group(first,second,third):
    elf1 = set(first)
    elf2 = set(second)
    elf3 = set(third)
    
    return elf1.intersection(elf2).intersection(elf3).pop()




def secondHalf():
    f = open("ruckSack.txt", "r")
    lines = f.readlines()
    total = 0
    for l in range(0,len(lines),3): #Iterate 3 at a time 
        commons = []
        j = l+3 #Get the next step
        for i in range(l,j): #Loop 0,1,2
            x = lines[i].strip()
            commons.append(x)
         
        value  = common_rucksack_by_group(commons[0],commons[1],commons[2])
        total += priority.index(value)+1
    print(total)



firstHalf()
secondHalf()