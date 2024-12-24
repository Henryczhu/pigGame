import pygame

import entities.Pig
import money.coin
import tiles.TileManager

pygame.init()


def resizeWin(larger):
    global win_height
    global win_width
    global screen
    if larger:
        if win_width < 2240 and win_height < 1360:
            win_width += 320
            win_height += 180
            resizeAll()
    elif win_width > 320 and win_height > 180:
        win_width -= 320
        win_height -= 180
        resizeAll()
    print(screen.get_rect())


def resizeAll():
    global screen
    pygame.display.quit()
    screen = pygame.display.set_mode((win_width, win_height))
    tileManager.resize(win_width, win_height)
    pig.resize(win_width, win_height)
    coin.resize(win_width, win_height)


win_width = 1920
win_height = 1080
screen = pygame.display.set_mode((win_width, win_height))
FRAME_RATE = 144
clock = pygame.time.Clock()

tileManager = tiles.TileManager.TileManager(win_width, win_height)
collectables = []

pig = entities.Pig.Pig(win_width, win_height)

coin = money.coin.Coin(win_width, win_height)

tick = 0

run = True
while run:
    clock.tick(FRAME_RATE)
    screen.fill((0, 0, 0))

    tick += 1

    coll = tileManager.update(tick)
    if coll:
        collectables.append(coll)
    tileManager.render(screen)

    collide = pig.checkClosest(collectables)
    if collide is not None:
        print(collide)
        tileManager.harvest(collectables[collide])
        del collectables[collide]
    pig.update()
    pig.render(screen)

    coin.update(tick)
    coin.render(screen)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                resizeWin(True)
            if event.key == pygame.K_MINUS:
                resizeWin(False)
                tileManager.resize(win_width, win_height)
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()