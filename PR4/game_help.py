import pygame
from constants import *


class Help():
    def __init__(self, costumes):
        big_font = pygame.font.Font(None, 64)
        self.small_font = pygame.font.Font(None, 36)

        text1 = big_font.render(" Управление: ", 1, C_LIGHT)
        text2 = self.small_font.render(
            " Влево: 'a' или стрелка влево ", 1, C_LIGHT)
        text3 = self.small_font.render(
            " Вправо: 'd' или стрелка вправо ", 1, C_LIGHT)
        text4 = self.small_font.render(
            " Прыжок: 'w' или стрелка вверх ", 1, C_LIGHT)
        text5 = self.small_font.render(" Выстрел: пробел ", 1, C_LIGHT)
        text6 = self.small_font.render(
            " Музыка вкл/выкл: 'm', громче: 'u', тише: 'j' ", 1, C_LIGHT)
        text7 = self.small_font.render(
            " Подсказка вкл/выкл (игра на паузе): 'h' ", 1, C_LIGHT)

        img = pygame.Surface([win_width, win_height])
        img.fill(C_DARK)
        img.set_alpha(200)

        # Добавляем изображения героя и врага:
        hero_img = costumes[0]
        enemy_img = costumes[1]

        img.blit(hero_img, (20, win_height - hero_img.get_height() - 20))
        img.blit(enemy_img, (win_width - enemy_img.get_width() - 20,
                     win_height - enemy_img.get_height() - 20))

        # Центрирование текста
        h = round(win_height / 8)
        step = 70
        for i, text in enumerate([text1, text2, text3, text4, text5, text6, text7]):
            x = (win_width - text.get_width()) // 2
            img.blit(text, (x, h + i * step))

        self.img = img

        # постоянная строка (жизни/очки):
        self.text_points = self.small_font.render("Очков:   ", 1, C_DARK)
        self.text_points_w = self.text_points.get_rect().width
        self.text_lives = self.small_font.render("Жизней:   ", 1, C_DARK)
        self.text_lives_w = self.text_lives.get_rect().width
        self.text_help = self.small_font.render(
            "Пауза/подсказка: 'h'", 1, C_DARK)
        self.text_height = self.text_help.get_rect().height

    def line(self, points=0, lives=1):
        tab = 50
        img = pygame.Surface([win_width, self.text_height], pygame.SRCALPHA)
        img.blit(self.text_lives, (0, 0))
        text = self.small_font.render(str(lives), 1, C_LIGHT)
        img.blit(text, (self.text_lives_w, 0))
        img.blit(self.text_points, (self.text_lives_w + tab, 0))
        text = self.small_font.render(str(points), 1, C_LIGHT)
        img.blit(text, (self.text_lives_w + tab + self.text_points_w, 0))
        img.blit(self.text_help, (self.text_lives_w +
                 tab + self.text_points_w + tab, 0))
        return img
