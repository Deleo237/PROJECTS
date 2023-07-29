#>>>>>>>>>>>>>>>>>>>HIGH AND LOW GAME<<<<<<<<<<<<<<<<<<<<<<
#<<<<<<<<<<<<<<<<<<<List of things to do>>>>>>>>>>>>>>>>>>>>
#1) Get the elements from the list and compare for highest
#2) Ask user for correct answer 
#3) Do comparison with user answer and highest
#4) If user is correct repeat else end and give the scores
from replit import clear
from art import logo,vs
from game import data
def compare(ans,f1,f2):
    """Check if the user is correct"""
    if ans=="A":
        if f1>f2:
            return 1
        else:
            return 0
    elif ans=="B":
        if f1<f2:
            return 1
        else:
            return 0
    else:
        return 2
l=1
inc=1
w=0
while l==1:
    print(logo)
    item1=data[inc]
    n1=item1["name"]
    f1=item1["follower_count"]
    d1=item1["description"]
    c1=item1["country"]
    if inc>1:
        print(f"You're right! Current score: {inc-1}")
    print(f"Compare A: {n1}, a {d1}, from {c1}.")
    print(vs)
    item2=data[inc+1]
    n2=item2["name"]
    f2=item2["follower_count"]
    d2=item2["description"]
    c2=item2["country"]
    print(f"Against B: {n2}, a {d2}, from {c2}.")
    ans=input("Who has more followers? Type 'A' or 'B': ").upper()
    l=compare(ans,f1,f2)
    if l==1:
        inc+=1
    elif l==2:
        w=1
        l=0
    clear()
print(logo)
if inc==33:
    print(f"YOU HAVE WON\nFINAL SCORE: {inc-1}")
elif w==1:
    print("<<<<<<<<<<<<<<<<<<< WRONG INPUT >>>>>>>>>>>>>>>>>>>>")
    print(f"Sorry, that's wrong final score: {inc-1}")
else:
    print(f"Sorry, that's wrong final score: {inc-1}")
    
#OR

from random import choice
def assign(item):
    """Sorts ort the information"""
    n=item["name"]
    d=item["description"]
    c=item["country"]
    return f"{n}, a {d}, from {c}"
l=1
inc=1
w=0
item2=choice(data)
while l==1:
    print(logo)
    item1=item2
    item2=choice(data)
    while item1==item2:
        item2=choice(data)
    if inc>1:
        print(f"You're right! Current score: {inc-1}")
    print(f"Compare A: {assign(item1)}.")
    print(vs)
    print(f"Against B: {assign(item2)}.")
    f1=item1["follower_count"]
    f2=item2["follower_count"]
    ans=input("Who has more followers? Type 'A' or 'B': ").upper()
    l=compare(ans,f1,f2)
    if l==1:
        inc+=1
        item1=item2
    elif l==2:
        w=1
        l=0
    clear()
print(logo)
if w==1:
    print("<<<<<<<<<<<<<<<<<<< WRONG INPUT >>>>>>>>>>>>>>>>>>>>")
print(f"Sorry, that's wrong final score: {inc-1}")