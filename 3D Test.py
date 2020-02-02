import pygame
from pygame import *
import sys
import random
pygame.init
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("3D Test")
x=0
y=0
z=0
f=10
objects=[]
for i in range (10000):
        sz=0-random.randint(0,1000)
        sx=random.randint(-100000,100000)
        sy=random.randint(-100000,100000)
        sr=random.randint(50,100)
        for z in range (5,10):
            d=random.randint(1,2)
            if d==2:
                px=sx+(sr/2)+random.randint(10,40)
            else:
                px=sx-(sr/2)-random.randint(10,40)
            d=random.randint(1,2)
            if d==2:
                py=sy+(sr/2)+random.randint(10,40)
            else:
                py=sy-(sr/2)-random.randint(10,40)
            pz=sz+random.randint(-30,30)
        objects.append([sx,sy,sz,sr,(255,255,255)])
        objects.append([px,py,pz,random.randint(5,15),(random.randint(0,255),random.randint(0,255),random.randint(0,0))])
def star(selfx,selfy,selfz,selfr,colour):
    global x
    global y
    global z
    global f
    selfx = selfx - x
    selfy = selfy - y
    selfz = selfz - z
    if (selfz < 0):
        rx = -f*selfx / selfz
        ry = -f*selfy / selfz
        rr = -f*selfr / selfz
        if int(rr)>0.01:
            pygame.draw.circle(screen,(colour),(int(rx)+400, int(ry)+300), int(rr))

def frame():
    #star(-200,-200,-400,50,(255,255,255))
    #star( 120, 120,-350, 2,(200,100,100))
    #star( 0, 120,-350, 10,(0,255,0))
    #star( 0, 120,-340, 5,(200,200,200))
    for x in range (len(objects)):
        star(objects[x][0],objects[x][1],objects[x][2],objects[x][3],objects[x][4])
            

clock = pygame.time.Clock()
while True:
    screen.fill((0,0,0))
    frame()
    pygame.display.update()
    if pygame.key.get_pressed()[K_a]:
        x=x-10
    if pygame.key.get_pressed()[K_d]:
        x=x+10
    if pygame.key.get_pressed()[K_w]:
        y=y-10
    if pygame.key.get_pressed()[K_s]:
        y=y+10
    if pygame.key.get_pressed()[K_e]:
        z=z-1
    if pygame.key.get_pressed()[K_q]:
        z=z+1
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    print (x, ", ", y, ", ", z)
    
    clock.tick(60)
    
