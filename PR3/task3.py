import pygame
import random

pygame.init()

WINDOWS_SIZE = (800, 600)
BACKGROUND = 'PR3/background.jpg'
PLAYER_IMG = 'PR3/hero.png'
ARROW_IMG = 'PR3/arrow.png'
ENEMY_IMG = 'PR3/enemy.png'

screen = pygame.display.set_mode(WINDOWS_SIZE)
pygame.display.set_caption("Погонина М.В. Упражнение 3")

img = pygame.image.load(BACKGROUND)
background_img = pygame.transform.scale(img, WINDOWS_SIZE)


# спрайты - объекты, которые объекты с изображением, координатами и логикой
# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, hero_x=100, hero_y=210, x_speed=0, y_speed=0):
        super().__init__()
        self.image_load = pygame.image.load(PLAYER_IMG)
        self.image = pygame.transform.scale(self.image_load, (90, 150))
        self.rect = self.image.get_rect()
        self.rect.x = hero_x
        self.rect.y = hero_y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.x < 10:
            self.rect.x = 10
        if self.rect.right > WINDOWS_SIZE[0] - 10:
            self.rect.right = WINDOWS_SIZE[0] - 10
        if self.rect.y < 10:
            self.rect.y = 10
        if self.rect.bottom > WINDOWS_SIZE[1] - 10:
            self.rect.bottom = WINDOWS_SIZE[1] - 10


# Класс стрелы
class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_load = pygame.image.load(ARROW_IMG)
        self.image = pygame.transform.scale(self.image_load, (50, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WINDOWS_SIZE[0]:
            self.kill()


# Класс цели
class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_load = pygame.image.load(ENEMY_IMG)
        self.image = pygame.transform.scale(
            self.image_load, (100, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = random.uniform(-2, 2)  # Плавная скорость
        self.y_speed = random.uniform(-2, 2)

    def update(self):
        # Движение
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Отражение от границ
        if self.rect.left < 0 or self.rect.right > WINDOWS_SIZE[0]:
            self.x_speed = -self.x_speed
        if self.rect.top < 0 or self.rect.bottom > WINDOWS_SIZE[1]:
            self.y_speed = -self.y_speed


player = Player()

# Дополнительные спрайты
sprite1 = Target(random.randint(100, 700), random.randint(100, 500))
sprite2 = Target(random.randint(100, 700), random.randint(100, 500))

# pygame.sprite.Group - группа спрайтов, для неё можно вызывать
# .draw(screen) (нарисовать все на экрне), .update() (обновить все спрайты)
# .add(sprite) (добавить спрайт в группу), .remove(sprite)
# (удалить спрайт из группы), .kill() (удалить спрайт из всех групп)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Группа стрел
arrows = pygame.sprite.Group()

clock = pygame.time.Clock()
running = True

while running:
    screen.blit(background_img, (0, 0))

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
            elif event.key == pygame.K_SPACE:
                # Создание стрелы
                arrow = Arrow(player.rect.right, player.rect.centery)
                all_sprites.add(arrow)
                arrows.add(arrow)

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.x_speed = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player.y_speed = 0

    # Обновление всех спрайтов
    all_sprites.update()

    # Проверка коллизий стрел с дополнительными спрайтами
    for arrow in arrows:
        hit_sprites = pygame.sprite.spritecollide(arrow, all_sprites, False)
        for hit_sprite in hit_sprites:
            # является ли спрайт экземпляром класса Target
            if isinstance(hit_sprite, Target):
                all_sprites.remove(hit_sprite)
                arrow.kill()

    # Отрисовка всех спрайтов
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
