import pygame

import entities.Pig
import money.CoinManager
import tiles.TileManager
import buttons.CoinDisplay
import buttons.TextManager

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


def resizeAll():
    global screen
    pygame.display.quit()
    screen = pygame.display.set_mode((win_width, win_height))
    tileManager.resize(win_width, win_height)
    coinManager.resize(win_width, win_height)
    pig.resize(win_width, win_height)
    coinDisplay.resize(win_width, win_height)


win_width = 1920
win_height = 1080
screen = pygame.display.set_mode((win_width, win_height))
FRAME_RATE = 100
clock = pygame.time.Clock()

tileManager = tiles.TileManager.TileManager(win_width, win_height)
collectables = []

coinManager = money.CoinManager.CoinManager(win_width, win_height)

pig = entities.Pig.Pig(win_width, win_height)

coinDisplay = buttons.CoinDisplay.CoinDisplay(win_width, win_height)
textManager = buttons.TextManager.TextManager(win_width, win_height)

tick = 0
money = 0

run = True
while run:
    clock.tick(FRAME_RATE)
    screen.fill((0, 0, 0))
    print(clock.get_fps())

    tick += 1

    coll = tileManager.update(tick)
    if coll:
        collectables.append(coll)
    tileManager.render(screen)

    money += coinManager.update(tick, coinDisplay.x, coinDisplay.y)
    coinManager.render(screen)

    collide = pig.checkClosest(collectables)
    if collide is not None:
        collectables[collide].takeDamage(2)
        if collectables[collide].health <= 0:
            tileManager.harvest(collectables[collide])
            coinManager.createCoin(collectables[collide].x, collectables[collide].y)
            del collectables[collide]
    pig.update()
    pig.render(screen)

    textManager.replaceText(0, money, win_width - (22 * len(str(money))) / (1920 / win_width),
                            win_height * 0.025, win_width, win_height)
    textManager.render(screen)

    coinDisplay.render(screen, len(str(money)))



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                resizeWin(True)
            if event.key == pygame.K_MINUS:
                resizeWin(False)
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()