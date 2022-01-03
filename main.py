from turtle import Screen, Turtle
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()


player = Snake()

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    player.move_snake()

    screen.onkeypress(player.move_left,"Left")
    screen.onkeypress(player.move_right,"Right")
    screen.onkeypress(player.move_up,"Up")
    screen.onkeypress(player.move_down,"Down")


    if player.segment[0].xcor() >= 300 or player.segment[0].xcor() <= -300 or player.segment[0].ycor() >= 300 or player.segment[0].ycor() <= -300:
        game_is_on = False




















screen.exitonclick()

