import pandas as pd
import turtle


def main():
    image = "blank_states_img.gif"
    screen = turtle.Screen()

    # Draw the map on screen
    screen.addshape(image)
    turtle.shape(image)

    # Turtle to write the states on the map
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    state_coords = pd.read_csv("50_states.csv")
    total_states = len(state_coords)
    n_guessed_states = 0

    while not state_coords.empty:
        answer_state = turtle.textinput(
                title=f"{n_guessed_states}/{total_states} Guess the state!",
                prompt="Input one of the remaining states:")

        if answer_state is None:
            break

        answer_state = answer_state.strip().title()

        if answer_state in state_coords.state.values:
            correct_state = state_coords[state_coords.state == answer_state].iloc[0]

            t.goto(correct_state.x, correct_state.y)
            t.write(answer_state)

            state_coords = state_coords[state_coords.state != answer_state]
            n_guessed_states += 1

    remaining_states = state_coords["state"]
    remaining_states.to_csv("states_to_learn.csv", index=False)

    screen.exitonclick()


if __name__ == "__main__":
    main()
