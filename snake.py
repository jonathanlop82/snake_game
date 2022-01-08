from turtle import Screen, Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self,size=3):
        self.size = size
        self.segment = []
        self.create_snake()


    def create_snake(self):
        position = 0
        for i in range(self.size):
            self.segment.append(Turtle(shape="square"))
            self.segment[i].color("green")
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
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def move_right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def move_up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def move_down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def grow_snake(self):
        self.segment.append(Turtle(shape="square"))
        self.segment[-1].penup()
        self.segment[-1].goto(self.segment[-2].position())
        self.segment[-1].color("green")
        self.size += 1

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.size = 3
        self.create_snake()
        self.segment[0] = self.segment[0]




