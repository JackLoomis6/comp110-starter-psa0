import math
import turtle


screen = turtle.Screen()
screen.bgcolor("pale turquoise")
t = turtle.Turtle()
t.speed(0)
t.pensize(5)


def draw_half_oval(width, height, base, outline, fill):
    t.penup()
    t.goto(-width, base)
    t.pendown()
    t.color(outline, fill)
    t.begin_fill()
    t.forward(width * 2)
    for angle in range(0, 181, 3):
        radians = math.radians(angle)
        t.goto(width * math.cos(radians), base + height * math.sin(radians))
    t.end_fill()


draw_half_oval(190, 170, -105, "darkgreen", "forestgreen")
draw_half_oval(174, 154, -89, "limegreen", "lightgreen")
draw_half_oval(158, 138, -73, "white", "ivory")
draw_half_oval(146, 126, -61, "darkred", "tomato")

for x, y, heading in [
    (-70, -6, 65),
    (-35, 44, 25),
    (5, 7, 70),
    (42, 54, 30),
    (72, 4, 65),
    (-35, -33, 35),
    (25, -28, 70),
]:
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    t.circle(6, 180)
    t.left(90)
    t.forward(11)
    t.end_fill()


t.hideturtle()
turtle.done()
