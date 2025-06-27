import pygame
from Globals import Global

class Tower:
    StartTime = Global.count 
    EndTime = Global.count +2000
    def __init__(self,x,y,width,height):
       self.tower_info = pygame.Rect(x,y,width,height)
    def Score_Add(self):
        global Score
        if self.StartTime>= self.EndTime:
            self.StartTime= Global.count
            self.EndTime= Global.count+2000
            Global.Score+=10
        else:
            self.StartTime +=10
    def get_tower_info(self):
        return self.tower_info