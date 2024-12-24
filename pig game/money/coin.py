import math
import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, win_width, win_height):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('../res/coin.png').convert_alpha()
        self.image = img
        self.coins = []
        self.loadRects()
        self.rect = self.coins[0].get_rect()
        self.win_width = win_width
        self.win_height = win_height
        self.x = self.win_width / 2
        self.y = self.win_height / 2
        self.rect.center = [self.x, self.y]
        self.aniFrame = 0

    def loadRects(self):
        for col in range(5):
            rect = pygame.Rect(col * 16, 0, 16, 16)
            img = self.image.subsurface(rect)
            self.coins.append(img)

    def update(self, tick):
        if tick % 10 == 0:
            self.aniFrame += 1
            if self.aniFrame > 3:
                self.aniFrame = 0

    def render(self, screen):
        img = pygame.transform.scale(self.coins[self.aniFrame], (self.win_width / 60, self.win_height / 33.75))
        screen.blit(img, self.rect.center)

    def resize(self, win_width, win_height):
        self.x *= (win_width / self.win_width)
        self.y *= (win_height / self.win_height)
        self.rect.center = [self.x, self.y]
        self.win_width = win_width
        self.win_height = win_height






