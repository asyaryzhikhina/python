##10
n=int(input())
import turtle
turtle.shape('turtle')
for i in range (n):
    for j in range (180):
     turtle.forward(2)
     turtle.left(2)
    turtle.right(180)
    for j in range (180):
      turtle.forward(2)
      turtle.left(2)
    turtle.right(360/n)
