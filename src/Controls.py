from Globals import Global
from Towers import Tower
import pygame
import os

#Place tower logic checks to see if tower can be placed
def Place_Tower(event):
    if event.type==pygame.MOUSEBUTTONDOWN and Global.CanPlaceTower:
        Mouse_x,Mouse_y= event.pos
        for t in Global.Towers[:]:
            if t.get_tower_Draw_info().collidepoint(Mouse_x,Mouse_y):
                Global.Score+=t.get_tower_info()["SellValue"]
                Global.Towers.remove(t)
                Global.CanPlaceTower=False
                break
        if Global.CanPlaceTower and len(Global.TowerBought)>=1:
            Mouse_x,Mouse_y= event.pos
            Tower_temp = Tower(Mouse_x-(Global.TowerBought[0]["SizeX"]/2),Mouse_y-(Global.TowerBought[0]["SizeY"]/2),Global.TowerBought[0]["SizeX"],Global.TowerBought[0]["SizeY"],Global.TowerBought[0]["TowerName"],Global.TowerBought[0]["SpriteSize"])
            Global.TowerBought=[]
            Global.Towers.append(Tower_temp)
        Global.CanPlaceTower =True

def HoldingTower(Core):
    if len(Global.TowerBought)>0:
        Mouse_x,Mouse_y= pygame.mouse.get_pos()
        current_path = os.path.dirname(__file__) 
        image_path = os.path.join(current_path, '..','Images',Global.TowerBought[0]["Image"])
        image_path =os.path.normpath(image_path)
        image= pygame.transform.scale(pygame.image.load(image_path),(Global.TowerBought[0]["SizeX"],Global.TowerBought[0]["SizeY"]))
        image.set_alpha(100)
        image2=pygame.transform.scale(pygame.image.load(image_path),(Global.TowerBought[0]["SizeX"],Global.TowerBought[0]["SizeY"]))
        image2.set_alpha(128)
        rect =image.get_rect()
        rect.topleft=(Mouse_x-(Global.TowerBought[0]["SizeX"]/2),Mouse_y-(Global.TowerBought[0]["SizeY"]/2))
        Global.WINDOW.blit(image,rect.topleft)
        Mousepos= pygame.mouse.get_pos()
        for s in Global.TUI_Group:
            if s.rect.collidepoint(Mousepos):
                Global.CanPlaceTower=False
                break
        if rect.colliderect(Core.get_core_Draw_info()[1]):
            Global.CanPlaceTower=False
        else:
            for t in Global.Towers:
                if t!=rect and rect.colliderect(t.get_tower_Draw_info()):
                    Global.CanPlaceTower=False
        if Global.CanPlaceTower==False:
            image2.fill((255, 0, 0, 128))
            Global.WINDOW.blit(image2,rect.topleft)
        else:
            Global.WINDOW.blit(image,rect.topleft)
        

        
        

