import pygame
from Globals import Global
from Core import Core
from Waves import Waves
from Rooms import *
import Rooms

pygame.font.init()
Player =Core((Global.WINDOW_WIDTH/2)-(100),(Global.WINDOW_HEIGHT/2)-(100),100,100)
def MainLoop():
    global Player 
    Rooms.GameState = "menu"
    Waves.intialize()
    Global.count=0
    while True:
        if Rooms.GameState == "menu":
            mainmenu()  # returns "game" or "quit"
            Global.Set_Default_Values()
            Waves.DefaultValues()
            Rooms.Player =Core((Global.WINDOW_WIDTH/2)-(100),(Global.WINDOW_HEIGHT/2)-(100),100,100)
            Waves.intialize()
        elif Rooms.GameState == "game":
            main()      # returns "menu" or "quit"
            Global.TUI_Group.empty()
        elif Rooms.GameState == "pause":
            pause()
        elif Rooms.GameState == "quit":
            pygame.quit()
            break




    
if __name__ =="__main__":
    pygame.init()
    MainLoop()