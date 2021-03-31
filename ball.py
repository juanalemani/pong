from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shape("square")
        self.penup()
        self.color("white")
        
    def move(self):
        new_x = self.xcor() + 8
        new_y = self.ycor() + 8
        self.goto(new_x,new_y)