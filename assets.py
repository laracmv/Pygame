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

        #fundos
        assets['fundo1'] = pygame.image.load('assets\\img\\fundo 1 jogo.jpg')
        assets['fundo2'] = pygame.image.load('assets\\img\\fundo 2 jogo.jpg')
        assets['fundo3'] = pygame.image.load('assets\\img\\fundo 3 jogo.jpg')
        assets['fundo4'] = pygame.image.load('assets\\img\\fundo 4 jogo.png')

        #tela inicio
        #assets[]

        pygame.mixer.music.load("assets//sons//barbie.wav")
        return assets