# Stefan Yuzhao Heng CS3

from tkinter import*
from random import*

PlayerNumber=0

def Initialize():
    global A
    global T
    global J
    global Q
    global K
    A = 'A'
    T = 'T'
    J = 'J'
    Q = 'Q'
    K = 'K'
    global Deck
    Deck = [0,A,2,3,4,5,6,7,8,9,T,J,Q,K,A,2,3,4,5,6,7,8,9,T,J,Q,K,A,2,3,4,5,6,7,8,9,T,J,Q,K,A,2,3,4,5,6,7,8,9,T,J,Q,K]
    global blank
    blank = " "
    global Card
    Card = [["Not Used"],[],[],[],[],[],[]]
    global Busted
    global BlackJack
    global OK
    OK = "OK"
    Busted = "Busted"
    BlackJack = "BlackJack"
    global StatusCount
    StatusCount = ["Not used",OK,OK,OK,OK,OK,OK]
    global Winner
    Winner = ["Not used",blank,blank,blank,blank,blank,blank]
    global BankerShown
    BankerShown = False
    global root
    root=Tk()
    root.title("Black Jack")
    cv=Canvas(root,width=800,height=800)
    cv.pack()
    
def SetPlayers():
    global root
    global labelInputText
    global button2
    global button3
    global button4
    global button5
    global button6
    Number = ["Not used",1,2,3,4,5,6]
    labelInputText=Label(root,text="Input the number of players:",anchor="w",bg="yellow")
    labelInputText.place(height=50,width=350,x=5,y=5)
    XCoor = 10
    button2=Button(root,text=Number[2])
    button2.place(height=30,width=30,x=XCoor,y=60)
    button2.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 40
    button3=Button(root,text=Number[3])
    button3.place(height=30,width=30,x=XCoor,y=60)
    button3.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 40
    button4=Button(root,text=Number[4])
    button4.place(height=30,width=30,x=XCoor,y=60)
    button4.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 40
    button5=Button(root,text=Number[5])
    button5.place(height=30,width=30,x=XCoor,y=60)
    button5.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 40
    button6=Button(root,text=Number[6])
    button6.place(height=30,width=30,x=XCoor,y=60)
    button6.bind("<Button-1>",NumberInput)

def hide(event):
    event.widget.pack_forget()
    
def NumberInput(event):
    global PlayerNumber 
    button=event.widget
    PlayerNumber = int(button["text"])
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    labelInputText.place_forget()
    SubMain()
    
def DisplayPlayers():
    global PlayerDisplay
    Number = ["Not used",1,2,3,4,5,6]
    PlayerDisplay = ["Not used","Banker","Player 2","Player 3","Player 4","Player 5","Player 6"]
    YCoor = 10
    for i in range (1,PlayerNumber+1):
        labelPlayerName=Label(root,text=PlayerDisplay[i]+":",anchor="w",bg="yellow")
        labelPlayerName.place(height=50,width=80,x=10,y=YCoor)
        YCoor = YCoor + 60

def PlayersDraw():
    DrawAll()
    DrawAll()
    CountPoints()

def DrawAll():
    global PlayerNumber
    for i in range(1,PlayerNumber + 1):
        Draw(i)

def Draw(i):
    temp = randint(1,52)
    while Deck[temp] == blank:
        temp = randint(1,52)
    Card[i].append(Deck[temp])
    Deck[temp] = blank

def CountPoints():
    global PointCount
    ACount = 0
    TypeCount = [["Not used"],[],[],[],[],[],[]]
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

def ShowCards():
    if BankerShown == False:
        for x in range (2,PlayerNumber+1):
            ShowCard(x)

def ShowCard(PlayerIndex):
    XCoor = 100
    YCoor = 10+60*(PlayerIndex-1)
    for i in range(1,len(Card[PlayerIndex])+1):
        labelThisCard=Label(root,text=Card[PlayerIndex][i-1],bg="yellow")
        labelThisCard.place(height=50,width=50,x=XCoor,y=YCoor)
        XCoor = XCoor + 60

def Main():
    Initialize()
    SetPlayers()

def SubMain():
    DisplayPlayers()
    PlayersDraw()
    ShowCards()

Main()
root.mainloop()
