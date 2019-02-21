from turtle import*
from tkinter import*
from random import*

def randomword():
    global word
    w=open('dict.txt','r')
    content=w.readlines()
    randline=content[randint(0,4093)]
    word=''
    try:
        for i in range(20):
            if randline[i]>='a' and randline[i]<='z':
                word=word+randline[i]
    except:x=0

def loadtk():
    global root
    global t
    root=Tk()
    root.title("Hangman Game")
    cv=Canvas(root,width=600,height=450)
    cv.pack()
    t=RawTurtle(TurtleScreen(cv))

def loadlists():
    global wordlist
    global incorrectlist
    global word
    wordlist=[" " for x in range(len(word))]
    incorrectlist=[" " for y in range(6)]

def drawhanger():
    global t
    global turtlemoving
    turtlemoving=True
    t.ht()
    t.penup()
    t.goto(-280,-200)
    t.pendown()
    t.forward(200)
    t.penup()
    t.backward(150)
    t.seth(90)
    t.pendown()
    t.forward(400)
    t.seth(0)
    t.forward(100)
    t.seth(270)
    t.forward(50)
    t.seth(180)
    turtlemoving=False

def printstatus(info,info2):
    global root
    label1=Label(root,text=info,anchor="w",bg="yellow")
    label1.place(height=50,width=350,x=250,y=150)
    label2=Label(root,text=info2,anchor="w",bg="blue")
    label2.place(height=50,width=350,x=250,y=200)
 
def drawman(times):
    global t
    global turtlemoving
    if times==1:
        turtlemoving=True
        t.circle(25)
        t.penup()
        t.seth(270)
        t.forward(50)
        turtlemoving=False
    if times==2:
        turtlemoving=True
        t.pendown()
        t.forward(100)
        t.seth(90)
        t.forward(50)
        turtlemoving=False
    if times==3:
        turtlemoving=True
        t.seth(150)
        t.forward(50)
        t.seth(330)
        t.forward(50)
        turtlemoving=False
    if times==4:
        turtlemoving=True
        t.seth(30)
        t.forward(50)
        t.seth(210)
        t.forward(50)
        t.seth(270)
        t.forward(50)
        turtlemoving=False
    if times==5:
        turtlemoving=True
        t.seth(300)
        t.forward(60)
        t.seth(120)
        t.forward(60)
        turtlemoving=False
    if times==6:
        turtlemoving=True
        t.seth(240)
        t.forward(60)
        t.penup()
        t.goto(-130,100)
        t.pendown()
        t.seth(0)
        t.circle(25,45)
        t.penup()
        t.seth(135)
        t.forward(10)
        t.pendown()
        t.forward(30)
        t.penup()
        t.seth(0)
        t.forward(21.2)
        t.seth(225)
        t.pendown()
        t.forward(30)
        turtlemoving=False

def restartbutton():
    button=Button(root,text='restart')
    button.place(height=40,width=60,x=520,y=20)
    button.bind("<Button-1>",restart)

def restart(event):
    global t
    t.reset()
    randomword()
    loadlists()
    info,info2=getinfo()
    printstatus(info,info2)
    loadletterbutton()
    drawhanger()

def loadletterbutton():
    for i in range(97,123):
        if i<106:
            xcoor=240+40*(i-97)
            ycoor=300
        elif i<114:
            xcoor=260+40*(i-106)
            ycoor=340
        else:
            xcoor=240+40*(i-114)
            ycoor=380
        button1=Button(root,text=chr(i))
        button1.place(height=30,width=30,x=xcoor,y=ycoor)
        button1.bind("<Button-1>",letterbutton)

def letterbutton(event):
    button=event.widget
    guess=button['text']
    if event.widget['state']!='disabled' and turtlemoving==False:
        disablebutton(button)
        determinecorrect(guess)
        info,info2=getinfo()
        printstatus(info,info2)
        checkstatus()

def determinecorrect(guess):
    global word
    correct=False
    for x in range(len(word)):
        if word[x]==guess:
            wordlist[x]=guess
            correct=True
    found=False
    temp=0
    while found==False and correct==False:
        if incorrectlist[temp]==" ":
            found=True
            incorrectguesses=temp+1
            incorrectlist[temp]=guess
            drawman(incorrectguesses)
        else: temp=temp+1

def getinfo():
    global word
    info="Word:"
    for x in range(len(word)):
        info=info+"[ "+wordlist[x]+" ]"
    info2="Missed:"
    for y in range(6):
        info2=info2+"[ "+incorrectlist[y]+" ]"
    return info,info2

def checkstatus():
    global word
    finish=True
    for x in range(len(word)):
        if wordlist[x]==" ":
            finish=False
    if finish==True:
        word="You Win, the correct word is "+word
        messagebox.showinfo("Game finished",word)
    if incorrectlist[5]!=" " and finish==False:
        finish=True
        word="You loose, the correct word is "+word
        messagebox.showinfo("Game finished",word)

def disablebutton(button):
    button['state']='disabled'
    button['bd']=0
    button['bg']='red'

def main():
    loadtk()
    drawhanger()
    randomword()
    loadlists()
    info,info2=getinfo()
    printstatus(info,info2)
    loadletterbutton()
    restartbutton()

main()
root.mainloop()
