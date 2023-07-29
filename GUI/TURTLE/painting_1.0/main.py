#Hirst Painting Part1
# import colorgram
# col=colorgram.extract('picb.png',30)
# c=[]
# for i in col:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     t=(r,g,b)
#     c.append(t)
# print(c)
#OR
from random import randint,choice
from turtle import Turtle,Screen
import turtle 
turtle.colormode(255)
def rc():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    t=(r,g,b)
    return t
a=[]
for i in range(100):
    a.append(rc())
#Part2
t=Turtle()
t.speed(0)
t.hideturtle()
t.setheading(225)
t.pu()
t.forward(350)
t.setheading(0)
for y in range(1,101):
    t.pu()
    t.fd(50)
    t.dot(20,choice(a))
    if y%10==0:
        t.setheading(90)
        t.pu()
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
s=Screen()
s.exitonclick()