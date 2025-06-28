import pygame
from Globals import Global

class Tower:
    StartTime = Global.count 
    EndTime = Global.count 
    index=0
    def __init__(self,x,y,width,height,Name):
       self.tower_info = pygame.Rect(x,y,width,height)
       for i, t in enumerate(Global.towers):
            if t["TowerName"]==Name:
                self.index= i
                break
    def Score_Add(self):
        if self.StartTime>= self.EndTime:
            self.StartTime= Global.count
            self.EndTime= Global.count+Global.towers[self.index]["Time"]
            Global.Score+=Global.towers[self.index]["Score"]
        else:
            self.StartTime +=10
    def get_tower_info(self):
        return self.tower_info