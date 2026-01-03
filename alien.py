import pgzrun
import random
import pygame
pygame.mixer.init()
pygame.mixer.music.load("Gun.mp3")
WIDTH = 500
HEIGHT = 500
TITLE = "Alien blaster"

alien = Actor("alien.png")
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


pgzrun.go()
