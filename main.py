from pgzero import keyboard
import pgzrun

WIDTH = 1280
HEIGHT = 480

dino = Actor("dino1")
dino.x = WIDTH/8
dino.y = HEIGHT/2

speedY = 0
currentSprite = 1

def gravity():
    if dino.y < HEIGHT/2:
        dino.y += 15

def jump():
    global speedY
    dino.y += speedY
    if speedY < 0:
        speedY += 2
    else:
        speedY = 0
    if keyboard.w or keyboard.space:
        if dino.y >= HEIGHT/2:
            speedY = -35

def dinoRun():
    global currentSprite
    if dino.y >= HEIGHT/2:
        if currentSprite > 1:
            currentSprite = 1
        else:
            currentSprite = 2
    dino.image = f"dino{currentSprite}"

#Start
clock.schedule_interval(dinoRun, 0.1)

def update():
    gravity()
    jump()


def draw():
    screen.fill((120,120,120))
    dino.draw()

pgzrun.go()