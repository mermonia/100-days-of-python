from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, step=10):
        super().__init__()
        self.hideturtle()
        self.setpos(0, 540)
        self.color('white')

        self.score_step = step
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score += self.score_step
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Cambria", 32, "bold"))

    def show_game_over(self):
        self.setpos(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Cambria", 32, "bold"))
