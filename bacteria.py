import pygame
import random
from red_laser import Redlaser
class Bacteria(pygame.sprite.Sprite):
    def __init__(self,x,y,red_lasergroup,bacteria_group):
        self.x=x
        self.y=y
        super().__init__()
        self.image=pygame.image.load("bacteria.png")
        self.image=pygame.transform.scale(self.image, (50,50))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.red_lasergroup=red_lasergroup
        self.bacteria_group=bacteria_group
        self.velocity=2
        self.direction=1

    def update(self):
        self.rect.x+=self.direction*self.velocity
        if self.rect.right>=950 or self.rect.left<=50:
            for bacteria in self.bacteria_group:
                bacteria.direction*=-1
                bacteria.rect.y+=0.1
        if random.randint(0,1000)>999 and len(self.red_lasergroup)<3:
            self.fire()

    def fire(self):
        Redlaser(self.rect.centerx,self.rect.bottom,self.red_lasergroup)
