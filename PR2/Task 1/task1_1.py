import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Погонина М.В. Упражненеи 1")
screen.fill('white')

width, height = screen.get_size()
center = (width // 2, height // 2)

center_width, center_height = 300, 200
center_x = center[0] - center_width // 2
center_y = center[1] - center_height // 2

# Третья четверть
circle_pos = (width // 4, height * 3 // 4)
pygame.draw.circle(screen, "red", circle_pos, 100, 0)
pygame.draw.circle(screen, "black", circle_pos, 100, 15)
pygame.draw.circle(screen, "red", center, 100)

pygame.draw.rect(screen, 'blue',
                 (center_x, center_y, center_width, center_height), 4)

for _ in range(5):
    random_width = random.randint(50, 150)
    random_height = random.randint(50, 150)
    random_x = random.randint(0, width - random_width)
    random_y = random.randint(0, height - random_height)
    random_color = [random.randint(0, 255) for _ in range(3)]
    pygame.draw.rect(screen, random_color,
                     (random_x, random_y, random_width, random_height))

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
