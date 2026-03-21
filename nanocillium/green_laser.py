import pygame
class Greenlaser(pygame.sprite.Sprite):
    def __init__(self,x,y,nano_lasergroup):
        super().__init__()
        self.image=pygame.image.load("green_laser.png")
        self.image=pygame.transform.scale(self.image, (10,50))
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        nano_lasergroup.add(self)
        self.velocity=10

    def update(self):
        self.rect.y=self.rect.y-self.velocity
        if self.rect.bottom < 0:
            self.kill()