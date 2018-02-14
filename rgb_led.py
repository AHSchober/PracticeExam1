import pygame

#LED is a 20x20 rectangle
LED_SIZE = 20
SCREEN_COLOR = (42,42,42)

class RgbLed:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = SCREEN_COLOR

    def setColor(self, r, g, b):
        # TODO: update self.color based on inputs
        self.color = (r, g, b)
        
    def draw(self, surf):
        r = pygame.Rect((0,0,LED_SIZE,LED_SIZE))
        
        r.center = (200,200)
        # TODO: center r on surf
        pygame.draw.rect(surf, self.color, r)
    
