from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.set_position()

    def set_position(self):
        self.goto(random.randint(-13,13) * 20, random.randint(-13,13) * 20)

