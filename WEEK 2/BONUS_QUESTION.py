import turtle

star = turtle.Turtle()

star.pencolor("blue")
for i in range(5):
    star.forward(50)
    star.right(144)

star.pencolor("red")
for i in range(5):
    star.forward(50)
    star.left(144)


turtle.done()
