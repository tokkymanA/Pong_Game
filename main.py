from turtle import*
from paddle import*
from ball import*
import time
from score_board import*

score = Score()
screen = Screen()
pong = Turtle()
ball = Ball()


screen.tracer(0)
pong.hideturtle()
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.title("Pong game by tokkyman")


ball.make_ball()
paddle_right = Paddle()
paddle_left = Paddle()
paddle_right.make_right()
paddle_left.make_left()


screen.listen()
screen.onkey(fun=paddle_right .move_up, key="Up")
screen.onkey(fun=paddle_right .move_down, key="Down")
screen.onkey(fun=paddle_left.move_up, key="w")
screen.onkey(fun=paddle_left.move_down, key="s")

game_on = True
timer = 0.1
while game_on:

    time.sleep(timer)
    screen.update()
    ball.ball_move()
    
    if ball.ycor() == 280 or ball.ycor() == -280 :
        ball.bounce_y()
   
    if ball.distance(paddle_right) <=50 and ball.xcor() >= 320:
        ball.bounce_x()
        timer = timer * 0.9


    if ball.distance(paddle_left) <=50 and ball.xcor()  <= -320:
        ball.bounce_x()
        timer = timer * 0.9
        


    if ball.xcor() > 400 :
        ball.restart_ball()
        timer = 0.1
        score.add_l()

    
    if ball.xcor() < -400:
        ball.restart_ball()
        timer = 0.1
        score.add_r()





screen.exitonclick()