#Copyright(c) 2022 Vishal Ahirwar.

from art import logo
from random import choice
"""Return Random Card from the deck"""
player_car=[]
computer_card=[]
def compare(user_score,computer_score):
    if(user_score==computer_score):
        return "Draw!"
    elif(computer_score==0):
        return "Lose, Opponent has Blackjack!"
    elif(user_score==0):
        return "win, with a Blackjack"
    elif(user_score>21):
        return "you went, over , You loose!"
    elif(computer_score>21):
        return "opponent went over, you win!"
    elif(user_score>computer_score):
        return "you win!"
    else:
        return "you lose!"


def Dealcard():
     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
     card=choice(cards)

     return card

def calculate_score(cards):
    '''take a list of cards and returns the sum of list's element'''
    if(sum(cards)==21 and len(cards)==2):
        return 0
    if(11 in cards and sum(cards)>21):
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
def InitGame():
    IsGameOver=False
    while not IsGameOver:
        player_card=[]
        computer_card=[]
        for _ in range(2):
            player_card.append(Dealcard())
            computer_card.append(Dealcard())
        user_score=calculate_score(player_card)
        computer_score=calculate_score(computer_card)
        print(f"Your Cards : {player_card} and Score : {calculate_score(player_card)}")
        print(f"Computer first Card : {computer_card[0]}")

        if(user_score==0 or computer_score==0 or user_score>21):
            IsGameOver=True
        else:
            user_should_deal=input("Type 'y' to get another card, Type 'n' to pass : ").lower()
            if(user_should_deal=='y'):
                player_card.append(Dealcard())
            else:
                IsGameOver=True
        while(computer_score!=0 and computer_score<17):
            computer_card.append(Dealcard())
            computer_score=calculate_score(computer_card)

    print(compare(user_score=user_score,computer_score=computer_score))
    print(f"Your Score : {user_score}\nComputer Score : {computer_score}")

        


while True:
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   
    FLAG=(input("Would like to start this Games??[type : yes or no ]"))
    if FLAG.lower()=='yes':
        InitGame()
        
    else:
        break

      
