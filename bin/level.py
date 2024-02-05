import pygame as pg
from tiles import Tile
from settings import tile_size, screen_width, screen_height
from player import Player
from particles import Particle
from menu import menu_display

class Game:
    def __init__(self,level_data,screen):
        self.screen = screen
        self.setup_level(level_data)
        self.world_mouvement = pg.math.Vector2(0,0)
        self.current_x = 0

        self.menu_activate = False

        self.particles_effects = pg.sprite.GroupSingle()

    def menu_settings(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE] and self.menu_activate == False:
            self.menu_activate = True
        elif keys[pg.K_ESCAPE] and self.menu_activate == True:
            self.menu_activate = False

    def create_jump_particles(self,pos):
        jump_particle_sprite = Particle((pos[0],pos[1]-15),'jump')
        self.particles_effects.add(jump_particle_sprite)

    def setup_level(self,layout):
        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x,y),tile_size,self.screen)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y),self.screen,self.create_jump_particles)
                    self.player.add(player_sprite)

    def camera(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x
        direction_y = player.direction.y

        if player_x < screen_width/3 and direction_x < 0:
            self.world_mouvement[0] = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width/3) and direction_x > 0:
            self.world_mouvement[0] = -8
            player.speed = 0
        else:
            self.world_mouvement[0] = 0
            player.speed = 8       

        # if player_y < screen_height/3 and direction_y < 0:
        #     # self.world_mouvement[1] = -direction_y
        #     # self.world_mouvement[1] -= 0.8=
        #     player.direction.y = 0
        # elif player_y > screen_height-(screen_height/3) and direction_y > 0 :
        #     self.world_mouvement[1] = -direction_y
        # else:
        #     self.world_mouvement[1] = 0

    def horizontal_player_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left                   
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_player_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 0.1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0.1:
            player.on_ceiling = False

    def run(self):
        if self.menu_activate == False:
            self.screen.fill('black')
            self.particles_effects.update(self.world_mouvement)
            self.particles_effects.draw(self.screen)
        
            self.tiles.update(self.world_mouvement)
            self.tiles.draw(self.screen)

            self.player.update()
            self.horizontal_player_collision()
            self.vertical_player_collision()
            self.player.draw(self.screen)

            self.camera()
        else:
            menu_display()
        self.menu_settings()