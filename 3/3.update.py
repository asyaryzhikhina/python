import turtle as tr
tr.shape('turtle')

def draw(n):
    if n == 0: 
        tr.forward(50)
        tr.right(90)
        tr.forward(100)
        tr.right(90)
        tr.forward(50)
        tr.right(90)
        tr.forward(100)
        tr.right(90)
        tr.penup()
        tr.forward(100)
        tr.pendown()

    elif n == 1:
        tr.penup()
        tr.right(90)
        tr.forward(50)
        tr.left(135)
        tr.pendown()
        tr.forward(70)
        tr.right(135)
        tr.forward(100)
        tr.penup()
        tr.left(180)
        tr.forward(100)
        tr.right(90)
        tr.forward(50)
        tr.pendown()

    elif n == 2: 
        tr.forward(50)
        tr.right(90)
        tr.forward(50)
        tr.right(45)
        tr.forward(70)
        tr.left(135)
        tr.forward(50)
        tr.penup()
        tr.left(90)
        tr.forward(100)
        tr.right(90)
        tr.forward(50)
        tr.pendown()
    
    elif n == 3: 
        tr.forward(50)
        tr.right(135)
        tr.forward(70)
        tr.left(135)
        tr.forward(50)
        tr.right(135)
        tr.forward(70)
        tr.penup()
        tr.left(135)
        tr.forward(100)
        tr.left(90)
        tr.forward(100)
        tr.right(90)
        tr.pendown()

    elif n == 4: 
        tr.right(90)
        tr.forward(50)
        tr.left(90)
        tr.forward(50)
        tr.right(90)
        tr.forward(50)
        tr.left(180)
        tr.forward(100)
        tr.penup()
        tr.right(90)
        tr.forward(50)
        tr.pendown()

    elif n == 5: 
        tr.forward(50)
        tr.left(180)
        tr.forward(50)
        tr.left(90)
        tr.forward(50)
        tr.left(90)
        tr.forward(50)
        tr.right(90)
        tr.forward(50)
        tr.right(90)
        tr.forward(50)
        tr.penup()
        tr.left(180)
        tr.forward(100)
        tr.left(90)
        tr.forward(100)
        tr.right(90)
        tr.pendown()

    elif n == 6: 
        tr.penup()
        tr.forward(50)
        tr.pendown()
        tr.right(135)
        tr.forward(70)
        tr.left(45)
        tr.forward(50)
        tr.left(90)
        tr.forward(50)
        tr.left(90)
        tr.forward(50)
        tr.left(90)
        tr.forward(50)
        tr.penup()
        tr.right(180)
        tr.forward(100)
        tr.left(90)
        tr.forward(50)
        tr.right(90)
        tr.pendown()

    elif n == 7:
        tr.forward(50)
        tr.right(135)
        tr.forward(70)
        tr.left(45)
        tr.forward(50)
        tr.penup()
        tr.left(90)
        tr.forward(100)
        tr.left(90)
        tr.forward(100)
        tr.right(90)

    elif n == 8:
        tr.forward(50)
        tr.right(90)
        tr.forward(50)
        tr.right(90)
        tr.forward(50)
        tr.right(90)
        tr.forward(50)
        tr.left(180)
        tr.forward(100)
        tr.left(90)
        tr.forward(50)
        tr.left(90)
        tr.forward(50)
        tr.penup()
        tr.forward(50)
        tr.right(90)
        tr.forward(50)
        tr.pendown()

    elif n == 9:
        tr.forward(50)
        tr.right(90)
        tr.forward(50)
        tr.right(90)
        tr.forward(50)
        tr.right(90)
        tr.forward(50)
        tr.left(180)
        tr.forward(50)
        tr.left(90)
        tr.forward(50)
        tr.right(135)
        tr.forward(70)
        tr.penup()
        tr.left(135)
        tr.forward(100)
        tr.left(90)
        tr.forward(100)
        tr.right(90)
        tr.pendown()        

L = list(map(int, input().split()))


for i in range(len(L)):
    if L[i] == 1: draw(1)
    elif L[i] == 2: draw(2)
    elif L[i] == 3: draw(3)
    elif L[i] == 4: draw(4)
    elif L[i] == 5: draw(5)
    elif L[i] == 6: draw(6)
    elif L[i] == 7: draw(7)
    elif L[i] == 8: draw(8)
    elif L[i] == 9: draw(9)
    elif L[i] == 0: draw(0)

tr.mainloop()