import pygame
import os

class Sprites():
    def __init__(self,image,image_width=0,image_height=0,ScaleX=0,ScaleY=0,Frame_Time=0,Frames=0):
        current_path = os.path.dirname(__file__) 
        self.image_path = os.path.join(current_path, '..','Images',image)
        self.image_path =os.path.normpath(self.image_path)
        self.image_loaded = pygame.image.load(self.image_path)
        self.Frame_Time= Frame_Time
        self.Frames= Frames
        self.currentFrame =0
        self.max_width =self.image_loaded.get_width()
        self.max_height =self.image_loaded.get_height()
        self.last_updated=pygame.time.get_ticks()
        self.frame_Count = 0
        if image_width==0 and image_height == 0:
            self.width =self.max_width
            self.height = self.max_height
        else:
            self.width =image_width
            self.height = image_height
        self.ScaleX= ScaleX
        self.ScaleY=ScaleY
        self.x=0
        self.y=0
    def get_image(self):

        self.update()
        if self.Frames==0:
            one_image= pygame.transform.scale(self.image_loaded.subsurface((self.width*self.currentFrame,self.y,self.width,self.height)),(self.ScaleX,self.ScaleY))
            return one_image
        if self.width*(self.currentFrame+1)> self.max_width:
            self.currentFrame=0
            self.y+=self.height
        image= self.image_loaded.subsurface((self.width*self.currentFrame,self.y,self.width,self.height))
        t_image= pygame.transform.scale(image,(self.ScaleX,self.ScaleY))
        return t_image
    @classmethod
    def temp_sprite(self,rect):
        temp = pygame.sprite.Sprite()
        temp.rect = rect
        return temp
    
    def update(self):
        now = pygame.time.get_ticks()
        if now -self.last_updated> self.Frame_Time:
            self.last_updated =now
            self.frame_Count+=1
            self.currentFrame+=1
        if self.frame_Count>self.Frames:
            self.frame_Count=0
            self.y=0
            self.currentFrame=0




