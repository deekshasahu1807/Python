from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("white")

def move_forwards(): # W: Forwards
    tim.forward(50)

def move_backwards(): # S: Backwards
    tim.backward(10)

def move_anti_clockwise(): # A: Counter-Clockwise
    tim.left(10)
    tim.forward(50)

def move_clockwise(): # D: Clockwise
    tim.right(10)
    tim.forward(50)

def clear_screen(): # C: Clear Drawing
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=move_anti_clockwise)
screen.onkey(key="D", fun=move_clockwise)
screen.onkey(key="C", fun=clear_screen)

screen.exitonclick()

