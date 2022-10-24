import pygame as pg
from random import randint
from hero import *

import pygame.sprite


class Spell(pg.sprite.Sprite):
    def __init__(self, width, posX, posY, screenH, screenW, screen):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/escudoradiante.png'))
        self.sprites.append(pygame.image.load('sprites/martelodeguerra.png'))
        self.sprites.append(pygame.image.load('sprites/espiritoguardiao.png'))
        self.sprites.append(pygame.image.load('sprites/laminasolar.png'))
        self.sprites.append(pygame.image.load('sprites/soardiabolico.png'))
        self.sprites.append(pygame.image.load('sprites/runasexplosivas.png'))
        self.actually = 0
        self.image = self.sprites[self.actually]
        self.screenW = screenW
        self.width = width
        self.posX = posX
        self.posY = posY
        self.screenH = screenH
        self.screen = screen
        self.vel_Y = 0.5
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
    def update(self, posY, screenH):
        if self.posY>= self.screenH:
            self.posY= 0
        self.posY += self.vel_Y

    def draw_shield(self):
        self.actually= 0
        self.screen.blit(self.image, (self.posX, self.posY))
    def draw_axe(self):
        self.actually = 1
        self.screen.blit(self.image, (self.posX, self.posY))

    def draw_runes(self):
        self.actually = 2
        self.screen.blit(self.image, (self.posX, self.posY))

    def draw_sound(self):
        self.actually = 3
        self.screen.blit(self.image, (self.posX, self.posY))

    def draw_spirit(self):
        self.actually = 4
        self.screen.blit(self.image, (self.posX, self.posY))

    def draw_solar(self):
        self.actually = 5
        self.screen.blit(self.image, (self.posX, self.posY))