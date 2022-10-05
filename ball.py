from turtle import*

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        
        
       
    def make_ball(self):

        self.color("white")
        self.shape("circle")

    def ball_move(self):
        
        self.penup()
        x_move_new = self.xcor() + self.x_move
        y_move_new = self.ycor() + self.y_move
        self.goto(x_move_new, y_move_new)
        
    def bounce_y(self):
        self.y_move *= -1

    
    def bounce_x(self):
        self.x_move *= -1

    def restart_ball(self):
        self.goto(0, 0)
        self.bounce_x()


    