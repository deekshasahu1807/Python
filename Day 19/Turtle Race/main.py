from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color : ")
if user_bet:
    is_race_on = True

colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
y = [-100, -70, -40, -10, 20, 50]

all_turtles = []
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-240, y=y[turtle_index])
    all_turtles.append(tim)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} is the winner!")
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()