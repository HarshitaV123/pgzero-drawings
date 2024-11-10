import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
TITLE = "Circles"
radius = 50
def draw():
    global radius
    screen.clear()
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    for i in range(10):
        screen.draw.circle((200,200),radius,(r,g,b))
        radius += 15
pgzrun.go()