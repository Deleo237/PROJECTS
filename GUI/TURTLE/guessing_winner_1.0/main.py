from random import randint
from turtle import Turtle,Screen
t1=Turtle()
t2=Turtle()
t3=Turtle()
t4=Turtle()
t5=Turtle()
t6=Turtle()
t7=Turtle()
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
t5.shape("turtle")
t6.shape("turtle")
t7.shape("turtle")
s=Screen()
c=["red","orange","yellow","green","blue","cyan","purple"]
s.setup(width=500,height=400)
race=0
b=s.textinput(title="Make A Bet",prompt="Which turtle will win the race? Enter a color: ")
t1.pu()
t1.color(c[0])
t2.pu()
t2.color(c[1])
t3.pu()
t3.color(c[2])
t4.pu()
t4.color(c[3])
t5.pu()
t5.color(c[4])
t6.pu()
t6.color(c[5])
t7.pu()
t7.color(c[6])
t1.goto(x=-240,y=-150)
t2.goto(x=-240,y=-100)
t3.goto(x=-240,y=-50)
t4.goto(x=-240,y=0)
t5.goto(x=-240,y=50)
t6.goto(x=-240,y=100)
t7.goto(x=-240,y=150)
#OR
py=[-150,-100,-50,0,50,100,150]
tt=[]
for i in range(7):
    t=Turtle(shape="turtle")
    t.pu()
    t.color(c[i])
    t.goto(x=-210,y=py[i])
    tt.append(t)
if b!=None:
        race=1
while race==1:
    for tl in tt:
        if tl.xcor()>220:
            race=0
            wc=tl.pencolor()
            if wc==b:
                print(f"You've won! The {wc} turtle is the winner!")
            else:
                print(f"You've lost! The {wc} turtle is the winner!")
        r=randint(0,10)
        tl.fd(r)
s.exitonclick()