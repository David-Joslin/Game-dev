import pgzrun
from random import randint
WIDTH = 500
HEIGHT = 500

def draw():
    width = WIDTH
    height = HEIGHT - 200

    r = 255
    g = randint(128,255)
    b = 0
    for i in range(20):
        box = Rect((0,0),(width,height))
        box.center = 150,150
        screen.draw.rect(box,(r,g,b))

        width -= 10
        height += 10
        r -= 8
        
        b += 3






pgzrun.go()