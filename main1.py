import pgzrun
import random

WIDTH = 750
HEIGHT = 600
TITLE = "Galoga game"
BLUE = (0,0,255)

ship = Actor("galoga")
bug = Actor("bug")

ship.pos = WIDTH/2,HEIGHT - 60
speed = 10

bullets = []
enemies = []
enemies.append(bug)
enemies[-1].x = 100
enemies[-1].y = -100

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

    for enemy in enemies:
        enemy.y += 2

        if enemy.y >= HEIGHT:
            enemy.y = -100
            enemy.x = random.randint(50,WIDHT-50)
    #checking if the enemy hits a bullet

        for bullet in bullets:
            if enemy.colliderect(bullet):
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