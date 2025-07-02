from Globals import Global
import os
import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        current_path = os.path.dirname(__file__) 
        image_path = os.path.join(current_path, '..','Images',"Factory.png")
        image_path =os.path.normpath(image_path)
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image,(width,height))
        self.rect =self.image.get_rect()
        self.rect.center = (x, y) 
        self.x=x
        self.y=y
        self.Vision= pygame.Rect(self.x,self.y, width *2, height*2)
        self.Target=None
    def Enemy_AI(self,Target):
        
        detected_target = self.Check_Target()
        if not(detected_target==False):
            Target= self.Check_Target()
        
        PointX = Target.x +(Target.width/2)
        PointY= Target.y + (Target.height/2)
        if self.rect.colliderect(Target.rect):
            Target.Health -=.1
            return
        if PointX >self.x:
            self.x +=1
        elif PointX <self.x:
            self.x -=1
        if PointY >self.y:
            self.y +=1
        elif PointY <self.y:
            self.y -=1
        self.rect.center =(self.x,self.y)
        self.Vision.center = (self.x,self.y)
        
    def Check_Target(self):
        for t in Global.Towers[:]:
            if self.Vision.colliderect(t.rect): 
                return t
        return False
        
    
            

        
    
