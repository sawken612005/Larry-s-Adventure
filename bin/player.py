import pygame as pg
from folder_gestion import import_folder
class Player(pg.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.character_assets()
        self.animation_speed = 0.10
        self.frame_index = 0
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pg.math.Vector2(0,0)
        self.speed = 1
        self.gravity = 0.8
        self.jump_speed = -16

        self.status = 'idle'
        self.face_direction = True

    def character_assets(self):
        character_path = 'graphics/character/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            print(full_path)
            self.animations[animation] = import_folder(full_path)

    def player_status(self):

        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def player_animation(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.face_direction == True:
            self.image = image
        else:
            flipped_image = pg.transform.flip(image,True,False)
            self.image = flipped_image


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def movement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            self.direction.x = 1
            self.face_direction = True
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
            self.face_direction = False
        else:
            self.direction.x = 0

        if keys[pg.K_SPACE] or keys[pg.K_UP]:
            self.jump()

        self.rect.x += self.direction.x * self.speed

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.movement()
        self.player_status()
        self.player_animation()