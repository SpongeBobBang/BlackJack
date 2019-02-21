# Stefan Yuzhao Heng CS3

from tkinter import*
from tkinter import messagebox
from tkinter import font
from random import*

def Initialize():
    global InfoShown
    global x
    global Disabled
    global labelInfoBG
    global PlayerNumber
    labelInfoBG = Label(root)
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
    labelBackGround=Label(root,bg="#030303")
    labelBackGround.place(height=4000,width=4000,x=0,y=0)
    
def SetPlayers():
    global root
    global labelInputText
    global button2
    global button3
    global button4
    global button5
    global button6
    root.focus_set()
    Number = ["Not used",1,2,3,4,5,6]
    labelInputText=Label(root,fg="white",activebackground="#bbbbbb",text="Input the number of players:",anchor="w",bg="#b0b0b0",font=("Marker Felt",23,"bold"))
    labelInputText.place(height=100,width=400,x=50,y=120)
    XCoor = 60
    button2=Button(root,fg="#bdd7ee",activebackground="#bbbbbb",bg="#b0b0b0",text=Number[2],font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    button2.place(height=50,width=50,x=XCoor,y=300)
    button2.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 75
    button3=Button(root,fg="#bdd7ee",activebackground="#bbbbbb",bg="#b0b0b0",text=Number[3],font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    button3.place(height=50,width=50,x=XCoor,y=300)
    button3.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 75
    button4=Button(root,fg="#bdd7ee",activebackground="#bbbbbb",bg="#b0b0b0",text=Number[4],font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    button4.place(height=50,width=50,x=XCoor,y=300)
    button4.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 75
    button5=Button(root,fg="#bdd7ee",activebackground="#bbbbbb",bg="#b0b0b0",text=Number[5],font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    button5.place(height=50,width=50,x=XCoor,y=300)
    button5.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 75
    button6=Button(root,fg="#bdd7ee",activebackground="#bbbbbb",bg="#b0b0b0",text=Number[6],font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    button6.place(height=50,width=50,x=XCoor,y=300)
    button6.bind("<Button-1>",NumberInput)
    root.bind("<Key>",KeyboardNumberCheck)
    
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
        labelPlayerName=Label(root,fg="white",text=PlayerDisplay[i]+":",anchor="w",bg="#030303",font=("造字工房悦黑（非商用）纤细体",15,"bold"))
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
    global StatusCount
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

def ShowCardsHidden():
    global BankerShown
    for e in range(2,PlayerNumber+1):
        Show2Cards(e)
        PlayerHidden(e)
    BankerHide()

def ShowCardsShown():
    global BankerShown
    for e in range(1,PlayerNumber+1):
        Show2Cards(e)
        PlayerShown(e)
        
def BankerShow():
    XCoor = 125
    YCoor = 10
    labelThisCard=Label(root,fg="white",text=Card[1][0],bg="#808080",font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    labelThisCard.place(height=60,width=50,x=XCoor,y=YCoor)
    XCoor = XCoor + 70
    Show2Cards(1)
    PlayerShown(1)

def BankerHide():
    Show2Cards(1)
    labelBankerUnknown=Label(root,text=blank,bg="#909090",font=("造字工房悦黑（非商用）纤细体",30,"bold"))
    labelBankerUnknown.place(height=60,width=50,x=195,y=10)

def Show2Cards(PlayerIndex):
    XCoor = 125
    YCoor = 10+70*(PlayerIndex-1)
    for i in range(1,3):
        labelThisCard=Label(root,fg="white",text=Card[PlayerIndex][i-1],bg="#b0b0b0",font=("造字工房悦黑（非商用）纤细体",30,"bold"))
        labelThisCard.place(height=60,width=50,x=XCoor,y=YCoor)
        XCoor = XCoor + 70

def PlayerHidden(PlayerIndex):
    XCoor = 125+70*2
    YCoor = 10+70*(PlayerIndex-1)
    for i in range(3,len(Card[PlayerIndex])+1):
        labelThisCard=Label(root,text=blank,bg="#909090",font=("造字工房悦黑（非商用）纤细体",30,"bold"))
        labelThisCard.place(height=60,width=50,x=XCoor,y=YCoor)
        XCoor = XCoor + 70

def PlayerShown(PlayerIndex):
    XCoor = 125+70*2
    YCoor = 10+70*(PlayerIndex-1)
    for i in range(3,len(Card[PlayerIndex])+1):
        labelThisCard=Label(root,fg="white",text=Card[PlayerIndex][i-1],bg="#909090",font=("造字工房悦黑（非商用）纤细体",30,"bold"))
        labelThisCard.place(height=60,width=50,x=XCoor,y=YCoor)
        XCoor = XCoor + 70

def PlayerTurn(CurrentPlayer):
    global labelSubBG
    labelSubBG=Label(root,bg="#b1b1b1")
    labelSubBG.place(height=200,width=270,x=15,y=10+70*PlayerNumber+5)
    labelPlayerName=Label(root,fg="white",text=PlayerDisplay[CurrentPlayer]+"'s turn:",bg="#b1b1b1",anchor="w",font=("造字工房悦黑（非商用）纤细体",18,"bold"))
    labelPlayerName.place(height=50,width=200,x=15+15,y=10+70*PlayerNumber+5)

def HitButton(CurrentPlayer):
    global ButtonHit
    ButtonHit=Button(root,fg="#bdd7ee",bg="#050505",text="HIT",activebackground="#bbbbbb",font=("造字工房悦黑（非商用）纤细体",15,"bold"))
    ButtonHit.place(height=50,width=80,x=80,y=10+70*PlayerNumber+70)
    ButtonHit.bind("<Button-1>",HitDone)
    x = CurrentPlayer
    root.bind("<Key>",KeyboardCheck)

def HitDone(event):
    global BankerShown
    global labelShowInfo
    Disabled = False
    if ButtonHit['state'] != 'disabled':
        Draw(x)
        CountPoints()
        ShowCardsHidden()
        if x ==1:
            ShowCardsShown()
    if StandPressed[x] == Y or StatusCount[x] == Busted:
        DisableHit(ButtonHit)
        Disabled = True

def KeyboardCheck(event):
    global x
    if event.char =='h':
        global BankerShown
        global labelShowInfo
        Disabled = False
        if ButtonHit['state'] != 'disabled':
            Draw(x)
            CountPoints()
            ShowCardsHidden()
            if x == 1:
                ShowCardsShown()
        if StandPressed[x] == Y or StatusCount[x] == Busted:
            DisableHit(ButtonHit)
            Disabled = True
    elif event.char == 's':
        StandPressed[x] = Y
        if StandPressed[x] == Y or StatusCount[x] == Busted:
            DisableHit(ButtonHit)
            Disabled = True
    elif event.char == 'i':
        global InfoShown
        global labelInfoBG
        if InfoShown == False:
            labelInfoBG=Label(root,bg="#b1b1b1")
            labelInfoBG.place(height=70,width=270,x=15,y=10+70*PlayerNumber+5+70+70+60)
            labelShowInfo.place_forget()
            GetInfo()
            InfoShown = True
        elif InfoShown == True:
            labelShowInfo.place_forget()
            labelInfoBG.place_forget()
            InfoShown = False
    elif event.char == 'p' or event.char =='e':
        if x != 1:
            DisplayPlayers()
            InfoShown = False
            labelShowInfo.place_forget()
            labelInfoBG.place_forget()
            if x >= 2 and x < PlayerNumber:
                x = x + 1
            elif x == PlayerNumber:
                x = 1
                BankerShown = True
                Show2Cards(1)
                for i in range(2,PlayerNumber+1):
                    PlayerShown(i)
            labelPlayerName=Label(root,fg="white",text=PlayerDisplay[x]+"'s turn:",bg="#b1b1b1",anchor="w",font=("造字工房悦黑（非商用）纤细体",18,"bold"))
            labelPlayerName.place(height=50,width=200,x=15+15,y=10+70*PlayerNumber+5)
            ButtonHit['state']="normal"
            if x == 1:
                ButtonNext['text'] = "END"
                ButtonNext.bind("<Button-1>",ShowResult)
            root.bind("<Key>",KeyboardCheck)
            root.bind("<Return>",KeyboardCheck)
        elif x == 1:
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
    elif event.char == 'r':
        LoadBackGround()
        Initialize()
        SetPlayers()

def KeyboardNumberCheck(event):
    if int(event.char) >= 2 and int(event.char) <= 6:
        global PlayerNumber 
        button=event.widget
        PlayerNumber = int(event.char)
        button2.place_forget()
        button3.place_forget()
        button4.place_forget()
        button5.place_forget()
        button6.place_forget()
        labelInputText.place_forget()
        SubMain()
        
def StandButton(x):
    ButtonStand=Button(root,fg="#bdd7ee",bg="#050505",text="STAND",activebackground="#bbbbbb",font=("造字工房悦黑（非商用）纤细体",15,"bold"))
    ButtonStand.place(height=50,width=80,x=180,y=10+70*PlayerNumber+70)
    ButtonStand.bind("<Button-1>",StandCheck)
    root.bind("<Key>",KeyboardCheck)

def StandCheck(event):
    StandPressed[x] = Y
    if StandPressed[x] == Y or StatusCount[x] == Busted:
        DisableHit(ButtonHit)
        Disabled = True

def ShowInfoButton():
    global labelShowInfo
    ButtonShowInfo=Button(root,fg="#bdd7ee",bg="#050505",text="SHOW INFO",activebackground="#bbbbbb",font=("造字工房悦黑（非商用）纤细体",15,"bold"))
    ButtonShowInfo.place(height=50,width=130,x=30,y=10+70*PlayerNumber+140)
    ButtonShowInfo.bind("<Button-1>",ShowInfo)
    root.bind("<Key>",KeyboardCheck)

def GetInfo():
    global labelShowInfo
    Info = "Your cards are: "+str(Card[x])+".\nYour score is "+str(PointCount[x])+"."
    labelShowInfo=Label(root,text=Info,anchor="w",bg="#808080")
    labelShowInfo.place(height=50,width=240,x=30,y=10+70*PlayerNumber+210)

def ShowInfo(event):
    global InfoShown
    global labelShowInfo
    global labelInfoBG
    if InfoShown == False:
        labelInfoBG=Label(root,bg="#b1b1b1")
        labelInfoBG.place(height=70,width=270,x=15,y=10+70*PlayerNumber+5+70+70+60)
        labelShowInfo.place_forget()
        GetInfo()
        InfoShown = True
    elif InfoShown == True:
        labelShowInfo.place_forget()
        labelInfoBG.place_forget()
        InfoShown = False

def NextButton():
    global ButtonNext
    ButtonNext=Button(root,fg="#bdd7ee",bg="#050505",text="PASS",activebackground="#bbbbbb",font=("造字工房悦黑（非商用）纤细体",15,"bold"))
    ButtonNext.place(height=50,width=80,x=180,y=10+70*PlayerNumber+140)
    ButtonNext.bind("<Button-1>",Next)

def Next(event):
    global labelShowInfo
    global ButtonNext
    global BankerShown
    global labelInfoBG
    global InfoShown
    DisplayPlayers()
    InfoShown = False
    labelShowInfo.place_forget()
    labelInfoBG.place_forget()
    global x
    if x >= 2 and x < PlayerNumber:
        x = x + 1
    elif x == PlayerNumber:
        x = 1
        BankerShown = True
        for i in range(2,PlayerNumber+1):
            PlayerShown(i)
        ShowCardsShown()
    labelPlayerName=Label(root,fg="white",text=PlayerDisplay[x]+"'s turn:",bg="#b1b1b1",anchor="w",font=("造字工房悦黑（非商用）纤细体",18,"bold"))
    labelPlayerName.place(height=50,width=200,x=15+15,y=10+70*PlayerNumber+5)
    ButtonHit['state']="normal"
    if x == 1:
        ButtonNext['text'] = "END"
        ButtonNext.bind("<Button-1>",ShowResult)
    root.bind("<Key>",KeyboardCheck)

def ShowResult(event):
    temp = ""
    global StatusCount
    labeltest=Label(root,text=StatusCount,bg="white",anchor="w")
    labeltest.place(height=50,width=400,x=50,y=400)
    for i in range (2,PlayerNumber+1):
        temp = temp+"Banker VS "+PlayerDisplay[i]+"\n"
        if StatusCount[1] != Busted and StatusCount[i] != Busted:
            if PointCount[1] > PointCount[i]:
                temp = temp+"                   Banker wins"
            elif PointCount[1] < PointCount[i]:
                temp = temp+"                   "+PlayerDisplay[i]+" wins"
            elif PointCount[1] == PointCount[i]:
                temp = temp+"                   Draw"
        elif StatusCount[1] != Busted and StatusCount[i] == Busted:
            temp = temp+"                   Banker wins"
        elif StatusCount[1] == Busted and StatusCount[i] != Busted:
            temp = temp+"                   "+PlayerDisplay[i]+" wins"
        elif StatusCount[1] == Busted and StatusCount[i] == Busted:
            temp = temp+"                   Banker wins"
        temp = temp+"\n"
    messagebox.showinfo(str(StatusCount)+"Game finished",temp)

def DisableHit(Button):
    Button['state']='disabled'

def RestartButton():
    ButtonRestart=Button(root,fg="#bdd7ee",bg="#050505",activebackground="#bbbbbb",text="RESTART",font=("造字工房悦黑（非商用）纤细体",18,"bold"))
    ButtonRestart.place(height=60,width=120,x=335,y=10+70*PlayerNumber+10)
    ButtonRestart.bind("<Button-1>",Restart)
    root.bind("<Key>",KeyboardCheck)

def Restart(event):
    LoadBackGround()
    Initialize()
    SetPlayers()

def NoticeButton():
    labelPlayerName=Label(root,text=PlayerDisplay[x]+"'s turn:",bg="#b1b1b1",anchor="w",font=("造字工房悦黑（非商用）纤细体",18,"bold"))
    labelPlayerName.place(height=50,width=200,x=15+15,y=10+70*PlayerNumber+5)

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
    ShowCardsHidden()
    PlayerTurn(x)
    HitButton(x)
    StandButton(x)
    ShowInfoButton()
    NextButton()
    RestartButton()

Main()
root.mainloop()
