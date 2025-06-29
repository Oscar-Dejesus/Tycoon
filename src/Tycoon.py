import pygame
from Globals import Global
from Tower_UI import *
import Tower_UI
from Towers import  *
from button import Button
from Controls import Place_Tower
from Controls import HoldingTower
pygame.font.init()



def main():
    run =True
    Global.count=0

    TUI_x=0
    for t in range(len(Global.Towers_Info)):
        TUI_x+=50*(t+1)
        T_UI= TowerUI(TUI_x,30,Global.Towers_Info[t]["TowerName"])
        Global.TUI_Group.add(T_UI,layer=5)
    
    T_Background= TowerUIBackground()
    Global.TUI_Group.add(T_Background,layer=0)

    #Draws all all assets to main game
    def draw(Towers):
        Global.CanPlaceTower=True
        Global.WINDOW.blit(Global.BG,(0,0))
        Display = Global.FONT.render(f"Score:{Global.Score}",1,"red")
        HoldingTower()
        for t in Towers:
            Global.WINDOW.blit(t.get_tower_Draw_info()[0],t.get_tower_Draw_info()[1])
        Global.TUI_Group.update()
        Global.TUI_Group.draw(Global.WINDOW)
        Mousepos= pygame.mouse.get_pos()
        for s in Global.TUI_Group:
            if s.rect.collidepoint(Mousepos):
                Global.CanPlaceTower=False
                break
            
        
        
        Global.WINDOW.blit(Display,(0,0))
        pygame.display.update()
        
    #Main Game loop
    while run:
        Global.count +=Global.clock.tick(60)
        for t in Global.Towers:
            t.Score_Add()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                break
           
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
        Global.clock.tick(60)
        draw()
        if run==False:
            main() 
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                break
    


if __name__ =="__main__":
    pygame.init()
    mainmenu()
