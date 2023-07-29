from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.pu()
        self.hideturtle()
        self.s=1
        self.dis()
    def levelup(self):
        """Add score"""
        self.s+=1
    def gv(self):
        """Shows that the game is over"""
        self.goto(0,0)
        self.write(arg="GAME OVER",move=False,align="center",font=FONT)
    def dis(self):
        self.clear()
        self.goto(-220,260)
        self.write(f"Level: {self.s}",False,"center",FONT)

        
