import pygame as pg

class Hero(pg.sprite.Sprite):

  def __init__(self, width, height, windowWidth, windowHeight, screen):
      super().__init__()
      self.width = width
      self.height = height
      self.image = pg.transform.scale(pg.image.load("Coleta.png"), (self.width, self.height))
      self.vel_X = 1.8
      self.windowWidth = windowWidth
      self.windowHeight = windowHeight
      self.x = windowWidth/2 - width/2
      self.y = 511
      self.screen = screen
      self.direction = -1
      #self.life = 3
      self.rect = self.image.get_rect()
      self.time = 10

  #Cria o desenho do Hero
  def draw(self):
      self.screen.blit(self.image, (self.x, self.y))

  #atualiza o herói na tela
  def update(self, all_sprites, time):
      comandos = pg.key.get_pressed()
      if comandos[pg.K_RIGHT] and self.x < self.windowWidth-self.width:
          self.x += self.vel_X
          if self.direction== -1:
              self.image = pg.transform.flip(self.image, True, False)
          self.direction = 1
      if comandos[pg.K_LEFT] and self.x > 0:
          self.x -= self.vel_X
          if self.direction == 1:
              self.image = pg.transform.flip(self.image, True, False)
          self.direction = -1
      self.rect.topleft = (self.x, self.y)