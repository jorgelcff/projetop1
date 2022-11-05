import pygame as pg

class Lovecraft(pg.sprite.Sprite):

  def __init__(self, width, height, windowWidth, windowHeight, screen, x):
      self.width = width
      self.height = height
      self.image = pg.transform.scale(pg.image.load("Tiamat_from_FFI_Pixel_Remaster_battle_sprite (1).png"), (self.width, self.height))
      self.windowWidth = windowWidth
      self.windowHeight = windowHeight
      self.x = x
      self.y = -50
      self.screen = screen
      self.rect = self.image.get_rect()
      self.rect.topleft= 5, 5

  #Cria o desenho do Hero
  def draw(self):
      self.screen.blit(self.image, (self.x, self.y))

