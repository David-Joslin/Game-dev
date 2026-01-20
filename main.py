import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False
bee = Actor("bee")
bee.pos = (100,100)
flower = Actor("flower")
flower.pos = (200,200)
message = " "
def draw():
    screen.blit("bg",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score: " + str(score),color="black", topleft=(10,10))
    if game_over:
        screen.fill("pink")
        global message
        message = "Times up! \nYour Final Score:"
        screen.draw.text(message + str(score),midtop = (WIDTH/2,20),
                         fontsize = 50,color = "red")
        
def place_flower():
    flower.x = random.randint(30,570)
    flower.y = random.randint(40,460)

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        bee.x = bee.x - 2

    if keyboard.right:
        bee.x = bee.x + 2

    if keyboard.up:
        bee.y = bee.y - 2

    if keyboard.down:
        bee.y = bee.y + 2
    flower_collected = bee.colliderect(flower)
    if flower_collected == True:
        score += 10
        place_flower()
clock.schedule(time_up, 60.0)
pgzrun.go()
    





