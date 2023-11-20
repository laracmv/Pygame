import pygame
from dados_jogo import ALTURA, LARGURA, JOGADOR1_ALTURA, JOGADOR1_LARGURA, JOGADOR2_ALTURA, JOGADOR2_LARGURA, PRETO

ALTURA_PULO = 2
VEL_PULO = 40

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

class Barradevida(pygame.sprite.Sprite):
    def __init__(self, saude, assets, x, y):
        # Construtor da classe mãe
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['barra_saude']
        self.assets = assets
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.saude = saude
       
        # pygame.draw.rect recebe = superfície a ser desenhada, cor, posicao a ser desenha(x e y) e medidas(largura e altura)
    
    def desenhar_barra(self, superficie):
        taxa = (self.saude)/100
        superficie.blit(self.image, self.rect)
        pygame.draw.rect(superficie, PRETO, (self.rect.x, self.rect.y, 400 * taxa, 100)) 
        


