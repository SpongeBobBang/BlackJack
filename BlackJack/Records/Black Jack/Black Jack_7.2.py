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
    global StatusCount
    global OK
    global Winner
    global A
    global T
    global J
    global Q
    global K
    global Busted
    global BlackJack
    global PlayerDisplay
    global blank
    blank = " "
    PlayerDisplay = ["Not used","Banker","Player 2","Player 3","Player 4","Player 5","Player 6"]
    Busted = "Busted"
    BlackJack = "BlackJack"
    OK = "OK"
    A = 'A'
    T = 'T'
    J = 'J'
    Q = 'Q'
    K = 'K'
    Deck = [0,
            A,2,3,4,5,6,7,8,9,T,J,Q,K,
            A,2,3,4,5,6,7,8,9,T,J,Q,K,
            A,2,3,4,5,6,7,8,9,T,J,Q,K,
            A,2,3,4,5,6,7,8,9,T,J,Q,K]
    Card = [["Not Used"],
            [],
            [],
            [],
            [],
            [],
            []]
    Winner = ["Not used",blank,blank,blank,blank,blank,blank]
    StatusCount = ["Not used",OK,OK,OK,OK,OK,OK]

def PlayersDraw():
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
    temp = 0
    print(PlayerDisplay[1]+"'s card:",Card[1][0],"Unknown -",end=" ")
    if A == Card[1][0]:
        temp = 11
    elif T == Card[1][0] or J == Card[1][0] or Q == Card[1][0] or K == Card[1][0]:
        temp = 10
    else:
        temp = Card[1][0]
    print(temp,end="")
    print("+/21")
    for e in range (2,PlayerNumber + 1):
        print(PlayerDisplay[e]+"'s card:",end=" ")
        for i in range (1,3):
            print(Card[e][i-1],end=" ")
        for i in range(len(Card[e])-2):
            print("Unknown",end=" ")
        if len(Card[e]) == 2:
            print("-",PointCount[e],end="")
            print("/21")
        elif len(Card[e]) >= 3:
            print("-",PointCount[e],end="")
            print("+/21")

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
            if A == Card[i][e]:
                ACount = ACount + 1
            elif T == Card[i][e] or J == Card[i][e] or Q == Card[i][e] or K == Card[i][e]:
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
        if PointCount[i] > 21:
            StatusCount[i] = Busted
        elif PointCount[i] == 21:
            StatusCount[i] = BlackJack
            
def Check():
    for i in range(1,PlayerNumber + 1):
        print(PointCount[i],end=" ")
    print()
    for i in range(1,PlayerNumber + 1):
        print(StatusCount[i],end=" ")
    print()

def Hit(i):
        Hit = " "
        while StatusCount[i] != Busted and (Hit != "Stand" and Hit != "S" and Hit != "s" and Hit != "stand"):
            Hit = str(input(PlayerDisplay[i]+", Hit or Stand?:"))
            if Hit == "Hit" or Hit == "H" or Hit == "h":
                Draw(i)
                CountPoints()
                DisplayCurrent()
                print("Your cards are:",end=" ")
                for x in range (len(Card[i])):
                    print(Card[i][x],end=" ")
                print()
                print("Your score is:",PointCount[i])
            elif Hit != "Stand" and Hit != "S" and Hit != "s" and Hit != "stand":
                print("I can't understand you.")
        if StatusCount[i] == Busted:
            print("Sorry, man, Your score has busted hence have lost this game. Click STAND to forward")
            Hit = str(input(PlayerDisplay[i]+", please click STAND:"))
            while Hit != "Stand" and Hit != "S" and Hit != "s" and Hit != "stand":
                Hit = str(input(PlayerDisplay[i]+", just give up & click STAND:"))
      
def CheckWin():
    if StatusCount[1] != Busted:
        print(PlayerDisplay[1],"-",PointCount[1],"Versus")
        for x in range(2,PlayerNumber+1):
            if StatusCount[x] != Busted:
                if PointCount[x] > PointCount[1]:
                    print("     ",PlayerDisplay[x],"-",PointCount[x],":",PlayerDisplay[x],"Wins")
                elif PointCount[x] < PointCount[1]:
                    print("     ",PlayerDisplay[x],"-",PointCount[x],":",PlayerDisplay[1],"Wins")
                elif PointCount[x] == PointCount[1]:
                    print("     ",PlayerDisplay[x],"-",PointCount[x],": Draw")
            elif StatusCount[x] == Busted:
                print("     ",PlayerDisplay[x],"-",Busted,":Draw")
    elif StatusCount[1] == Busted:
        print(PlayerDisplay[1],"-",Busted,"Versus")
        for x in range(2,PlayerNumber+1):
            if StatusCount[x] != Busted:
                print("     ",PlayerDisplay[x],"-",PointCount[x],":",PlayerDisplay[x],"Wins")
            elif StatusCount[x] == Busted:
                print("     ",PlayerDisplay[x],"-",Busted,":Draw")

def Main():
    SetPlayers()
    Initialize()
    PlayersDraw()
    DisplayCurrent()
    for i in range (2,PlayerNumber + 1):
        Hit(i)
    Hit(1)
    CheckWin()

Main()
