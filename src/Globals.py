import pygame


pygame.font.init()

class Global():
    Score =500
    count=0
    WINDOW_WIDTH= 1000
    WINDOW_HEIGHT = 800
    TUI_Group = pygame.sprite.LayeredUpdates()
    Enemies_killed_wave =0
    Wave_Number=0
    ENEMEY_Group = pygame.sprite.LayeredUpdates()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),pygame.RESIZABLE | pygame.SCALED)
    BG = pygame.transform.scale(pygame.image.load("/Users/oscardejesus/Documents/GitHub/Tycoon/Tycoon/Images/BG.png"), (WINDOW.get_width(),WINDOW.get_height()))
    clock = pygame.time.Clock()
    FONT = pygame.font.SysFont("arial", 25)
    Towers = []
    CanPlaceTower = True
    TowerBought =[]
    Towers_Info=[{"TowerName":"Blue",   "Default_Attr":"Score_Add", "Score": 10, "Time":2000, "SellValue":100, "Cost":100, "Health":100, "SizeX":100, "SizeY":100, "Image":"Construction_Tower.png", "SpriteSize":(0,0)},
                 {"TowerName":"Space",  "Default_Attr":"Score_Add", "Score": 20, "Time":1500, "SellValue":150, "Cost":200, "Health":100, "SizeX":100, "SizeY":100, "Image":"space.png",   "SpriteSize":(0,0)},
                 {"TowerName":"Bullet", "Default_Attr":"regBullet", "Score": .5,  "Time":100,  "SellValue":150, "Cost":200, "Health":100, "SizeX":100, "SizeY":100, "Image":"Factory.png", "SpriteSize":(0,0)}]
    Tower_upgrades={"Bullet":[{"fourBullets":50},{"Score_Add":50}],"Blue":[{}],"Space":[{"Score_Add":50}]}
    
    Enemy_Info=[{"EnemyName":"Zombie","Health":40,"SizeX":50,"SizeY":50,"Image":"Factory.png","Speed":2}]
    Bullet_Group=pygame.sprite.LayeredUpdates()
    Game_Over= False
    Tower_clicked= None
    @classmethod
    def Set_Default_Values(cls):
        cls.Tower_clicked= None
        cls.Towers = []
        cls.Enemies_killed_wave =0
        cls.Wave_Number=0
        cls.Score=500
        cls.ENEMEY_Group.empty()
        cls.Bullet_Group.empty()

