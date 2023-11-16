import pygame
from configuracoes import ALTURA, LARGURA, JOGADOR1_ALTURA, JOGADOR1_LARGURA, JOGADOR2_ALTURA, JOGADOR2_LARGURA

ALTURA_PULO = 2
VEL_PULO = 20

PARADO = 0
PULANDO = 1
CAINDO = 2

class Jogador1(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['jogador1']
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 4
        self.rect.bottom = ALTURA - 10
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

        # Usado para decicir se o jogador pode ou não pular
        self.state = PARADO

    # Esse metodo atualiza a posição do personagem
    def update(self):
        # Atualiza a movimentação no eixo x
        self.rect.x += self.speedx
        self.speedy += ALTURA_PULO
        if self.rect.y > 0:
            self.state = CAINDO
        self.rect.y += self.speedy

        # Manter dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA
            self.speedy = 0
            self.state = PARADO
        if self.rect.top < 0:
            self.rect.top = 0
        
    def pulo(self):
        if self.state == PARADO:
            self.speedy -= VEL_PULO
            self.state = PULANDO

class Jogador2(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['jogador2']
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 1.5
        self.rect.bottom = ALTURA - 10
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

        # Usado para decicir se o jogador pode ou não pular
        self.state = PARADO

    # Esse metodo atualiza a posição do personagem
    def update(self):
        # Atualiza a movimentação no eixo x
        self.rect.x += self.speedx
        self.speedy += ALTURA_PULO
        if self.rect.y > 0:
            # levando em consideração o eixo 0 presente no canto sup esquerdo
            self.state = CAINDO
        self.rect.y += self.speedy

        # Manter dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA
            self.speedy = 0
            self.state = PARADO
        if self.rect.top < 0:
            self.rect.top = 0
        
    def pulo(self):
        if self.state == PARADO:
            self.speedy -= VEL_PULO
            self.state = PULANDO