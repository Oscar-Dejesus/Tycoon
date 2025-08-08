import pygame
from Globals import Global
from  Sprites import Sprites
import os
class Button(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.Sprite = Sprites("button.jpeg",0,0,width,height,0,0)
        self.image = self.Sprite.get_image()
        self.rect =self.image.get_rect()
   
        
        self.x= x
        self.y=y
        self.width= width
        self.height = height
        self.rect.topleft =(x,y)
        self.clicked= False
    def draw(self):
        Global.WINDOW.blit(self.image,(self.rect.x,self.rect.y))
    def updatePos(self,x,y):
        self.rect.topleft =(x,y)
    def check_clicked(self):
        action =False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] ==1 and not(self.clicked):
            self.clicked = True
            action =True
        if pygame.mouse.get_pressed()[0] ==0:
            self.clicked=False
        return action