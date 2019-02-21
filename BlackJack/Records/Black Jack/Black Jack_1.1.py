from random import*

def SetPlayers():
    PlayerNumber = int(input("Input the number of players: "))
    while PlayerNumber < 2 or PlayerNumber > 6:
        PlayerNumber = int(input("This game only allows 2 to 6 players: "))

def Initialize():
    global Deck
    global Card
    Deck = ["A",2,3,4,5,6,7,8,9,"J","Q","K",
            "A",2,3,4,5,6,7,8,9,"J","Q","K",
            "A",2,3,4,5,6,7,8,9,"J","Q","K",
            "A",2,3,4,5,6,7,8,9,"J","Q","K"]
    Card = [["Not Used"],
            [],
            [],
            [],
            [],
            [],
            []]

def PlayersDraw():
    for i in range(1,PlayerNumber):
        temp = randint(1,52)
        while Deck[temp] == blank:
            temp = randint(1,52)
        Card[PlayerNumber].append(Deck[temp])
        Deck[temp] = blank

def Player2Hit():
    global temp
    global blank
    blank = " "
    temp = randint(1,52)
    while Deck[temp] == blank:
        temp = randint(1,52)
    Card[2].append(Deck[temp])
    Deck[temp] = blank

def DisplayCurrent():
    for card in Card[2]:
        print("Player 2's card:",Card[2])

def Main():
    SetPlayers()
    Initialize()
    Player2Hit()
    DisplayCurrent()

Main()
