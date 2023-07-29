from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.n=0
        self.dis()
    def track(self):
        """Add score"""
        self.n+=1
    def gv(self):
        """Shows that the game is over"""
        self.goto(0,0)
        self.write(arg="GAME OVER",move=False,align="center",font=("Courier",20,"bold"))
    def dis(self):
        """Display the scores"""
        self.clear()
        self.hideturtle()
        self.goto(0,280)
        self.color("white")
        self.write(arg=f"SCORE: {self.n}",move=False,align="center",font=("Courier",15,"bold"))
