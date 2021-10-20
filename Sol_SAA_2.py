import turtle

side = int(input('Enter the value of side : '))
angle = int(input('Enter the angle for turn : '))

for variable in range(0, 4):
    turtle.forward(side)
    turtle.left(angle)

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

for variable in range(0, 4):
    turtle.forward(side)
    turtle.left(angle)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()

for variable in range(0, 4):
    turtle.forward(side)
    turtle.left(angle)

turtle.penup()
turtle.goto(100, 0)
turtle.pendown()

for variable in range(0, 4):
    turtle.forward(side)
    turtle.left(angle)
