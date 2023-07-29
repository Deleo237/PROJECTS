from turtle import Turtle
from random import choice,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CORD=[-240,-220,-200,-180,-160,-140,-120,-100,-80,-60,-40,-20,0,20,40,60,80,100,120,140,160,180,200,220,240]

class CarManager():
    def __init__(self):
        self.d=STARTING_MOVE_DISTANCE
        self.n=6
        self.motos=[]
    def create(self):
        ch=randint(1,self.n)
        if ch==1:
            moto=Turtle()
            moto.shape("square")
            moto.shapesize(1,2,4)
            moto.color(choice(COLORS))
            moto.pu()
            moto.goto(300,choice(CORD))
            self.motos.append(moto)
    def move(self):
        for m in self.motos:
            m.backward(self.d)
    def levelup(self):
        self.d+=MOVE_INCREMENT
        if self.n>2:
            self.n-=1
    