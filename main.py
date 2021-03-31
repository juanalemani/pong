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

screen.listen()
screen.onkey(paddle_1.go_up,key="Up")
screen.onkey(paddle_1.go_down,key="Down")
screen.onkey(paddle_2.go_up,key="w")
screen.onkey(paddle_2.go_down,key="s")
is_on = True

while is_on == True:
    time.sleep(0.1)
    screen.update()
    ball.move()




screen.exitonclick()