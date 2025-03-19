import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Погонина М.В. Упражнение 2")
clock = pygame.time.Clock()

width, height = screen.get_size()


def random_color():
    return [random.randint(0, 255) for _ in range(3)]


# Славарь парметров для круга
circle = {'pos': [55, 55], 'radius': 50, 'color': random_color(), 'speed': 5}

# Славарь парметров для треугольника
triangle = {'points': [[5, 355], [115, 355], [55, 270]],
            'color': random_color(), 'speed': 4}

# Славарь парметров для прямоугольника
rect = {'rect': pygame.Rect(5, 545, 110, 50),
        'color': random_color(), 'speed': 3}

running = True
while running:
    screen.fill('white')

    circle['pos'][0] += circle['speed']
    # Условие для изменения напраления движения объекта
    if (
            circle['pos'][0] - circle['radius'] <= 0 or
            circle['pos'][0] + circle['radius'] >= width
    ):
        circle['speed'] *= -1
        circle['color'] = random_color()

    for point in triangle['points']:
        point[0] += triangle['speed']
    xs = [p[0] for p in triangle['points']]
    if min(xs) <= 0 or max(xs) >= width:
        triangle['speed'] *= -1
        triangle['color'] = random_color()

    rect['rect'].x += rect['speed']
    if rect['rect'].left <= 0 or rect['rect'].right >= width:
        rect['speed'] *= -1
        rect['color'] = random_color()

    # Отоброажение фигур
    pygame.draw.circle(screen, circle['color'],
                       circle['pos'], circle['radius'])
    pygame.draw.polygon(screen, triangle['color'], triangle['points'])
    pygame.draw.rect(screen, rect['color'], rect['rect'])

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Проверка попадания на фигуру для смены её цвета
            dx = mouse_x - circle['pos'][0]
            dy = mouse_y - circle['pos'][1]
            if dx*dx + dy*dy <= circle['radius']**2:
                circle['color'] = random_color()

            if pygame.draw.polygon(
                screen, triangle['color'], triangle['points']
            ).collidepoint(event.pos):
                triangle['color'] = random_color()

            if rect['rect'].collidepoint(event.pos):
                rect['color'] = random_color()

    clock.tick(60)

pygame.quit()
