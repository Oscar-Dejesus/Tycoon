import pygame
from Globals import Global
import os
from Sprites import Sprites
class Tower:
    index=0

    def __init__(self,x,y,width,height,Name,SpriteSize):
       for i, t in enumerate(Global.Towers_Info):
            if t["TowerName"]==Name:
                self.index= i
                break
       self.StartTime = Global.count 
       self.EndTime= Global.count+Global.Towers_Info[self.index]["Time"]
       
       self.sprite = Sprites(Global.Towers_Info[self.index]["Image"],SpriteSize[0],SpriteSize[1],width,height,5000,0)
       self.image= self.sprite.get_image()
       self.rect=self.image.get_rect()
       self.rect.topleft = (x, y) 

       self.tower_info =self.rect
       self.Max_Health = Global.Towers_Info[self.index]["Health"]
       self.Health = Global.Towers_Info[self.index]["Health"]
       self.x = x
       self.y =y
       self.width = width
       self.height = height
    def Tower_Loop(self):
        self.Score_Add()
        self.Check_Dead()
    
    
    def Score_Add(self):
        if self.StartTime>= self.EndTime:
            self.StartTime= Global.count
            self.EndTime= Global.count+Global.Towers_Info[self.index]["Time"]
            Global.Score+=Global.Towers_Info[self.index]["Score"]
        else:
            self.StartTime +=10
    def DrawHealth(self):
        rect =pygame.Rect(self.x,self.y+self.height-10,self.width * (self.Health/self.Max_Health),10)
        pygame.draw.rect(Global.WINDOW,(0, 255, 0),rect,border_radius=5)


    def Check_Dead(self):
        if self.Health <=0:
            Global.Towers.remove(self)
    def get_tower_info(self):
        return Global.Towers_Info[self.index]
        
    def drawTower(self):
        self.image= self.sprite.get_image()
        self.rect=self.image.get_rect()
        self.rect.topleft = (self.x, self.y) 
        Global.WINDOW.blit(self.image,(self.x,self.y))
        self.DrawHealth()
    def get_tower_Draw_info(self):
        return self.tower_info