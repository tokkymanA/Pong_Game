from turtle import Turtle
from unicodedata import name


class Score(Turtle):
    def __init__(self) :
        super().__init__()
        
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=('Arial', 50 , "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=('Arial', 50 , "normal"))



    def add_l(self):
        self.l_score += 1
        self.update_score()

    def add_r(self):
        self.r_score += 1
        self.update_score()