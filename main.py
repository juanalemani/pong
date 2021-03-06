from scoreboard import Scoreboard
from ball import Ball
from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((350,0))
paddle_2 = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_1.go_up,key="Up")
screen.onkey(paddle_1.go_down,key="Down")
screen.onkey(paddle_2.go_up,key="w")
screen.onkey(paddle_2.go_down,key="s")
is_on = True

while is_on == True:
    time.sleep(ball.move_spead)
    screen.update()
    ball.move()
    
    if abs(ball.ycor()) > 295:
        ball.bounce_y()

    if ball.xcor() > 395:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -395:
        ball.reset_position()
        scoreboard.r_point()

    if (ball.distance(paddle_1) < 50  and ball.xcor() > 310) or (ball.distance(paddle_2) < 50 and ball.xcor() <-310): 
        ball.bounce_x()
    

screen.exitonclick()