from random import choice
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
try:
    dt=pandas.read_csv("./data/learnwords.csv")
except:
    dt=pandas.read_csv("./data/french_words.csv")
lan=dt.to_dict("records")
cd={}
def rt():
    global cd,ft
    w.after_cancel(ft)
    cd=choice(lan)
    l1=cd["French"]
    c.itemconfig(cim,image=im1)
    c.itemconfig(cte,text="French",fill="black")
    c.itemconfig(ctt,text=l1,fill="black")
    ft=w.after(5000,ch)
def ch():
    l2=cd["English"]
    c.itemconfig(cim,image=im2)
    c.itemconfig(cte,text="English",fill="white")
    c.itemconfig(ctt,text=l2,fill="white")
def wg():
    lan.remove(cd)
    dt=pandas.DataFrame(lan)
    dt.to_csv("./data/learnwords.csv",index=False)
    rt()
        
w=Tk()
w.title("Flashy")
ft=w.after(5000,ch)
w.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
im1=PhotoImage(file="./images/card_front.png")
im2=PhotoImage(file="./images/card_back.png")
c=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
cim=c.create_image(400,263,image=im1)
cte=c.create_text(400,150,text="",fill="white",font=("Ariel",40,"italic"))
ctt=c.create_text(400,263,text="",fill="white",font=("Ariel",60,"bold"))
c.grid(row=0,column=0,columnspan=2)
im3=PhotoImage(file="./images/right.png")
b1=Button(image=im3,highlightthickness=0,command=rt)
b1.grid(row=1,column=1)
im4=PhotoImage(file="./images/wrong.png")
b2=Button(image=im4,highlightthickness=0,command=wg)
b2.grid(row=1,column=0)
rt()

w.mainloop()