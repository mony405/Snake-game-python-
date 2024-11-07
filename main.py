from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

scr=Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title("Snack game")
scr.tracer(0)

food=Food()
snake=Snake()
score=Score()
scr.listen()

scr.onkey(snake.up ,"Up")
scr.onkey(snake.down ,"Down")
scr.onkey(snake.left ,"Left")
scr.onkey(snake.right ,"Right")
game_on = True

while game_on:
    scr.update()
    time.sleep(0.09)
    snake.move()
    # detect collision with food
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    # detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.reset_scoreboard()
        snake.reset_snake()
    # tail collies with tail
    for segment in snake.seg[1:] :
        if snake.head.distance(segment)<10:
            score.reset_scoreboard()
            snake.reset_snake()
scr.exitonclick()