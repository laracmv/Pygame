import pygame
from dados_jogo import largura, altura, l, a, posg, posk, black,post
from sys import exit
from assets import *

pygame.init()
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock() #controla os frames por segundo

font = pygame.font.Font(None, 50) #font type, font size

assets = load_assets()

#imagem do céu
sky_surface = assets[FUNDO]

#pygame.Surface((l,a))
#teste_surface.fill(branco)

#imagem do chão
ground_surface = assets[PISO]

#texto pra aparecer na surface
texto_surface = font.render('Batalha no Insper',False,black) #o render mostra o texto, AA, e color


jogo = True

while True:
    for event in pygame.event.get(): #dá todos os eventos
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #o loop acaba, ele nao uptade anymore

    
    tela.blit(sky_surface,posk) #aqui recebe a surface e a position
    tela.blit(ground_surface,posg)
    tela.blit(texto_surface,post)


    pygame.display.update() #ele atualiza a display.set_mode
    clock.tick(60) #esse loop não vai correr a mais que 60 frames por segundo, not run too fast