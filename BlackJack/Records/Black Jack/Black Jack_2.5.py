# Stefan Yuzhao Heng CS3
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
    PlayerDisplay = ["Not used",
                   "Banker",
                   "Player 2",
                   "Player 3",
                   "Player 4",
                   "Player 5",
                   "Player 6"]
    print(PlayerDisplay[1],"'s card: [",Card[1][0],",Unknown]")
    for e in range (2,PlayerNumber + 1):
        for i in range (1,len(Card[e])):
            print(PlayerDisplay[e],"'s card:",Card[e])

def CountPoints():
    ACount = 0
    TCount = 0
    CardCount = [["Not used"],
                 [],
                 [],
                 [],
                 [],
                 [],
                 []]
    for i in range(1, PlayerNumber + 1):
        for e in range(0, len(Card[i])):
            if "A" == Card[i][e]:
                ACount = ACount + 1
            elif "J" == Card[i][e] or "Q" == Card[i][e] or "K" == Card[i][e]:
                TCount = TCount + 1
        CardCount[i].append(ACount)
        CardCount[i].append(TCount)
        ACount = 0
        TCount = 0
    for i in range(1,PlayerNumber + 1):
        print(CardCount[i])

def Main():
    SetPlayers()
    Initialize()
    PlayersDraw()
    DisplayCurrent()
    CountPoints()

Main()
