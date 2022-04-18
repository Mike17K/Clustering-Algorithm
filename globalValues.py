import math
from shutil import move
import random

from scipy import rand


N = 3

accuracy = 5 #pixel

volume = 0.00

workspace = (1200,1200) #y,x
grid = (100,100) #διαχορισμος του επιπεδου #y,x

total_arrays_Y = workspace[0]//grid[0]
total_arrays_X = workspace[1]//grid[1]

class Point:
    instances = {}
    number = 0
    def __init__(self,y,x):
        self.x = x
        self.y = y
        self.id = None
        Point.instances[str(self.y)+'-'+str(self.x)] = self
        Point.number +=1

    def __str__(self):
        return '('+str(self.y)+','+str(self.x)+')'

    @staticmethod
    def update():
        for key in Point.instances.keys():
            p = Point.instances[key]
            dist=math.inf
            for i in movingPoint.instances:
                tmp_dist = distance((p.y,p.x),(i.y,i.x))
                if dist>tmp_dist:
                    dist = tmp_dist
                    p.id = i.id

def distance(p1 : tuple,p2 : tuple):
    dx = abs(p1[1] - p2[1])
    dy = abs(p1[0] - p2[0])
    return math.sqrt(dx**2 + dy**2)

class movingPoint:
    speed = 0.01
    number = 0
    instances = []
    def __init__(self,y,x):
        self.x = x
        self.y = y
        self.target = [None,None]

        self.id = movingPoint.number
        movingPoint.number +=1
        movingPoint.instances.append(self)

movingPoint(random.randint(0,workspace[0]),random.randint(0,workspace[1]))
movingPoint(random.randint(0,workspace[0]),random.randint(0,workspace[1]))
movingPoint(random.randint(0,workspace[0]),random.randint(0,workspace[1]))
