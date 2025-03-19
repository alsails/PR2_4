import pygame

pygame.init()

WINDOWS_SIZE = (800, 600)
BACKGROUND = 'PR3/background.jpg'
PLAYER_IMG = 'PR3/hero.png'

SPEED = 0
SDVIG = 0

screen = pygame.display.set_mode(WINDOWS_SIZE)
pygame.display.set_caption("Погонина М.В. Упражнение 2")

img = pygame.image.load(BACKGROUND)
background_img = pygame.transform.scale(img, WINDOWS_SIZE)


class Player(pygame.sprite.Sprite):
    def __init__(self, filename, hero_x=100, hero_y=210, x_speed=0, y_speed=0):
        super().__init__()
        self.image_load = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image_load, (90, 150))
        self.rect = self.image.get_rect()
        self.rect.x = hero_x
        self.rect.y = hero_y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        # Движение спрайта
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.x < 10:
            self.rect.x = 10
        if self.rect.right > WINDOWS_SIZE[0] - 10:
            self.rect.right = WINDOWS_SIZE[0] - 10


player = Player(PLAYER_IMG)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_speed = -5
            elif event.key == pygame.K_RIGHT:
                player.x_speed = 5
            elif event.key == pygame.K_UP:
                player.y_speed = -5
            elif event.key == pygame.K_DOWN:
                player.y_speed = 5

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.x_speed = 0
                SPEED = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player.y_speed = 0

    # Движение фона, когда персонаж упирается в границы окна
    if player.rect.left <= 10:
        SPEED = 5 if player.x_speed < 0 else 0
    elif player.rect.right >= WINDOWS_SIZE[0] - 10:
        SPEED = -5 if player.x_speed > 0 else 0
    else:
        SPEED = 0

    # Сдвиг фона
    SDVIG = (SDVIG + SPEED) % WINDOWS_SIZE[0]
    screen.blit(background_img, (SDVIG - WINDOWS_SIZE[0], 0))
    screen.blit(background_img, (SDVIG, 0))

    # Обновление игрока
    player.update()

    # Отрисовка игрока
    screen.blit(player.image, player.rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
