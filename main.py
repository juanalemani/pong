from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((350,0))
paddle_2 = Paddle((-350,0))

screen.listen()
screen.onkey(paddle_1.go_up,key="Up")
screen.onkey(paddle_1.go_down,key="Down")
screen.onkey(paddle_2.go_up,key="w")
screen.onkey(paddle_2.go_down,key="s")
is_on = True
while is_on == True:
    screen.update()





screen.exitonclick()