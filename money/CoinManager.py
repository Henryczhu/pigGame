import random
import pygame
import tiles.Tile as Tile
from money import Coin


class CoinManager:
    def __init__(self, win_width, win_height):
        img = pygame.image.load('../res/coin.png').convert_alpha()
        self.image = img
        self.win_width = win_width
        self.win_height = win_height
        self.images = []
        self.coins = []
        self.loadRects()

    def loadRects(self):
        for col in range(5):
            rect = pygame.Rect(col * 16, 0, 16, 16)
            img = self.image.subsurface(rect)
            self.images.append(img)

    def update(self, tick, tx, ty):
        gained = 0
        delete = []
        for coin in self.coins:
            if coin.update(tick, tx, ty):
                print(coin)
                delete.append(coin)
        for coin in delete:
            gained += 1
            self.coins.remove(coin)
        return gained

    def render(self, screen):
        for coin in self.coins:
            coin.render(screen)

    def resize(self, win_width, win_height):
        self.win_width = win_width
        self.win_height = win_height
        for coin in self.coins:
            coin.resize(self.win_width, self.win_height)

    def createCoin(self, x, y):
        self.coins.append(Coin.Coin(self.win_width, self.win_height, self.images, x, y))