import turtle                                         
import numpy as np

turtle.shape('turtle')                                     
rad = 20                                                
x = 1                                                 
n = 3                                                 
turtle.up()                                                
turtle.goto(rad, 0)                                          
turtle.down()  

def polygon(x):                                       
    for x in range (1, n+1):                                     
        turtle.left((180 - 360 / n) / 2)                   
        turtle.left(360 / n)                               
        turtle.forward(2 * rad * np.sin(np.pi/n))                                     
        turtle.right((180 - 360 / n) / 2)                  
for n in range (3,12):                                        
    polygon(x)                                        
    n += 1                                            
    rad += 20                                           
    turtle.up()                                            
    turtle.goto(rad, 0)                                      
    turtle.down()  
