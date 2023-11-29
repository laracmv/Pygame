import pygame
from dados_jogo import *
from tela_de_jogo import tela_de_jogo
from telainicio import *

pygame.init()
pygame.mixer.init()


# Gerar tela principal
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo de Luta')


state = INICIAR
# mudar para state = iniciar quando tiver criado tela de inicio
while state != FIM:
<<<<<<< HEAD
    #if state == INICIO:
=======
    if state == INICIAR:
        state = telainicio(tela)
>>>>>>> ddce6be12e1515045abd790586051dc4d6df5eb6
    # Usa esse 1o if quanto tiver tela inicio
    if state == JOGO:
        # vai para tela do jogo
        state = tela_de_jogo(tela)
    else:  
        state = FIM
    
    tela.fill((PRETO))

pygame.quit()
