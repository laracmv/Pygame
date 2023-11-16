import pygame
from configuracoes import JOGADOR1_ALTURA, JOGADOR1_LARGURA, JOGADOR2_ALTURA, JOGADOR2_LARGURA

def load_assets():
        assets = {}
        assets['jogador1'] = pygame.image.load("assets//img//lutador1.png").convert_alpha()
        assets['jogador1'] = pygame.transform.scale(assets['jogador1'], (JOGADOR1_LARGURA, JOGADOR1_ALTURA))
        assets['jogador2'] = pygame.image.load("assets//img//lutador2.png").convert_alpha()
        assets['jogador2'] = pygame.transform.scale(assets['jogador2'], (JOGADOR2_LARGURA, JOGADOR2_ALTURA))
        return assets