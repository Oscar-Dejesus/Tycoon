import pygame
from Globals import Global
import os
class Tower:
    index=0

    def __init__(self,x,y,width,height,Name):
       for i, t in enumerate(Global.Towers_Info):
            if t["TowerName"]==Name:
                self.index= i
                break
       self.StartTime = Global.count 
       self.EndTime= Global.count+Global.Towers_Info[self.index]["Time"]
       current_path = os.path.dirname(__file__) 
       image_path = os.path.join(current_path, '..','Images',Global.Towers_Info[self.index]["Image"])
       image_path =os.path.normpath(image_path)
       image= pygame.image.load(image_path)
       self.image= pygame.transform.scale(image,(width,height))
       self.rect=self.image.get_rect()
       self.rect.topleft = (x, y) 
       self.tower_info = (self.image,(x,y),self.rect)
    def Score_Add(self):
        if self.StartTime>= self.EndTime:
            self.StartTime= Global.count
            self.EndTime= Global.count+Global.Towers_Info[self.index]["Time"]
            Global.Score+=Global.Towers_Info[self.index]["Score"]
        else:
            self.StartTime +=10
    def get_tower_info(self):
        return Global.Towers_Info[self.index]
        
    def get_tower_Draw_info(self):
        return self.tower_info