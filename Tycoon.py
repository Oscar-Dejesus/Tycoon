import pygame
import time 
import math
pygame.font.init()
#Global Variables
class Global():
    Score =0
    count=0
    WINDOW = pygame.display.set_mode((1000,800))
    WINDOW_WIDTH= 1000
    WINDOW_HEIGHT = 800
    BG = pygame.transform.scale(pygame.image.load("space.png"), (1000,800))
    clock = pygame.time.Clock()
    FONT = pygame.font.SysFont("arial",25)
    Towers = []

class Button():
    def __init__(self,x,y,Scale):
        self.x= x
        self.y=y
        image= pygame.image.load('button.jpeg')
        width = image.get_width()
        height =image.get_height()
        self.image= pygame.transform.scale(image,(int(width *Scale),int(height*Scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft =(x,y)
    
    def draw(self):

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            print("hover")
        Global.WINDOW.blit(self.image,(self.rect.x,self.rect.y))









def main():
    run =True
    Global.count=0
    def draw(Towers):
        Global.WINDOW.blit(Global.BG,(0,0))
        Display = Global.FONT.render(f"Score:{Global.Score}",1,"red")
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
            
            if keys[pygame.K_LEFT]:
                run =False
                UI()
    
        draw(Global.Towers)
        

def UI():
    run =True
    def draw():
        Global.WINDOW.fill(100)
        start_button.draw()
        pygame.display.update()
    
    start_button =Button((Global.WINDOW_WIDTH-250)/2,(Global.WINDOW_HEIGHT-150)/2,.5)
    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
                break
        Global.clock.tick(60)
        draw()
    


    


def Place_Tower(event):
    Placing=True
    if event.type==pygame.MOUSEBUTTONDOWN:
        Mouse_x,Mouse_y= event.pos
        for t in Global.Towers[:]:
            if t.get_tower_info().collidepoint(Mouse_x,Mouse_y):
                Global.Towers.remove(t)
                Placing=False
                break
        if Placing:
            Mouse_x,Mouse_y= event.pos
            Tower_temp = Tower(Mouse_x-50,Mouse_y-50,100,100)
            Global.Towers.append(Tower_temp)



   
class Tower:
    StartTime = Global.count 
    EndTime = Global.count +2000
    def __init__(self,x,y,width,height):
       self.tower_info = pygame.Rect(x,y,width,height)
    def Score_Add(self):
        global Score
        if self.StartTime>= self.EndTime:
            self.StartTime= Global.count
            self.EndTime= Global.count+2000
            Global.Score+=10
        else:
            self.StartTime +=10
    def get_tower_info(self):
        return self.tower_info

if __name__ =="__main__":
    pygame.init()
    UI()
