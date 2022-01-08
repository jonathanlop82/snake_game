from turtle import Turtle

with open("my_file.txt") as file:
    HIGH_SCORE = int(file.read())

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.count = 0
        self.high_score = HIGH_SCORE
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"Score: {self.count}  High Score: {self.high_score}", False, align='center', font=('Courier', 20, 'normal'))

    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
        self.count = 0
        self.write_score()
        with open("my_file.txt", mode="w") as file:
            file.write(str(self.high_score))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER \nScore: {self.count}", False, align='center', font=('Courier', 30, 'normal'))

    def sum_point(self):
        self.count += 1
        self.write_score()