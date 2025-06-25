from turtle import Turtle, Screen
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]

myScreen = Screen()

myScreen.setup(width=1000, height=800)
user_bet = myScreen.textinput(title="Bet", prompt="What color do you think will win?")


def generate_turtle(turtle_color, position):
    generated_turtle = Turtle(shape="turtle")
    generated_turtle.color(turtle_color)
    generated_turtle.penup()
    generated_turtle.shapesize(stretch_wid=2, stretch_len=2)
    generated_turtle.goto(-460, 250 - position * 100)
    return generated_turtle


turtles = []
for i, color in enumerate(COLORS):
    new_turtle = generate_turtle(color, i)
    turtles.append(new_turtle)

winner = None
race_has_finished = False
while not race_has_finished:
    for turtle in turtles:
        turtle.forward(randint(1, 10))
        if turtle.xcor() > 450:
            race_has_finished = True
            winner = turtle.color()[0]

if winner == user_bet:
    print(f"You've won! The {winner} turtle won!")
else:
    print(f"You've lost. The {winner} turtle won.")


myScreen.exitonclick()
