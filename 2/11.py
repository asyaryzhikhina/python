n=int(input())
import turtle
turtle.shape('turtle')
for i in range (1, n+1):
    turtle.circle(10+i**2)
    turtle.right(180)
    turtle.circle(10+i**2)
    turtle.right(180)
