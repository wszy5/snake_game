from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
snake.create_snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        scoreboard.get_point()
        scoreboard.show_score()
        snake.extend()

    if snake.turtles[0].xcor() > 290 or snake.turtles[0].xcor() < -290 or snake.turtles[0].ycor() > 290 or snake.turtles[0].ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    for turtle in snake.turtles[1:]:
        if snake.turtles[0].distance(turtle) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
