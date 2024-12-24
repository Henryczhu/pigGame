import random

import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, images, row, col, win_width, win_height, time, type):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.row = row
        self.col = col
        self.time = time
        self.type = type
        self.width = win_width / 32
        self.height = win_height / 18
        self.x = (self.width * self.col)
        self.y = (self.height * self.row)
        self.rect = self.images[self.time][self.type].get_rect()
        self.rect.center = [self.x, self.y]
        self.growth_stage = 0

    def render(self, screen):
        img = pygame.transform.scale(self.images[self.time][self.type], (self.width, self.height))
        screen.blit(img, self.rect.center)

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.x = (self.width * self.col)
        self.y = (self.height * self.row)
        self.rect = self.images[0][0].get_rect()
        self.rect.center = [self.x, self.y]

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type