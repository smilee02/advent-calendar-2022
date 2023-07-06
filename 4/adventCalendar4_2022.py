def firstHalf():
    f = open("campCleanup.txt", "r")
    lines = f.read().splitlines()
    total = 0
    for x in lines:
        elf1,elf2 = x.split(",")
        start1,end1 = [int (n) for n in elf1.split("-")]
        start2,end2 = [int (n) for n in elf2.split("-")]
    
        if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1): #I want that the second elf is in the first elf or vice versa
            total+=1
    print(total)


def secondHalf():
    f = open("campCleanup.txt", "r")
    lines = f.read().splitlines()
    total = 0
    for x in lines:
        elf1,elf2 = x.split(",")
        start1,end1 = [int (n) for n in elf1.split("-")]
        start2,end2 = [int (n) for n in elf2.split("-")]
        #If the end of the first elf overlaps the start of the second elf and the start of the second overlaps end of second or vice versa
        if (end1 >= start2 and start1 <= end2) or (end2 >= start1 and start2 <= end1): #I want that the second elf is in the first elf or vice versa
            total+=1
    print(total)


firstHalf()
secondHalf()