from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


snake =  []
position = 0
#Init Snake body
for i in range(3):
    snake.append(Turtle(shape="square"))
    snake[i].color("white")
    snake[i].goto(x=position,y=0)
    position -= 20












screen.exitonclick()

