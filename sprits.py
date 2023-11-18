import pygame
from configuracoes import ALTURA, LARGURA, JOGADOR1_ALTURA, JOGADOR1_LARGURA, JOGADOR2_ALTURA, JOGADOR2_LARGURA

ALTURA_PULO = 2
VEL_PULO = 20

PARADO = 0
PULANDO = 1
CAINDO = 2

class Jogador(pygame.sprite.Sprite):
    def __init__(self, assets, x, y, tipo):
        # Construtor da classe mãe
        pygame.sprite.Sprite.__init__(self)

        self.tipo = tipo
        self.image = assets[f'jogador{self.tipo}']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0
        self.speedy = 0
        self.assets = assets
        self.saude = 100

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
    
    # Se o jogador bater no oponenente, o oponenete perderá vida 
    def bateu(self, jogador, oponente):
        self.jogador = jogador
        self.oponente = oponente
        if (pygame.sprite.collide_mask(jogador, oponente)):
            oponente.saude -=10
            print(f" quando bate: {self.saude}")



