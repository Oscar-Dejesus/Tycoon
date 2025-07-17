from Globals import Global
import os
import pygame
from Sprites import Sprites
import random
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,name):
        pygame.sprite.Sprite.__init__(self)
        self.index = 0
        for i, n in enumerate(Global.Enemy_Info):
            if n["EnemyName"] == name:
                self.index= i
                break

        self.width = Global.Enemy_Info[self.index]["SizeX"]
        self.height= Global.Enemy_Info[self.index]["SizeY"]
        self.sprite =Sprites(Global.Enemy_Info[self.index]["Image"],0,0,self.width,self.height,5000,0)
        
        self.image = self.sprite.get_image()

        self.rect =self.image.get_rect()

        self.rect.center = (x, y) 
        self.x=x
        self.y=y
        self.Vision= pygame.Rect(self.x,self.y, self.width *3, self.height*3)
        self.Target=None
        self.health=Global.Enemy_Info[self.index]["Health"]
        self.speed =random.randint(1,4)
    def Enemy_AI(self,Target):
        if self.health<=0:
            Global.ENEMEY_Group.remove(self)
            return
        detected_target = self.Check_Target()
        if not(detected_target==False):
            Target= self.Check_Target()
        

        PointX = Target.x +(Target.width/2)
        PointY= Target.y + (Target.height/2)
        if self.rect.colliderect(Target.rect):
            Target.Health -=.1
            return
        if PointX >self.x:
            for _ in range(self.speed):
                if PointX <=self.x: 
                    break
                self.x +=1
        if PointX <self.x:
            for _ in range(self.speed):
                if PointX >=self.x:
                    break
                self.x -=1
                
        if PointY >self.y:
            for _ in range(self.speed):
                if PointY <=self.y:
                    break
                self.y +=1
                
        if PointY <self.y:
            for _ in range(self.speed):

                if PointY >=self.y:
                    break
                self.y -=1
                
        
        self.rect.center =(self.x,self.y)
        self.Vision.center = (self.x,self.y)

    def Check_Target(self):
        for t in Global.Towers[:]:
            if self.Vision.colliderect(t.rect): 
                return t
        return False
    
        
    
            

        
    
