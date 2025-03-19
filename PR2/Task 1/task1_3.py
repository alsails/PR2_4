import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Погонина М.В. Упражнение 1")
screen.fill('white')

width, height = screen.get_size()
center = (width // 2, height // 2)



pygame.display.flip()

# Цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
