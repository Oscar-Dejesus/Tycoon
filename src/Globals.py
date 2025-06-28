import pygame
pygame.font.init()

class Global():
    Score =100
    count=0
    WINDOW_WIDTH= 1000
    WINDOW_HEIGHT = 800
    TUI_Group = pygame.sprite.LayeredUpdates()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    BG = pygame.transform.scale(pygame.image.load("/Users/oscardejesus/Documents/GitHub/Tycoon/Images/SpaceBG.png"), (1000,800))
    clock = pygame.time.Clock()
    FONT = pygame.font.SysFont("arial",25)
    Towers = []
    CanPlaceTower = True
    TowerBought=0
    towers=[{"TowerName":"Blue", "Score": 10,"Time":2000}]