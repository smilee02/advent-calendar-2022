
def check_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


f = open("elfsCalories.txt", "r")
caloriesElfs = []
calorie = 0
lines = f.readlines()
for x in lines:
    if check_number(x):

        calorie += int(x)
    else:

        caloriesElfs.append(calorie)

        calorie = 0


f.close()
caloriesElfs.sort(reverse=True)

print("Calories of Top Elf")
print(caloriesElfs[0])


sum = caloriesElfs[0] + caloriesElfs[1] + caloriesElfs[2]
print("Sum of Calories of The Top 3 Elfs")
print(sum)