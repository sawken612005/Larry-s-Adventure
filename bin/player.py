import pygame as pg
from folder_gestion import import_folder

class Player(pg.sprite.Sprite):
    def __init__(self,pos,screen, create_jump_particles):
        super().__init__()
        self.character_assets()
        self.animation_speed = 0.10
        self.frame_index = 0
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.status = 'idle'

        self.run_particles = import_folder(self.character_path+'/particles/run')
        self.particles_frame = 0
        self.particles_animation_speed = 0.15
        self.screen = screen
        self.create_jump_particles = create_jump_particles

        self.direction = pg.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -18

        self.jump_limitation = 1
        self.face_direction = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_right = False
        self.on_left = False

    def character_assets(self):
        self.character_path = 'graphics/character/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():
            full_path = self.character_path + animation
            self.animations[animation] = import_folder(full_path)

    def particles_run_animation(self):
        if self.status == 'run' and self.on_ground:
            self.particles_frame += self.particles_animation_speed
            if self.particles_frame >= len(self.run_particles):
                self.particles_frame = 0

            run_particle = self.run_particles[int(self.particles_frame)]

            pos = self.rect.bottomleft
            player_sprite_size_x = self.image.get_size()[0]
            if self.face_direction:
                self.screen.blit(run_particle,(pos[0]-10,pos[1]-11))
            else:
                self.screen.blit(pg.transform.flip(run_particle,True,False),(pos[0]+player_sprite_size_x,pos[1]-11))

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

        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def keyboard_mouvement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            self.direction.x = 1
            self.face_direction = True
        elif keys[pg.K_LEFT]:
            self.direction.x  = -1
            self.face_direction = False
        else:
            self.direction.x = 0
            
        if (keys[pg.K_SPACE] or keys[pg.K_UP]) and self.jump_limitation == 1:
            self.jump()
            self.jump_limitation = 0
            self.on_ground = False
            self.create_jump_particles(self.rect.midbottom)

        if self.on_ground:
            self.jump_limitation = 1
        else:
            self.jump_limitation = 0

    def update(self):
        self.keyboard_mouvement()
        self.player_status()
        self.player_animation()
        self.particles_run_animation()
        