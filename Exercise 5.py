import random
def SWG():
    print("Welcome to snake water gun game")
    user = input ("Enter your chioce (snake, water, gun) :")
    computer = random.choice(["snake","water","gun", "\n"])
    print(f"user choice {user} and computer choice{computer}")
    if user ==computer :
        print("draw game")
    elif user == "snake" and computer ==' water':
        print ("you won")
    elif user =="gun" and computer== "snake":
        print("you won")
    else:
        print("you lose")
SWG()