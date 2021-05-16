from turtle import Turtle, Screen
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake(parts=3)
        self.head = self.turtles[0]

    def create_snake(self, parts):
        x = 0
        for t in range(parts):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.color("green")
            new_turtle.shape("square")
            new_turtle.goto(x, 0)
            x -= 20
            self.turtles.append(new_turtle)

    def add_part_snake(self):
        new_part = Turtle()
        new_part.hideturtle()
        new_part.speed(0)
        new_part.penup()
        new_part.color("green")
        new_part.shape("square")
        self.turtles.append(new_part)

    def move(self):
        # print(len(self.turtles))
        for n in range(len(self.turtles) - 1, 0, -1):
            self.turtles[n - 1].showturtle()
            xcor = self.turtles[n - 1].xcor()
            ycor = self.turtles[n - 1].ycor()
            self.turtles[n].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)
        # print(self.turtles[0].heading())
        # print(self.turtles[1].heading())
        # print(self.turtles[2].heading())
        # print(self.turtles[0].towards(self.turtles[1].position()))

    def up(self):
        if self.head.heading() != DOWN:
            if self.turtles[0].towards(self.turtles[1].position()) != 90.0:
                self.head.setheading(UP)
                self.turtles[1].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            if self.turtles[0].towards(self.turtles[1].position()) != 270.0:
                self.head.setheading(DOWN)
                self.turtles[1].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            if self.turtles[0].towards(self.turtles[1].position()) != 180.0:
                self.head.setheading(LEFT)
                self.turtles[1].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            if self.turtles[0].towards(self.turtles[1].position()) != 0.0:
                self.head.setheading(RIGHT)
                self.turtles[1].setheading(RIGHT)
