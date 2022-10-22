import pygame as pg
import random
from random import randint

class General(pg.sprite.Sprite):
    def check_collision(sprite: pg.sprite.Sprite, group: pg.sprite.Group):
        """
        parametro da sprite: Sprite que vai ser usada para checar colisões
        parametro do grupo: grupo de sprites que vai ser checado
        Essa função checa se uma sprite de um grupo colide com uma outra sprite.
        """
        if pg.sprite.spritecollide(sprite, group, dokill=True):
            return True
        return False

    def is_dead(self):
        #Essa função checa se a vida do personagem chegou a zero
        if self.life <1:
            return True
        else:
            return False


# Checa se o inimigo perdeu vida/morreu
class Enemy(General):
    def enemy_loss(inimigo):
        inimigo.life -= 1
        if inimigo.life < 1:
            inimigo.kill()


class Player(General):
    # Checa se o pikachu vai ganhar vida
    def player_gain(player):
        if player.life < 3:
            player.life += 1

    # Checa se o pikachu perdeu vida/morreu
    def player_loss(player):
        player.life -= 1
        if player.life < 1:
            return True

    # Buffa o pikachu
    def player_buff(player):
        player.velocidadeX = 5
        player.intervalo = 250

    # Nerfa o pikachu
    def player_nerf(player):
        player.velocidadeX = 3
        player.intervalo = 500

class Zubat(pg.sprite.Sprite):
    # Classe responsável por criar o inimigo zubat
    def __init__(self, width, height, windowWidth, windowHeight, tela):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pg.transform.scale(pg.image.load('./sword.png'), (self.width, self.height))
        self.velocidadeY = 2
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.x = randint(0, self.windowWidth - self.width)
        self.y = -height
        self.tela = tela
        self.rect = self.image.get_rect()
        self.life = 1

    def draw(self):
        self.tela.blit(self.image, (self.x, self.y))

    # Atualiza o zubat na tela
    def update(self, bullet, berries, pikachu, item, sound):

        if General.check_collision(self, bullet):
            Enemy.enemy_loss(self)
            sound.play()


        # movimenta o pokemon de acordo com a velocidade.
        self.y += self.velocidadeY
        if self.y >= self.windowHeight - self.height:
            self.kill()
            if Player.player_loss(pikachu):
                pg.quit()
        self.rect.topleft = (self.x, self.y)