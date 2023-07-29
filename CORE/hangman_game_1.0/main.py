#Hangman is progress
#The flow chard I have done is in a png format in this folder of day 7
from random import choice
from replit import clear
from hangman_words import word_list
from hangman_art import logo,stages
word=word_list
name=choice(word)
n=len(name)
sname=[]
tname=[]
for i in range(n):
    sname.append("_")
#OR
# for i in name:
#     sname.append("_")
live=6
z=0
print(logo)
while z==0:
    guess=input("Enter a letter: ").lower()
    tname=sname
    clear()
    l=0
    p=0
    for i in range(n):
        j=name[i]
        k=sname[i]
        if (j==guess) and (k!=guess):
            sname[i]=j
            l=1
        elif (j==guess) and (k==guess):
            p=1
    #OR
    # for i in name:
    #     if i==guess:
    #         sname[j]=i
    #         l=1
    #     j+=1
    print(f"{' '.join(sname)}")
    if p==1:
        print(f"{guess} has already beeen selected\nYou are losing life by doing this repeatition")
    if l==1:
        if "_" not in sname:
            z=1
        if "_" in sname:
            z=0
    else:
        live-=1
        if p==0:
            print(f"{guess} is not found in the word")
        if live==0:
            z=1
        else:
            z=0
    print(f"You are left with {live} live \n{stages[live]}")
    #OR
    # if "_" in sname:
    #     z=0
    # else: 
    #     z=1
if live==0:
    print("YOU LOSE")
    print(f"The word is \n{' '.join(name)}")
else:
    print("YOU WIN")