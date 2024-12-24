import random
import pygame
import tiles.Tile as Tile


class TileManager:
    def __init__(self, win_width, win_height):
        self.win_width = win_width
        self.win_height = win_height
        self.images = [[], [], [], [], []]
        self.tiles = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        self.loadImages()
        self.createTiles()
        self.spawn_rate = 20
        self.special_tiles = random.choices(
            population=[1, 2, 3, 4, 5, 6],
            weights=[0, 0.1, 0.4, 0, 0.1, 0.4],
            k=10
        )

    def update(self, tick):
        if tick % self.spawn_rate == 0:
            if random.randint(0, 5) == 0:
                type = random.choice(self.special_tiles)
                randomTile = self.tiles[random.randint(0, 17)][random.randint(0, 31)]
                if randomTile.getType() == 0:
                    randomTile.setType(type)
                    return randomTile
        return None



    def render(self, screen):
        for row in range(18):
            for col in range(32):
                self.tiles[row][col].render(screen)

    def loadImages(self):
        self.images[0].append(pygame.image.load('../res/GRASS TILE - DAY.png').convert())
        for i in range(1, 7):
            self.images[0].append(pygame.image.load('../res/GRASS DETAIL ' + str(i) + ' - DAY.png').convert())
        self.images[1].append(pygame.image.load('../res/GRASS TILE - NIGHT.png').convert())
        for i in range(1, 7):
            self.images[1].append(pygame.image.load('../res/GRASS DETAIL ' + str(i) + ' - NIGHT.png').convert())
        self.images[2].append(pygame.image.load('../res/GROUND TILE - DAY.png').convert())
        for i in range(1, 6):
            self.images[2].append(pygame.image.load('../res/GROUND DETAIL ' + str(i) + ' - DAY.png').convert())
        self.images[0].append(pygame.image.load('../res/GROUND TILE - NIGHT.png').convert())
        for i in range(1, 6):
            self.images[3].append(pygame.image.load('../res/GROUND DETAIL ' + str(i) + ' - NIGHT.png').convert())
        for i in range(1, 3):
            self.images[4].append(pygame.image.load('../res/FENCE ' + str(i) + ' - DAY.png').convert())
            self.images[4].append(pygame.image.load('../res/FENCE ' + str(i) + ' - NIGHT.png').convert())

    def createTiles(self):
        for row in range(18):
            for col in range(32):
                img_col = 0
                self.tiles[row].append(Tile.Tile(self.images, row, col, self.win_width, self.win_height, 0, img_col))

    def resize(self, win_width, win_height):
        for row in range(18):
            for col in range(32):
                self.tiles[row][col].resize(win_width / 32, win_height / 18)

    def harvest(self, tile):
        tile.setType(0)