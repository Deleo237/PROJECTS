from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class Ui:
    def __init__(self,ques:QuizBrain):
        self.q=ques
        self.w=Tk()
        self.w.title("Quizzler")
        self.w.config(padx=20,pady=20,bg=THEME_COLOR)
        self.l=Label(text=f"Score: 0",fg="white",bg=THEME_COLOR,font=('Arial',10,"bold"))
        self.l.grid(row=0,column=1)
        self.c=Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.qt=self.c.create_text(150,125,width=280,text="This is text",fill=THEME_COLOR,font=('Arial',20,"italic"))
        self.c.grid(row=1,column=0,columnspan=2,pady=50)
        imf=PhotoImage(file="/images/false.png")
        imt=PhotoImage(file="/images/true.png")
        self.bf=Button(image=imf,highlightthickness=0,command=self.tr)
        self.bf.grid(row=2,column=0)
        self.bt=Button(image=imt,highlightthickness=0,command=self.fa)
        self.bt.grid(row=2,column=1)
        self.getques()
        self.w.mainloop()
    def getques(self):
        self.c.config(bg="white")
        if self.q.still_has_questions():
            q_text=self.q.next_question()
            self.l.config(text=f"Score: {self.q.score}")
            self.c.itemconfig(self.qt,text=q_text)
        else:
            q_text="THIS IS ALL ABOUT THE QUESTION"
            self.c.itemconfig(self.qt,text=q_text)
            self.l.config(text=f"Final Score: {self.q.score}")
            self.bt.config(state="disabled")
            self.bf.config(state="disabled")
    def tr(self):
        self.isright(self.q.check_answer("True"))
    def fa(self):
        self.isright(self.q.check_answer("False"))
    def isright(self,n):
        if n:
            self.c.config(bg="green")
        else:
            self.c.config(bg="red")
        self.w.after(1000,self.getques)
