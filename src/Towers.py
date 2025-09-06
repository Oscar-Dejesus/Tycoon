import pygame
from Globals import Global
from Sprites import Sprites

from Upgrades import Upgrades
class Tower:
    index=0

    def __init__(self,x,y,Name):
       for i, t in enumerate(Global.Towers_Info):
            if t["TowerName"]==Name:
                self.index= i
                break
        
       self.StartTime = Global.count 
       self.EndTime= Global.count+Global.Towers_Info[self.index]["Time"]
       self.width = Global.Towers_Info[self.index]["SizeX"]
       self.height = Global.Towers_Info[self.index]["SizeY"]
       self.sprite = Sprites(Global.Towers_Info[self.index]["Image"],Global.Towers_Info[self.index]["SpriteSize"][0],Global.Towers_Info[self.index]["SpriteSize"][1],self.width,self.height)
      
       self.image= self.sprite.get_image()
       self.rect=self.image.get_rect()
       self.rect.topleft = (x, y) 
       
       self.UpgradeIndex=0

       self.tower_info =self.rect
       self.Max_Health = Global.Towers_Info[self.index]["Health"]
       self.Health = Global.Towers_Info[self.index]["Health"]
       self.x = x
       self.y =y
       self.Name = Name


       self.Vision= pygame.Rect(self.x,self.y, self.width *5, self.height*5)
       self.Upgrade = Upgrades()
       self.Upgrade.AddUpgrade(Global.Towers_Info[self.index]["Default_Attr"])
    def Tower_Loop(self):
        if self.Timer():
            for s in self.Upgrade.Upgrades_list:
                if hasattr(self.Upgrade, s):
                    getattr(self.Upgrade, s)(self)
        
        self.Check_Dead()
        Mousepos= pygame.mouse.get_pos()
        UI_Touch=False
        for s in Global.TUI_Group:
            if s.rect.collidepoint(Mousepos):
                UI_Touch =True
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.event.peek(pygame.MOUSEBUTTONDOWN)and Global.CanPlaceTower==True:
            Global.Tower_clicked=self
        elif pygame.event.peek(pygame.MOUSEBUTTONDOWN) and Global.Tower_clicked==self and UI_Touch==False:
            Global.Tower_clicked=None
                
    def getUpgradeObj(self):
        return self.Upgrade
    
    def addUpgrade(self,UpgradeName):
        self.Upgrade.AddUpgrade(UpgradeName)
    def Timer(self):
        if self.StartTime>= self.EndTime:
            self.StartTime= Global.count
            self.EndTime= Global.count+Global.Towers_Info[self.index]["Time"]
            return True
        else:
            self.StartTime =Global.count
    def DrawHealth(self):
        rect =pygame.Rect(self.x,self.y+self.height-5,self.width * (self.Health/self.Max_Health),5)
        pygame.draw.rect(Global.WINDOW,(0, 255, 0),rect,border_radius=5)
    def Check_Dead(self):
        if self.Health <=0:
            Global.Towers.remove(self)

    
    def drawTower(self):
        self.image= self.sprite.get_image()
        self.rect=self.image.get_rect()
        self.rect.topleft = (self.x, self.y) 
        self.Vision.center = (self.x,self.y)
        Global.WINDOW.blit(self.image,(self.x,self.y))
        self.DrawHealth()
        
    def get_tower_info(self):
        return Global.Towers_Info[self.index]
    def get_tower_Draw_info(self):
        return self.tower_info
    

