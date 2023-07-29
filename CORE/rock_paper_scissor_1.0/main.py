#Rock Paper Scissors
from random import randint
from replit import clear
while True:
    u=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    m=randint(0,2)
    if u==0 or u==1 or u==2:
        if u==0:
            print("You Choosed:\n    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---,__(___)\n")
        elif u==1:
            print("You Choosed:\n    _______\n---'   ____)____\n          ______)_\n          ________)\n          _______)\n--,___________)\n")
        else:
            print("You Choosed:\n    _______\n---'   ____)____\n           ______)\n        __________)\n       (____)\n---,__(____)\n")
        if m==0:
            print("Computer Choosed:\n    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---,__(___)\n")
        elif m==1:
            print("Computer Choosed:\n    _______\n---'   ____)____\n          ______)_\n          ________)\n          _______)\n--,___________)\n")
        else:
            print("Computer Choosed:\n    _______\n---'   ____)____\n           ______)\n        __________)\n       (____)\n---,__(____)\n")
        if u==m:
            print("\n\nYOU DRAW\n\n")
        elif u==0 and m==2:
            print("\n\nYOU WIN\n\n")
        elif u==1 and m==0:
            print("\n\nYOU WIN\n\n")
        elif u==2 and m==1:
            print("\n\nYOU WIN\n\n")
        else:
            print("\n\nYOU LOSE\n\n")
    else:
        print("WRONG INPUT\n\n\nSO YOU LOSE\n\n")
    ans=input("Input clear to clear the screen:\n")
    if ans=='clear':
        clear()
