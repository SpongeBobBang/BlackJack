from random import*

def SetPlayers():
    global PlayerNumber
    PlayerNumber = int(input("Input the number of players: "))
    while PlayerNumber < 2 or PlayerNumber > 6:
        PlayerNumber = int(input("This game only allows 2 to 6 players: "))

def Initialize():
    global Deck
    global Card
    Deck = [0,
            'A',2,3,4,5,6,7,8,9,'J','Q','K',
            'A',2,3,4,5,6,7,8,9,'J','Q','K',
            'A',2,3,4,5,6,7,8,9,'J','Q','K',
            'A',2,3,4,5,6,7,8,9,'J','Q','K']
    Card = [["Not Used"],
            [],
            [],
            [],
            [],
            [],
            []]

def PlayersDraw():
    global temp
    global blank
    blank = " "
    print("Initial drawing starts...")
    DrawAll()
    DrawAll()

def DrawAll():
    for i in range(1,PlayerNumber + 1):
        temp = randint(1,52)
        while Deck[temp] == blank:
            temp = randint(1,52)
        Card[i].append(Deck[temp])
        Deck[temp] = blank

def Player2Hit():
    temp = randint(1,52)
    while Deck[temp] == blank:
        temp = randint(1,52)
    Card[2].append(Deck[temp])
    Deck[temp] = blank

def DisplayCurrent():
    for i in range (1,len(Card[1])):
        print("Banker's card:",Card[1])
    for i in range (1,len(Card[2])):
        print("Player 2's card:",Card[2])
    for i in range (1,len(Card[3])):
        print("Player 3's card:",Card[3])
    for i in range (1,len(Card[4])):
        print("Player 4's card:",Card[4])
    for i in range (1,len(Card[5])):
        print("Player 5's card:",Card[5])
    for i in range (1,len(Card[6])):
        print("Player 6's card:",Card[6])

def Main():
    SetPlayers()
    Initialize()
    PlayersDraw()
    DisplayCurrent()

Main()
