import pygame
from configuracoes import LARGURA, ALTURA, PRETO, JOGO, FIM, INICIAR
from tela_de_jogo import tela_de_jogo

pygame.init()
pygame.mixer.init()

# Gerar tela principal

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo de Luta')


state = JOGO
# mudar para state = iniciar quando tiver criado tela de inicio
while state != FIM:
    # if state == INICIO:
    # Usa esse 1o if quanto tiver tela inicio
    if state == JOGO:
        state = tela_de_jogo(tela)
    else:
        state = FIM
    
    tela.fill((PRETO))

pygame.quit()
