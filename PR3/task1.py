import pygame
import time

pygame.init()

WINDOWS_SIZE = (800, 600)
BACKGROUND = 'PR3/background.jpg'
SPEED = 0
SDVIG = 0

screen = pygame.display.set_mode(WINDOWS_SIZE)
pygame.display.set_caption("Погонина М.В. Упражнение 1")

img = pygame.image.load(BACKGROUND)
background_img = pygame.transform.scale(img, WINDOWS_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                SPEED = -5
            elif event.key == pygame.K_RIGHT:
                SPEED = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                SPEED = 0

    SDVIG = (SDVIG + SPEED) % WINDOWS_SIZE[0]

    screen.blit(background_img, (SDVIG - WINDOWS_SIZE[0], 0))
    screen.blit(background_img, (SDVIG, 0))

    pygame.display.update()
    time.sleep(0.02)
