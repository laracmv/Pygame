import pygame
from dados_jogo import *
from tela_de_jogo import tela_de_jogo
from inicial import tela_inicial
from fimjogo import tela_final

pygame.init()
pygame.mixer.init()

# Gerar tela principal
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Rinha de Bicho')

state = INICIAR
while state != FIM:
    
    if state == INICIAR: #leva até a tela de inicio
        state = tela_inicial(tela)
    if state == JOGO: # vai para tela do jogo
        
        state = tela_de_jogo(tela)
    if state == FINAL: #leva até a tela final
        state = tela_final(tela)  
    else:  
        state = FIM
    
    tela.fill((PRETO))

pygame.quit()
