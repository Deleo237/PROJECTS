from turtle import Turtle
COR=[0,-20,-40]
D=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.tt=[]
        self.create()
        self.h=self.tt[0] 
    def create(self):
        for i in range(len(COR)):
            t=Turtle(shape="square")
            t.color("cyan")
            t.pu()
            t.goto(x=COR[i],y=0)
            self.tt.append(t)
    def move(self):
        for n in range(len(self.tt)-1,0,-1):
            nx=self.tt[n-1].xcor()
            ny=self.tt[n-1].ycor()
            self.tt[n].goto(nx,ny)
        self.h.fd(D)
    def up(self):
        if self.h.heading()!=DOWN:
            self.h.setheading(UP)
    def down(self):
        if self.h.heading()!=UP:
            self.h.setheading(DOWN)
    def left(self):
        if self.h.heading()!=RIGHT:
            self.h.setheading(LEFT)
    def right(self):
        if self.h.heading()!=LEFT:
            self.h.setheading(RIGHT)