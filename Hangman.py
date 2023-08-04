import random
import re
print("Hello Dear!\nWelcome to hangman Game\n")
guess = 6
win = False
user_gauss = []

###user input
def p_input():
    name = input("Enter Your gauss latter(you have "+str(guess)+" guess left) : ")
    while len(name) > 1 or not re.match("^[a-z]*$", name) or name in user_gauss:
        if len(name) > 1 or not re.match("^[a-z]*$", name):
            print("\n--- Just latter!--- \n")
        elif name in user_gauss:
            print("\n--- you use this latter before ---\n")
        name = input("Enter Your gauss latter(you have "+str(guess)+" guess left) : ")
    user_gauss.append(name)
    return name

###Generate random world
def world(): 
    world_list = ["Apple","Forest","Ocean","Castle","River","Meadow","Sunset","Valley","Island","Clouds","Moon","Beach","Star","Grove","Hill","Lake","Bridge","Cave","Ruins","Spring"]
    world = random.choice(world_list)
    return world

###player guess
world = world()
p_world = ""

for i in range(0,len(world)):
    p_world = p_world+"_ "

###checking input latter
def game(name,world,p_world):
    x = world.find(name)
    if x >= 0:
        while x >= 0:
            p_world = p_world[:x*2] + name + p_world[(x*2)+1:]
            if world[x+1:].find(name) >= 0:
                x = world[x+1:].find(name) + x+1
            else:
                x = -2
    return p_world
        
def hangman(guess):
    if guess == 6:
        print(" ====")
        print("||  |")
        print("||   ")
        print("||   ")
        print("||   ")
    elif guess == 5:
        print(" ====")
        print("||  |")
        print("||  O ")
        print("||   ")
        print("||   ")
    elif guess == 4:
        print(" ====")
        print("||  |")
        print("||  O")
        print("||   \ ")
        print("||   ")
    elif guess == 3:
        print(" ====")
        print("||  |")
        print("||  O")
        print("|| / \ ")
        print("||   ")
    elif guess == 2:
        print(" ====")
        print("||  |")
        print("||  O")
        print("|| /|\ ")
        print("||   ")
    elif guess == 1:
        print(" ====")
        print("||  |")
        print("||  O")
        print("|| /|\ ")
        print("||   \ ")
    elif guess == 0:
        print(" ====")
        print("||  |")
        print("||  O")
        print("|| /|\ ")
        print("|| / \ ")
    return
    

###the game
world = world.lower()
print(p_world)
while guess > 0:
    print("\n")
    hangman(guess)
    print("\n")
    name = p_input()
    if p_world == game(name,world,p_world):
        guess -= 1
    p_world = game(name,world,p_world)
    if "_" not in p_world:
        win = True
        break
    print("\n",p_world)

if win == True:
    print("\n\nPerfect!, you saved him\n")
    print("   \O/ ")
    print("    |  ")
    print("   / \ ")
    print("\nyour letter is ",world)
else:
    print("oh you killed him\n")
    hangman(0)
