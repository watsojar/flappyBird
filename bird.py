from turtle import Turtle

STARTING_POS = (-220, 0)
FALL = 12
JUMP = 60


class Bird(Turtle):

    def __init__(self):
        super(Bird, self).__init__()
        self.color("white")
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POS)
        self.right(45)

    def fall(self):
        newY = self.ycor() - FALL
        self.goto(self.xcor(), newY)

    def jump(self):
        self.left(90)
        newY = self.ycor() + JUMP
        self.goto(self.xcor(), newY)
        self.right(90)
