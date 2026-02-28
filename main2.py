import pgzrun
import random

WIDTH = 750
HEIGHT = 600
TITLE = "Galoga game"
BLUE = (0,0,255)

ship = Actor("galoga")
bug = Actor("bug")

ship.pos = WIDTH/2,HEIGHT - 60
speed = 2
direction = 1

bullets = []
enemies = []

for x in range(10):

    enemies.append(bug)
    enemies[-1].x = 100 + 70*x
    enemies[-1].y = -30

Score = 0
def display_score():
    screen.draw.text(str(Score),(100,30))


def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50


def update():
    global Score
    global direction
    moveDown = False
    if keyboard.left:
        ship.x -= 10
        if ship.x <= 0:
            ship.x = 0
    elif keyboard.right:
        ship.x += 10
        if ship.x >= WIDTH:
            ship.x = WIDTH

    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    if (len(enemies)>0) and (enemies[0].x < 20 or enemies[-1].x > WIDTH-30):
        moveDown = True 
        direction = direction*(-1)
    for enemy in enemies:
        enemy.x += 5*direction
        if moveDown == True:
            enemy.y += 10

        
    #checking if the enemy hits a bullet

        for bullet in bullets:
            if enemy.colliderect(bullet):
                Sounds.eep.play()
                Score +=100
                bullets.remove(bullet)
                enemies.remove(enemy)

def draw():
    screen.clear()
    screen.fill((0,200,0))
    for bullet in bullets:
        bullet.draw()

    for enemy in enemies:
        enemy.draw()

    ship.draw()

    display_score()






    

pgzrun.go()