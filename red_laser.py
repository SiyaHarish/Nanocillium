import pygame
WIDTH,HEIGHT= 1000,800
class Redlaser(pygame.sprite.Sprite):
    def __init__(self,x,y,laser_group):
        self.x=x
        self.y=y
        super().__init__()
        self.image=pygame.image.load("red_laser.png")
        self.image=pygame.transform.scale(self.image, (10,50))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.velocity=10
        laser_group.add(self)

    def update(self):
        self.rect.y=self.rect.y+self.velocity
        if self.rect.bottom > HEIGHT:
            self.kill()
