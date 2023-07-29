############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
from random import choice
from art import logo
from replit import clear
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """Returns a random card from the list"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    ch=choice(cards)
    return ch
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(card):
    """Returns the sum of a list of card"""
    a=sum(card)
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if a==21 and len(card)==2:
        return 0
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if a>21 and 11 in card:
        card.remove(11)
        card.append(1)
        a=sum(card)
    return a
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw.
#If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. 
#If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user,comp):
    """Compare user score and computer score"""
    if comp==user:
        print("You Draw")
    elif comp==0:
        print("You Lose, Opyponent has a Blackjack")
    elif user==0:
        print("You Win,You have a Blackjack")
    elif user>21:
        print("You Lose,You went over")
    elif comp>21:
        print("You Win,Opponent went over")
    elif user>comp:
        print("You Win")
    else:
        return "You Lose"
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
start="yes"
while start=="yes":
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    #user_cards = []
    #computer_cards = []
    user_cards = []
    computer_cards = []
    con="y"
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(logo)
    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while con=="y":
        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        u=calculate_score(user_cards)
        c=calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {u}")
        print(f"Computer's first card: {computer_cards[0]}")
        if c==0 or u==0 or u>21:
            con="n"
        else:
            con=input(f"The sum of your card is {u}\nWould you like to draw a card\nType 'y' to add 'n' not to add: ")
            #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            if con=="y":
                user_cards.append(deal_card())
            elif con=="n":
                con=="n"
            else:
                print("Wrong Input")
    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while c<17 and c!=0:
        computer_cards.append(deal_card())
        c=calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {u}")
    print(f"Computer's final hand: {computer_cards}, final score: {c} ")
    compare(u,c)
    start=input("Will you like to play again.\nType 'yes' to play again and 'no' to quit the game: ")
    clear()
print("++++++++++++++++++++++++GAME OVER++++++++++++++++++++++++")