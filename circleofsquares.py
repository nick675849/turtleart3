import turtle

turtle.color("blue")
turtle.speed(50)
def square():
    for i in range(4):
        turtle.right(90)
        turtle.forward(100)
square()
turtle.color("pink")
for i in range(15):
    square()
    turtle.right(5)
turtle.color("blue")
for i in range(15):
    square()
    turtle.right(5)
turtle.color("red")
for i in range(15):
        square()
        turtle.right(5)
turtle.color("gree")
for i in range(15):
    square()
    turtle.right(5)


turtle.exitonclick()
