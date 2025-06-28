import pygame
from Globals import Global
from button import Button
Background_X =0
Background_Y= Global.WINDOW_HEIGHT-200
class TowerUI(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface((100,100))
        self.image.fill('blue')
        self.rect =self.image.get_rect()
        self.x=x
        self.y= y
        self.rect.topleft=(Background_X+self.x,Background_Y+self.y)

        self.Clicked= False
    def GameUI(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not(self.Clicked) and Global.Score>=100:
            self.Clicked=True
            Global.Score-=100
            Global.TowerBought+=1
        if pygame.mouse.get_pressed()[0] == 0:
            self.Clicked=False
    def update(self):
        self.rect.topleft=(Background_X+self.x,Background_Y+self.y)
        self.GameUI()

class TowerUIBackground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface((Global.WINDOW_WIDTH,200))
        self.image.fill('green')
        self.rect =self.image.get_rect()
        self.rect.topleft=(Background_X,Background_Y)
        self.close_button=Button(Background_X,Background_Y-20,.2)
    
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
        