# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# X lose, Y draw, and Z win.

# outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)

#Value of my Tool
def my_value(v):

    if v == 'X':

        return 1
    elif v == 'Y':
        return 2
    else:
        return 3

#What I Need To Play
def my_play(o, v):

    if o == "A":  # Rock
        if v == 'X':  # Lose
            return 'Z'
        elif v == 'Y':  # Draw
            return 'X'
        else:  # Win
            return 'Y'

    elif o == "B":  # Paper
        if v == 'X':  # Lose
            return 'X'
        elif v == 'Y':  # Draw
            return 'Y'
        else:  # Win
            return 'Z' 

    else:  # Scissor
        if v == 'X':  # Lose
            return 'Y'
        elif v == 'Y':  # Draw
            return 'Z'
        else:  # Win
            return 'X'


#Outcome of the round
def round(o, v):
    if o == "A":  # Rock
        if v == 'X':  # Rock
            return 3
        elif v == 'Y':  # Paper
            return 6
        else:  # Scissor
            return 0

    elif o == "B":  # Paper
        if v == 'X':  # Rock
            return 0
        elif v == 'Y':  # Paper
            return 3
        else:  # Scissor
            return 6

    else:  # Scissor
        if v == 'X':  # Rock
            return 6
        elif v == 'Y':  # Paper
            return 0
        else:  # Scissor
            return 3


def firstHalf():

    f = open("rockPaperScissor.txt", "r")
    lines = f.readlines()
    total = 0
    for x in lines:
        x = x.strip()
        battle = x.split(" ")
        opponent = battle[0]
        you = battle[1]
        value = my_value(you)
        total += round(opponent, you) + value

    f.close()
    print(total)


def secondHalf():

    f = open("rockPaperScissor.txt", "r")
    lines = f.readlines()
    total = 0
    for x in lines:
        x = x.strip()
        battle = x.split(" ")
        opponent = battle[0]
        you = battle[1]
        you = my_play(opponent,you)
        value = my_value(you)
        total += round(opponent, you) + value

    f.close()
    print(total)


firstHalf()
secondHalf()
