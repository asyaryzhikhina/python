import numpy as np
import turtle
turtle.shape('turtle')
for i in range (3,12):
    for t in range (i):
       turtle.left(180-((180*(i-2)/i)))
       turtle.fd(i*20)
    r=(i*2)/(2*np.sin((np.pi)/i))
    turtle.penup()
    turtle.fd(r*0.8)
    turtle.right(180-((180*(i-2)/i)))
    turtle.fd(r*0.8)
    turtle.left(180-((180*(i-2)/i)))
    turtle.pendown()
