import pygame
import random
from Globals import Global
from Enemy import Enemy
class Waves:
    Waves= [{"Wave":1,"Bad":10}]
    @classmethod
    def SpawnEnemy(cls,name,num):

        
        for i in range(num):
            y = random.randint(0,Global.WINDOW_HEIGHT)
            x=-100
            E1 =Enemy(x,y,name)
            Global.ENEMEY_Group.add(E1)
        return y
    @classmethod
    def WaveStart(cls,Wave):
        for w in cls.Waves:
            if w["Wave"] == Wave:
                currentwave=w
        for name, Num in list(currentwave.items())[1:]:
            cls.SpawnEnemy(name,Num)
    

    