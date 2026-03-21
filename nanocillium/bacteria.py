import pygame
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
        

    def fire(self):
        Redlaser(self.rect.centerx,self.rect.bottom,self.red_lasergroup)
