import pygame
from bacteria import Bacteria
from nanobot import Nanobot
pygame.init()
pygame.font.init()
screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption("Nanocillium")
clock=pygame.time.Clock()
font=pygame.font.Font(None,36)


nanobotgroup=pygame.sprite.Group()
bacteria_group=pygame.sprite.Group()
nano_lasergroup=pygame.sprite.Group()
bacterialaser=pygame.sprite.Group()

bot=Nanobot(nano_lasergroup)
nanobotgroup.add(bot)


num_rows=5
num_columns=10
start_x=100
start_y=50
spacing_x=100
spacing_y=100
for row in range(num_rows):
    for column in range(num_columns):
        x=start_x + column * spacing_x
        y=start_y + row * spacing_y
        bacteria = Bacteria(x,y,bacterialaser,bacteria_group)
        bacteria_group.add(bacteria)
print(len(bacteria_group))

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bot.fire()

    screen.fill("blue")
    score_text=font.render(f"Score:{bot.score}",True,(255,255,255))
    score_rect=score_text.get_rect(centerx=300,top=15)
    lives_text=font.render(f"Lives:{bot.lives}",True,(255,255,255))
    lives_rect=lives_text.get_rect(centerx=800,top=15)
    if pygame.sprite.spritecollide(bot,bacterialaser,True):
        bot.lives-=1

    if pygame.sprite.groupcollide(bacteria_group,nano_lasergroup,True,True):
        bot.score+=1
    if bot.score >=50:
        screen.fill("pink")
        print("You Win!")
        running=False

    pygame.draw.line(screen,"black",(0,50),(1000,50),4)
    
    pygame.draw.line(screen,"black",(0,700),(1000,700),4)

    nanobotgroup.draw(screen)
    nanobotgroup.update(event)
    bacteria_group.update()
    bacteria_group.draw(screen)
    nano_lasergroup.update()
    nano_lasergroup.draw(screen)
    bacterialaser.update()
    bacterialaser.draw(screen)

    screen.blit(score_text,score_rect)
    screen.blit(lives_text,lives_rect)
    pygame.display.update()
    clock.tick(60)

    if bot.lives <= 0:
        print("Game Over")
        running=False

pygame.quit()

