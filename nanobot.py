import pygame
from green_laser import Greenlaser
width,height=1200,800
class Nanobot(pygame.sprite.Sprite):
    def __init__(self,lasergroup):
        super().__init__()
        self.image=pygame.image.load("nanobot1.png")
        self.image=pygame.transform.scale(self.image, (100,100))
        self.rect=self.image.get_rect()
        self.rect.centerx=width/2
        self.rect.bottom=height
        self.lasergroup=lasergroup
        self.lives=3
        self.score=0

    def update(self, event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                self.rect.x-=10
            if event.key==pygame.K_RIGHT:
                self.rect.x+=10

    def fire(self):
        if len(self.lasergroup) < 2:
            Greenlaser(self.rect.centerx,self.rect.top,self.lasergroup)
            
    