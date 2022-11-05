import pygame as pg
from random import randint
from hero import *

import pygame.sprite


class Spell(pg.sprite.Sprite):
    def __init__(self, posX, posY, screenH, screenW, screen, actually, name):
        """

        :rtype: object
        """
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/escudoradiante.png'))
        self.sprites.append(pygame.image.load('sprites/martelodeguerra.png'))
        self.sprites.append(pygame.image.load('sprites/espiritoguardiao.png'))
        self.sprites.append(pygame.image.load('sprites/laminasolar.png'))
        self.sprites.append(pygame.image.load('sprites/soardiabolico.png'))
        self.sprites.append(pygame.image.load('sprites/runasexplosivas.png'))
        self.actually = actually
        self.image = self.sprites[self.actually]
        self.screenW = screenW
        self.posX = posX
        self.posY = posY
        self.screenH = screenH
        self.screen = screen
        self.vel_Y = 0.7
        self.rect = self.image.get_rect()
        self.rect.topleft = 5, 5
        self.colisions= [ ]

    def update(self, posY, screenH):
        if self.posY>= self.screenH:
            self.posY= 0
            self.posX = randint(20, 980)
        self.posY += self.vel_Y
        self.rect.topleft = self.posX, self.posY

    def draw(self):
        self.image = self.sprites[self.actually]
        self.screen.blit(self.image, (self.posX, self.posY))

    def checkcolision(self):
        self.posY = 0
        self.posX = randint(20, 980)
        return True