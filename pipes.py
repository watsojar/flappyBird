from turtle import Turtle
import random

SPAWN_POINT = 400
PIPE_MOVE = 10


class Pipes(Turtle):

    def __init__(self):
        super(Pipes, self).__init__()
        self.hideturtle()
        self.pipes = []

    def spawnPipe(self):
        bottomPipe = Turtle()
        topPipe = Turtle()
        bottomPipe.hideturtle()
        topPipe.hideturtle()
        bottomPipe.shape("square")
        topPipe.shape("square")
        bottomPipe.color("green")
        topPipe.color("red")
        bottomPipe.penup()
        topPipe.penup()
        topPipe.turtlesize(stretch_wid=20, stretch_len=4)
        bottomPipe.turtlesize(stretch_wid=20, stretch_len=4)

        randomY = random.randint(-500, -50)
        topPipeYAdjustment = randomY + 600

        bottomPipe.goto(SPAWN_POINT, randomY)
        topPipe.goto(SPAWN_POINT, topPipeYAdjustment)

        topPipe.showturtle()
        bottomPipe.showturtle()

        self.pipes.append(bottomPipe)
        self.pipes.append(topPipe)

    def movePipes(self):
        for pipe in self.pipes:
            newX = pipe.xcor() - PIPE_MOVE
            pipe.goto(newX, pipe.ycor())

    def destroyUsedPipes(self):
        for index in range(0, len(self.pipes) - 1):
            if self.pipes[index].xcor() < -400:
                usedTurtle = self.pipes[index]
                usedTurtle.hideturtle()
                usedTurtle.clear()
                del self.pipes[index]
