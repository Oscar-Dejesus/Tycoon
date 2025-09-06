import pygame
from Globals import Global
from  Sprites import Sprites
import os
class Button(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,text="",image="Button.png"):
        pygame.sprite.Sprite.__init__(self)
        self.Sprite = Sprites(image,0,0,width,height,0,0)
        self.image = self.Sprite.get_image()
        self.rect =self.image.get_rect()
        
        self.text= text
        self.x= x
        self.y=y
        self.width= width
        self.height = height
        self.rect.topleft =(x,y)
        self.clicked= False
    def draw(self):
        Global.WINDOW.blit(self.image,(self.rect.x,self.rect.y))
        text= Global.FONT.render(self.text,1,"white")
        Global.WINDOW.blit(text,(self.rect.x+self.width/2-text.get_width()/2,self.rect.y+self.height/2-text.get_height()/2))
    def updatePos(self,x,y):
        self.rect.topleft =(x,y)
    def updateImage(self,image):
        self.Sprite = Sprites(image,0,0,self.width,self.height,0,0)
        self.image = self.Sprite.get_image()

    def setText(self,text):
        self.text= text
    def check_clicked(self):
        action =False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] ==1 and not(self.clicked):
            self.clicked = True
            action =True
        if pygame.mouse.get_pressed()[0] ==0:
            self.clicked=False
        return action