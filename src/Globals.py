import pygame
pygame.font.init()

class Global():
    Score =500
    count=0
    WINDOW_WIDTH= 1500
    WINDOW_HEIGHT = 1000
    TUI_Group = pygame.sprite.LayeredUpdates()
    ENEMEY_Group = pygame.sprite.LayeredUpdates()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),pygame.RESIZABLE | pygame.SCALED)
    BG = pygame.transform.scale(pygame.image.load("/Users/oscardejesus/Documents/GitHub/Tycoon/Tycoon/Images/SpaceBG.png"), (WINDOW.get_width(),WINDOW.get_height()))
    clock = pygame.time.Clock()
    FONT = pygame.font.SysFont("arial", 25)
    Towers = []
    CanPlaceTower = True
    TowerBought =[]
    Towers_Info=[{"TowerName":"Blue","Type":"Money", "Score": 10,"Time":2000,"SellValue":100,"Cost":100,"Health":100, "SizeX":100,"SizeY":100,"Image":"Factory.png","SpriteSize":(0,0)},
                 {"TowerName":"Space","Type":"Money", "Score": 20,"Time":1500,"SellValue":150,"Cost":200,"Health":100,"SizeX":100,"SizeY":100,"Image":"space.png","SpriteSize":(100,100)},
                 {"TowerName":"hello","Type":"Bullet","Time":100,"SellValue":150,"Cost":200,"Health":100,"SizeX":100,"SizeY":100,"Image":"Factory.png","SpriteSize":(100,100)}]
           
    Enemy_Info=[{"EnemyName":"bad","Health":40,"SizeX":50,"SizeY":50,"Image":"Factory.png"}]
    Bullet_Group=pygame.sprite.LayeredUpdates()
    Game_Over= False