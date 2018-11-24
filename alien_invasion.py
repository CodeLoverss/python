import pygame
from pygame.locals import *
import time
import random


class plane(object):
    def __init__(self):
        planeImageName='./images/hero.gif'
        self.image=pygame.image.load(planeImageName).convert()
        self.x=250
        self.y=600
        self.speed=5
        self.bullets=[]
        self.left=False
        self.right=False
        self.shoot=False
        self.time2=0

    def draw(self,screen):
        self.keep_move()
        screen.blit(self.image,(self.x, self.y))#画自己的飞机
        for temp in self.bullets:
           temp.draw()#调用bullet类中的draw函数
        pygame.display.update()
    def move(self,position):
        if position=='left':
            self.x-=10
        if position=='right':
            self.x+=10
        if position=='space':#点击空格 实例化一个子弹对象 并添加到列表中
            self.bullets.append(bullet(screen,self.x+47,self.y-15,'Player'))
    def keep_move(self):
        if self.right:
            self.x+=3
        if self.left:
            self.x-=3
        if self.shoot:
            time1=float(time.time())
            if abs(time1-self.time2)>=0.2:
                self.bullets.append(bullet(screen,self.x+47,self.y-15,'Player'))
                self.time2=time1

class bullet(object):
    def __init__(self,screen,x,y,PlaneName):
        self.PlaneName=PlaneName
        self.x=x
        self.y=y
        self.window=screen

        if self.PlaneName=='enemyPlane':
            bgImageFile='./images/bullet-1.gif'
        elif self.PlaneName=='Player':
            bgImageFile='./images/bullet.gif'
        self.atom=pygame.image.load(bgImageFile).convert()
    def draw(self):
        if self.PlaneName=='enemyPlane':
            self.y+=1
        elif self.PlaneName=='Player':
            self.y-=2
        self.window.blit(self.atom,(self.x,self.y))#画出己方子弹或敌方子弹

class enemy(object):
    def __init__(self,screen,x,y):
        enemyImage='./images/enemy-1.gif'
        bullet='./images/bullet-1.gif'
        self.x=x
        self.y=y
        self.bullets=[]
        self.left=False
        self.right=False
        self.window=screen
        self.enemyPlane=pygame.image.load(enemyImage).convert()
        self.bullet=pygame.image.load(bullet).convert()
    def __del__(self):
        print('')
    def move(self,screen):#敌机移动
        if self.x>440:
            self.right=False
            self.left=True
        elif self.x<0:
            self.left=False
            self.right=True
        if self.left:
            self.x-=0.5
            self.y+=0.2
        else:
            self.x+=0.5
            self.y+=0.2
        randoms=random.randint(1,300)
        str=[30,80]
        if randoms in str:
            self.bullets.append(bullet(self.window,self.x+20,self.y+28,'enemyPlane'))
        for temp in self.bullets:
                temp.draw()
    def draw(self):
        self.window.blit(self.enemyPlane,(self.x,self.y))

#函数入口
if __name__ == '__main__':
    k=True
    screen=pygame.display.set_mode((480,740),0,0)
    bgImageFile='./images/background.png'
    background=pygame.image.load(bgImageFile).convert()
    player=plane()
    enemies=enemy(screen,0,0)
    while True:
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            if event.type==KEYDOWN:
                if event.key==K_a or event.key==K_LEFT:
                    player.left=True
                    player.move('left')
                if event.key==K_d or event.key==K_RIGHT:
                    player.right=True
                    player.move('right')
                if event.key==K_SPACE:
                    player.shoot=True
                    player.move('space')
            if event.type==KEYUP:
                if event.key==K_a or event.key==K_LEFT:
                    player.left=False
                if event.key==K_d or event.key==K_RIGHT:
                    player.right=False
                if event.key==K_SPACE:
                    player.shoot=False

        p=[]
        p1=[]
        p2=[]
        for tem in player.bullets:
            if tem.y<0:
                continue
            elif k==True:
                p.append((tem.x,tem.y))#我方子弹
                p1.append((enemies.x,enemies.y))#敌机位置列表

                for i,j in zip(p,p1):
                   #print(i)
                    #print(j)
                    if(abs(i[0]-j[0])<=20 and abs(i[1]-j[1])<=20):
                        print('您击中了敌机')
                        for s in range(1,5):
                            print(s)
                            bgImg='./images/enemy0_down'+str(s)+'.png'
                            show=pygame.image.load(bgImg).convert()
                            if s==1 and k==True:
                                k=False
                                del enemies
                            sc=screen.blit(show,(j[0],j[1]))
                            if sc:
                                print('加载图片')
                            #time.sleep(0.01)
                        break
        if k==True:
            enemies.move(screen)
            enemies.draw()
        player.draw(screen)

        time.sleep(0.01)

