import pygame as pg
from hero import *
pg.init()

largura, altura = 1080, 720
tela = pg.display.set_mode((largura,altura))
pg.display.set_caption('Dragão de Nome Impronunciável')
background = pg.image.load("./background.jpg")
#Aqui criamos a tela

relogio = pg.time.Clock()
hero = Hero(110,110, largura, altura, tela)
bala = pg.sprite.Group()
tempo = pg.time.get_ticks()

x = largura/2 - 20
y = 0
while True:
  #Aqui checamos se o usuario clicou no X para fechar o jogo
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit()

  hero.draw()

  pg.draw.rect(tela, (255, 255, 0), (x, y, 40, 50))
  if y >= altura:
    y=0
  y = y + 1



  pg.display.update()
  hero.update(bala, tempo)

  tela.blit(background, (0, 0))



