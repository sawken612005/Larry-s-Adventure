import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, size, surface):
        super().__init__()
        self.display = surface
        # self.image = pg.image.load("graphics\\terrain\\tiles_pat.png").convert_alpha()
        # self.display.blit(self.image,pos)
        self.image = pg.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,mouvement):
        self.rect.x += mouvement[0]
        self.rect.y += mouvement[1]