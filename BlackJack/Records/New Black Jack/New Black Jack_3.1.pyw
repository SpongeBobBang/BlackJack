# Stefan Yuzhao Heng CS3

from tkinter import*
from random import*

def Initialize():
    global InfoShown
    global x
    global Disabled
    Disabled = False
    x=2
    InfoShown =False
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
    global Y
    Y = "Y"
    global StandPressed
    StandPressed = ["Not used",blank,blank,blank,blank,blank,blank]
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
    if BankerShown == True:
        ShowCard(1)
    else:
        for x in range (2,PlayerNumber+1):
            ShowCard(x)

def ShowCard(PlayerIndex):
    XCoor = 100
    YCoor = 10+60*(PlayerIndex-1)
    for i in range(1,3):
        labelThisCard=Label(root,text=Card[PlayerIndex][i-1],bg="yellow")
        labelThisCard.place(height=50,width=50,x=XCoor,y=YCoor)
        XCoor = XCoor + 60
    for i in range(3,len(Card[PlayerIndex])+1):
        labelThisCard=Label(root,text="U",bg="yellow")
        labelThisCard.place(height=50,width=50,x=XCoor,y=YCoor)
        XCoor = XCoor + 60

def HitButton(CurrentPlayer):
    global ButtonHit
    labelPlayerName=Label(root,text=PlayerDisplay[CurrentPlayer]+"'s turn:",anchor="w",bg="yellow")
    labelPlayerName.place(height=50,width=120,x=5,y=10+60*PlayerNumber+50)
    ButtonHit=Button(root,text="Hit")
    ButtonHit.place(height=50,width=50,x=100,y=10+60*PlayerNumber+100)
    ButtonHit.bind("<Button-1>",HitDone)
    x = CurrentPlayer
    StandButton(x)

def HitDone(event):
    Disabled = False
    if StandPressed[x] == Y or StatusCount[x] == Busted:
        DisableHit(ButtonHit)
        Disabled = True
    if Disabled == False:
        Draw(x)
        CountPoints()
        ShowCards()
    if InfoShown == True:
        labelShowInfo=Label(root,text=Card[x],anchor="w")
        labelShowInfo.place(height=50,width=100,x=100,y=10+60*PlayerNumber+200)

def StandButton(x):
    ButtonStand=Button(root,text="Stand")
    ButtonStand.place(height=50,width=50,x=200,y=10+60*PlayerNumber+100)
    ButtonStand.bind("<Button-1>",StandCheck)

def StandCheck(event):
    StandPressed[x] = Y
    if StandPressed[x] == Y or StatusCount[x] == Busted:
        DisableHit(ButtonHit)
        Disabled = True

def ShowInfoButton():
    ButtonShowInfo=Button(root,text="ShowInfo")
    ButtonShowInfo.place(height=50,width=100,x=50,y=10+60*PlayerNumber+150)
    ButtonShowInfo.bind("<Button-1>",ShowInfo)

def ShowInfo(event):
    global InfoShown
    if InfoShown == False:
        labelShowInfo=Label(root,text=Card[x],anchor="w")
        labelShowInfo.place(height=50,width=120,x=100,y=10+60*PlayerNumber+200)
        InfoShown = True
    elif InfoShown == True:
        InfoShown = False
        ButtonShowInfo.palce_forget()
    if StandPressed[x] == Y or StatusCount[x] == Busted:
        DisableHit(ButtonHit)
        Disabled = True

def NextButton():
    ButtonNext=Button(root,text="Next")
    ButtonNext.place(height=50,width=50,x=200,y=10+60*PlayerNumber+150)
    ButtonNext.bind("<Button-1>",Next)

def Next(event):
    DisplayPlayers()
    global x
    if x >= 2 and x < PlayerNumber:
        x = x + 1
    elif x == PlayerNumber:
        x = 1
    labelTest=Label(root,text=x,bg="green")
    labelTest.place(height=50,width=300,x=400,y=400)
    ButtonHit['bg']="green"
    
def DisableHit(Button):
    Button['state']='disabled'
    Button['bd']=0
    Button['bg']='red'

def Main():
    Initialize()
    SetPlayers()

def SubMain():
    DisplayPlayers()
    PlayersDraw()
    ShowCards()
    HitButton(x)
    StandButton(x)
    ShowInfoButton()
    NextButton()

Main()
root.mainloop()
