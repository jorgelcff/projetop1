import pygame as pg
from random import randint
from hero import *

import pygame.sprite


class Damage(pg.sprite.Sprite):
    def __init__(self, posX, posY, screenH, screenW, screen, actually, name, decreaseW, decreaseH, vel_Y):
        """
        :rtype: object
        """
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.sprites = []
        self.sprites.append(pygame.image.load('nerfs/breathe_weakening.png'))
        self.sprites.append(pygame.image.load('nerfs/flaming_blast.png'))
        self.sprites.append(pygame.image.load('nerfs/intimidating_curtain.png'))
        self.sprites.append(pygame.image.load('nerfs/turbulence.png'))
        self.actually = actually
        self.image = self.sprites[self.actually]
        self.screenW = screenW
        self.posX = posX
        self.posY = posY
        self.screenH = screenH
        self.screen = screen
        self.decreaseW = decreaseW
        self.decreaseH = decreaseH
        self.vel_Y = vel_Y
        self.image = pg.transform.scale(self.image, (self.decreaseW/3, self.decreaseH/3))
        self.rect = self.image.get_rect()
        self.rect.topleft = 5, 5
        self.colisions= [ ]

    def update(self, posY, screenH):
        if self.posY>= self.screenH:
            self.posY = 250
            self.posX = randint(20, 980)
        self.posY += self.vel_Y
        self.rect.topleft = self.posX, self.posY

    def draw(self):
        self.image = self.sprites[self.actually]
        self.screen.blit(self.image, (self.posX, self.posY))

    def checkcolision(self):
        self.posY = 250
        self.posX = randint(20, 980)
