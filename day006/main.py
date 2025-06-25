def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
go_to_left = 1

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()