import pygame
from Globals import Global
from Sprites import Sprites
import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,speed=0,direction=0,bulletType=""):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = Sprites(bulletType,0,0,width,height)
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
        if self.x > Global.WINDOW_WIDTH+50 or self.x < -50 or self.y > Global.WINDOW_HEIGHT-50 or self.y < -50:
            Global.Bullet_Group.remove(self)
            return
        collisions = pygame.sprite.spritecollide(self, Global.ENEMEY_Group, False)
        
        if collisions:
            collisions[0].health -=1
            Global.Bullet_Group.remove(self)
            return

        
    def BasicMovement(self,radian):
        self.x += math.cos(radian) *self.speed
        self.y -=math.sin(radian)*self.speed
        self.rect.center = (self.x, self.y) 
class BullePattern():
    @classmethod
    def regBullet(cls,Tower):
        t= Sprites.temp_sprite(Tower.Vision)
        enemy =  pygame.sprite.spritecollideany(t,Global.ENEMEY_Group)
        if enemy:
            angle_radians = math.atan2(Tower.rect.centery - enemy.rect.centery, enemy.rect.centerx - Tower.rect.centerx)
            B = Bullet(Tower.rect.centerx ,Tower.rect.centery,10,10,4,angle_radians,"Bullet.png")
            Global.Bullet_Group.add(B)
    @classmethod
    def fourBullets(cls,Tower):
        t= Sprites.temp_sprite(Tower.Vision)
        enemy =  pygame.sprite.spritecollideany(t,Global.ENEMEY_Group)
        if enemy:
            angle_radians = math.atan2(Tower.rect.centery - enemy.rect.centery, enemy.rect.centerx - Tower.rect.centerx)
            B = Bullet(Tower.rect.centerx ,Tower.rect.centery,10,10,4,angle_radians,"Bullet.png")
            B1 = Bullet(Tower.rect.centerx ,Tower.rect.centery,10,10,4,angle_radians+math.pi,"Bullet.png")
            B2 = Bullet(Tower.rect.centerx ,Tower.rect.centery,10,10,4,angle_radians+math.pi/2,"Bullet.png")
            B3 = Bullet(Tower.rect.centerx ,Tower.rect.centery,10,10,4,angle_radians+ math.pi* 3/2,"Bullet.png")
            Global.Bullet_Group.add(B)
            Global.Bullet_Group.add(B1)
            Global.Bullet_Group.add(B2)
            Global.Bullet_Group.add(B3)