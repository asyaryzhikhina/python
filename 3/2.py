##2
import turtle
from math import sqrt
def draw_zero():
    turtle.pendown()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
def draw_one():
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(sqrt(200))
    turtle.right(180-45)
    turtle.forward(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
  def draw_two():
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
  def draw_three():
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.penup()
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.penup()
    turtle.left(180)
    turtle.forward(20)
  def draw_four():
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.right(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.penup()
    turtle.right(180)
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
  def draw_five():
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.pendown()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.penup()
    turtle.left(180)
    turtle.forward(20)
  def draw_six():
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.pendown()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.penup()
    turtle.right(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
def draw_seven():
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.penup()
    turtle.forward(10)
  def draw_eight():
    turtle.pendown()
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.penup()
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.penup()
    turtle.left(180)
    turtle.forward(20)
  def draw_nine():
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.penup()
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.penup()
    turtle.left(180)
    turtle.forward(20)
  def need(numbers):
    turtle.speed(100)
    turtle.penup()
    turtle.goto(-300, 0)
    for i in numbers:
        if i == 0:
            draw_zero()
        if i == 1:
            draw_one()
        if i == 2:
            draw_two()
        if i == 3:
            draw_three()
        if i == 4:
            draw_four()
        if i == 5:
            draw_five()
        if i == 6:
            draw_six()
        if i == 7:
            draw_seven()
        if i == 8:
            draw_eight()
        if i == 9:
            draw_nine()
    turtle.exitonclick()
numbers = [int(i) for i in input().split()]
need(numbers)

##3
with open('input.txt') as file:
    for line in file:
       need(line) 

##4

turtle.speed(100)
turtle.back(500)
turtle.forward(1000)
turtle.back(900)
turtle.shape('circle')

s=450
for j in range(13):
    s=int(2*s/3)
    c=turtle.xcor()
    for i in range(s+1):
        turtle.goto(i+c,4*s*(i/s-(i/s)**2))
turtle.exitonclick()

##5
from random import randint

number_of_turtles = 50
steps_of_time_number = 100


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-300, 300), randint(-300, 300))


for i in range(steps_of_time_number):
    for unit in pool:
        wh = randint(0, 359)
        unit.right(wh)
        unit.forward(2)
