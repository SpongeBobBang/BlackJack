# Stefan Yuzhao Heng CS3

from tkinter import*
from tkinter import messagebox
from tkinter import font
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

def LoadInterface():
    global root
    root=Tk()
    root.title("Black Jack")
    cv=Canvas(root,width=500,height=720)
    cv.pack()
    LoadBackGround()

def LoadBackGround():
    labelBackGround=Label(root,bg="#bbbbbb")
    labelBackGround.place(height=4000,width=4000,x=0,y=0)
    
def SetPlayers():
    global root
    global labelInputText
    global button2
    global button3
    global button4
    global button5
    global button6
    Number = ["Not used",1,2,3,4,5,6]
    labelInputText=Label(root,text="Input the number of players:",anchor="w",bg="#bbbbbb",font=("Marker Felt",23,"bold"))
    labelInputText.place(height=100,width=400,x=50,y=120)
    XCoor = 60
    button2=Button(root,text=Number[2],font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    button2.place(height=50,width=50,x=XCoor,y=300)
    button2.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 75
    button3=Button(root,text=Number[3],font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    button3.place(height=50,width=50,x=XCoor,y=300)
    button3.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 75
    button4=Button(root,text=Number[4],font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    button4.place(height=50,width=50,x=XCoor,y=300)
    button4.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 75
    button5=Button(root,text=Number[5],font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    button5.place(height=50,width=50,x=XCoor,y=300)
    button5.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 75
    button6=Button(root,text=Number[6],font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    button6.place(height=50,width=50,x=XCoor,y=300)
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
    global labelPlayerName
    Number = ["Not used",1,2,3,4,5,6]
    PlayerDisplay = ["Not used","Banker","Player 2","Player 3","Player 4","Player 5","Player 6"]
    YCoor = 10
    for i in range (1,PlayerNumber+1):
        labelPlayerName=Label(root,text=PlayerDisplay[i]+":",anchor="w",bg="#bbbbbb",font=("造字工房悦黑（非商用）纤细体",15,"bold"))
        labelPlayerName.place(height=60,width=80,x=15,y=YCoor)
        YCoor = YCoor + 70

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
    global BankerShown
    CheckBankerShow()
    ShowPlayers()

def CheckBankerShow():
    XCoor = 125
    YCoor = 10
    labelThisCard=Label(root,text=Card[1][0],bg="#808080",font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    labelThisCard.place(height=60,width=50,x=XCoor,y=YCoor)
    XCoor = XCoor + 70
    labelThisCard=Label(root,text=blank,bg="#909090",font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    labelThisCard.place(height=60,width=50,x=XCoor,y=YCoor)
    if BankerShown == True:
        ShowCard(1)

def ShowPlayers():
        for x in range (2,PlayerNumber+1):
            ShowCard(x)

def ShowCard(PlayerIndex):
    XCoor = 125
    YCoor = 10+70*(PlayerIndex-1)
    for i in range(1,3):
        labelThisCard=Label(root,text=Card[PlayerIndex][i-1],bg="#b0b0b0",font=("造字工房悦黑（非商用）纤细体",30,"bold"))
        labelThisCard.place(height=60,width=50,x=XCoor,y=YCoor)
        XCoor = XCoor + 70
    PlayerHidden(PlayerIndex)

def PlayerHidden(PlayerIndex):
    XCoor = 125+70*2
    YCoor = 10+70*(PlayerIndex-1)
    for i in range(3,len(Card[PlayerIndex])+1):
        labelThisCard=Label(root,text=blank,bg="#909090",font=("造字工房悦黑（非商用）纤细体",30,"bold"))
        labelThisCard.place(height=60,width=50,x=XCoor,y=YCoor)
        XCoor = XCoor + 70

def PlayerTurn(CurrentPlayer):
    labelPlayerName=Label(root,bg="#b1b1b1")
    labelPlayerName.place(height=270,width=270,x=15,y=10+70*PlayerNumber+5)
    labelPlayerName=Label(root,text=PlayerDisplay[CurrentPlayer]+"'s turn:",bg="#b1b1b1",anchor="w",font=("造字工房悦黑（非商用）纤细体",18,"bold"))
    labelPlayerName.place(height=50,width=200,x=15+15,y=10+70*PlayerNumber+5)

def HitButton(CurrentPlayer):
    global ButtonHit
    ButtonHit=Button(root,text="HIT",font=("造字工房悦黑（非商用）纤细体",15,"bold"))
    ButtonHit.place(height=50,width=80,x=80,y=10+70*PlayerNumber+70)
    ButtonHit.bind("<Button-1>",HitDone)
    x = CurrentPlayer
    StandButton(x)

def HitDone(event):
    global labelShowInfo
    Disabled = False
    if ButtonHit['state'] != 'disabled':
        Draw(x)
        CountPoints()
        ShowCards()
    if StandPressed[x] == Y or StatusCount[x] == Busted:
        DisableHit(ButtonHit)
        Disabled = True
    if InfoShown == True:
        GetInfo()

def StandButton(x):
    ButtonStand=Button(root,text="STAND",font=("造字工房悦黑（非商用）纤细体",15,"bold"))
    ButtonStand.place(height=50,width=80,x=180,y=10+70*PlayerNumber+70)
    ButtonStand.bind("<Button-1>",StandCheck)

def StandCheck(event):
    StandPressed[x] = Y
    if StandPressed[x] == Y or StatusCount[x] == Busted:
        DisableHit(ButtonHit)
        Disabled = True

def ShowInfoButton():
    global labelShowInfo
    ButtonShowInfo=Button(root,text="SHOW INFO",font=("造字工房悦黑（非商用）纤细体",15,"bold"))
    ButtonShowInfo.place(height=50,width=130,x=30,y=10+70*PlayerNumber+140)
    ButtonShowInfo.bind("<Button-1>",ShowInfo)

def ShowInfo(event):
    global InfoShown
    global labelShowInfog
    global Info
    if InfoShown == False:
        labelShowInfo.place_forget()
        GetInfo()
        InfoShown = True
    elif InfoShown == True:
        InfoShown = False
        labelShowInfo.place_forget()

def GetInfo():
    Info = "Your cards are: "+str(Card[x])+".\nYour score is "+str(PointCount[x])+"."
    labelShowInfo=Label(root,text=Info,anchor="w",bg="#808080")
    labelShowInfo.place(height=50,width=150+len(Card[x])*30,x=30,y=10+70*PlayerNumber+210)

def NextButton():
    global ButtonNext
    ButtonNext=Button(root,text="PASS",font=("造字工房悦黑（非商用）纤细体",15,"bold"))
    ButtonNext.place(height=50,width=80,x=180,y=10+70*PlayerNumber+140)
    ButtonNext.bind("<Button-1>",Next)

def Next(event):
    global labelShowInfo
    global ButtonNext
    global BankerShown
    DisplayPlayers()
    InfoShown = False
    global x
    if x >= 2 and x < PlayerNumber:
        x = x + 1
    elif x == PlayerNumber:
        x = 1
        BankerShown = True
        ShowCard(1)
    labelPlayerName=Label(root,text=PlayerDisplay[x]+"'s turn:",bg="#b1b1b1",anchor="w",font=("造字工房悦黑（非商用）纤细体",18,"bold"))
    labelPlayerName.place(height=50,width=200,x=15+15,y=10+70*PlayerNumber+5)
    ButtonHit['state']="normal"
    labelShowInfo.place_forget()
    if x == 1:
        ButtonNext['text'] = "END"
        ButtonNext.bind("<Button-1>",ShowResult)

def ShowResult(event):
    temp = ""
    for i in range (2,PlayerNumber+1):
        temp = temp+"Banker VS "+PlayerDisplay[i]+"\n"
        if PointCount[1] > PointCount[i]:
            temp = temp+"                   Banker wins"
        elif PointCount[1] < PointCount[i]:
            temp = temp+"                   "+PlayerDisplay[i]+" wins"
        elif PointCount[1] == PointCount[i]:
            temp = temp+"                   Draw"
        temp = temp+"\n"
    messagebox.showinfo("Game finished",temp)

def DisableHit(Button):
    Button['state']='disabled'

def RestartButton():
    ButtonRestart=Button(root,text="RESTART",font=("造字工房悦黑（非商用）纤细体",18,"bold"))
    ButtonRestart.place(height=60,width=120,x=335,y=10+70*PlayerNumber+10)
    ButtonRestart.bind("<Button-1>",Restart)

def Restart(event):
    LoadBackGround()
    Initialize()
    SetPlayers()

def Main():
    LoadInterface()
    Initialize()
    SetPlayers()

def SubMain():
    global labelShowInfo
    labelShowInfo = Label(root)
    global BankerShown
    BankerShown = False
    DisplayPlayers()
    PlayersDraw()
    ShowCards()
    PlayerTurn(x)
    HitButton(x)
    StandButton(x)
    ShowInfoButton()
    NextButton()
    RestartButton()

Main()
root.mainloop()
