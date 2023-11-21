import pygame
from dados_jogo import *

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
        self.defende = False
        
        # pode ou não bater
        self.ultima_porrada = pygame.time.get_ticks()
        # numero de ticks para pode bater de novo
        self.bater_ticks = 500

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

        # serve para atrasar a porrada 
        now = pygame.time.get_ticks()
        ticks_transcorridos = now - self.ultima_porrada

        if ticks_transcorridos > self.bater_ticks:
            self.ultima_porrada = now
            if (pygame.sprite.collide_mask(jogador, oponente)):
                oponente.saude -=10
                print("Bateu")

class Barradevida(pygame.sprite.Sprite):
    def __init__(self, assets, x, y):
        # Construtor da classe mãe
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['barra_saude']
        self.assets = assets
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
       
    def desenhar_barra(self, superficie, vida):
        self.vida = vida
        # taxa = usado para saber quantos porcento do total o jogador tem de vida, também para gerar o tamanho da barra de vida, multiplicando ele pelo tamanho dela
        taxa = (self.vida)/100
        # desenha o contorno da barra de vida
        superficie.blit(self.image, self.rect)
        # recebe a superfície a ser desenhada, a cor da vida, a posição dele(x,y, largura, altura) e a curvatura da barrra
        pygame.draw.rect(superficie, CORAL, (self.rect.x + 14, self.rect.y + 19 , 620 * taxa, 80),border_radius=20)
