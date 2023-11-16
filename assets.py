import pygame
from configuracoes import JOGADOR1_ALTURA, JOGADOR1_LARGURA

def load_assets():
        assets = {}
        assets['jogador'] = pygame.image.load("assets//img//lutador1.png").convert_alpha()
        assets['jogador'] = pygame.transform.scale(assets['jogador'], (JOGADOR1_LARGURA, JOGADOR1_ALTURA))
        return assets