import pygame
import sys
from objects import Objects
from game_manager import Game_manager
from operations import Operations
#Инициализация pyGame
pygame.init()



#таймер
clock = pygame.time.Clock()

#создаём экран
screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)

gm = Game_manager()
op = Operations()

#фон
background = pygame.image.load(f"textures/background.jpg")
background = pygame.transform.scale(background,(1280,720))

#главный игровой цикл:
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                localx, localy = pygame.mouse.get_pos()
                gm.robots.append(Objects(localx, localy,"character.png", True, "robot"))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                localx, localy = pygame.mouse.get_pos()
                if not op.is_position_occupied(gm,localx, localy):
                    gm.walls.append(Objects(localx, localy, "wall.png", True, "wall"))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                localx, localy = pygame.mouse.get_pos()
                if not op.is_position_occupied(gm,localx, localy):
                    gm.floors.append(Objects(localx, localy,"floor1.png", False, "floor"))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:  
                localx, localy = pygame.mouse.get_pos()
                x, y = localx // 48, localy // 48
                op.delete(x,y,gm)

    #управление фоном
    screenSize = screen.get_size()
    background = pygame.transform.scale(background,screenSize)
    screen.blit(background,(0,0))
    
    gm.cycle(screen)

    # Обновляем экран
    pygame.display.flip()

    clock.tick(60)