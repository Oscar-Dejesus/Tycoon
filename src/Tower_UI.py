import pygame
from Globals import Global
from button import Button
import os
Background_X =0
Background_Y= Global.WINDOW_HEIGHT-200
#Tower Class 
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
        self.image= pygame.transform.scale(image,(Global.Towers_Info[self.index]["SizeX"]*.5,Global.Towers_Info[self.index]["SizeY"]*.5))
        self.rect =self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.topleft=(Background_X+self.x,Background_Y+self.y)
        self.Clicked= False
    #Checks to see if players clicked on UI itself 
    def GameUI(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not(self.Clicked) and Global.Score>=100 and len(Global.TowerBought)<1:
            Global.TowerBought.append(Global.Towers_Info[self.index])
            self.Clicked=True
            Global.Score-=Global.Towers_Info[self.index]["Cost"]
        if pygame.mouse.get_pressed()[0] == 0:
            self.Clicked=False
    def update(self):
        self.rect.topleft=(Background_X+self.x,Background_Y+self.y)
        self.GameUI()


# Background for the TowerUI
class TowerUIBackground(pygame.sprite.Sprite):
    #Sets defualt values and creates button for it
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface((Global.WINDOW_WIDTH,200))
        self.image.fill('green')
        self.rect =self.image.get_rect()
        self.rect.topleft=(Background_X,Background_Y)
        self.close_button=Button(Background_X,Background_Y-20,.2)
    # handles button logic and draws iself in background
    def update(self):
        global Background_Y
        self.rect.topleft=(Background_X,Background_Y)
        Global.TUI_Group.add(self.close_button,layer=0)
        pressed=self.close_button.draw()
        if pressed == True and not(Background_Y ==Global.WINDOW_HEIGHT):
            Background_Y =Global.WINDOW_HEIGHT
            self.close_button.updatePos(Background_X,Background_Y-20)
        elif pressed:
            Background_Y =Global.WINDOW_HEIGHT-200
            self.close_button.updatePos(Background_X,Background_Y-20)
        