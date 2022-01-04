from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.count = 0
        self.write_score()


    def write_score(self):
        self.write(f"Score: {self.count}", False, align='center', font=('Arial', 20, 'normal'))

    def sum_point(self):
        self.count += 1