from turtle import Turtle


class ScoreCounter(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.score = 0

        self.color('white')
        self.penup()
        self.hideturtle()
        self.setpos(x, y)
        self.write(self.score, align='center', font=('Cambria', 40, 'bold'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, align='center', font=('Cambria', 40, 'bold'))
