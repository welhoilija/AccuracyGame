#accyracypygame

import pygame
import random
from math import sqrt



pygame.init()

font = pygame.font.Font('freesansbold.ttf', 32) 
# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (0, 0, 255)


screenwh = (700, 500)
screen = pygame.display.set_mode(screenwh)
pygame.display.set_caption("Accyracygame")
background = pygame.Surface(screenwh)
pygame.draw.rect(background,BLACK,(120,120,50,50))

def getColor():
    #color = (random.randint(0, 14), random.randint(0, 99), random.randint(0, 177))
    color = (255,105,180)
    return (color)

def getPos():
    pos = (random.randint(30, 670), random.randint(30, 470))
    return (pos)

#def drawCircle():
    #color=getColor()
    #pos=getPos()
    #pygame.draw.circle(screen, color, pos, 30)
    #Pallot.append(pos)

class drawCircle(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)




def getMousePos():
    mousepos = pygame.mouse.get_pos()
    return (mousepos)

def redrawGameWindow():
    screen.blit(background, (0,0))
    for item in Pallot:
        item.draw(screen)
    screen.blit(text, textRect)
    pygame.display.update()

running = 1
Pallot = []
oldclock = 1000
score = 0
font = pygame.font.Font('freesansbold.ttf', 32) 
  
# create a text suface object, 
# on which text is drawn on it. 
text = font.render(str(score), True, RED, GREEN)

  
# create a rectangular object for the 
# text surface object 
textRect = text.get_rect()  
  
# set the center of the rectangular object. 
textRect.center = (30, 30) 




while running == 1 and len(Pallot) <= 10:
    clock = pygame.time.get_ticks()
    print(clock)
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = 0

    mousepos = getMousePos()
    print(mousepos)
    

    if clock > (oldclock + 750):
        Pallot.append(drawCircle(x = random.randint(30, 670), y = random.randint(30, 470), radius = 30, color = RED))
        oldclock = clock

    for item in Pallot:
        
        x_good = mousepos[0] in range(item.x - 30, item.x + 30)
        y_good = mousepos[1] in range(item.y - 30, item.y + 30)
        if x_good == True and y_good == True and event.type == pygame.MOUSEBUTTONUP:
            Pallot.pop(Pallot.index(item))
            print("hit")
            score =+ 1

    text = font.render(str(score), True, RED, GREEN)
    redrawGameWindow()
