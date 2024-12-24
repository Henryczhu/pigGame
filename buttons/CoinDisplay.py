import math
import pygame


class CoinDisplay(pygame.sprite.Sprite):
    def __init__(self, win_width, win_height):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('../res/coin.png').convert_alpha()
        rect = pygame.Rect(0, 0, 16, 16)
        self.image = img.subsurface(rect)
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.win_width = win_width
        self.win_height = win_height
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        self.resize(win_width, win_height)

    def render(self, screen, len_money):
        self.x = self.win_width * (0.97 - (0.0112 * len_money))
        self.rect.center = [self.x, self.y]
        image = pygame.transform.scale(self.image, (self.win_width / 40, self.win_height / 22.5))
        screen.blit(image, self.rect.center)

    def resize(self, win_width, win_height):
        self.y = win_height / 33.75
        self.rect.center = [self.x, self.y]
        self.win_width = win_width
        self.win_height = win_height






