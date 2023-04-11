from turtle import Screen, Turtle


class Snake(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.squares = []
        self.snake_size = 3
        self.speed = speed
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for i in range(self.snake_size):
            new_square = Turtle("square")
            new_square.color("blue")
            new_square.penup()
            new_square.goto(new_square.xcor() - 20 * i, new_square.ycor())
            self.squares.append(new_square)

    def add_square(self, position):
        new_square = Turtle("square")
        new_square.color("blue")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def grow(self):
        self.add_square(self.squares[-1].pos())

    def move(self):
        for sq_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[sq_num - 1].xcor()
            new_y = self.squares[sq_num - 1].ycor()
            self.squares[sq_num].goto(new_x, new_y)
        self.head.forward(20 * self.speed)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def border_collision(self):
        if int(self.head.xcor()) >= 300 or int(self.head.ycor()) >= 300 or int(self.head.xcor()) <= -300 or int(
                self.head.ycor()) <= -300:
            return True
        else:
            return False

