import pygame
from dados_jogo import JOGADOR1_ALTURA, JOGADOR1_LARGURA, JOGADOR2_ALTURA, JOGADOR2_LARGURA


PISO = "piso"
FUNDO = "fundo"
GALINHA = 'galinha'

def load_assets():
        assets = {}
        # convert_alpha() - uso com imagem de fundo transparente
        assets['jogador1'] = pygame.image.load("assets//img//lutador1.png").convert_alpha()
        assets['jogador1'] = pygame.transform.scale(assets['jogador1'], (JOGADOR1_LARGURA, JOGADOR1_ALTURA))
        assets['jogador2'] = pygame.image.load("assets//img//lutador2.png").convert_alpha()
        assets['jogador2'] = pygame.transform.scale(assets['jogador2'], (JOGADOR2_LARGURA, JOGADOR2_ALTURA))
        # convert() - usado c imagem de fundo normal
        assets[FUNDO] = pygame.image.load("assets//img//fundo.webp").convert()
        assets[PISO] = pygame.image.load("assets//img//ground.jpg").convert_alpha()

        #foto da galinha individual, teste
        # assets[GALINHA] = pygame.image.load("assets//img//galinha//images.png").convert_alpha()
        assets["barra_saude"] = pygame.image.load("assets//img//Barradevida.png").convert_alpha()
        
        return assets