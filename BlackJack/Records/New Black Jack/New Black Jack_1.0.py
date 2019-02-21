# Stefan Yuzhao Heng CS3

from tkinter import*

def Initialize():
    global root
    global t
    root=Tk()
    root.title("Black Jack")
    cv=Canvas(root,width=800,height=800)
    cv.pack()
    
def SetPlayers():
    global root
    global labelInputText
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    Number = ["Not used",1,2,3,4,5,6]
    labelInputText=Label(root,text="Input the number of players:",anchor="w",bg="yellow")
    labelInputText.place(height=50,width=350,x=5,y=5)
    XCoor = 10
    button1=Button(root,text=Number[1])
    button1.place(height=30,width=30,x=XCoor,y=60)
    button1.bind("<Button-1>",NumberInput)
    XCoor = XCoor + 40
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
    PlayerNumber = button["text"]
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    labelInputText.place_forget()
    DisplayPlayers()

def DisplayPlayers():
    Number = ["Not used",1,2,3,4,5,6]
    PlayerDisplay = ["Not used","Banker","Player 2","Player 3","Player 4","Player 5","Player 6"]
    YCoor = 10
    for i in range (1,PlayerNumber+1):
        labelPlayerName=Label(root,text=PlayerDisplay[i]+":",anchor="w",bg="yellow")
        labelPlayerName.place(height=50,width=80,x=10,y=YCoor)
        YCoor = YCoor + 60
    

def Main():
    Initialize()
    SetPlayers()

Main()
root.mainloop()
