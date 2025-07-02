import pygame
import os
from Globals import Global
class Core():
    Health = 100
    Dead =False
    def __init__(self,x,y,width,height):
        current_path = os.path.dirname(__file__) 
        image_path = os.path.join(current_path, '..','Images',"Factory.png")
        image_path =os.path.normpath(image_path)
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image,(width,height))
        self.rect =self.image.get_rect()
        self.rect.topleft = (x, y) 
        self.Max_Health = 1000
        self.Health = 1000
        self.x=x
        self.y=y
        self.width = width
        self.height= height

    def DrawHealth(self):
        rect =pygame.Rect(self.x,self.y+self.height-20,100 * (self.Health/self.Max_Health),20)
        pygame.draw.rect(Global.WINDOW,(0, 255, 0),rect,border_radius=5)
        
    def draw(self):
        Global.WINDOW.blit(self.image,(self.x,self.y))
        self.DrawHealth()

    def get_core_Draw_info(self):
        return (self.image,(self.x,self.y),self.rect)
    
    def check_Health(self):
        if self.Health <=100:
            Dead=True
    


    def is_Dead():
        global Dead
        return Dead
    
