import pygame as pg
from settings import *

import random

class Player(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(WHITE)
        player_image = pg.image.load('British spitfire.png')
        player_xs = pg.transform.scale(player_image, (50, 50))
        self.image = player_xs
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH//2
        self.rect.y = HEIGHT

        self.change_x = 0
        self.change_y = 0


    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        keys = pg.key.get_pressed()
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            self.change_x = 5
        elif keys[pg.K_LEFT]:
            self.change_x = -5
        else:
            self.change_x = 0

        if keys[pg.K_DOWN]:
            self.change_y = 5
        elif keys[pg.K_UP]:
            self.change_y = -5
        else:
            self.change_y = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        colors = [RED, GREEN, ORANGE, YELLOW, BLUE]
        random_index = random.randrange(0,len(colors))
        self.randomcolor = colors[random_index]
        enemy_image = pg.image.load('german fighter.png')
        enemy_xs1 = pg.transform.scale(enemy_image, (50, 50))
        enemy_xs = pg.transform.rotate(enemy_xs1, 180)
        self.image = enemy_xs
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, WIDTH-30)
        self.rect.centery = random.randint(-100, -50)

        self.change_x = 0
        self.change_y = 0

        self.y_velo = random.randint(4, 8)

    def update(self):
        self.rect.y += self.y_velo

        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-100, -50)
            self.rect.centerx = random.randint(0, WIDTH - 30)


class Bullet(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 20))
        self.image.fill (WHITE)
        bullet_image = pg.image.load('lasershot.png')
        laser_xs1 = pg.transform.scale(bullet_image, (10,25))
        laser_xs = pg.transform.rotate(laser_xs1, 180)
        self.image = laser_xs
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.y_velo = -10
    def update(self):

        self.rect.y += self.y_velo
        if self.rect.bottom < 0:
            self.kill()

