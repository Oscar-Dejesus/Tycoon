import pygame
import random
from Globals import Global
from Enemy import Enemy
class Waves:
    Waves= [{"Wave":1,"Bad":2,"Time":5000},{"Wave":-1}]
    Current_Wave=[]
    StartTime = None
    EndTime= None
    nextwave =False
    Waves_ended = False
    Global.Enemies_killed_wave=0

    @classmethod
    def SpawnEnemy(cls,name,num):

        for _ in range(num):

            x, y = random.choice([(-100, random.randint(0, Global.WINDOW_HEIGHT)),(Global.WINDOW_WIDTH + 100, random.randint(0, Global.WINDOW_HEIGHT)),(random.randint(0,Global.WINDOW_WIDTH),-100),(random.randint(0,Global.WINDOW_WIDTH),Global.WINDOW_HEIGHT +100)])
            
            E1 =Enemy(x,y,name)
            Global.ENEMEY_Group.add(E1)
    @classmethod
    def intialize(cls):
        cls.Current_Wave=[]
        cls.StartTime = None
        cls.EndTime= None
        cls.nextwave =False
        Global.Enemies_killed_wave=0
    @classmethod
    def Wave_Logic(cls):
        if cls.Waves_ended:
            return
        if Global.Wave_Number==0:
            Global.Wave_Number+=1
            cls.WaveStart(Global.Wave_Number)

        elif Global.Enemies_killed_wave>=cls.Current_Wave["Bad"]:
            Global.Wave_Number+=1
            Global.Enemies_killed_wave=0
            cls.nextwave =True
        
        if cls.nextwave is not False and cls.Timer():
                cls.nextwave=False
                cls.WaveStart(Global.Wave_Number)
    @classmethod
    def Timer(cls):
        if cls.EndTime == None:
            cls.EndTime= Global.count+cls.Current_Wave["Time"]
        if cls.EndTime== None:
            cls.EndTime= Global.count+cls.Current_Wave["Time"]
        if Global.count>= cls.EndTime:
            cls.EndTime=None
            return True
    @classmethod
    def DefaultValues(cls):
        cls.Current_Wave=[]
        cls.StartTime = None
        cls.EndTime= None
        cls.nextwave =False
        cls.Waves_ended = False
    @classmethod
    def WaveStart(cls,Wave_num):
        for w in cls.Waves:
            if w["Wave"] == Wave_num:
                cls.Current_Wave=w
                cls.enemies_killed=0
                break
            elif w["Wave"] ==-1:
                cls.Current_Wave=w
                cls.Waves_ended=True
                return
        name =list(cls.Current_Wave.keys())[1]
        num=cls.Current_Wave[name]
        cls.SpawnEnemy(name,num)



    
