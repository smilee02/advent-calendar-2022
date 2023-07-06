def checkNumber(tree, collumn, row):


fileName = "gridTree.txt"
grid = []
with open(fileName, 'r') as f:
    lines = f.read().splitlines()
    numbers = []
    for x in lines:
        for i in x:
            n = int(i)
            numbers.append(n)
        grid.append(numbers)
        numbers = []

for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        print(grid[i][j])
        checkNumber(grid[i][j], j, i)
