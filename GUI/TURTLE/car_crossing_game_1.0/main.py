import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
p=Player()
c=CarManager()
sc=Scoreboard()
screen.onkeypress(p.move,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    sc.dis()
    #Increase cars
    c.create()
    #Move cars
    c.move()
    #Detect if cross successful
    if p.ycor()>=290:
        p.levelup()
        c.levelup()
        sc.levelup()
        
    #Detect collision with car
    for car in c.motos:
        if car.distance(p)<25:
            sc.gv()
            game_is_on=False

screen.exitonclick()