from turtle import*

class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        
        


    def make_right(self):
        
        # self.padle.screen.tracer(0)
        self.setheading(90)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.goto(350, 0)
        # self.padle.screen.update()
        
        
    def make_left(self):
        
        # self.padle.screen.tracer(0)
        self.setheading(90)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.goto(-350, 0)
        # self.padle.screen.update()

        
    def move_up(self):

        self.forward(20)
        
        
    def move_down(self):

        self.backward(20)