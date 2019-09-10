
import turtle

turtle.color("red")
turtle.speed(500)
side = 20
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()

def star():
   for i in range(5):
       turtle.forward(side)
       turtle.left(144)
for i in range(70):
   star()
   turtle.right(5)
   side += 2

turtle.penup()
turtle.goto(100,100)
turtle.pendown()
side = 20
for i in range(70):
   star()
   turtle.right(5)
   side += 2

turtle.penup()
turtle.goto(-400, -400)
turtle.pendown()
side = 20
def square():
    for i in range(4):
        turtle.right(90)
        turtle.forward(100)

square()
turtle.penup()
turtle.goto(-600, 300)
turtle.pendown()
side = 20
turtle.color("blue")
for i in range(75):
    square()
    turtle.right(5)
turtle.penup()
turtle.goto(600, -300)
turtle.pendown()
side = 20
turtle.color("blue")
for i in range(75):
    square()
    turtle.right(5)


turtle.exitonclick()

