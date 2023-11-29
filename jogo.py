import pygame
from dados_jogo import *
from tela_de_jogo import tela_de_jogo
from inicial import tela_inicial
from fimjogo import tela_final

pygame.init()
pygame.mixer.init()


# Gerar tela principal
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo de Luta')


state = INICIAR
# mudar para state = iniciar quando tiver criado tela de inicio
while state != FIM:
    #if state == INICIO:
    if state == INICIAR:
        state = tela_inicial(tela)
    # Usa esse 1o if quanto tiver tela inicioq
        state = telainicio(tela)
    # Usa esse 1o if quanto tiver tela inicio
    if state == JOGO:
        # vai para tela do jogo
        state = tela_de_jogo(tela)
    if state == FINAL: 
        state = tela_final(tela)  
    else:  
        state = FIM
    
    tela.fill((PRETO))

pygame.quit()
