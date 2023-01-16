import time
from email.mime import image
from tkinter import *
from tkinter.ttk import Combobox
from turtle import left

from playsound import playsound

screen=Tk()
screen.title("MP3 player(powerderd_by 'py*')")
screen.geometry('700x500+00+00')
icon_pic=PhotoImage(file='C:\\Users\\neha\\Links\\project3Mp3\\images.png')
screen.iconphoto(False,icon_pic)
screen.config(bg='black')
screen.resizable(False,False)


logoimp=PhotoImage(file = 'C:\\Users\\neha\\Links\\project3Mp3\\vvp.png')
Label(screen,image=logoimp, bg = "black",height=400,width=520).place(x=90,y=50)


#adding frames
f1=Frame(screen,bg='red',width=3000,height=100)
f1.pack(side=TOP)
f2=Frame(screen,width=100,bg='green',height=900)
f2.pack(side=LEFT)
f3=Frame(screen,bg='green',width=100,height=900)
f3.pack(side=RIGHT)
f4=Frame(screen,bg='red',width=3000,height=100)
f4.pack(side=BOTTOM)

#adling some label
l1=Label(f1,text='MP3 PLAYER',fg='black',bg='red',font='"Segoe Script" 30 bold')
l1.place(x=210,y=10)

logoimp1=PhotoImage(file = 'C:\\Users\\neha\\Links\\project3Mp3\\ddnt.png')
Label(f1,image=logoimp1, bg = "black",height=60,width=60).place(x=10,y=11)

def devine():
    musvar=musisc.get() # ***most imp to learn that if you want any thing to work from entry label or list or combobox or from anyway first to get() it on particular variable or object the use it
    try:
        if 'dewani' in musvar:
            playsound("C:\\Users\\neha\\Links\\project3Mp3\\mysngs\\dewani.mp3")
        elif 'dil_galti' in musvar:
            playsound("C:\\Users\\neha\\Links\\project3Mp3\\mysngs\\dilgalti.mp3")
        elif 'keasria' in musvar:
            playsound("C:\\Users\\neha\\Links\\project3Mp3\\mysngs\\kesaria.mp3")
        elif 'rockstar' in musvar:
            playsound("C:\\Users\\neha\\Links\\project3Mp3\\mysngs\\rocks.mp3")
        elif 'let me u' in musvar:
            #logoimp1=logoimp
            #logoimp1=PhotoImage(file = 'play.png')
            #Label(screen,image=logoimp1, bg = "black",height=600,width=600).place(x=103,y=12)
            playsound("C:\\Users\\neha\\Links\\project3Mp3\\mysngs\\djsnk.mp3")
        elif 'shiva' in musvar:
            
            playsound("C:\\Users\\neha\\Links\\project3Mp3\\mysngs\\shiva.mp3")
        elif 'breakup vibe' in musvar:
            playsound("C:\\Users\\neha\\Links\\project3Mp3\\mysngs\\The_Breakup_Song.mp3")

        
        elif '404' in musvar:
            lblere=Label(screen,text='Not available yet',bg='yellow',fg='red',font='italic 45 bold')
            lblere.place(x=110,y=100)
        else:
            lbere3=Label(screen,text='Songs cannot be empty',bg='purple',fg='red',font='arial 33 bold')
            lbere3.place(x=100,y=100)
     
       #time.sleep(7)
    except Exception as Er:
        lbere2=Label(screen,text='bad request :( ',bg='yellow',width=62,height=3,fg='red',font='arial 10 bold')
        lbere2.place(x=100,y=100)

   

        
def info():
    l4=Label(f4,text='''                        >model 2.2
                        >gen1stdr
                        >ver#ER
               >anu12104565@gmail.com''',fg='yellow',bg='red',font='italic 8 bold')
    l4.place(x=320,y=10)

def destr():
    screen.destroy()


#varry1=StringVar()
#enty=Entry(screen,textvariable=varry1).pack()




#adding combo
musisc=Combobox(screen,values=('keasria','let me u','rockstar','dil_galti','shiva','breakup vibe','dewani','404'))
musisc.place(x=290,y=210)


#buttons implementationsss
#img_fr_btply=PhotoImage(file='play.png')
btn1=Button(text='PLAY',command=devine,bg='powder blue',bd=2)
btn1.place(x=330,y=260)

btn2=Button(text='defo',command=info,font=('arial 6 bold'),bg='yellow',bd=2)
btn2.place(x=540,y=380)

btn3=Button(text='Quit',command=destr,bg='red',bd=2)
btn3.place(x=400,y=260)

screen.mainloop()#most imp
