import pygame
from Globals import Global
from button import Button
from Sprites import Sprites
import os
Background_X =0
Background_Y= Global.WINDOW_HEIGHT-200

class TowerUI(pygame.sprite.Sprite):
    #sets position and loads images
    def __init__(self,x,y,Name):
        pygame.sprite.Sprite.__init__(self)
        for i, t in enumerate(Global.Towers_Info):
            if t["TowerName"]==Name:
                self.index= i
                break
        current_path = os.path.dirname(__file__) 
        image_path = os.path.join(current_path, '..','Images',Global.Towers_Info[self.index]["Image"])
        image_path =os.path.normpath(image_path)
        image= pygame.image.load(image_path)
        self.image= pygame.transform.scale(image,(50,50))
        self.rect =self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.topleft=(Background_X+self.x,Background_Y+self.y)
        self.Clicked= False
    #Checks to see if players clicked on UI itself 
    def GameUI(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not(self.Clicked) and Global.Score>=Global.Towers_Info[self.index]["Cost"] and len(Global.TowerBought)<1:
            Global.TowerBought.append(Global.Towers_Info[self.index])
            self.Clicked=True
            Global.Score-=Global.Towers_Info[self.index]["Cost"]
        if pygame.mouse.get_pressed()[0] == 0:
            self.Clicked=False
    def update(self):
        self.rect.topleft=(Background_X+self.x,Background_Y+self.y)
        self.GameUI()
    def Draw_Overlay(self):
        pass

class UpgradeUI(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 200
        self.height = Global.WINDOW_HEIGHT
        self.x=Global.WINDOW_WIDTH-self.width
        self.y=0
        self.image = pygame.Surface((self.width,Global.WINDOW_HEIGHT))
        self.image.fill('green')
        self.rect =self.image.get_rect()
        self.Upgrades= []
        self.rect.topleft=(self.x,self.y)  

        self.Sell_Button = Button(self.x-50,self.y,100,50)
        self.Upgrade_Button1= Button(self.x+10,self.y+100,self.width-10,self.height/2-100)
        self.Upgrade_Button2= Button(self.x +10,self.y+self.height/2,self.width-10,self.height/2-100)

    def update(self):
        if Global.Tower_clicked!= None:

            self.Upgrades = Global.Tower_upgrades.get(Global.Tower_clicked.Name)
            self.rect.topleft=(self.x,0)

        else:
            self.rect.topleft=(self.x+self.width,0)
            return
        if self.Sell_Button.check_clicked():
                Global.Score+=Global.Tower_clicked.get_tower_info()["SellValue"]
                Global.Towers.remove(Global.Tower_clicked)
                Global.Tower_clicked=None
                return
        if  len(self.Upgrades)-1<=Global.Tower_clicked.UpgradeIndex or Global.Tower_clicked.UpgradeIndex==-1:
            self.Upgrade_Button1.setText("No More Upgrades")
            self.Upgrade_Button2.setText("No More Upgrades")
            Global.Tower_clicked.UpgradeIndex=-1
            return
        

        if self.Upgrades and Global.Tower_clicked.UpgradeIndex>=0:
            key1 = list(self.Upgrades[Global.Tower_clicked.UpgradeIndex].keys())[0]
            key2 =list(self.Upgrades[Global.Tower_clicked.UpgradeIndex + 1].keys())[0]
            self.Upgrade_Button1.setText(key1)
            self.Upgrade_Button2.setText(key2)
            
            if self.Upgrade_Button1.check_clicked() and Global.Score>=self.Upgrades[Global.Tower_clicked.UpgradeIndex].get(key1):
                Global.Score-=self.Upgrades[Global.Tower_clicked.UpgradeIndex].get(key1)
                Global.Tower_clicked.addUpgrade(key1)
                Global.Tower_clicked.UpgradeIndex+=2

            if self.Upgrade_Button2.check_clicked()and Global.Score>=self.Upgrades[Global.Tower_clicked.UpgradeIndex + 1].get(key2):
                Global.Score-=self.Upgrades[Global.Tower_clicked.UpgradeIndex+1].get(key2)
                Global.Tower_clicked.addUpgrade(key2)
                Global.Tower_clicked.UpgradeIndex+=2
                
        


        

        
    def Draw_Overlay(self):
        self.Sell_Button.updatePos(self.rect.x+5,self.rect.y+5)
        self.Upgrade_Button1.updatePos(self.rect.x+10,self.rect.y+100)
        self.Upgrade_Button2.updatePos(self.rect.x+10,self.y+self.height/2+100)
        self.Sell_Button.draw()
        self.Upgrade_Button1.draw()
        self.Upgrade_Button2.draw()


        
# Background for the TowerUI
class TowerUIBackground(pygame.sprite.Sprite):
    #Sets defualt values and creates button for it
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface((Global.WINDOW_WIDTH,200))
        self.image.fill('green')
        self.rect =self.image.get_rect()
        self.rect.topleft=(Background_X,Background_Y)
        self.close_button=Button(Background_X,Background_Y-100,100,100,"","Arrow_Down.png")
        
    # handles button logic and draws iself in background
    def update(self):
        global Background_Y
        self.rect.topleft=(Background_X,Background_Y)
        self.close_button.draw()
        pressed=self.close_button.check_clicked()
        if pressed == True and not(Background_Y ==Global.WINDOW_HEIGHT):
            Background_Y =Global.WINDOW_HEIGHT
            self.close_button.updatePos(Background_X,Background_Y-100)
            self.close_button.updateImage("Arrow_Up.png")
        elif pressed:
            Background_Y =Global.WINDOW_HEIGHT-200
            self.close_button.updatePos(Background_X,Background_Y-100)
            self.close_button.updateImage("Arrow_Down.png")
    def Draw_Overlay(self):
        pass