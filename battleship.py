import re
import os
import time
import sys

field1 = []
for i in range(10):
    field1.append([])
    for n in range (10):
        field1[i].append(0)

field2 = []
for i in range(10):
    field2.append([])
    for n in range (10):
        field2[i].append(0)

def check(n, ori, sp, sl):
    #sp[0] = sor
    #sp[1] = oszlop
    if ori == "H":
        l = sp[1]
        if l + sl > len(n[sp[1]]):
            return True
        while l < sl + sp[1]:
            if n[sp[0]][l] == 2:
                return True
            l = l + 1

    if ori == "V":
        l = sp[0]
        if l + sl > len(n[sp[0]]):
            return True
        while l < sl + sp[0]:
            if n[l][sp[1]] == 2:
                return True
            l = l + 1
    return False

def placeshiphori(n, sp, sl):
    l = 0
    k = sp[1]
    while l < sl:
            n[sp[0]][k] = 2             #LINE EQUALS: n[column.index(h1)][int(h2)-1] = 2
            k = k + 1                   #LINE EQUALS: h2 = int(h2) + 1
            l = l + 1

def placeshipvert(n, sp, sl):
    l = 0
    k = sp[0]
    while l < sl:
            n[k][sp[1]] = 2
            k = k + 1
            l = l + 1          

def placement(n, info): # n = number of field, info = number of player
    draw(n, info)
    carrier(n)
    os.system('cls' if os.name == 'nt' else 'clear')
    draw(n, info)
    battleship(n)
    os.system('cls' if os.name == 'nt' else 'clear')
    draw(n, info)
    cruiser(n)
    os.system('cls' if os.name == 'nt' else 'clear')
    draw(n, info)
    submarine(n)
    os.system('cls' if os.name == 'nt' else 'clear')
    draw(n, info)
    destroyer(n)
    os.system('cls' if os.name == 'nt' else 'clear')
    draw(n, info)
    print("\nYou've successfully placed all your ships on the sea.")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

def carrier(n):
    shiplength = 5
    column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    pattern = "[A-J] [1-9]|10"
    orient = input("\nHow would you like to place your CARRIER (5 units long)? Horizontally or vertically (H/V)? ")
    while True:
        validop = ["H", "V"]
        if orient not in validop:
            orient = input("\nHow would you like to place your CARRIER (5 units long)? Horizontally or vertically (H/V)? ")
        else:
            break
    if orient == "H": #horizontal placement
        while True:
            coords = input("\nPlease provide the bow (start) coordinates separated by spaces (example: A 2): ")
            if re.findall(pattern, coords):
                h1, h2 = coords.split(" ")
                sp = (column.index(h1), int(h2)-1)
                if check(n, orient, sp, shiplength) == True:
                    print("\nOops, you either already placed something here, or your ship sailed off the map. Please try again.")
                    continue
                placeshiphori(n, sp, shiplength)
                break
    elif orient == "V": #vertical placement
        while True:
            coords = input("\nPlease provide the bow (start) coordinates separated by spaces (example: B 2): ")
            if re.findall(pattern, coords):
                h1, h2 = coords.split(" ")
                sp = (column.index(h1), int(h2)-1)
                if check(n, orient, sp, shiplength) == True:
                    print("\nOops, you either already placed something here, or your ship sailed off the map. Please try again.")
                    continue
                placeshipvert(n, sp, shiplength)   
                break

def battleship(n):
    shiplength = 4
    column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    pattern = "[A-J] [1-9]|10"
    orient = input("\nHow would you like to place your BATTLESHIP (4 units long)? Horizontally or vertically (H/V)? ")
    while True:
        validop = ["H", "V"]
        if orient not in validop:
            orient = input("\nHow would you like to place your BATTLESHIP (4 units long)? Horizontally or vertically (H/V)? ")
        else:
            break
    if orient == "H": #horizontal placement
        while True:
            coords = input("\nPlease provide the bow (start) coordinates separated by spaces (example: A 2): ")
            if re.findall(pattern, coords):
                h1, h2 = coords.split(" ")
                sp = (column.index(h1), int(h2)-1)
                if check(n, orient, sp, shiplength) == True:
                    print("\nOops, you either already placed something here, or your ship sailed off the map. Please try again.")
                    continue
                placeshiphori(n, sp, shiplength)
                break
    elif orient == "V": #vertical placement
        while True:
            coords = input("\nPlease provide the bow (start) coordinates separated by spaces (example: B 2): ")
            if re.findall(pattern, coords):
                h1, h2 = coords.split(" ")
                sp = (column.index(h1), int(h2)-1)
                if check(n, orient, sp, shiplength) == True:
                    print("\nOops, you either already placed something here, or your ship sailed off the map. Please try again.")
                    continue
                placeshipvert(n, sp, shiplength)   
                break

def cruiser(n):
    shiplength = 3
    column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    pattern = "[A-J] [1-9]|10"
    orient = input("\nHow would you like to place your CRUISER (3 units long)? Horizontally or vertically (H/V)? ")
    while True:
        validop = ["H", "V"]
        if orient not in validop:
            orient = input("\nHow would you like to place your CRUISER (3 units long)? Horizontally or vertically (H/V)? ")
        else:
            break
    if orient == "H": #horizontal placement
        while True:
            coords = input("\nPlease provide the bow (start) coordinates separated by spaces (example: A 2): ")
            if re.findall(pattern, coords):
                h1, h2 = coords.split(" ")
                sp = (column.index(h1), int(h2)-1)
                if check(n, orient, sp, shiplength) == True:
                    print("\nOops, you either already placed something here, or your ship sailed off the map. Please try again.")
                    continue
                placeshiphori(n, sp, shiplength)
                break
    elif orient == "V": #vertical placement
        while True:
            coords = input("\nPlease provide the bow (start) coordinates separated by spaces (example: B 2): ")
            if re.findall(pattern, coords):
                h1, h2 = coords.split(" ")
                sp = (column.index(h1), int(h2)-1)
                if check(n, orient, sp, shiplength) == True:
                    print("\nOops, you either already placed something here, or your ship sailed off the map. Please try again.")
                    continue
                placeshipvert(n, sp, shiplength)   
                break

def submarine(n):
    shiplength = 3
    column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    pattern = "[A-J] [1-9]|10"
    orient = input("\nHow would you like to place your SUBMARINE (3 units long)? Horizontally or vertically (H/V)? ")
    while True:
        validop = ["H", "V"]
        if orient not in validop:
            orient = input("\nHow would you like to place your SUBMARINE (3 units long)? Horizontally or vertically (H/V)? ")
        else:
            break
    if orient == "H": #horizontal placement
        while True:
            coords = input("\nPlease provide the bow (start) coordinates separated by spaces (example: A 2): ")
            if re.findall(pattern, coords):
                h1, h2 = coords.split(" ")
                sp = (column.index(h1), int(h2)-1)
                if check(n, orient, sp, shiplength) == True:
                    print("\nOops, you either already placed something here, or your ship sailed off the map. Please try again.")
                    continue
                placeshiphori(n, sp, shiplength)
                break
    elif orient == "V": #vertical placement
        while True:
            coords = input("\nPlease provide the bow (start) coordinates separated by spaces (example: B 2): ")
            if re.findall(pattern, coords):
                h1, h2 = coords.split(" ")
                sp = (column.index(h1), int(h2)-1)
                if check(n, orient, sp, shiplength) == True:
                    print("\nOops, you either already placed something here, or your ship sailed off the map. Please try again.")
                    continue
                placeshipvert(n, sp, shiplength)   
                break

def destroyer(n):
    shiplength = 2
    column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    pattern = "[A-J] [1-9]|10"
    orient = input("\nHow would you like to place your DESTROYER (2 units long)? Horizontally or vertically (H/V)? ")
    while True:
        validop = ["H", "V"]
        if orient not in validop:
            orient = input("\nHow would you like to place your DESTROYER (2 units long)? Horizontally or vertically (H/V)? ")
        else:
            break
    if orient == "H": #horizontal placement
        while True:
            coords = input("\nPlease provide the bow (start) coordinates separated by spaces (example: A 2): ")
            if re.findall(pattern, coords):
                h1, h2 = coords.split(" ")
                sp = (column.index(h1), int(h2)-1)
                if check(n, orient, sp, shiplength) == True:
                    print("\nOops, you either already placed something here, or your ship sailed off the map. Please try again.")
                    continue
                placeshiphori(n, sp, shiplength)
                break
    elif orient == "V": #vertical placement
        while True:
            coords = input("\nPlease provide the bow (start) coordinates separated by spaces (example: B 2): ")
            if re.findall(pattern, coords):
                h1, h2 = coords.split(" ")
                sp = (column.index(h1), int(h2)-1)
                if check(n, orient, sp, shiplength) == True:
                    print("\nOops, you either already placed something here, or your ship sailed off the map. Please try again.")
                    continue
                placeshipvert(n, sp, shiplength)   
                break

def draw(n, info):
    g = 0
    h = 0
    letter = 65
    print("\n")
    print(" PLACEMENT PHASE (PLAYER %s)\n" % info)    
    print("    | 1 2 3 4 5 6 7 8 9 10|")
    print(" –––|–––––––––––––––––––––|")
    for g in range(0, 10):
        print(" %2s |" % chr(letter), end=' ')
        for h in range(0, 10):
            if n[g][h] == 0:
                print("~", end=' ')
            elif n[g][h] == 2:
                print("o", end=' ')
        letter = letter+1
        print("|\r")       
    print(" –––|–––––––––––––––––––––|")

def drawbattle(n, info):
    g = 0
    h = 0
    letter = 65
    print("\n")
    print("   BATTLE PHASE (PLAYER %s)\n" % info)    
    print("    | 1 2 3 4 5 6 7 8 9 10|")
    print(" –––|–––––––––––––––––––––|")
    for g in range(0, 10):
        print(" %2s |" % chr(letter), end=' ')
        for h in range(0, 10):
            if n[g][h] == 0 or n[g][h] == 2:
                print("~", end=' ')
            elif n[g][h] == 1:
                print("x", end=' ')
            elif n[g][h] == 3:
                print("x", end=' ')
        letter = letter+1
        print("|\r")       
    print(" –––|–––––––––––––––––––––|")

def battle(n, info): # n = field number, info = player number, sr = ship_remaining
    global ship_remaining1
    global ship_remaining2
    global gameoff
    trgpattern = "[A-J] [1-9]|10"
    column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    drawbattle(n, info)
    print("\nSink the enemy ships!")
    while True:
        target = input("\nProvide a target for your artillery (example: C 2): ")
        if re.findall(trgpattern, target):
            t1, t2 = target.split(" ")
            sp = (column.index(t1), int(t2)-1)

            if n[sp[0]][sp[1]] == 0:
                n[sp[0]][sp[1]] = 1
                os.system('cls' if os.name == 'nt' else 'clear')
                drawbattle(n, info)
                print("\nOops! It looks like you missed. Better luck next time!")
                print("\nIt's Player %s's turn..." % info)
                time.sleep(3)
            elif n[sp[0]][sp[1]] == 1:
                print("\nYou already took a shot there.")
                continue
            elif n[sp[0]][sp[1]] == 2:
                n[sp[0]][sp[1]] = 3
                if info == 1:
                    ship_remaining2 = ship_remaining2 - 1
                    if ship_remaining2 == 0:
                        gameoff = 0
                        gameover(2)
                elif info == 2:
                    ship_remaining1 = ship_remaining1 - 1
                    if ship_remaining1 == 0:
                        gameoff = 0
                        gameover(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                drawbattle(n, info)
                print("\nBOOM! YOU'VE HIT AN ENEMY SHIP!")
                if info == 1:
                    print("\nEnemy lives remaining: ", ship_remaining2)
                elif info == 2:
                    print("\nEnemy lives remaining: ", ship_remaining1)
                print("\nIt's Player %s's turn..." % info)
                time.sleep(3)
            elif n[sp[0]][sp[1]] == 3:
                print("\nYou already took a shot there.")
                continue
            
            
            break
    return
    
def gameover(info):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("CONGRATS, PLAYER %s, YOU WON!!!" % info)
    time.sleep(8)
    sys.exit()

# ---------------------------------- MAIN CODE STARTS HERE -----------------------------------

os.system('cls' if os.name == 'nt' else 'clear')

print("                                     |__")
print("                                     |\/")
print("                                     ---")
print("                                     / | [")
print("                              !      | |||")
print("                            _/|     _/|-++'")
print("                        +  +--|    |--|--|_ |-")
print("                     { /|__|  |/\__|  |--- |||__/")
print("                    +---------------___[}-_===_.'____                 /\")")
print("                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _")
print(" __..._____--==/___]_|__|_____________________________[___\==--____,------' .7")
print("|                                                                         /")
print(" \________________________________________________________________________|")
print("\n")
print(" ____         _______  _______  _       ______   _____  _    _  _____  _____  ")
print("|  _ \    /\ |__   __||__   __|| |     |  ____| / ____|| |  | ||_   _||  __ \ ")
print("| |_) |  /  \   | |      | |   | |     | |__   | (___  | |__| |  | |  | |__) |")
print("|  _ <  / /\ \  | |      | |   | |     |  __|   \___ \ |  __  |  | |  |  ___/ ")
print("| |_) |/ ____ \ | |      | |   | |____ | |____  ____) || |  | | _| |_ | |     ")
print("|____//_/    \_\|_|      |_|   |______||______||_____/ |_|  |_||_____||_|     ")
print("\n")
input("                           Press ENTER to start...")                                                                                  

os.system('cls' if os.name == 'nt' else 'clear')

placement(field1, 1)
print("\nPlayer 2 placement phase commencing...")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

placement(field2, 2)
print("\nBattle phase commencing...")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


print("                                     |__")
print("                                     |\/")
print("                                     ---")
print("                                     / | [")
print("                              !      | |||")
print("                            _/|     _/|-++'")
print("                        +  +--|    |--|--|_ |-")
print("                     { /|__|  |/\__|  |--- |||__/")
print("                    +---------------___[}-_===_.'____                 /\")")
print("                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _")
print(" __..._____--==/___]_|__|_____________________________[___\==--____,------' .7")
print("|                                                                         /")
print(" \________________________________________________________________________|")
print("\n")
print("            ____        _   _   _        _____  _                    ")
print("           |  _ \      | | | | | |      |  __ \| |                   ")
print("           | |_) | __ _| |_| |_| | ___  | |__) | |__   __ _ ___  ___ ")
print("           |  _ < / _` | __| __| |/ _ \ |  ___/| '_ \ / _` / __|/ _ \ ")
print("           | |_) | (_| | |_| |_| |  __/ | |    | | | | (_| \__ \  __/")
print("           |____/ \__,_|\__|\__|_|\___| |_|    |_| |_|\__,_|___/\___|")

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

ship_remaining1 = 2
ship_remaining2 = 2

gameoff = 1

while gameoff == 1:
    battle(field2, 1)
    os.system('cls' if os.name == 'nt' else 'clear')
    battle(field1, 2)
    os.system('cls' if os.name == 'nt' else 'clear')
    continue