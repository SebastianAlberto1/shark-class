import pygame
import sys
import os
from pygame.locals import *

SCREEN_SIZE = (1000,600)
FLOOR_POSITION = 550

keypressed = {'a':False, 'd':False}
class Game():
    def __init__(self,imagePath,screen) -> None:
        self.img = pygame.image.load(os.path.join("./", imagePath))
        self.screen = screen
    pass

    def draw_background(self):
        self.screen.blit(self.img,(0,0))
        pass
        


class Entity () :
    def __init__(self, imagePath, size, screen) -> None:

        img = pygame.image.load(os.path.join("./", imagePath))
        self.img = pygame.transform.scale(img, size)

        self.screen = screen
        self.pos = [SCREEN_SIZE[0]/2, 0]
        self.velocity = [0,0]

        pass
    def changePosition(self,coordinates):
        self.pos[0] = coordinates [0]
        self.pos[1] = coordinates [1]

    def draw(self):
        self.screen.blit(self.img, (self.pos[0],self.pos[1]))
        pass

    def jump(self):
        self.velocity[1] = -5
    
    def draw(self):
            self.screen.blit(self.img, (self.pos[0],self.pos[1]))
            pass
    
    def update( self ):
        self.pos[0] = self.pos[0] + self.velocity[0]
        self.pos[1] = self.pos[1] + self.velocity[1]

        #this is just a comment, compiler will ignore

        if(self.pos[1] < FLOOR_POSITION):
            self.velocity[1] = self.velocity[1] + 0.08
        else:
            self.velocity[1] = 0

        if(keyPressed['d']):
            self.velocity[0] = 1
        else: 
            self.velocity[0] = 0
            pass

        self.draw()
        pass


pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode(SCREEN_SIZE)

ball_1 = Entity("ball.png", (50,50), screen)
ball_2 = Entity("ball.png", (50,50), screen)
ball_3 = Entity("ball.png", (50,50), screen)
ball_2.changePosition([100,0])
ball_3.changePosition([300,0])
bg = Game("background.png", screen)

while True:
    clock.tick(60)
    bg.draw_background()
    ball_1.update()
    ball_2.update()
    ball_3.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_w):
                ball_1.jump()

            if(event.key == pygame.K_d):
                keyPressed['d'] = True

        if event.type == pygame.KEYUP:
            if(event.key == pygame.K_d):
                keyPressed['d'] = False

        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()