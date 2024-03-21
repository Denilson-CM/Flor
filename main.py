import turtle
from math import sqrt, pi, cos, sin

# Configuración inicial
turtle.speed(0)
turtle.bgcolor("black")
turtle.goto(0, -40)
turtle.setup(width=900, height=500)

# Dibujo de los círculos
for i in range(16):
    for j in range(18):
        turtle.color('#FFA216')
        turtle.rt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.lt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.rt(180)
    turtle.circle(40, 24)

# Dibujo de la espiral dorada
turtle.color('black')
turtle.shape('circle')
turtle.shapesize(0.5)
turtle.fillcolor('#8B4513')
golden_angle = 137.508
phi = golden_angle * (pi / 180)

for i in range(110):
    r = 4 * sqrt(i)
    theta = i * phi
    x = r * cos(theta)
    y = r * sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * golden_angle)
    turtle.pendown()
    turtle.stamp()

# Texto "TE AMO IRIS"
turtle.penup()
turtle.goto(0, 200)
turtle.color('white')
turtle.write("TE AMO IRIS", align="center", font=("Arial", 24, "normal"))
turtle.pendown()

# Cuadrado simple
obj = turtle.Turtle()
for i in range(4):
    obj.forward(100)
    obj.right(90)

# Finalización
turtle.done()
