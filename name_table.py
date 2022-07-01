from turtle import Turtle

FONT = ("Courier", 10, "normal")


class NameTable(Turtle):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def coordinates(self, x, y):
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(f"{self.name}", align="left", font=FONT)

    def game_finished(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Congratulations, you win the game!", align="left", font=FONT)
