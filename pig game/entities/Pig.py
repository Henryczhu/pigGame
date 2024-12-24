import math
import pygame


class Pig(pygame.sprite.Sprite):
    def __init__(self, win_width, win_height):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('../res/pig.png').convert_alpha()
        self.image = img
        self.pigs = []
        self.loadRects()
        self.dir = 0
        self.rect = self.pigs[0][0].get_rect()
        self.win_width = win_width
        self.win_height = win_height
        self.x = self.win_width / 2
        self.y = self.win_height / 2
        self.rect.center = [self.x, self.y]
        self.targeting = False
        self.target = None
        self.aniFrame = 0

    def loadRects(self):
        imgRow = []
        for col in range(4):
            rect = pygame.Rect(col * 64, 0, 64, 64)
            img = self.image.subsurface(rect)
            imgRow.append(img)
        self.pigs.append(imgRow)
        imgRow = []
        for col in range(4):
            rect = pygame.Rect(col * 64, 128, 64, 64)
            img = self.image.subsurface(rect)
            imgRow.append(img)
        self.pigs.append(imgRow)
        imgRow = []
        for col in range(4):
            rect = pygame.Rect(col * 64, 64, 64, 64)
            img = self.image.subsurface(rect)
            imgRow.append(img)
        self.pigs.append(imgRow)
        imgRow = []
        for col in range(4):
            rect = pygame.Rect(col * 64, 64, 64, 64)
            img = self.image.subsurface(rect)
            img = pygame.transform.flip(img, True, False)
            imgRow.append(img)
        self.pigs.append(imgRow)

    def checkClosest(self, collectables):
        if len(collectables) > 0:
            distances = []
            for coll in collectables:
                dx = abs(coll.x - self.x)
                dy = abs(coll.y - self.y)
                distances.append(math.sqrt(dx ** 2 + dy ** 2))
            smallDis = -1
            smallI = 0
            for i in range(len(distances)):
                if smallDis > distances[i] or smallDis == -1:
                    smallDis = distances[i]
                    smallI = i
            self.targeting = True
            self.target = collectables[smallI]
            if smallDis < 10:
                return smallI
        return None


    def update(self):
        if self.targeting:
            self.aniFrame += 0.1
            if self.aniFrame > 3:
                self.aniFrame = 0
            tx = self.target.x
            ty = self.target.y
            dx = tx - self.x
            dy = ty - self.y
            if abs(dx) > 5:
                if dx > 0:
                    self.dir = 2
                else:
                    self.dir = 3
                self.x += dx / abs(dx) * 5
            elif abs(dy) > 5:
                if dy < 0:
                    self.dir = 1
                else:
                    self.dir = 0
                self.y += dy / abs(dy) * 5
            self.rect.center = [self.x, self.y]


    def render(self, screen):
        img = pygame.transform.scale(self.pigs[self.dir][int(self.aniFrame)], (self.win_width / 30, self.win_height / 16.875))
        screen.blit(img, self.rect.center)

    def resize(self, win_width, win_height):
        self.x *= (win_width / self.win_width)
        self.y *= (win_height / self.win_height)
        self.rect.center = [self.x, self.y]
        self.win_width = win_width
        self.win_height = win_height






