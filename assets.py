import pygame
from dados_jogo import JOGADOR1_ALTURA, JOGADOR1_LARGURA, JOGADOR2_ALTURA, JOGADOR2_LARGURA, BMANA_LARGURA, BMANA_ALTURA, som
import os

BOTAO1 = 'botao1'

def load_assets():
        assets = {}
        assets["barra_saude"] = pygame.image.load("assets//img//Barradevida.png").convert_alpha() # convert_alpha() - uso com imagem de fundo transparente
        assets['barra_mana'] = pygame.image.load("assets//img//Barradevida.png").convert_alpha()
        assets['barra_mana'] = pygame.transform.scale(assets['barra_mana'], (BMANA_LARGURA, BMANA_ALTURA))
        assets["tempo_fonte"] = pygame.font.Font("assets//fontes//PressStart2P.ttf", 42)
        
        assets['botao1'] = pygame.image.load('assets\\img\\botao.jpg')
        
        # ------Carrega sons do jogo
        pygame.mixer.music.load("assets//sons//barbie.wav") #musica principal
        pygame.mixer.music.set_volume(0.3) #nivel de som
        assets['galinha_hit'] = pygame.mixer.Sound("assets//sons//galinhahit.wav")
        assets['galinha_hit'].set_volume(som)
        assets['pedra_hit'] = pygame.mixer.Sound("assets//sons//pedrahit.wav")
        assets['sapo_hit'] = pygame.mixer.Sound("assets//sons//sapohit.wav")
        assets['sapo_hit'].set_volume(som)
        return assets