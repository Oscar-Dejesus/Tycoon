import pygame
import os
from Globals import Global
from Sprites import Sprites
class Core():
    Health = 100
    Dead =False
    def __init__(self,x,y,width,height):
        self.sprite = Sprites("IDLE.png",96,96,width,height,100,9)
        self.image =self.sprite.get_image()
        self.rect =self.image.get_rect()


        self.rect.topleft = (x, y) 
        self.Max_Health = 100
        self.Health = 100
        self.x=x
        self.y=y
        self.width = width
        self.height= height
    
    def DrawHealth(self):
        rect =pygame.Rect(self.x,self.y+self.height-10,100 * (self.Health/self.Max_Health),10)
        pygame.draw.rect(Global.WINDOW,(0, 255, 0),rect,border_radius=5)

    def draw(self):
        self.image = self.sprite.get_image()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        Global.WINDOW.blit(self.image,(self.x,self.y))
        self.DrawHealth()

    def get_core_Draw_info(self):
        return ((self.x,self.y),self.rect)

    def check_Health(self):
        if self.Health <=0:
            Global.Game_Over=True
    
    def is_Dead():
        global Dead
        return Dead
    
