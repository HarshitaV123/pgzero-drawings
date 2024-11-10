import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
TITLE = "Rectangles" 

def draw():
    screen.clear()
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    width = WIDTH
    height = HEIGHT - 300
    for i in range(12):
        box=Rect((0,0),(width,height))
        box.center=(WIDTH//2,HEIGHT//2)
        screen.draw.rect(box,(r,g,b))

        width -=10
        height +=10
        

pgzrun.go()
