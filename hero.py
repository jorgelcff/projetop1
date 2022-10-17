import pygame as pg

class Hero(pg.sprite.Sprite):

  def __init__(self, width, height, windowWidth, windowHeight, tela):
      super().__init__()
      self.width = width
      self.height = height
      self.image = pg.transform.scale(pg.image.load("./hero.webp"), (self.width, self.height))
      self.velocidadeX = 3
      self.windowWidth = windowWidth
      self.windowHeight = windowHeight
      self.x = windowWidth/2 - width/2
      self.y = 610
      self.tela = tela
      self.direcao = -1
      self.life = 3
      self.rect = self.image.get_rect()
      self.tempoAnterior = 0
      self.intervalo = 500
      self.tempo = 10

  #Cria o desenho do Hero
  def draw(self):
      self.tela.blit(self.image, (self.x, self.y))

  #atualiza o herói na tela
  def update(self, bala, tempo):
      comandos = pg.key.get_pressed()
      if comandos[pg.K_RIGHT] and self.x < self.windowWidth-self.width:
          self.x += self.velocidadeX
          if self.direcao == -1:
              self.image = pg.transform.flip(self.image, True, False)
          self.direcao = 1
      if comandos[pg.K_LEFT] and self.x > 0:
          self.x -= self.velocidadeX
          if self.direcao == 1:
              self.image = pg.transform.flip(self.image, True, False)
          self.direcao = -1
      self.rect.topleft = (self.x, self.y)