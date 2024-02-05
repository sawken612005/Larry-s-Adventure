import pygame as pg, sys
from settings import *
from level import Game


pg.init()
screen = pg.display.set_mode((screen_width,screen_height))
clock = pg.time.Clock()
level = Game(level_map,screen)
# background = pg.image.load("graphics\\terrain\\background.png").convert_alpha()

menu_activate = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # screen.blit(background,(0,0))
    level.run()
    
    pg.display.update()
    clock.tick(60)