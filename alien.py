import pgzrun
import random
import pygame
pygame.mixer.init()
pygame.mixer.music.load("Gun.mp3")
WIDTH = 500
HEIGHT = 500
TITLE = "Alien blaster"

alien = Actor("alien.jpg")
message = ""
def draw():
    screen.clear()
    # screen.fill("blue")
    screen.blit("nightsky.png",(0,0))
    alien.draw()
    screen.draw.text(message,center=(250,10),fontsize=30)

def place():
    alien.x = random.randint(50,WIDTH-50)
    alien.y = random.randint(50,WIDTH-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        pygame.mixer.music.play()
        message = "Good shot!"
        place()
    else:
        message = "Try again!"

alien2 = Actor("alien2.png")
score = 0

def place2():
    alien2.x = random.randint(50, WIDTH - 50)
    alien2.y = random.randint(50, HEIGHT - 50)

place2()

def on_mouse_down(pos):
    global message, score
    if alien.collidepoint(pos):
        pygame.mixer.music.play()
    
        score += 1
        message = "Good shot!"
        place()
    elif alien2.collidepoint(pos):
        score -= 1
        message = "Wrong alien!"
        place2()
    else:
        message = "Try again!"

def draw():
    screen.clear()
    screen.blit("nightsky.png", (0, 0))
    alien.draw()
    alien2.draw()
    screen.draw.text(message, center=(250, 10), fontsize=30)
    screen.draw.text("Score: " + str(score), topleft=(10, 10), fontsize=30)



pgzrun.go()
