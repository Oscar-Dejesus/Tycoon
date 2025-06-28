import pygame
from Globals import Global
class Button(pygame.sprite.Sprite):
    def __init__(self,x,y,Scale):
        super().__init__() 
        self.x= x
        self.y=y
        image= pygame.image.load('/Users/oscardejesus/Documents/GitHub/Tycoon/Images/button.jpeg')
        width = image.get_width()
        height =image.get_height()
        self.image= pygame.transform.scale(image,(int(width *Scale),int(height*Scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft =(x,y)
        self.clicked= False
    def draw(self):
        action =False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] ==1 and not(self.clicked):
            self.clicked = True
            action =True
        if pygame.mouse.get_pressed()[0] ==0:
            self.clicked=False
        
        Global.WINDOW.blit(self.image,(self.rect.x,self.rect.y))
        return action
    def updatePos(self,x,y):
        self.rect.topleft =(x,y)