import pgzrun

import random 

HEIGHT = 800
WIDTH = 800

message = ""

a1 = Actor("monster")
a1.pos = 300,300

def draw():
    screen.clear()
    a1.draw()
    screen.draw.text(message,center = (300,10))

def move_monster():
    a1.x = random.randint(80,WIDTH-80)
    a1.y = random.randint(80,HEIGHT-80)

def on_mouse_down(pos):
    global message
    if a1.collidepoint(pos):
        move_monster()
        message = "Victory"
    else:
        message = "Mission Failed"



move_monster()

pgzrun.go()