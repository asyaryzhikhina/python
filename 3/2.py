##2
import turtle as t
t.color('Blue')
t.shape('turtle')



a = [(1, 10, 90, 20, 90, 10, 90, 20, 0, 90, 20), 
     (0, 270, 10, 1, 135, 14, 225, 20, 0, 180, 20, 270, 10), 
     (1, 10, 270, 10, 270, 10, 90, 10, 90, 10, 90, 0, 20, 270, 10), 
     (1, 10, 225, 14, 135, 10, 225, 14, 135, 0, 10, 90, 20, 270, 10),
     (1, 270, 10, 90, 10, 270, 10, 180, 20, 0, 270, 10), 
     (1, 10, 180, 10, 90, 10, 90, 10, 270, 10, 270, 10, 180, 10, 90, 0, 20, 270, 10), 
     (0, 10, 225, 1, 14, 45, 10, 90, 10, 90, 10, 90, 10, 225, 0, 14, 315, 10), 
     (1, 10, 225, 14, 45, 10, 0, 90, 10, 90, 20, 270, 10),
     (1, 270, 10, 90, 10, 180, 10, 90, 10, 90, 10, 90, 20, 90, 10, 180, 10, 0, 10), 
     (1, 270, 10, 90, 10, 90, 10, 90, 10, 90, 0, 20, 90, 1, 10, 90, 20, 270, 0, 10)]

for i in list((t.textinput('Введите индекс', 'индекс: '))):
    i = int(i)
    for j in range(len(a[i])):
        if a[i][j] > 20:
            t.left(a[i][j])
        elif a[i][j] == 0:
            t.up()
        elif a[i][j] == 1:
            t.down()
        else:
            t.forward(a[i][j])

t.exitonclick()


##3
with open('input.txt') as file:
    for line in file:
       import turtle as t
       t.color('Blue')
       t.shape('turtle')

       a = [(1, 10, 90, 20, 90, 10, 90, 20, 0, 90, 20), 
     (0, 270, 10, 1, 135, 14, 225, 20, 0, 180, 20, 270, 10), 
     (1, 10, 270, 10, 270, 10, 90, 10, 90, 10, 90, 0, 20, 270, 10), 
     (1, 10, 225, 14, 135, 10, 225, 14, 135, 0, 10, 90, 20, 270, 10),
     (1, 270, 10, 90, 10, 270, 10, 180, 20, 0, 270, 10), 
     (1, 10, 180, 10, 90, 10, 90, 10, 270, 10, 270, 10, 180, 10, 90, 0, 20, 270, 10), 
     (0, 10, 225, 1, 14, 45, 10, 90, 10, 90, 10, 90, 10, 225, 0, 14, 315, 10), 
     (1, 10, 225, 14, 45, 10, 0, 90, 10, 90, 20, 270, 10),
     (1, 270, 10, 90, 10, 180, 10, 90, 10, 90, 10, 90, 20, 90, 10, 180, 10, 0, 10), 
     (1, 270, 10, 90, 10, 90, 10, 90, 10, 90, 0, 20, 90, 1, 10, 90, 20, 270, 0, 10)]

        for i in list((t.textinput('Введите индекс', 'индекс: '))):
          i = int(i)
          for j in range(len(a[i])):
            if a[i][j] > 20:
              t.left(a[i][j])
            elif a[i][j] == 0:
              t.up()
           elif a[i][j] == 1:
             t.down()
           else:
             t.forward(a[i][j])

t.exitonclick()


##4

t.speed(100)
t.back(500)
t.forward(1000)
t.back(900)
t.shape('circle')

s=450
for j in range(13):
    s=int(2*s/3)
    c=t.xcor()
    for i in range(s+1):
        t.goto(i+c,4*s*(i/s-(i/s)**2))
t.exitonclick()

##5
from random import randint

number = 50
steps = 100


pool = [t.Turtle(shape='turtle') for i in range(number)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-300, 300), randint(-300, 300))


for i in range(steps):
    for unit in pool:
        wh = randint(0, 359)
        unit.right(wh)
        unit.forward(2)
