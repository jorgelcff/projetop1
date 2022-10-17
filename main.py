import pygame as pg
from hero import *

pg.init()

largura, altura = 1080, 720
tela = pg.display.set_mode((largura,altura))
pg.display.set_caption('Dragão de Nome Impronunciável')
background = pg.image.load("./background.jpg")
#Aqui criamos a tela


hero = Hero(110,110, largura, altura, tela)
bala = pg.sprite.Group()
tempo = pg.time.get_ticks()

while True:

  #Aqui checamos se o usuario clicou no X para fechar o jogo
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit()

  hero.draw()

  pg.display.update()
  hero.update(bala, tempo)

  tela.blit(background, (0, 0))

