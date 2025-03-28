from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update()

    def update(self):
        self.hideturtle()
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
