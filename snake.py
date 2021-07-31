from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITIONS = [(-20, 0), (-40, 0), (-60, 0)]

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.move()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)



    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.turtles.append(turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)
            self.move()

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)
            self.move()

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)
            self.move()

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)
            self.move()

    def move(self):
        for seq_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[seq_num - 1].xcor()
            new_y = self.turtles[seq_num - 1].ycor()
            self.turtles[seq_num].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def reset(self):
        for t in self.turtles:
            t.goto(x=1000, y=1000)
        self.turtles.clear()
        self.create_snake()
