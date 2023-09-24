import turtle
turtle.shape('turtle')
for i in range (5):
    turtle.right(180-180/5)
    turtle.fd(100)
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
for i in range (11):
    turtle.right(180-180/11)
    turtle.fd(100)
