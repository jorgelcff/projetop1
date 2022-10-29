# imports pygame, random e locals
import pygame as pg
import pygame.font
from hero import *
from atk import *

pg.init()
from random import randint

# Aqui criamos a tela
wight, height = 1080, 600
screen = pg.display.set_mode((wight, height))
pg.display.set_caption('Dragão de Nome Impronunciável')
background = pg.image.load("background.jpg")

# Posições referências
x_pos = randint(20, 1000)
y_pos = 0

# Frames, objetos drops, protagonista e outros
clock = pg.time.Clock()  # Usar para frame
hero = Hero(90, 90, wight, height, screen)  # Criando a partir de classe
hit = pg.sprite.Group()  # Grupo para itens que vão colidir

# Objetos drops
shield_radiant = Spell(45, x_pos, y_pos, wight, height, screen, 0, ' Shield Radiant')
war_axe = Spell(45, x_pos, y_pos, wight, height, screen, 1, ' War Axe')
explosive_runes = Spell(45, x_pos, y_pos, wight, height, screen, 5, ' Explosive Runes')
spirit_guardian = Spell(45, x_pos, y_pos, wight, height, screen, 2, ' Sound Devilish')
sound_devilish = Spell(45, x_pos, y_pos, wight, height, screen, 4, ' Spirit Guardian')
solar_blade = Spell(45, x_pos, y_pos, wight, height, screen, 3, ' Solar Blade')
#testetestetstetstetst cjvjvjdhbcommits

listSpell = [shield_radiant, war_axe, explosive_runes, spirit_guardian, solar_blade, solar_blade]

probab = 8
text = str  # Uso comparativo

all_sprites = pg.sprite.Group()
time = pg.time.get_ticks()
font = pg.font.SysFont('Tempus San ITC', 15, True, False)
atack = " "


def percentage(number_l, number_r, item, name, height=height, y_pos=y_pos, probab=probab, hit=hit):
    if probab <= 20 and name == " Shield Radiant":
        hit.add(item)
        item.draw()
        item.update(y_pos, height)
        if hero.rect.colliderect(item.rect):
            item.checkcolision()
            return name
    elif probab > 20:
        if number_l >= probab > number_r:
            hit.add(item)
            item.draw()
            item.update(y_pos, height)
            if hero.rect.colliderect(item.rect):
                item.checkcolision()
                return name
    else:
        pass


# variaveis para posição dos objetos
count_skills = 0

# loop principal
while True:
    percentage(0, 20, shield_radiant, " Shield Radiant", probab= probab)
    percentage(55, 20, war_axe, " War Axe", probab= probab)
    percentage(75, 55, explosive_runes, " Explosive Runes", probab= probab)
    percentage(90, 75, sound_devilish, " Sound Devilish", probab= probab)
    percentage(105, 90, spirit_guardian, " Spirit Guardian", probab= probab)
    percentage(110, 105, solar_blade, " Solar Blade", probab= probab)

    # Aqui checamos se o usuario clicou no X para fechar o jogo
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        # iterando o objeto protagonista na tela
    hero.draw()

    collision = pg.sprite.spritecollide(hero, hit, True)
    if count_skills < 8:
        if 0 < probab <= 20:
            if collision:
                count_skills += 1
                atack += shield_radiant.name
                probab = randint(0, 110)
                hit.remove(shield_radiant)
            if not collision and shield_radiant.posY > height:
                hit.remove(shield_radiant)
                probab = randint(0, 110)
        elif 55 >= probab > 20:
            if collision:
                count_skills += 1
                atack += war_axe.name
                probab = randint(0, 110)
                hit.remove(war_axe)
            if not collision and war_axe.posY > height:
                hit.remove(war_axe)
                probab = randint(0, 110)
        elif 75 >= probab > 55:
            if collision:
                count_skills += 1
                atack += explosive_runes.name
                probab = randint(0, 110)
                hit.remove(explosive_runes)
            if not collision and explosive_runes.posY > height:
                hit.remove(explosive_runes)
                probab = randint(0, 110)
        elif 90 >= probab > 75:
            if collision:
                count_skills += 1
                atack += sound_devilish.name
                probab = randint(0, 110)
                hit.remove(sound_devilish)
            if not collision and sound_devilish.posY > height:
                hit.remove(sound_devilish)
                probab = randint(0, 110)
        elif 105 >= probab > 90:
            if collision:
                count_skills += 1
                atack += spirit_guardian.name
                probab = randint(0, 110)
                hit.remove(spirit_guardian)
            if not collision and spirit_guardian.posY > height:
                hit.remove(spirit_guardian)
                probab = randint(0, 110)
        else:
            if collision:
                count_skills += 1
                atack += solar_blade.name
                probab = randint(0, 110)
                hit.remove(solar_blade)
            if not collision and solar_blade.posY > height:
                hit.remove(solar_blade)
                probab = randint(0, 110)

    skills = f'Ataques: {atack}'
    txt_format = font.render(skills, True, (245, 255, 255))

    pg.display.flip()
    hero.update(all_sprites, time)
    screen.blit(background, (0, 0))
    screen.blit(txt_format, (500, 40))
