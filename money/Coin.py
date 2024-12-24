import math
import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, win_width, win_height, images, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('../res/coin.png').convert_alpha()
        self.image = img
        self.coins = images
        self.win_width = win_width
        self.win_height = win_height
        self.rect = self.coins[0].get_rect()
        self.x = x
        self.y = y
        self.rect.center = [self.x, self.y]
        self.aniFrame = 0


    def update(self, tick, tx, ty):
        speed = self.win_width / 96
        if self.x < tx:
            if self.x + speed > tx:
                self.x += tx - self.x
            else:
                self.x += speed
        elif self.x > tx:
            if self.x - speed < tx:
                self.x += tx - self.x
            else:
                self.x -= speed
        elif self.y > ty:
            if self.y - speed < ty:
                self.y += ty - self.y
            else:
                self.y -= speed
        elif self.y < ty:
            if self.y + speed > ty:
                self.y += ty - self.y
            else:
                self.y += speed
        if abs(self.x - tx) < 5 and abs(self.y - ty) < 5:
            return True
        self.rect.center = [self.x, self.y]
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






