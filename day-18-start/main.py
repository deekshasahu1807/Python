import turtle as t
import random

screen = t.Screen()
tim = t.Turtle()
t.colormode(255)

# Change the shape & color of turtle
tim.shape("turtle")
tim.color("red", "yellow")

# Draw a square
for _ in range(4):
    tim.forward(100)
    tim.right(90)

# Draw a dashed line using a loop
for _ in range(15):
    tim.forward(10)    # Draw a line segment
    tim.penup()        # Lift the pen to skip
    tim.forward(10)    # Create a blank space
    tim.pendown()  # Lower the pen to draw

# Draw shapes: triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "coral"]
sides = 3
while sides <= 10:
    angle = 360 / sides
    # Triangle
    for _ in range(sides):
        tim.pencolor(random.choice(colors))
        tim.forward(100)
        tim.right(angle)
    sides += 1

# Draw random pattern using random color
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for i in range(200):
    tim.pencolor(random_color())
    tim.fd(50)
    tim.setheading(random.choice(directions))

# Draw Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()

