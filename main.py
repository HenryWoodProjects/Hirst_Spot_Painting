import colorgram
import turtle as t
import random

t.colormode(255)
timmy_colour = (20, 100, 240)
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color(timmy_colour)
timmy.pensize(50)


def random_colour(number_of_colours):
    random_number = random.randint(1, number_of_colours) - 1
    image_colours = colorgram.extract('Logo.png', number_of_colours)
    new_colour = image_colours[random_number]
    rgb = new_colour.rgb
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    rgb_tuple = (r, g, b)
    return rgb_tuple


def draw_dot(number_of_colours, dot_size):
    dot_colour = random_colour(number_of_colours)
    timmy.pencolor(dot_colour)
    timmy.dot(dot_size)


def new_column(columns, dot_spacing):
    timmy.backward(columns * dot_spacing)
    timmy.left(90)
    timmy.forward(dot_spacing)
    timmy.right(90)


def draw_art(number_of_colours, dot_size, dot_spacing, rows, columns):
    row = 1
    column = 1
    while row <= rows:
        while column <= columns:
            timmy.pendown()
            draw_dot(number_of_colours, dot_size)
            timmy.penup()
            timmy.forward(dot_spacing)
            column += 1
        new_column(columns, dot_spacing)
        row += 1
        column = 1


timmy.speed("fastest")
timmy.penup()
timmy.backward(250)
timmy.right(90)
timmy.forward(250)
timmy.left(90)
draw_art(6, 20, 50, 10, 10)

screen = t.Screen()
screen.exitonclick()
