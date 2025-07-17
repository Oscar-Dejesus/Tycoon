import pygame
from Globals import Global
from Sprites import Sprites
import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,speed,direction,bulletType):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = Sprites(bulletType,0,0,width,height,99999,0)
        self.image= self.sprite.get_image()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y) 
        self.bulletType= bulletType
        self.x= x
        self.y= y
        self.width= width
        self.height= height
        self.speed = speed
        self.direction = direction
    def Bullet_Loop(self):
        self.BulletCollision()
        self.BasicMovement(self.direction)
    def BulletCollision(self):
        collisions = pygame.sprite.spritecollide(self, Global.ENEMEY_Group, False)

        if collisions:
            collisions[0].health -=1
            Global.Bullet_Group.remove(self)

        
    def BasicMovement(self,radian):
        self.x += math.cos(radian) *self.speed
        self.y -=math.sin(radian)*self.speed
        self.rect.center = (self.x, self.y) 