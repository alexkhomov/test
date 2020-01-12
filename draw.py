import turtle

painter = turtle.Turtle()
painter.pensize(10)

for _ in range(12):
    painter.forward(300)
    painter.left(150)

turtle.done()