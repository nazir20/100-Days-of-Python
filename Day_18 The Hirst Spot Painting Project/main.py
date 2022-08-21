# @imports
import colorgram  # pip install colorgram
import turtle as turtle_module
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 40)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


turtle = turtle_module.Turtle()
turtle_module.colormode(255)
turtle.speed(0)
turtle.penup()
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):

    turtle.dot(20, random.choice(rgb_colors))
    turtle.forward(50)
    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

