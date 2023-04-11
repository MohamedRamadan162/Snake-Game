from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")

diff = screen.textinput("difficulty", "Choose a difficulty (easy/ medium/ hard")


def difficulty(diffi):
    if diffi == "easy":
        return 0.7
    elif diffi == "medium":
        return 1
    elif diffi == "hard":
        return 1.7


screen.tracer(0)

snake = Snake(difficulty(diff))
food = Food()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

score = 0
score_board = ScoreBoard()
run = True
while run:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.spawn()
        snake.grow()
        score += 1
        score_board.increase_score()
    if snake.border_collision():
        score_board.game_over()
        run = False

    for square in snake.squares[1:]:
        if snake.head.distance(square) <= 10:
            score_board.game_over()
            run = False


screen.exitonclick()
