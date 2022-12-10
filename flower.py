# from turtle import *
# import turtle as tur

# tur = tur.Turtle()
 

# tur.penup ()
# tur.left (90)
# tur.fd (200)
# tur.pendown ()
# tur.right (90)
 

# tur.fillcolor ("red")
# tur.begin_fill ()
# tur.circle (10,180)
# tur.circle (25,110)
# tur.left (50)
# tur.circle (60,45)
# tur.circle (20,170)
# tur.right (24)
# tur.fd (30)
# tur.left (10)
# tur.circle (30,110)
# tur.fd (20)
# tur.left (40)
# tur.circle (90,70)
# tur.circle (30,150)
# tur.right (30)
# tur.fd (15)
# tur.circle (80,90)
# tur.left (15)
# tur.fd (45)
# tur.right (165)
# tur.fd (20)
# tur.left (155)
# tur.circle (150,80)
# tur.left (50)
# tur.circle (150,90)
# tur.end_fill ()
 

# tur.left (150)
# tur.circle (-90,70)
# tur.left (20)
# tur.circle (75,105)
# tur.setheading (60)
# tur.circle (80,98)
# tur.circle (-90,40)

# tur.left (180)
# tur.circle (90,40)
# tur.circle (-80,98)
# tur.setheading (-83)

# tur.fd (30)
# tur.left (90)
# tur.fd (25)
# tur.left (45)
# tur.fillcolor ("dark green")
# tur.begin_fill ()
# tur.circle (-80,90)
# tur.right (90)
# tur.circle (-80,90)
# tur.end_fill ()
# tur.right (135)
# tur.fd (60)
# tur.left (180)
# tur.fd (85)
# tur.left (90)
# tur.fd (80)
 
# tur.right (90)
# tur.right (45)
# tur.fillcolor ("dark green")
# tur.begin_fill ()
# tur.circle (80,90)
# tur.left (90)
# tur.circle (80,90)
# tur.end_fill ()
# tur.left (135)
# tur.fd (60)
# tur.left (180)
# tur.fd (60)
# tur.right (90)
# tur.circle (200,60)
# tur.done()



from turtle import *
import turtle as tur
from random import randint
tur.colormode(255)

def daisy():
    
    
    # for i in range(2):
    #     if i == 0:
    #         tur.pencolor((255, 105, 180))
    #     else:
    #         tur.pencolor((0, 105, 180))
    #     for j in range(17):

    #         circle(200+(i*300), 30)
    #         left(90)
    #         circle(60, 90)
    #         left(120)
    #         circle(60, 90)
    #         left(90)
    #         circle(60, 90)
    #         left(120)
    #         circle(60, 90)
    #         left(90)
    #         circle(200+(i*300),  30 )

    


    # for x in range(20):
    #         for i in range(2):
    #             tur.pencolor((255, 105, 180))
    #             for j in range(17):

    #                 circle((200 - (x * 10)) +(i*300), 30)
    #                 left(90)
    #                 circle(50, 90)
    #                 left(120)
    #                 circle(50, 90)
    #                 left(90)
    #                 circle(50, 90)
    #                 left(120)
    #                 circle(50, 90)
    #                 left(90)
    #                 circle((200 - (x * 10) )+(i*300), 30 )
        
        
    tur.bgcolor((0,0,0))    
    for i in range(2):
        
        tur.begin_fill()
        if i == 0:
            tur.fillcolor((255,255,255))
            tur.pencolor((252, 200, 0))
            tur.speed(10)
            tur.pensize(1)
        else:
            tur.fillcolor((252, 200, 0))
            tur.pencolor((252, 200, 0))
            tur.speed(0)
            tur.pensize(5)
        for j in range(12):
            
            circle(500-(i*300), 30)
            left(90)
            circle(60, 90)
            left(120)
            circle(60, 90)
            left(90)
            circle(60, 90)
            left(120)
            circle(60, 90)
            left(90)
            circle(500-(i*300),  30 )
        tur.end_fill()


    
    
    
daisy()
mainloop()