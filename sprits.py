import pygame
from dados_jogo import *
from animacao import *

ALTURA_PULO = 2
VEL_PULO = 40

PARADO = 0
PULANDO = 1
CAINDO = 2

class Jogador(pygame.sprite.Sprite):
    # dicionario para a classe inteira, usado para criar um unico dicionario com numero de golpes consecutivos 
    dicgolpes = {}

    def __init__(self,luta_dic, assets, x, y, tipojogador, tipooponente):
        # Construtor da classe mãe
        pygame.sprite.Sprite.__init__(self)

        self.tipojogador = tipojogador
        self.tipooponente = tipooponente
        # self.image = assets[f'jogador{self.tipojogador}']
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

        #define direcao inicial do jogador
        if self.tipojogador == 1:
            self.direcao = 'direita' 
        else:
            self.direcao = 'esquerda'
        
        # adiciona os jogadores como chaves do dicionario e o numero de golpes como valores
        if f'jogador{self.tipojogador}' not in Jogador.dicgolpes:
            Jogador.dicgolpes[f'jogador{self.tipojogador}'] = 0

        print(Jogador.dicgolpes)

        # pode ou não bater
        self.ultima_porrada = pygame.time.get_ticks()
        # ultima defesa
        self.ultima_defesa = pygame.time.get_ticks()
        # numero de ticks para pode bater de novo
        self.bater_ticks = 1000
        self.defesa_ticks = 2000

        # Usado para decicir se o jogador pode ou não pular
        self.state = PARADO

    # Esse metodo atualiza a posição do personagem
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

        # serve para atrasar a porrada 
        now = pygame.time.get_ticks()
        ticks_transcorridos = now - self.ultima_porrada

        if ticks_transcorridos > self.bater_ticks:
            self.ultima_porrada = now
            if (pygame.sprite.collide_mask(jogador, oponente)):
                oponente.saude -=10
                # se conseguir bater adiciona mais um golpe no dic pro jogador e zera o oponente.
                self.dicgolpes[f'jogador{self.tipojogador}'] +=1
                self.dicgolpes[f'jogador{self.tipooponente}'] = 0
                self.atc_index = 1
                #toca o som de jogador batendo
                if self.luta_dic == galinha:
                    self.assets['galinha_hit'].play()
                if self.luta_dic == pedra:
                    self.assets['pedra_hit'].play()
                if self.luta_dic == sapo:
                    self.assets['sapo_hit'].play()

    def defesa(self):
        nowdefesa = pygame.time.get_ticks() 
        ticks_transcorridos = nowdefesa - self.ultima_defesa
        self.defende = False
        if ticks_transcorridos > self.defesa_ticks:
            self.ultima_defesa = nowdefesa
            self.defende = True
            print("Defendeu")
    

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

class BarraMana(pygame.sprite.Sprite):
    def __init__(self, assets, x, y, tipojogador, tipooponente):
        # Construtor da classe mãe
        pygame.sprite.Sprite.__init__(self)

        self.tipojogador = tipojogador
        self.tipooponente = tipooponente
        self.image = assets['barra_mana']
        self.assets = assets
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.centerx = x
        self.centery = y

        # mana - mana inicial
        self.mana = 0
        # taxamana - quantos pixels vai aumentar 
        self.taxamana = 1
        self.ultimo_mana = pygame.time.get_ticks()
        # ticks_mana - quantos milisegundos vai ter entre cada incremento
        self.ticks_mana = 100

    def drawbarra(self, superficie):
        larguramana = (475 * (self.mana / 100))
        superficie.blit(self.image, (self.centerx, self.centery))
        pygame.draw.rect(superficie, AZUL, (self.centerx + 13, self.centery + 10, larguramana, 30),border_radius = 8)

    def update(self):
        nowbarra = pygame.time.get_ticks()
        ticks_transcorridosbarra = nowbarra - self.ultimo_mana

        if ticks_transcorridosbarra > self.ticks_mana:
            # if para quando ocorre combos, acessa o dicionario de golpes e ve que bateu sem parar
            if Jogador.dicgolpes[f'jogador{self.tipojogador}'] > 3:
                print("funcionou")
                self.taxamana = 2
                self.ultimo_mana = nowbarra
                self.mana = min(self.mana + self.taxamana, 100)
            else:
                # if de uma barra de mana normal
                self.taxa = 1
                self.ultimo_mana = nowbarra
                # soma o valor da mana com a taxa, o limitando a 100 (largura maxima)
                self.mana = min(self.mana + self.taxamana, 100)
        