from turtle import speed
import pygame as pg
from sklearn.linear_model import PassiveAggressiveClassifier
from functions import *
from globalValues import *
import math

screen = pg.display.set_mode(workspace)

file = 'peos.mp3'
pg.init()
pg.mixer.init()
pg.mixer.music.load(file)
pg.mixer.music.set_volume(volume)
pg.mixer.music.play()

running = True
while running:
    
    screen.fill((255, 255, 255))
    Point.update()

    tmp = [[0,0] for _ in range(movingPoint.number)] 
    n = [0 for _ in range(movingPoint.number)] 
    for key,val in Point.instances.items():
        tmp[val.id]=[tmp[val.id][0]+val.y,tmp[val.id][1]+val.x]
        n[val.id]=n[val.id]+1

        pg.draw.circle(screen, (0, 255, 255), (val.x,val.y), accuracy)
    
    x,y = pg.mouse.get_pos()
    pg.draw.circle(screen, (0, 0, 255), (x,y), accuracy,2)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEMOTION:
            t1 , t2, t3 = pg.mouse.get_pressed(num_buttons=3)
            if t3: 
                if Point.number==0: break
                for key,val in Point.instances.items():
                    if distance((val.y,val.x),(y,x))<2*accuracy:
                        del Point.instances[key]
                        Point.number-=1
                        break
            elif t2:
                Point(y,x) #ADD POINT
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button==4: 
                accuracy+=1
                volume+=0.01
                volume=min(volume,1)
                
                pg.mixer.music.set_volume(volume)
            if event.button==5:
                accuracy-=1
                volume-=0.01
                volume=max(volume,0.01)
                pg.mixer.music.set_volume(volume)
            if event.button==1: Point(y,x) #ADD POINT
            if event.button==3: #REMOVE POINT     
                if Point.number==0: break
                for key,val in Point.instances.items():
                    if distance((val.y,val.x),(y,x))<2*accuracy:
                        del Point.instances[key]
                        Point.number-=1
                        break
    
    

    for mv in movingPoint.instances:
        if n[mv.id]!=0:
            print(n[mv.id])
            mv.target = [tmp[mv.id][0]/n[mv.id],tmp[mv.id][1]/n[mv.id]]

        if mv.target != [None,None]:
            mv.x += (mv.target[1]-mv.x)*movingPoint.speed
            mv.y += (mv.target[0]-mv.y)*movingPoint.speed
        pg.draw.circle(screen, (0, 255, 0), (mv.x,mv.y), 2*accuracy)
    
    pg.display.flip()
    
'''

    pg.draw.circle(screen, (0, 0, 255), (250, 250), 75)

'''

# Done! Time to quit.

pg.quit()