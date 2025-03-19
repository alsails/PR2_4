import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Погонина М.В. Упражнение 1")
screen.fill('white')

width, height = screen.get_size()
center = (width // 2, height // 2)


# Функция отрисовки домика
def draw_house():
    # Домик
    house_width, house_height = 300, 200
    house_x = center[0] - house_width // 2
    house_y = center[1] - house_height // 2

    pygame.draw.rect(screen, (60, 179, 113),
                     (house_x, house_y, house_width, house_height))  # корпус

    # Крыша
    left_corner = (house_x, house_y)
    right_corner = (house_x + house_width, house_y)
    top_peak = (house_x + house_width // 2, house_y - 120)
    pygame.draw.polygon(screen, (83, 128, 134),
                        [left_corner, right_corner, top_peak])  # крыша

    # Дверь
    door_width, door_height = 90, 120
    door_x = house_x + (house_width // 2) - (door_width // 2)
    door_y = house_y + house_height - door_height  # по низу дома
    pygame.draw.rect(screen, (165, 112, 58),
                     (door_x, door_y, door_width, door_height))  # дверь

    # Окошко
    roof_center_x = house_x + house_width // 2
    roof_center_y = house_y - 40
    window_radius = 25
    pygame.draw.circle(screen, (255, 255, 224),
                       (roof_center_x, roof_center_y), window_radius)  # окно

    # Перекладины
    line_color = (0, 0, 0)
    line_width = 3
    pygame.draw.line(screen, line_color,
                     (roof_center_x, roof_center_y - window_radius),
                     (roof_center_x, roof_center_y + window_radius),
                     line_width)
    pygame.draw.line(screen, line_color,
                     (roof_center_x - window_radius, roof_center_y),
                     (roof_center_x + window_radius, roof_center_y),
                     line_width)

    return house_x, house_y, house_width, house_height


house_x, house_y, house_width, house_height = draw_house()

desired_height = 150
image = pygame.image.load('PR2/Task 1/grass.png')
scaled_image = pygame.transform.scale(image, (width, desired_height))

screen.blit(scaled_image, (0, house_y + house_height - 115))
pygame.display.flip()

# Задержка
pygame.time.delay(1000)
screen.fill('white')
draw_house()
screen.blit(scaled_image, (0, house_y + house_height - 50))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
