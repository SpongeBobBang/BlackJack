# Rachel S2O3
from tkinter import*
from tkinter import messagebox
import sys

root=Tk()
root.title("Test Yourself!")
cv=Canvas(root,width=600,height=200)
cv.pack()
def score(event):
    global score
    global no
    answer=event.widget['text']
    if answer=="A":score=score+1
    elif answer=="B":score=score+3
    else:score=score+5
    no=no+1
    if no==12:
        info="Your score is "+str(score)
        messagebox.showinfo('Your Score',info)
        sys.exit()
    else:
        label1=Label(root,text=question[no],anchor="nw",bg="white",wraplength=550,justify=LEFT,font=("",12))
        label1.place(height=100,wiydth=550,x=25,y=10)
A=Button(root,text='A')
A.place(height=50,width=90,x=20,y=130)
A.bind("<Button-1>",score)
B=Button(root,text='B')
B.place(height=50,width=90,x=130,y=130)
B.bind("<Button-1>",score)
C=Button(root,text='C')
C.place(height=50,width=90,x=240,y=130)
C.bind("<Button-1>",score)
no=0
score=0
question=["Which kind of person do you like? A. Stronger than me B. Like and respect me C. Need me",
         "When your friend doesn’t understand and agree with your advice, you will :A. Avoid this problem B. Continue to explain C. Listen to his/her advice",
         "You are having a party with your friends; when you feel upset, you will:A. Do not hide but you will stay here until the party is over.B. Hide your upset and avoid others to see your unhappiness.C. Find an excuse and leave.",
         "When you met a trouble on your working, after work you will:A. Hide it on your heart.B. Talk to your friends.C. Go out for a walk by yourself, forget the trouble.",
         "There is person who you just familiar with; he is trying to teach you a thing that you are very clear with. You will A. Keep silent and keep unlistening.B. Tell him that you already known.C. Wait until he is finished and show that you are very proficent.",
         "You think yourself is :A. Do not have a good chance; otherwise there will be a better life.B. I always spend a plenty of time to do something that I don’t want to do.C. The life that I have know is equal to the effort that I did before.",
         "There will be a holiday soon. You will :A.Spend plenty of time to think about the things that you gonna do.B. Holiday is boring.C. No special feeling.",
         "If the dress up of your family is unsuitable before you go out. You will:A. Insist on leting him/her change the dress up.B. Advise him/her to change the dress up.C.It doesn’t matter.",
         "When a extremly important thing gonna happen. You will :A. Hope to get some supports and encourages.B. Don’ t want to talk this thing with other people.C. Talk with friends with a relaxed mood.",
         "When someone annoyed you. You will :A. Complain about him/her with others.B. Nagging a few words occasionally.C. It doesn’t matter.",
         "When your best friend be angry with you. You will :A. Worry about him and think wether I did something wrong.B. Ask him what the matter with him constantly.C. Ignore him, let him recover by himself.",
         "After you disputed with somebody. You will :A. Still hold you point and prove it.B. Pretend nothing happened.C. Keep calm quickly and apologize."]
label1=Label(root,text=question[0],anchor="nw",bg="white",wraplength=550,justify=LEFT,font=("",12))
label1.place(height=100,width=550,x=25,y=10)  
root.mainloop()
