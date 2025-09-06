from Globals import Global
from Tower_UI import *
from Towers import  *
from button import Button
from Controls import Place_Tower
from Controls import HoldingTower
from Controls import *
from Core import Core
from Waves import Waves


Player =Core((Global.WINDOW_WIDTH/2)-(100),(Global.WINDOW_HEIGHT/2)-(100),100,100)
GameState = None
def Default_room():
    TUI_x=0
    for t in range(len(Global.Towers_Info)):
        TUI_x=50+(t*150)
        T_UI= TowerUI(TUI_x,30,Global.Towers_Info[t]["TowerName"])
        Global.TUI_Group.add(T_UI,layer=5)

    T_Background= TowerUIBackground()
    
    Global.TUI_Group.add(T_Background,layer=0)
    Global.TUI_Group.add(UpgradeUI())
    
def main():

    # Initializing variables like towers player ect
    run =True
    room =Default_room()

    
    #Draws all all assets to main game
    def draw():
        Global.CanPlaceTower=True
        Global.WINDOW.blit(Global.BG,(0,0))
        Display = Global.FONT.render(f"Score:{Global.Score}",1,"red")
        Player.draw()
        HoldingTower(Player)
        for t in Global.Towers:
            t.drawTower()

        #Drawing bullets and enemies
        Global.ENEMEY_Group.update()
        Global.ENEMEY_Group.draw(Global.WINDOW)
        Global.Bullet_Group.update()
        Global.Bullet_Group.draw(Global.WINDOW)
        
        
        Global.TUI_Group.update()
        Global.TUI_Group.draw(Global.WINDOW)
        for sprite in Global.TUI_Group:
            sprite.Draw_Overlay()
        

        Global.WINDOW.blit(Display,(0,0))
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
                    draw()
                    GameState="pause"
                    run =False
                    break
            Place_Tower(event)
        for e in Global.ENEMEY_Group:
            e.Enemy_AI(Player)  
        Player.check_Health()

        draw()
        if Global.Game_Over:
            Global.Towers = []
            Global.Score=500
            GameState ="menu"
            break
        for b in Global.Bullet_Group:
            b.Bullet_Loop()
        Waves.Wave_Logic()
    
def pause():
    overlay = pygame.Surface(pygame.display.get_window_size(),pygame.SRCALPHA)
    overlay.fill((128, 128, 128, 128))
    Text = Global.FONT.render("Paused",True,"red")
    Exit_Button=Button(10,0,100,50)
    Global.WINDOW.blit(overlay,(0,0))
    Global.WINDOW.blit(Text,((Global.WINDOW.get_width()/2)- Text.get_width()/2,(Global.WINDOW.get_height()/2)-Text.get_height()/2))
    Exit_Button.draw()
    pygame.display.update()
    global GameState
    while True:
        if Exit_Button.check_clicked() ==True:
            GameState="menu"
            return
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
        
        start_button.draw()
        pygame.display.update()
    start_button =Button((Global.WINDOW_WIDTH-250)/2,(Global.WINDOW_HEIGHT-150)/2,200,100,"Start Game")
    while run:

        Global.clock.tick(60)
        draw()
        if start_button.check_clicked() ==True:
            run =False
        if run==False:
            GameState ="game" 
            Global.Game_Over = False
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                GameState ="quit"
                break


