import pygame
from dados_jogo import JOGADOR1_ALTURA, JOGADOR1_LARGURA, JOGADOR2_ALTURA, JOGADOR2_LARGURA, som, BSAUDE_ALTURA, BSAUDE_LARGURA, LARGURA, ALTURA
import os

BOTAO1 = 'botao1'

def load_assets():
        assets = {}
        assets["barra_saude"] = pygame.image.load("assets//img//Barradevida.png").convert_alpha() # convert_alpha() - uso com imagem de fundo transparente
        assets['barra_saude'] = pygame.transform.scale(assets['barra_saude'], (BSAUDE_LARGURA, BSAUDE_ALTURA))

        #Fonte
        assets["tempo_fonte"] = pygame.font.Font("assets//fontes//PressStart2P.ttf", 42)
        
        #fundos
        assets['fundo3'] = pygame.image.load('assets\\img\\fundo 3 jogo.jpg').convert()
        assets['fundo3'] = pygame.transform.scale(assets['fundo3'], (LARGURA, ALTURA))
        
        assets['chao'] = pygame.image.load('assets\\img\\ground.jpg')

        #Sons
        pygame.mixer.music.load("assets//sons//barbie.wav")
        pygame.mixer.music.set_volume(0.3) #nivel de som
        assets['galinha_hit'] = pygame.mixer.Sound("assets//sons//galinhahit.wav")
        assets['galinha_hit'].set_volume(som)
        assets['sapo_hit'] = pygame.mixer.Sound("assets//sons//sapohit.wav")
        assets['sapo_hit'].set_volume(som)
        
        return assets