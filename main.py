import serial, time

arduino = serial.Serial(port="/dev/ttyACM0", baudrate=115200, timeout=0.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

# while True:
#     if keyboard.is_pressed('left'):
#         value = write_read("1")
#     elif keyboard.is_pressed('right'):
#         value = write_read("2");
    
#     if keyboard.is_pressed('up'):
#         value = write_read("3")
#     elif keyboard.is_pressed('down'):
#         value = write_read("4")

import pygame, sys
import pygame.locals

pygame.init()
BLACK = (0,0,0)
WIDTH = 1366
HEIGHT = 768

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
windowSurface.fill(BLACK)
pygame.display.set_caption('Nerf Turret')

while True:
    for event in pygame.event.get():

        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                value = write_read("1")
            elif event.key == pygame.K_RIGHT:
                value = write_read("2")
            if event.key == pygame.K_UP:
                value = write_read("3")
            elif event.key == pygame.K_DOWN:
                value = write_read("4")
            if event.key == pygame.K_r:
                value = write_read("-1")