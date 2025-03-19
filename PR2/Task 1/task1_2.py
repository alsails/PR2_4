import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Погонина М.В. Упражнение 1")


def draw_house(screen, width, height):
    screen.fill('white')

    center = (width // 2, height // 2)

    top_peak = center

    # Размеры дома
    house_width, house_height = 300, 200
    roof_height = 120

    bottom_offset = height - 20 - (top_peak[1] + roof_height + house_height)

    # Координаты углов
    left_corner = (top_peak[0] - house_width // 2,
                   top_peak[1] + roof_height + bottom_offset)
    right_corner = (top_peak[0] + house_width // 2,
                    top_peak[1] + roof_height + bottom_offset)
    bottom_left = (left_corner[0], left_corner[1] + house_height)
    bottom_right = (right_corner[0], right_corner[1] + house_height)

    # Линии крыши
    pygame.draw.line(screen, (0, 0, 0), top_peak, left_corner, 3)
    pygame.draw.line(screen, (0, 0, 0), top_peak, right_corner, 3)
    pygame.draw.line(screen, (0, 0, 0), left_corner, right_corner, 3)

    # Линии стен
    pygame.draw.line(screen, (0, 0, 0), left_corner, bottom_left, 3)
    pygame.draw.line(screen, (0, 0, 0), right_corner, bottom_right, 3)
    pygame.draw.line(screen, (0, 0, 0), bottom_left, bottom_right, 3)

    # Линии двери
    door_width, door_height = 90, 120
    door_x = bottom_left[0] + (house_width // 2) - (door_width // 2)
    door_y = bottom_left[1] - door_height
    pygame.draw.line(screen, (0, 0, 0), (door_x, door_y),
                     (door_x, bottom_left[1]), 3)
    pygame.draw.line(screen, (0, 0, 0), (door_x + door_width,
                     door_y), (door_x + door_width, bottom_left[1]), 3)
    pygame.draw.line(screen, (0, 0, 0), (door_x, door_y),
                     (door_x + door_width, door_y), 3)

    # Линии окна
    window_size = 50
    window_x = bottom_left[0] + (house_width // 4) - (window_size // 2)
    window_y = bottom_left[1] - house_height // 2 - (window_size // 2)
    pygame.draw.line(screen, (0, 0, 0), (window_x, window_y),
                     (window_x + window_size, window_y), 3)
    pygame.draw.line(screen, (0, 0, 0), (window_x, window_y + window_size),
                     (window_x + window_size, window_y + window_size), 3)
    pygame.draw.line(screen, (0, 0, 0), (window_x, window_y),
                     (window_x, window_y + window_size), 3)
    pygame.draw.line(screen, (0, 0, 0), (window_x + window_size, window_y),
                     (window_x + window_size, window_y + window_size), 3)

    # Перекладины окна
    pygame.draw.line(screen, (0, 0, 0),
                     (window_x, window_y + window_size // 2),
                     (window_x + window_size, window_y + window_size // 2), 3)
    pygame.draw.line(screen, (0, 0, 0),
                     (window_x + window_size // 2, window_y),
                     (window_x + window_size // 2, window_y + window_size), 3)


running = True
while running:
    width, height = screen.get_size()
    draw_house(screen, width, height)  # Вызов функции для отрисовки домика

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h),
                                             pygame.RESIZABLE)

    pygame.display.flip()  # Обновление экрана

pygame.quit()
