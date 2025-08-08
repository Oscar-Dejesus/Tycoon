import pygame
from Bullets import Bullet
from Globals import Global
from Sprites import Sprites
import math
class Upgrades():
    
    def __init__(self):
        self.Upgrades_list= []
    def AddUpgrade(self,UpgradeName):
        self.Upgrades_list.append(UpgradeName)
    def removeUpgrade(self,UpgradeName):
        self.Upgrades_list.remove(UpgradeName)
    def Score_Add(self,Tower):
        Global.Score+=Tower.get_tower_info()["Score"]


    def fourBullets(self,Tower):
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
    
    def regBullet(self,Tower):
        t= Sprites.temp_sprite(Tower.Vision)
        enemy =  pygame.sprite.spritecollideany(t,Global.ENEMEY_Group)
        if enemy:
            angle_radians = math.atan2(Tower.rect.centery - enemy.rect.centery, enemy.rect.centerx - Tower.rect.centerx)
            B = Bullet(Tower.rect.centerx ,Tower.rect.centery,10,10,4,angle_radians,"Bullet.png")
            Global.Bullet_Group.add(B)


