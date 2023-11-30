import pygame
from dados_jogo import *
from animacao import *

ALTURA_PULO = 2
VEL_PULO = 40

PARADO = 0
PULANDO = 1
CAINDO = 2

class Jogador(pygame.sprite.Sprite):
    def __init__(self,luta_dic, assets, x, y, tipojogador, tipooponente):
        # Construtor da classe mãe
        pygame.sprite.Sprite.__init__(self)

        self.tipojogador = tipojogador
        self.tipooponente = tipooponente
        self.img_index = 0
        self.atc_index = 0
        self.image = luta_dic['idle'][self.img_index]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0
        self.speedy = 0
        self.assets = assets
        self.saude = 100
        self.defende = False
        self.luta_dic = luta_dic
        self.j2ganhou = False
        self.j1ganhou = False

        #define direcao inicial do jogador
        if self.tipojogador == 1:
            self.direcao = 'direita' 
        else:
            self.direcao = 'esquerda'
        
        # pode ou não bater
        self.ultima_porrada = pygame.time.get_ticks()
        # ultima defesa
        self.ultima_defesa = pygame.time.get_ticks()
        # numero de ticks para pode bater de novo
        self.bater_ticks = 1000
        self.defesa_ticks = 2000

        # Usado para decicir se o jogador pode ou não pular
        self.state = PARADO
    
    def update(self):

        #serve para deixar a imagem correta caso o jogador ande para direita
        if self.direcao == 'direita':

            #animacao quando ocorre um ataque
            if self.atc_index != 0: 
                if self.atc_index < len(self.luta_dic['hit']):
                    self.image = self.luta_dic['hit'][self.atc_index]
                    self.atc_index += 1
                else:
                    self.atc_index = 0

            # animacao quando esta parado        
            else: 
                self.img_index += 1
                if self.img_index >= len(self.luta_dic['idle']):
                    self.img_index = 0
                self.image = self.luta_dic['idle'][self.img_index]

        #inverte imagem quando ele anda para esquerda
        if self.direcao == 'esquerda':

            #animacao quando ocorre um ataque
            if self.atc_index != 0: 
                if self.atc_index < len(self.luta_dic['hit']):
                    self.image = pygame.transform.flip(self.luta_dic['hit'][self.atc_index], True, False)
                    self.atc_index += 1
                else:
                    self.atc_index = 0

            # animacao quando esta parado        
            else: 
                self.img_index += 1
                if self.img_index >= len(self.luta_dic['idle']):
                    self.img_index = 0
                self.image = pygame.transform.flip(self.luta_dic['idle'][self.img_index], True, False)

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
        if self.rect.bottom > ALTURA - 75:
            self.rect.bottom = ALTURA - 75
            self.speedy = 0
            self.state = PARADO

    def pulo(self):
        if self.state == PARADO:
            self.speedy -= VEL_PULO
            self.state = PULANDO
    
    # Se o jogador bater no oponenente, o oponenete perderá vida 
    def bateu(self, jogador, oponente):
        self.jogador = jogador
        self.oponente = oponente

        now = pygame.time.get_ticks()
        ticks_transcorridos = now - self.ultima_porrada

        if ticks_transcorridos > self.bater_ticks: #serve para não ser possivel bater sem parar, so depois um tempo
            self.ultima_porrada = now
            if (pygame.sprite.collide_mask(jogador, oponente)):
                oponente.saude -=10
                self.atc_index = 1
                #toca o som de jogador batendo
                if self.luta_dic == galinha:
                    self.assets['galinha_hit'].play()
                if self.luta_dic == sapo:
                    self.assets['sapo_hit'].play()

    def defesa(self):
        nowdefesa = pygame.time.get_ticks() 
        ticks_transcorridos = nowdefesa - self.ultima_defesa
        self.defende = False
        if ticks_transcorridos > self.defesa_ticks:
            self.ultima_defesa = nowdefesa
            self.defende = True
    
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
        pygame.draw.rect(superficie, CORAL, (self.rect.x + 14, self.rect.y + 11 , 475 * taxa, 60),border_radius=20)


        