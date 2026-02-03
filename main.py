import pgzrun
import random
import time

WIDTH = 800
HEIGHT = 600

TITLE = "Satellite game"
satellites = []
lines = []
next_satellite = 0
num_of_satellites = 10
start_time = 0
total_time = 0
end_time = 0
def create_satellite():
    global start_time
    for count in range(0,num_of_satellites):
        satellite = Actor("satellite")
        satellite.pos = (random.randint(30, WIDTH - 30),(random.randint(40, HEIGHT - 40)))
        satellites.append(satellite)
    start_time = time.time()#used to get current time of ur computer

def draw():
    pass

pgzrun.go()