# Stefan Yuzhao Heng CS3
from random import*

def SetPlayers():
    global PlayerNumber
    PlayerNumber = int(input("Input the number of players: "))
    while PlayerNumber < 2 or PlayerNumber > 6:
        PlayerNumber = input("This game only allows 2 to 6 players: ")

def Initialize():
    global Deck
    global Card
    Deck = [0,
            'A',2,3,4,5,6,7,8,9,'T','J','Q','K',
            'A',2,3,4,5,6,7,8,9,'T','J','Q','K',
            'A',2,3,4,5,6,7,8,9,'T','J','Q','K',
            'A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    Card = [["Not Used"],
            [],
            [],
            [],
            [],
            [],
            []]

def PlayersDraw():
    global blank
    blank = " "
    DrawAll()
    DrawAll()
    CountPoints()

def DrawAll():
    for i in range(1,PlayerNumber + 1):
        Draw(i)

def Draw(i):
    temp = randint(1,52)
    while Deck[temp] == blank:
        temp = randint(1,52)
    Card[i].append(Deck[temp])
    Deck[temp] = blank

def DisplayCurrent():
    global PlayerDisplay
    PlayerDisplay = ["Not used",
                     "Banker",
                     "Player 2",
                     "Player 3",
                     "Player 4",
                     "Player 5",
                     "Player 6"]
    print(PlayerDisplay[1]+"'s card:",Card[1][0],end=" ")
    for i in range(len(Card[1])-1):
        print("Unknown",end=" ")
    print("- 16+/21")
    for e in range (2,PlayerNumber + 1):
        print(PlayerDisplay[e]+"'s card:",end=" ")
        for i in range (1,len(Card[e])+1):
            print(Card[e][i-1],end=" ")
        print("-",PointCount[e],end="")
        print("/21")

def CountPoints():
    global PointCount
    ACount = 0
    TypeCount = [["Not used"],
                 [],
                 [],
                 [],
                 [],
                 [],
                 []]
    PointCount = ["Not used",0,0,0,0,0,0]
    for i in range(1, PlayerNumber + 1):
        for e in range(0, len(Card[i])):
            if "A" == Card[i][e]:
                ACount = ACount + 1
            elif "T" == Card[i][e] or "J" == Card[i][e] or "Q" == Card[i][e] or "K" == Card[i][e]:
                PointCount[i] = PointCount[i] + 10
            else:
                PointCount[i] = PointCount[i] + Card[i][e]
        TypeCount[i].append(ACount)
        if ACount >= 1:
            PointCount[i] = PointCount[i]+10+ACount
            if PointCount[i] > 21:
                PointCount[i] = PointCount[i] - 10
        ACount = 0
    for i in range(1,PlayerNumber + 1):
        print(PointCount[i],end=" ")
    print()

def Banker():
    ee

def Hit():
    global temp
    for i in range (1,PlayerNumber + 1):
        Hit = " "
        while Hit != "Stand" and Hit != "S" and Hit != "s":
            Hit = str(input(PlayerDisplay[i]+", Hit or Stand?:"))
            if Hit == "Hit" or Hit == "H" or Hit == "h":
                Draw(i)
                CountPoints()
                DisplayCurrent()
            elif Hit != "Stand" and Hit != "S" and Hit != "s":
                print("I can't understand you.")

def Main():
    SetPlayers()
    Initialize()
    PlayersDraw()
    DisplayCurrent()
    CountPoints()
    Hit()

Main()
