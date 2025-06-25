from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-580, 560)
        self.color("black")

        self.level = 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def show_game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        self.forward(0)
