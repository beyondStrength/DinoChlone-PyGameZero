from random import randint
from pgzero import keyboard, clock
import pgzrun

WIDTH = 1280
HEIGHT = 480

dino = Actor("dino1")
dino.x = WIDTH/8
dino.y = HEIGHT/2

speedY = 0
currentSprite = 1

obstacles = []

def instantiateObstacle():
    obstacle = Actor("obstacle"+str(randint(1,3)))
    obstacle.pos = WIDTH+obstacle.width, HEIGHT/2
    obstacles.append(obstacle)

def moveObstacles():
    for o in obstacles:
        o.x -= 10

def gravity():
    if dino.y < HEIGHT/2:
        dino.y += 25

def jump():
    global speedY
    dino.y += speedY
    if speedY < 0:
        speedY += 2
    else:
        speedY = 0
    if keyboard.w or keyboard.space or keyboard.up:
        if dino.y >= HEIGHT/2:
            speedY = -50

def animation():
    global currentSprite
    if currentSprite == 2:
            currentSprite = 1
    elif currentSprite == 1:
        currentSprite = 2
    if dino.y >= HEIGHT/2:
        dino.image = f"dino{currentSprite}"
    for o in obstacles:
        if o.image != "obstacle3":
            o.image = "obstacle"+str(currentSprite)
    

#Start
clock.schedule_interval(animation, 0.1)
clock.schedule_interval(instantiateObstacle, 1)

def update():
    gravity()
    jump()
    moveObstacles()


def draw():
    screen.fill((120,120,120))
    dino.draw()
    for o in obstacles:
        o.draw()

pgzrun.go()