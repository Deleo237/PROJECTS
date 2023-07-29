from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Player(Turtle):
    def __init__(self):
        """Creates the turtle"""
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.c=0
        self.levelup()
        self.left(90)
    def move(self):
        """Moves the turtle upward"""
        self.fd(MOVE_DISTANCE)
    def levelup(self):
        """Next level"""
        self.goto(STARTING_POSITION)
        self.color(COLORS[self.c])
        self.c+=1