import pygame
import time
import random
import math
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Circle Game")
score = 0
level=0
a=0
b=0

class Player (pygame.sprite.Sprite):
    def __init__(self):
        global score
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(((score +12)*2, (score +12)*2)).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        self.rect =self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.image = pygame.Surface(((score +12)*2, (score +12)*2)).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, (255,255,255), (score +12, score +12), score +12)
        self.rect =self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()      

class Ball (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.side = random.randint(1,4)
        global score
        global pos
        if self.side==1:
            self.x=900
            self.y=random.randint(0,600)
            self.ychange=random.randint(-2,2)
            self.xchange=-1
        elif self.side==2:
            self.x=-100
            self.y=random.randint(0,600)
            self.ychange=random.randint(-2,2)
            self.xchange=1
        elif self.side==3:
            self.y=-100
            self.x=random.randint(0,800)
            self.xchange=random.randint(-2,2)
            self.ychange=1
        elif self.side==4:
            self.y=700
            self.x=random.randint(0,800)
            self.xchange=random.randint(-2,2)
            self.ychange=-1

        color=random.randint(1,6)
        if color==1:
            color=(255,0,0)
        elif color==2:
            color=(0,255,0)
        elif color==3:
            color=(0,255,0)
        elif color==4:
            color=(255,255,0)
        elif color==5:
            color=(255,0,255)
        elif color==6:
            color=(0,255,255)
            
        self.size=((score)+10*(random.randint(1,5)))
        self.image = pygame.Surface(((self.size*2),(self.size*2))).convert_alpha()
        self.image.fill((111, 111, 111, 0))
        pygame.draw.circle(self.image, ((color)), (self.size, self.size), self.size)
        self.rect =self.image.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        global score
        global level
        global b
        if b==1:
            self.__init__()
        self.x=self.x+self.xchange/18
        self.y=self.y+self.ychange/18
        self.rect.center = (self.x,self.y)
        if self.x>900 or self.x<-100 or self.y>700 or self.y<-100:
            self.__init__()

        x1 = self.x
        x2 = pygame.mouse.get_pos()[0]
        y1 = self.y
        y2 = pygame.mouse.get_pos()[1]
        dist = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        r1 = self.size
        r2 = player.rect.width / 2
        
        if dist < r1 + r2:
            if self.size<score+12:
                self.__init__()
                if int(self.size/28)>0:
                    score=score+int(self.size/28)
                else:
                    score=score+1
            else:
                level=2

balls = pygame.sprite.Group()
playergroup = pygame.sprite.Group()
player = Player()
playergroup.add(player)
for i in range (30):
    balls.add(Ball())
while True:
    if level==0:
        if score>0:
            f = pygame.font.Font(None, 40)
            s = "Your last score was: "+str(score)
            surf = f.render(s,1,(255,255,255))
            screen.blit(surf,(10,550))
            
        f = pygame.font.Font(None, 100)
        surf = f.render("Circle Game",1,(255,255,255))
        screen.blit(surf,(200,230))
        f = pygame.font.Font(None, 50)
        surf = f.render("Press space to start",1,(255,255,255))
        screen.blit(surf,(240,300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()

            if event.type==KEYDOWN:
                if event.key == K_SPACE:
                    level=1
        
    if level==1:
        screen.fill((0,0,0))
        playergroup.update()
        playergroup.draw(screen)
        balls.update()
        balls.draw(screen)
        f = pygame.font.Font(None, 40)
        s = "score: "+str(score)
        surf = f.render(s,1,(255,255,255))
        screen.blit(surf,(10,10))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type==QUIT:
                    exit()

    if level==2:
        screen.fill((0,0,0))
        f = pygame.font.Font(None, 70)
        surf = f.render("Your final score was:",1,(255,0,0))
        screen.blit(surf,(170,250))
        f = pygame.font.Font(None, 70)
        s = str(score)
        surf = f.render(s,1,(255,0,0))
        screen.blit(surf,(390,300))
        pygame.display.update()
        exit()
