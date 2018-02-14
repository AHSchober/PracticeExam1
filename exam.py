#!/usr/bin/python

import pygame, sys
import serial
from pygame.locals import *
import rgb_led

SCREEN_COLOR = (42,42,42)
BLACK = (255,255,255)
LENGTH = 400

s = serial.Serial("/dev/ttyACM0")

def main():
    pygame.init()
    window = pygame.display.set_mode((LENGTH,LENGTH))
    pygame.display.set_caption('ES432 Practice Exam')
    # TODO: create an LED object
    my_led = rgb_led.RgbLed(LENGTH,LENGTH)
    
    
    while(True):
        #1 Handle pygame events
        # TODO: exit game when user clicks X button
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #2 Run game logic
        # TODO: read buttons from arduino
        #       and set LED color
        
        rgb = serial_in()
        red = rgb[0] * 255
        green = rgb[1] * 255
        blue = rgb[2] * 255
        my_led.setColor(red,green,blue)
        
        #3 Draw to the screen
        draw_world(window)
        my_led.draw(window)
        pygame.display.update()

def draw_world(surf):
    surf.fill(SCREEN_COLOR)
    
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('ES432 Practice Exam', True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (LENGTH/2,25)

    surf.blit(textSurfaceObj, textRectObj)

def serial_in():
    s.write('p')
    l = s.readline() 
    x = l.rstrip().split(',')
    rgb = [int(val) for val in x]
    return rgb
    
main()
