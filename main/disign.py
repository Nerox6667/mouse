from turtle import *

speed(0)

penup()
backward(750)
right(90)
forward(100)
left(90)


def f(a):
    forward(a)

def b(b):
    backward(b)

def l():
    left(90)

def r():
    right(90)








def game_over():
    pendown()
    l()
    f(200)
    r()
    f(150)
    r()
    f(20)
    r()
    f(130)
    l()
    f(160)
    l
    f(110)
    l()
    f(60)
    l()
    f(40)
    r()
    f(20)
    r()
    f(60)
    r()
    f(100)
    r()
    f(150)






game_over()

# def polygone(n, cote):
#     for i in range(n):
#         forward(cote)
#         left(360/n)
#
#
#
# polygone(4, 50)

exitonclick()