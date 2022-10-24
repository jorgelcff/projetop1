#imports pygame, random e locals
import pygame as pg
import pygame.font


from hero import*
from atk import*
pg.init()
from random import randint


wight, height = 1080, 600
screen = pg.display.set_mode((wight, height))
pg.display.set_caption('Dragão de Nome Impronunciável')
background = pg.image.load("background.jpg")
#Aqui criamos a tela
x_pos= randint(20, 1000)
y_pos= randint(10, 550)

#frames, objeto protagonista e outros
clock = pg.time.Clock()
hero = Hero(90,90, wight, height, screen) #Criando a partir de classe
probab = 20
hit = pg.sprite.Group()
if probab<=20:
  shield_radiant = Spell(45, x_pos, y_pos, wight, height, screen)
  chosen = "shield"
  probab = randint(1, 110)
elif 55<=probab>20:
  war_axe = Spell(45, x_pos, y_pos, wight, height, screen)
  chosen = "axe"
  probab = randint(1, 110)
elif 75<=probab>55:
  explosive_runes = Spell(45, x_pos, y_pos,wight, height, screen)
  chosen = "runes"
  probab = randint(1, 110)
elif 90<=probab>75:
  sound_devilish= Spell(45, x_pos, y_pos, wight, height, screen)
  chosen = "sound"
  probab = randint(1, 110)
elif 105<=probab>90:
  spirit_guardian= Spell(45, x_pos, y_pos, wight, height, screen)
  chosen = "spirit"
  probab = randint(1, 110)
else:
  solar_blade= Spell(45, x_pos, y_pos, wight, height, screen)
  chosen = "solar"
  probab = randint(1, 110)

all_sprites = pg.sprite.Group()
time = pg.time.get_ticks()
font = pg.font.SysFont('Tempus San ITC', 15, True, False)
atack= " "

#variaveis para posição dos objetos
count_skills = 0
#loop principal
while True:
  #Aqui checamos se o usuario clicou no X para fechar o jogo
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit()

  #iterando o objeto protagonista na tela
  hero.draw()
  if chosen== "shield":
    shield_radiant.draw_shield()
  elif chosen == "axe":
    war_axe.draw_axe()
  elif chosen == "sound":
    sound_devilish.draw_sound()
  elif chosen == "runes":
    explosive_runes.draw_runes()
  elif chosen == "spirit":
    spirit_guardian.draw_spirit()
  else:
    solar_blade.draw_solar()
  skills = f'Ataques: {atack}'
  txt_format = font.render(skills, True, (245, 255, 255))

  '''if colliderect(hero):
    x_pos = randint(40, 600)
    y_pos = 10
    ataques+= "Soar diabólico "
    count_skills += 1
  if count_skills>4:
    pg.quit()
    exit()'''
  collision = pg.sprite.spritecollide(hero, hit, True)
  print(collision)
  pg.display.flip()
  hero.update(all_sprites, time)
  if chosen== "shield":
    shield_radiant.update(y_pos, height)
  elif chosen== "axe":
    war_axe.update(y_pos, height)
  elif chosen == "sound":
    sound_devilish.update(y_pos, height)
  elif chosen == "runes":
    explosive_runes.update(y_pos, height)
  elif chosen == "spirit":
    spirit_guardian.update(y_pos, height)
  elif chosen== "solar":
    solar_blade.update(y_pos, height)

  screen.blit(background, (0, 0))
  screen.blit(txt_format, (500, 40))



