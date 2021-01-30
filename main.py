"""
Flappy Bird

Create a bird
    be able to jump
        effected by gravity

create pipes
    have pipes travel towards bird
    randomly generate heights every X pixels
    detect collisions

scoreboard
    add score each time successfully goes through pipe
    be able to read and write to high score file

"""

from turtle import Screen
from bird import Bird
from pipes import Pipes
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("blue")

bird = Bird()
pipe = Pipes()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(bird.jump, "space")

gameRun = True
numLoops = 0
while gameRun:
    time.sleep(0.05)
    screen.update()
    if scoreboard.score > scoreboard.highScore:
        scoreboard.newHighScore()
    scoreboard.writeScore()
    bird.fall()
    pipe.movePipes()
    if numLoops == 0 or numLoops % 30 == 0:
        pipe.spawnPipe()

    # check for pipe collisions
    for elm in pipe.pipes:
        birdX = bird.xcor()
        pipeX = elm.xcor()
        if pipeX - 55 < birdX < pipeX + 55 and (bird.distance(elm) < 200):
            gameRun = False
            break
        # check if player scored a point
        if birdX > pipeX + 55 and pipeX > -282:
            scoreboard.updateScore()

    # check if bird hit ground
    if bird.ycor() < -300:
        gameRun = False

    pipe.destroyUsedPipes()
    numLoops += 1

scoreboard.gameOver()

screen.exitonclick()
