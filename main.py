from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
import random

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.clear()
        score.score_up()
        snake.add_part_snake()

    for n in range(1, len(snake.turtles)):
        if snake.head.distance(snake.turtles[n]) < 10:
            print("lose")
            screen.clear()
            screen.bgcolor("black")
            score.final_score()
            game_on = False
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        print("lose")
        screen.clear()
        screen.bgcolor("black")
        score.final_score()
        game_on = False
        # screen.clear()


screen.exitonclick()
