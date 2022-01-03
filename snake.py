from turtle import Screen, Turtle
import time


class Snake:

    def __init__(self,size=3):
        self.size = size
        self.segment = []
        self.create_snake()


    def create_snake(self):
        position = 0
        for i in range(self.size):
            self.segment.append(Turtle(shape="square"))
            self.segment[i].color("white")
            self.segment[i].penup()
            self.segment[i].goto(x=position, y=0)
            position -= 20

    def move_snake(self):

        time.sleep(0.1)
        for i in range(self.size - 1, 0, -1):
            previous_pos = self.segment[i - 1].position()
            self.segment[i].goto(previous_pos)
            # time.sleep(1)

        self.segment[0].forward(20)

    def move_left(self):
        self.segment[0].setheading(180)

    def move_right(self):
        self.segment[0].setheading(0)

    def move_up(self):
        self.segment[0].setheading(90)

    def move_down(self):
        self.segment[0].setheading(270)


