import random
import pygame
import tiles.Tile as Tile
from money import Coin


class TextManager:
    def __init__(self, win_width, win_height):
        self.win_width = win_width
        self.win_height = win_height
        self.font = pygame.font.Font('../res/font.otf', 24)
        self.texts = []
        self.x = []
        self.y = []
        self.addText(0, self.win_width * (1 - 0.012 * 1), 28)

    def render(self, screen):
        for i in range(len(self.texts)):
            screen.blit(self.texts[i], (self.x[i], self.y[i]))

    def addText(self, text, x, y):
        l = len(str(text))
        text = self.font.render(str(text), True, (0, 0, 0))
        text = pygame.transform.scale(text, (22 * l, 48))
        self.texts.append(text)
        self.x.append(x)
        self.y.append(y)

    def replaceText(self, index, text, x, y, win_width, win_height):
        l = len(str(text))
        text = self.font.render(str(text), True, (0, 0, 0))
        text = pygame.transform.scale(text, ((win_width * 0.0115) * l, (win_height * 0.044)))
        self.texts[index] = text
        self.x[index] = x
        self.y[index] = y
