# imports pygame, random e locals
import pygame as pg
import pygame.font
from hero import *
from atk import *
from nerf import *
from dragon import *
pg.init()
from random import randint

# Aqui criamos a tela
wight, height = 1080, 600
screen = pg.display.set_mode((wight, height))
pg.display.set_caption('Dragão de Nome Impronunciável')
background = pg.image.load("background.jpg")

# Sonoro
pygame.mixer.music.set_volume(1)
msc_fundo = pygame.mixer.music.load('epic_bckgrnd_msc.mp3')
pygame.mixer.music.play(-1)

som_dragao_vida = pygame.mixer.Sound('dragon_roar.wav')
som_amoz_vida = pygame.mixer.Sound('metallic_clank.wav')

som_dos_vencedores = pygame.mixer.Sound('brasilsil.wav')
som_dos_perdedores =pygame.mixer.Sound('losing_sound.wav')

# Posições referências
y_pos = 0

# Frames, objetos drops, protagonista e outros
clock = pg.time.Clock()  # Usar para frame
hero = Hero(90, 90, wight, height, screen)  # Criando a partir de classe
hit = pg.sprite.Group() #Grupo para itens que vão colidir e trazer beneficios ao jogador
hit_dmg = pg.sprite.Group() #Grupo para itens que vão colidir e trazer maleficios ao jogador

#Vidas
life_dragon = 200
life_amoz = 100

# Objetos drops
shield_radiant = Spell(randint(20, 900), y_pos, wight, height, screen, 0, ' Shield Radiant')
war_axe = Spell(randint(20, 900), y_pos, wight, height, screen, 1, ' War Axe')
explosive_runes = Spell(randint(20, 900), y_pos, wight, height, screen, 5, ' Explosive Runes')
spirit_guardian = Spell(randint(20, 900), y_pos, wight, height, screen, 2, ' Spirit Guardian')
sound_devilish = Spell(randint(20, 900), y_pos, wight, height, screen, 4, ' Sound Devilish')
solar_blade = Spell(randint(20, 900), y_pos, wight, height, screen, 3, ' Solar Blade')

#Objetos do dragão

turbulence = Damage(randint(20, 900), 225, wight, height, screen, 3, ' Turbulence', 640, 640, 0.9)
flaming_blast = Damage(randint(20, 900), 225, wight, height, screen, 1, ' Flaming Blast', 400, 400, 0.7)
breathe_weakening = Damage(randint(20, 900), 225, wight, height, screen, 0, ' Breathe Weakening', 500, 300, 0.9)
intimidating_curtain = Damage(randint(20, 900), 225, wight, height, screen, 2, ' Intimidating Curtain', 550, 550, 0.6)


#Criando o dragão
impronunciable = Lovecraft(250, 290, wight, height, screen, 400)

#Probabilidades para os itens, textos da tela e outros
probab = randint(0, 110)
probab_dragon = randint(1, 4)
all_sprites = pg.sprite.Group()
time = pg.time.get_ticks()
font = pg.font.SysFont('Tempus San ITC', 15, True, False)
font_screen = pg.font.SysFont('Tempus San ITC', 150, True, False)
font_score = pg.font.SysFont('Tempus San ITC', 80, True, False)
font_analyse = pg.font.SysFont('Tempus San ITC', 20, True, False)


#Funções principais responsáveis pela queda, pela desenho, pela comparação, colisão e etc.
def percentage(number_l, number_r, item, name, height=height, y_pos=y_pos, probab=probab, hit=hit, life_amoz= life_amoz, life_dragon=life_dragon):
    if probab <= 20 and name == " Shield Radiant":
        hit.add(item)
        if life_dragon > 0 and life_amoz:
            item.draw()
            item.update(y_pos, height)
        if hero.rect.colliderect(item.rect):
            item.checkcolision()
            return name
    elif probab > 20:
        if number_l >= probab > number_r:
            hit.add(item)
            if life_dragon > 0 and life_amoz:
                item.draw()
                item.update(y_pos, height)
            if hero.rect.colliderect(item.rect):
                item.checkcolision()
                return name
    else:
        pass
def dragon_kit(item, name, number, impronunciable = impronunciable, height=height, y_pos=y_pos, wight =wight, probab_dragon = probab_dragon, hit_dmg = hit_dmg, life_amoz = life_amoz, life_dragon = life_dragon):
    if probab_dragon == number:
        hit_dmg.add(item)
        if life_dragon>0 and life_amoz>0:
            item.draw()
            item.update(y_pos, height)
        if item.posY<height:
            impronunciable.x = item.posX
        if hero.rect.colliderect(item.rect):
            item.checkcolision()
            non_colision = False
            return non_colision
        elif not hero.rect.colliderect(item.rect) and item.posY>=height:
            item.checkcolision()
            non_colision = True
            return non_colision
    else:
        pass

asmodeus, poisoned, count_asmodeus, rage, score = 0, 0, 0, 0, 0
s_shield, s_axe, s_sound, s_runes, s_spirit, s_blade = 0, 0, 0, 0, 0, 0
protection, reflection = False, False

while True:
    if life_dragon<0:
        life_dragon=0
    if life_amoz<0:
        life_amoz=0
    if life_dragon<100:
        rage = 12
    if life_dragon==0 or life_amoz==0:
        impronunciable.x= wight//2
    #Chamadas para comparação
    percentage(0, 20, shield_radiant, " Shield Radiant", probab= probab, life_amoz=life_amoz, life_dragon= life_dragon)
    percentage(55, 20, war_axe, " War Axe", probab= probab, life_amoz=life_amoz, life_dragon= life_dragon)
    percentage(75, 55, explosive_runes, " Explosive Runes", probab= probab, life_amoz=life_amoz, life_dragon= life_dragon)
    percentage(90, 75, sound_devilish, " Sound Devilish", probab= probab, life_amoz=life_amoz, life_dragon= life_dragon)
    percentage(105, 90, spirit_guardian, " Spirit Guardian", probab= probab, life_amoz=life_amoz, life_dragon= life_dragon)
    percentage(110, 105, solar_blade, " Solar Blade", probab= probab, life_amoz=life_amoz, life_dragon= life_dragon)

    breathe = dragon_kit(breathe_weakening, breathe_weakening.name, 1, probab_dragon = probab_dragon, life_amoz=life_amoz, life_dragon= life_dragon)
    flaming = dragon_kit(flaming_blast, flaming_blast.name, 2, probab_dragon = probab_dragon, life_amoz=life_amoz, life_dragon= life_dragon)
    intimidating = dragon_kit(intimidating_curtain, intimidating_curtain.name, 3, probab_dragon = probab_dragon, life_amoz=life_amoz, life_dragon= life_dragon)
    thunder_blue = dragon_kit(turbulence, turbulence.name, 4, probab_dragon = probab_dragon, life_amoz=life_amoz, life_dragon= life_dragon)
    #Laço para quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    #Desenho dos dois sprites principais
    hero.draw()
    impronunciable.draw()


    collision = pg.sprite.spritecollide(hero, hit, True)

    if life_dragon>0 and life_amoz>0:
        if 0 <= probab <= 20:
            if collision:
                score += 2
                s_shield += 1
                poisoned = 0
                protection = True
                probab = randint(0, 110)
                hit.remove(shield_radiant)
                if hero.vel_X!= 1.5:
                    hero.vel_X=1.5
            if not collision and shield_radiant.posY > height:
                probab = randint(0, 110)
                hit.remove(shield_radiant)


        elif 55 >= probab > 20:
            if collision:
                score+= 4
                s_axe += 1
                life_amoz -= poisoned
                som_amoz_vida.play()
                life_dragon -= randint(10, 15)+asmodeus
                probab = randint(0, 110)
                hit.remove(war_axe)
                if hero.vel_X<=1.5:
                    hero.vel_X+=0.3
                if asmodeus>0 and 3>count_asmodeus>=0:
                    count_asmodeus += 1
                elif count_asmodeus==3:
                    asmodeus = 0
                    count_asmodeus = 0
            if not collision and war_axe.posY > height:
                probab = randint(0, 110)
                hit.remove(war_axe)

        elif 75 >= probab > 55:
            if collision:
                score+= 6
                s_runes += 1
                dex_dragon = randint(1, 2)
                life_amoz -= poisoned
                som_amoz_vida.play()
                probab = randint(0, 110)
                hit.remove(explosive_runes)
                if dex_dragon==1:
                    life_dragon-= randint(25, 35)+asmodeus+5
                    som_dragao_vida.play()
                elif dex_dragon==2:
                    life_dragon-= randint(25, 35)+5//2
                    som_dragao_vida.play()
                if asmodeus>0 and 3>count_asmodeus>=0:
                    life_dragon-= 5
                    som_dragao_vida.play()
                    count_asmodeus+= 1
                elif count_asmodeus==3:
                    asmodeus= 0
                    count_asmodeus = 0
                if hero.vel_X!= 1.5:
                    hero.vel_X=1.5
            if not collision and explosive_runes.posY > height:
                probab = randint(0, 110)
                hit.remove(explosive_runes)


        elif 90 >= probab > 75:
            if collision:
                score+= 8
                s_sound += 1
                life_amoz -= 10+poisoned
                som_amoz_vida.play()
                probab = randint(0, 110)
                hit.remove(sound_devilish)
                if asmodeus==0:
                    asmodeus += 10
                    count_asmodeus= 0
                    probab = randint(0, 110)
                    hit.remove(sound_devilish)
                if hero.vel_X!= 1.5:
                    hero.vel_X=1.5
            if not collision and sound_devilish.posY > height:
                probab = randint(0, 110)
                hit.remove(sound_devilish)


        elif 105 >= probab > 90:
            if collision:
                score+=10
                s_spirit += 1
                reflection = True
                poisoned=0
                probab = randint(0, 110)
                hit.remove(spirit_guardian)
            if hero.vel_X != 1.5:
                hero.vel_X = 1.5
            if not collision and spirit_guardian.posY > height:
                probab = randint(0, 110)
                hit.remove(spirit_guardian)

        elif probab>105:
            if collision:
                score += 12
                s_blade += 1
                life_dragon-= randint(40, 50)
                life_amoz -= poisoned
                som_amoz_vida.play()
                probab = randint(0, 110)
                hit.remove(solar_blade)
                if life_amoz<100:
                    life_amoz += randint(15, 30)
                    if life_amoz>100:
                        life_amoz=100
                if hero.vel_X!= 1.5:
                    hero.vel_X=1.5
                if asmodeus>0 and 3>count_asmodeus>=0:
                    count_asmodeus+= 1
                elif count_asmodeus==3:
                    asmodeus= 0
                    count_asmodeus = 0
            if not collision and solar_blade.posY > height:
                probab = randint(0, 110)
                hit.remove(solar_blade)




        if probab_dragon==1:
            if breathe==False:
                hit_dmg.remove(breathe_weakening)
                probab_dragon = randint(1, 4)
                if hero.vel_X>0.9:
                    hero.vel_X -= 0.6
            elif breathe==True:
                hit_dmg.remove(breathe_weakening)
                probab_dragon = randint(1, 4)


        elif probab_dragon==2:
            dmg = randint(10, 20) + rage
            if flaming == False:
                hit_dmg.remove(flaming_blast)
                probab_dragon = randint(1, 4)
                if protection:
                    life_amoz-= dmg//2+poisoned
                    protection = False
                elif protection == False:
                    life_amoz -= dmg+poisoned
                    som_amoz_vida.play()
                if reflection:
                    life_dragon -= dmg//3
                    som_dragao_vida.play()
                    reflection = False
            elif flaming==True:
                hit_dmg.remove(flaming_blast)
                probab_dragon = randint(1, 4)


        elif probab_dragon==3:
            dmg = randint(1, 12) + rage
            if intimidating ==False:
                hit_dmg.remove(intimidating_curtain)
                poisoned+=3
                probab_dragon = randint(1, 4)
                if protection:
                    life_amoz -= dmg//2
                    som_amoz_vida.play()
                    protection = False
                elif protection==False:
                    life_amoz-= dmg
                if reflection:
                    life_dragon-= dmg//3
                    som_dragao_vida.play()
            elif intimidating==True:
                hit_dmg.remove(intimidating_curtain)
                probab_dragon = randint(1, 4)


        elif probab_dragon==4:
            dmg = randint(5, 25)+rage
            if thunder_blue==False:
                hit_dmg.remove(turbulence)
                probab_dragon = randint(1, 4)
                if protection:
                    life_amoz-= dmg//2+poisoned
                    protection = False
                elif protection == False:
                    life_amoz -= dmg+poisoned
                    som_amoz_vida.play()
                if reflection:
                    life_dragon -= dmg//3
                    som_dragao_vida.play()
                    reflection = False
            elif thunder_blue==True:
                hit_dmg.remove(turbulence)
                probab_dragon = randint(1, 4)

    hp_dragon = f'Vida do ?: {life_dragon}'
    hp_amoz = f'Vida de Amoz: {life_amoz}'
    txt_sc = f'SCORE: {str(score)}'
    tabel = f'Shield Radiant: x{s_shield}, War Axe: x{s_axe}, Explosive Runes: x{s_runes}, Sound Devilish: x{s_sound}, Spirit Guardian: x{s_spirit} and Solar Blade: x{s_blade}'

    txt_format_drg = font.render(hp_dragon, True, (245, 255, 255))
    txt_format_amz = font.render(hp_amoz, True, (245, 255, 255))


    if poisoned != 0:
        status_poisoned= "Envenenado"
        txt_psnd = font.render(status_poisoned, True, (65, 255, 80))
        screen.blit(txt_psnd, (925, 575))
    if hero.vel_X<1.5:
        status_slowed = "Lentidão"
        txt_slwd = font.render(status_slowed, True, (0, 0, 30))
        screen.blit(txt_slwd, (925, 560))
    if life_amoz == 0 and life_dragon>0:
        game_over = "YOU LOSE!"
        txt_format_go = font_screen.render(game_over, True, (200, 30, 50))
        txt_format_score = font_score.render(txt_sc, True, (20, 20, 20))
        txt_format_tabel= font_analyse.render(tabel, True, (145, 0, 0))
        screen.blit(txt_format_score, (390, 325))
        screen.blit(txt_format_go, (248, 222))
        screen.blit(txt_format_tabel, (158, 375))
        som_dos_perdedores.play()
    if life_dragon == 0 and life_amoz>0:
        game_won= "YOU WIN!"
        txt_format_gw = font_screen.render(game_won, True, (25, 55, 180))
        txt_format_score = font_score.render(txt_sc, True, (20, 20, 20))
        txt_format_tabel= font_analyse.render(tabel, True, (0, 5, 133))
        screen.blit(txt_format_gw, (248, 222))
        screen.blit(txt_format_score, (390, 325))
        screen.blit(txt_format_tabel, (158, 375))
        som_dos_vencedores.play()
    if life_amoz == 0 and life_dragon== 0:
        tie = "DRAW"
        txt_format_dw = font_screen.render(tie, True, (159, 43, 104))
        txt_format_score = font_score.render(txt_sc, True, (20, 20, 20))
        txt_format_tabel = font_analyse.render(tabel, True, (128, 0, 32))
        screen.blit(txt_format_score, (390, 325))
        screen.blit(txt_format_dw, (360, 222))
        screen.blit(txt_format_tabel, (158, 375))
        som_dos_perdedores.play()

    pg.display.flip()
    hero.update(all_sprites, time)
    screen.blit(background, (0, 0))
    screen.blit(txt_format_drg, (35, 550))
    screen.blit(txt_format_amz, (925, 550))

