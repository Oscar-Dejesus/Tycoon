import pygame
import time 
import math
from Globals import Global
from Tower_UI import TowerUI
from Towers import  Tower
from button import Button
pygame.font.init()



def main():
    run =True
    Global.count=0
    T_UI= TowerUI()
    def draw(Towers):
        Global.WINDOW.blit(Global.BG,(0,0))
        Display = Global.FONT.render(f"Score:{Global.Score}",1,"red")
        T_UI.GameUI()
        T_UI.draw()
        for t in Towers:
            pygame.draw.rect(Global.WINDOW,'blue',t.get_tower_info())
        
        Global.WINDOW.blit(Display,(0,0))
        pygame.display.update()
    while run:
        Global.count +=Global.clock.tick(60)
        for t in Global.Towers:
            t.Score_Add()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                break
            # Tower placement/deletion Check
           
            Place_Tower(event)
                
            keys = pygame.key.get_pressed()
        draw(Global.Towers)

def mainmenu():
    run =True
    def draw():
        nonlocal run
        Global.WINDOW.fill((0, 212, 255))
        if start_button.draw() ==True:
            run =False
        pygame.display.update()
    
    start_button =Button((Global.WINDOW_WIDTH-250)/2,(Global.WINDOW_HEIGHT-150)/2,.5)
    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                break
        
        Global.clock.tick(60)
        draw()
    main()

    


def Place_Tower(event):
    
    if event.type==pygame.MOUSEBUTTONDOWN and Global.CanPlaceTower:
        Mouse_x,Mouse_y= event.pos
        for t in Global.Towers[:]:
            if t.get_tower_info().collidepoint(Mouse_x,Mouse_y):
                Global.Towers.remove(t)
                Global.Score+=50
                Global.CanPlaceTower=False
                break
        if Global.CanPlaceTower and Global.Score>=100:
            Mouse_x,Mouse_y= event.pos
            Tower_temp = Tower(Mouse_x-50,Mouse_y-50,100,100)
            Global.Score -= 100
            Global.Towers.append(Tower_temp)
        Global.CanPlaceTower =True




if __name__ =="__main__":
    pygame.init()
    mainmenu()
