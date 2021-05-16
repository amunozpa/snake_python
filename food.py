from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-290, 290), random.randint(-290, 290))
