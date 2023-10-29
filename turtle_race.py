from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet",
                                prompt=f"Color choices are: {colors}").lower()

all_turtles = []

x_value = -230
y_value = -100
for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=x_value, y=y_value)
    y_value += 40
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle = turtle

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if winner_turtle:
    winner_turtle_color = winner_turtle.pencolor()
    result_turtle = Turtle()
    result_turtle.penup()
    result_turtle.hideturtle()
    if user_bet == winner_turtle_color:
        result_turtle.write(f"You won! The {winner_turtle_color} turtle is the winner!", align="center", font=(
            "Arial", 16, "normal"))
    else:
        result_turtle.write(f"You lost! The {winner_turtle_color} turtle is the winner.", align="center", font=(
            "Arial", 16, "normal"))

screen.exitonclick()
