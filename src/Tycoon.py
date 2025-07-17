import pygame
from Globals import Global
from Tower_UI import *
from Towers import  *
from button import Button
from Controls import Place_Tower
from Controls import HoldingTower
from Core import Core
from Waves import Waves
from Bullets import Bullet
import math
import random

pygame.font.init()


GameState = None
def MainLoop():
    global GameState
    GameState = "menu"
    while True:
        if GameState == "menu":
            mainmenu()  # returns "game" or "quit"
        elif GameState == "game":
            main()      # returns "menu" or "quit"
        elif GameState == "pause":
            pause()
        elif GameState == "quit":
            pygame.quit()
            break
def SpawnEnemy():
    y = random.randint(0,Global.WINDOW_HEIGHT)
    x=-100
    return y


def main():

    # Initializing variables like towers player ect
    run =True
    Global.count=0
    Exit_Button=Button(Global.WINDOW_WIDTH-250,0,.5)
    TUI_x=0
    for t in range(len(Global.Towers_Info)):
        TUI_x=50+(t*150)
        T_UI= TowerUI(TUI_x,30,Global.Towers_Info[t]["TowerName"])
        Global.TUI_Group.add(T_UI,layer=5)
    
    T_Background= TowerUIBackground()
    Global.TUI_Group.add(T_Background,layer=0)
    Player =Core((Global.WINDOW_WIDTH/2)-(100),(Global.WINDOW_HEIGHT/2)-(100),100,100)
    Waves.WaveStart(1)
    #Draws all all assets to main game
    def draw(Towers):
        Global.CanPlaceTower=True
        Global.WINDOW.blit(Global.BG,(0,0))
        Display = Global.FONT.render(f"Score:{Global.Score}",1,"red")
        Player.draw()
        HoldingTower(Player)
        for t in Towers:
            t.drawTower()

        #Drawing bullets and enemies
        Global.ENEMEY_Group.update()
        Global.ENEMEY_Group.draw(Global.WINDOW)
        Global.Bullet_Group.update()
        Global.Bullet_Group.draw(Global.WINDOW)
        
        
        Global.TUI_Group.update()
        Global.TUI_Group.draw(Global.WINDOW)

        Global.WINDOW.blit(Display,(0,0))
        if Exit_Button.draw() ==True:
            return False
        pygame.display.update()
    
    global GameState    

    #Main Game loop
    while run:
        Global.count +=Global.clock.tick(60)
        for t in Global.Towers:
            t.Tower_Loop()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                GameState ="quit"
                break
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    draw(Global.Towers)
                    GameState="pause"
                    run =False
                    break
            Place_Tower(event)
        for e in Global.ENEMEY_Group:
            e.Enemy_AI(Player)  
        Player.check_Health()
        if draw(Global.Towers) == False:
            Global.Towers = []
            Global.Score=500
            GameState ="menu"
            break
        if Global.Game_Over:
            Global.Towers = []
            Global.Score=500
            GameState ="menu"
            break
        for b in Global.Bullet_Group:
            b.Bullet_Loop()
    Global.TUI_Group.empty()
    Global.ENEMEY_Group.empty()
    Global.Bullet_Group.empty()

def pause():
    overlay = pygame.Surface(pygame.display.get_window_size(),pygame.SRCALPHA)
    overlay.fill((128, 128, 128, 128))
    Text = Global.FONT.render("Paused",True,"red")
    Global.WINDOW.blit(overlay,(0,0))
    Global.WINDOW.blit(Text,((Global.WINDOW.get_width()/2)- Text.get_width()/2,(Global.WINDOW.get_height()/2)-Text.get_height()/2))
    pygame.display.update()
    global GameState
    while True:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                GameState="quit"
                return
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    GameState="game"
                    return
            
    

def mainmenu():
    global GameState
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
            GameState ="game" 
            Global.Game_Over = False
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                GameState ="quit"
                break

if __name__ =="__main__":
    pygame.init()
    MainLoop()