"""Use turtle so that when you enter a number it creates a polygon with that many sides."""
import turtle
sides = int(input("Please enter the number of sides that you want the polygon to have: "))
x = 360/sides
for i in range(sides):
    turtle.pendown()
    turtle.forward(50)
    turtle.right(x)
turtle.done()
