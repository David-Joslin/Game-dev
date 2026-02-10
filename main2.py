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

    star_positions = [
        (400, 120),  
        (460, 260),
        (600, 260),
        (490, 350),
        (530, 500),
        (400, 410),
        (270, 500),
        (310, 350),
        (200, 260),
        (340, 260)
    ]

    for count in range(0, num_of_satellites):
        satellite = Actor("satellite")
        satellite.pos = star_positions[count]
        satellites.append(satellite)

    start_time = time.time()

def draw():
    global total_time
    screen.blit("bg", (0, 0))

    number = 1
    for satellite in satellites:
        screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1] + 20))
        satellite.draw()
        number += 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255, 150, 0))

    if next_satellite < num_of_satellites:
        total_time = time.time() - start_time
        screen.draw.text("Time: " + str(round(total_time, 2)),
                         (20, 20), fontsize=20, color="white")
    else:
        screen.draw.text("Finished! Total time: " + str(round(total_time, 2)),
                         (20, 20), fontsize=20, color="white")

def update():
    pass

def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite < num_of_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite - 1].pos,
                              satellites[next_satellite].pos))
            next_satellite += 1
        else:
            print("Wrong satellite")
            lines = []
            next_satellite = 0

create_satellite()
pgzrun.go()
