import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Погонина М.В. Упражнение 1")
width, height = screen.get_size()

PLAYER_IMG = 'PR2/hero.png'


def draw_line(screen, width, height):
    screen.fill('white')
    end_pos = (0, 0)

    for _ in range(5):
        if _ == 0:

            start_pos = (random.randint(10, width - 10),
                         random.randint(10, height - 10))
        else:
            start_pos = end_pos

        end_pos = (random.randint(10, width - 10),
                   random.randint(10, height - 10))

        pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 3)


draw_line(screen, width, height)

image = pygame.image.load('PR2/Task 1/hero.png')
scaled_image = pygame.transform.scale(image, (90, 150))

screen.blit(scaled_image, (400, 450))
pygame.display.flip()

# Задержка
pygame.time.delay(1000)
screen.fill('white')
draw_line(screen, width, height)

screen.blit(scaled_image, (100, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
