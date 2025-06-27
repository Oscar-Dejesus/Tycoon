import pygame
from Globals import Global
class TowerUI():
    def __init__(self):
        self.rect = pygame.draw.rect(Global.WINDOW,'blue',pygame.Rect(100,0,100,100))
        self.Clicked= False
    def GameUI(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            Global.CanPlaceTower=False
        else:
            Global.CanPlaceTower=True
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not(self.Clicked) and Global.Score>=100:
            self.Clicked=True
            Global.Score-=100
        if pygame.mouse.get_pressed()[0] == 0:
            self.Clicked=False
    def draw(self):
        pygame.draw.rect(Global.WINDOW,'blue',self.rect)