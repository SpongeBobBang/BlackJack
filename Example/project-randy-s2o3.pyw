from turtle import*
from tkinter import*
from random import*

def randomword():
    correctword=False
    while correctword==False:
        if readdictconfig()=="AdvancedDictionary=True":word=processdict()
        else: word=processadvdict()
        if len(word)<getmin() or len(word)>getmax():
            correctword=False
        else: correctword=True
    return word

def processdict():
    w=open('dict.txt','r')
    content=w.readlines()
    randline=content[randint(0,4093)]
    word=''
    try:
        for i in range(20):
            if randline[i]>='a' and randline[i]<='z':
                word=word+randline[i]
    except:x=0
    return word

def processadvdict():
    w=open('advdict.txt','r')
    content=w.readlines()
    randline=content[randint(0,8454)]
    word=''
    fullword=False
    i=0
    while fullword==False:
        if randline[i]>='a' and randline[i]<='z' and randline[i]!="":
            word=word+randline[i]
            i=i+1
        else: fullword=True
    return word

def getmin():
    content=readconfig()
    minvar=int(str(content[2][14])+str(content[2][15]))
    return minvar

def getmax():
    content=readconfig()
    maxvar=int(str(content[3][14])+str(content[3][15]))
    return maxvar


def getword():
    global word
    content=readconfig()
    config=content[0].strip()
    if config=="InputWord=True":
        word=enterword()  
    else:
        AdvancedDictionary=True
        word=randomword()

def readdictconfig():
    content=readconfig()
    config=content[1].strip()
    

def enterword():
    wordentered=False
    while wordentered==False:
        valid=0
        word=simpledialog.askstring('Hangman game','Enter a word(press cancel to generate one)')
        try:
            length=len(word)
            for i in range(length):
                if word[i]>='a' and word[i]<='z':
                    valid=valid+1
            if valid==length and length!=0:
                wordentered=True
        except:
            word=randomword()
            wordentered=True
    return word
    

def loadtk():
    global root
    global t
    root=Tk()
    root.title("Hangman Game")
    root.resizable(0, 0)
    cv=Canvas(root,width=600,height=450)
    cv.pack()
    t=RawTurtle(TurtleScreen(cv))

def loadlists():
    global wordlist
    global incorrectlist
    wordlist=[" " for x in range(len(word))]
    incorrectlist=[" " for y in range(6)]

def drawhanger():
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
    label1=Label(root,text=info,anchor="w",bg="white",wraplength=350,justify=LEFT)
    label1.place(height=50,width=350,x=250,y=150)
    label2=Label(root,text=info2,anchor="w",bg="white")
    label2.place(height=50,width=350,x=250,y=200)
 
def drawman(times):
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

def settingsbutton():
    button=Button(root,text='settings')
    button.place(height=40,width=60,x=440,y=20)
    button.bind("<Button-1>",setting)

def restart(event):
    if turtlemoving==False:
        t.reset()
        getword()
        loadlists()
        info,info2=getinfo()
        printstatus(info,info2)
        loadletterbutton()
        drawhanger()
        restartbutton()

def setting(event):
    global settings
    settings=Tk()
    settings.title("Settings")
    settings.resizable(0, 0)
    settings.bind("<Destroy>",root.focus_set())
    cv=Canvas(settings,width=120,height=156)
    cv.pack()
    content=readconfig()
    settingsbutton1(content,settings)
    settingsbutton2(content,settings)
    settingsbutton3(content,settings)
    settingsbutton4(content,settings)

def settingsbutton1(content,settings):
    config=content[0].strip()
    button=Button(settings,text='Generate a word')
    if config!="InputWord=True":
        button['text']="Input a word" 
    button.place(height=40,width=125,x=0,y=0)  
    button.bind("<Button-1>",changewordinput)

def settingsbutton2(content,settings):
    config=content[1].strip()
    button=Button(settings,text='Normal dictionary')
    if config!="AdvancedDictionary=True":
        button['text']="Advanced dictionary"
    button.place(height=40,width=125,x=0,y=40)
    button.bind("<Button-1>",changedictionary)

def settingsbutton3(content,settings):
    minvar=int(str(content[2][14])+str(content[2][15]))
    textvar="Minimum Letters:"+str(minvar)
    button=Button(settings,text=textvar)
    button.place(height=40,width=125,x=0,y=80)
    button.bind("<Button-1>",minword)

def settingsbutton4(content,settings):
    maxvar=int(str(content[3][14])+str(content[3][15]))
    textvar="Maximum Letters:"+str(maxvar)
    button=Button(settings,text=textvar)
    button.place(height=40,width=125,x=0,y=120)
    button.bind("<Button-1>",maxword)

def writeconfig(content):
    w=open('config.txt','w+')
    w.writelines(content)

def readconfig():
    w=open('config.txt','r+')
    content=w.readlines()
    return content

def minword(event):
    minletter=simpledialog.askinteger('Hangman game','Enter Minimum letters for random words(Min 2, Max 14)')
    settings.destroy()
    content=readconfig()
    maxletter=int(str(content[3][14])+str(content[3][15]))
    if minletter>1 and minletter<10 and maxletter>=minletter:
        content[2]="Minimumletter=0"+str(minletter)+"\n"
        writeconfig(content)
    elif minletter>9 and minletter<15 and maxletter>=minletter:
        content[2]="Minimumletter="+str(minletter)+"\n"
        writeconfig(content)

def maxword(event):
    maxletter=simpledialog.askinteger('Hangman game','Enter Maximum letters for random words(Min 2, Max 99)')
    settings.destroy()
    content=readconfig()
    minletter=int(str(content[2][14])+str(content[2][15]))
    if maxletter>1 and maxletter<10 and maxletter>=minletter:
        content[3]="Maximumletter=0"+str(maxletter)
        writeconfig(content)
    elif maxletter>9 and maxletter<100 and maxletter>=minletter:
        content[3]="Maximumletter="+str(maxletter)
        writeconfig(content)

def changewordinput(event):
    button=event.widget
    content=readconfig()
    if button['text']=='Generate a word':
        button['text']="Input a word"
        content[0]="InputWord=False\n"
        writeconfig(content)
    else:
        button['text']='Generate a word'
        content[0]="InputWord=True\n"
        writeconfig(content)

def changedictionary(event):
    button=event.widget
    content=readconfig()
    if button['text']=='Normal dictionary':
        button['text']="Advanced dictionary"
        content[1]="AdvancedDictionary=False\n"
        writeconfig(content)
    else:
        button['text']='Normal dictionary'
        content[1]="AdvancedDictionary=True\n"
        writeconfig(content)

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
        button=Button(root,text=chr(i))
        button.place(height=30,width=30,x=xcoor,y=ycoor)
        button.bind("<Button-1>",letterbutton)
        for j in range(len(word)):
            if wordlist[j]==chr(i): 
                disablebutton(button)
        for k in range(6):
            if incorrectlist[k]==chr(i):
                disablebutton(button)
    root.bind("<Key>",keyboardletter)
                
def letterbutton(event):
    button=event.widget
    guess=button['text']
    if event.widget['state']!='disabled' and turtlemoving==False:
        determinecorrect(guess)
        info,info2=getinfo()
        printstatus(info,info2)
        checkstatus()

def keyboardletter(event):
    if event.char>='a' and event.char<='z':
        entered=False
        for j in range(len(word)):
            if wordlist[j]==event.char:
                entered=True
        for k in range(6):
            if incorrectlist[k]==event.char:
                entered=True
        if entered==False and turtlemoving==False:
            determinecorrect(event.char)
            info,info2=getinfo()
            printstatus(info,info2)
            checkstatus()

def determinecorrect(guess):
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
            loadletterbutton()
            drawman(incorrectguesses)
        else: temp=temp+1
    if correct==True:
        loadletterbutton()

def getinfo():
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
        text="You Win, the correct word is "+word
        messagebox.showinfo("Game finished",text)
    if incorrectlist[5]!=" " and finish==False:
        finish=True
        text="You loose, the correct word is "+word
        messagebox.showinfo("Game finished",text)

def disablebutton(button):
    button['state']='disabled'
    button['bd']=0
    button['bg']='red'

def main():
    loadtk()
    drawhanger()
    getword()
    loadlists()
    info,info2=getinfo()
    printstatus(info,info2)
    loadletterbutton()
    restartbutton()
    settingsbutton()
    root.focus_set()
    
main()
root.mainloop()
