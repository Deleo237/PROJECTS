from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def rt():
    w.after_cancel(timer) # type: ignore    
    c1.itemconfig(t1,text="00:00")
    l1.config(text="Timer")
    l2.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def st():
    global reps
    reps+=1
    ws=WORK_MIN*60
    sbs=SHORT_BREAK_MIN*60
    lbs=LONG_BREAK_MIN*60
    if reps%8==0:
        l1.config(text="Long Extra Time",fg=RED)
        count(lbs)
    elif reps%2==1:
        l1.config(text="Baking Time",fg=PINK)
        count(ws)
    else:
        l1.config(text="Short Extra Time",fg=GREEN)
        count(sbs)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count(ct):
    m=ct//60
    s=ct%60
    if s<10:
        s="0"+str(s)
    c1.itemconfig(t1,text=f"{m}:{s}")
    if ct>0:
        global timer
        timer=w.after(1000,count,ct-1)
    else:
        st()
        m=""
        for i in range(reps//2):
            m+="✔️"
        l2.config(text=m)
# ---------------------------- UI SETUP ------------------------------- #
w=Tk()
w.title("Cake timer")
w.config(padx=100,pady=100,bg=YELLOW )
#w.minsize(width=,height=)
im1=PhotoImage(file="cake_PNG13102.png")
im2=PhotoImage(file="cake_PNG13118.png")
im3=PhotoImage(file="R.png")
im4=PhotoImage(file="tomato.png")
#Canvas Widget:Helps to draw something and draw another ontop it
c1=Canvas(width=200,height=158,bg=YELLOW,highlightthickness=0)
c1.create_image(100,79,image=im1)
t1=c1.create_text(100,90,text="00:00",fill="cyan",font=(FONT_NAME,35,"bold"))
c2=Canvas(width=200,height=200,bg=YELLOW,highlightthickness=0)
c2.create_image(100,100,image=im2)
t2=c2.create_text(100,100,text="00:00",fill="red",font=(FONT_NAME,35,"bold"))
c3=Canvas(width=200,height=166,bg=YELLOW,highlightthickness=0)
c3.create_image(100,83,image=im3)
t3=c3.create_text(100,75,text="00:00",fill="blue",font=(FONT_NAME,35,"bold"))
c4=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
c4.create_image(100,112,image=im4)
t4=c4.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
c1.grid(row=1,column=1)
# c2.grid(row=1,column=1)
# c3.grid(row=1,column=1)
# c4.grid(row=1,column=1)
l1=Label(text="Time",font=('Arial',30,"bold"),fg=GREEN,bg=YELLOW)
l1.grid(row=0,column=1)
l2=Label(font=('Arial',15,"bold"),fg=GREEN,bg=YELLOW)
l2.grid(row=3,column=1)
b1=Button(text="Start",command=st,fg=PINK)
b1.grid(row=2,column=0)
b2=Button(text="Reset",command=rt,fg=PINK)
b2.grid(row=2,column=2)
w.mainloop()