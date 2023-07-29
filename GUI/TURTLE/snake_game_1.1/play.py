#Snake game in action
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
s=Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("DELEOTECH Snake Game")
s.tracer(0)
sn=Snake()
fo=Food()
sc=Score()
s.listen()
s.onkey(sn.up,"Up")
s.onkey(sn.down,"Down")
s.onkey(sn.left,"Left")
s.onkey(sn.right,"Right")
# fo.move()
p=1
while p==1:
    s.update()
    time.sleep(0.2)
    sn.move()
    sc.dis()
    #Detecting collision with food and keeping scores
    if sn.h.distance(fo)<15:
        fo.refresh()
        sn.extend()
        sc.track()
    #Detecting collision with wall
    if sn.h.xcor()<-280 or sn.h.ycor()<-280 or sn.h.xcor()>280 or sn.h.ycor()>280:
        sc.gv()
        
        p=0
    #Detecting collision with body
    for i in sn.tt[1:]:
        if sn.h.distance(i)<10:
            sc.gv()
            p=0
    if p==0:
        anss=str(s.textinput(f"Your Score is {sc.n}","Will you like to play again"))
        ans=anss.upper()
        if ans=="YES":
            p=1
        elif ans=="NO":
            p=0
        else:
            p=0
    #OR
    # for i in sn.tt:
    #     if i==sn.h:
    #         pass
    #     elif sn.h.distance(i)<10:
    #         sc.gv()
    #         p=0
s.exitonclick()