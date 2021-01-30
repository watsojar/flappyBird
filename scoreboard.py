from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.score = 0
        self.color("white")
        with open("data.txt") as data:
            self.highScore = int(data.read())

    def writeScore(self):
        self.write(f"Score: {int(self.score)} \nHigh score: {int(self.highScore)}", align="center",
                   font=("Calibre", 30, "normal"))

    def newHighScore(self):
        self.clear()
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{int(self.highScore)}")

    def updateScore(self):
        self.clear()
        self.score += 0.5

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game over!", align="center", font=("Calibre", 80, "normal"))
        self.goto(0, -100)
        self.write(f"Score: {int(self.score)}", align="center", font=("Calibre", 30, "normal"))
