#Auction 
from replit import clear
from art import logo
d={}
def bidder(n,b):
    d[n]=b
print(logo)
ans="yes"
print("WELCOME TO MY GITHUB 'auction 1.0' PROJECT.")
while ans=="yes":
    nn=input("What is your name?: ")
    bb=int(input("What's your bid?: $"))
    bidder(nn,bb)
    ans=input("Are there any other bidders? Type 'yes' or 'no'\n")
    clear()
l=0
n=""

# Looking for the hightest bidder
for i in d:
    if l<d[i]:
        l=d[i]
        n=i
print(f"The winner is {n} with a bid of ${l}")