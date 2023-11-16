import pygame
from configuracoes import FPS, LARGURA, ALTURA, PRETO, JOGADOR1_LARGURA, JOGADOR1_ALTURA
from assets import load_assets

def tela_de_jogo(tela):
    
    
    
    class Jogador(pygame.sprite.Sprite):
        def __init__(self, groups, assets):
            # Construtor da classe mãe
            pygame.sprite.Sprite.__init__(self)

            self.image = assets['jogador']
            self.rect = self.image.get_rect()
            self.rect.centerx = LARGURA / 2
            self.rect.bottom = ALTURA - 10
            self.speedx = 0
            self.speedy = 0
            self.groups = groups
            self.assets = assets

        # Esse metodo atualiza a posição do personagem
        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            # Manter dentro da tela
            if self.rect.right > LARGURA:
                self.rect.right = LARGURA
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > ALTURA:
                self.rect.bottom = ALTURA
            if self.rect.top < 0:
                self.rect.top = 0

    # funcao do jogo
    # Para ajuste da velocidade
    clock = pygame.time.Clock()

    # Carrega o arquivo assets.py
    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

    #Criar jogadores 
    Jogador1 = Jogador(groups, assets)
    all_sprites.add(Jogador1)

    MORTO = 0
    JOGANDO = 1
    state = JOGANDO

    tecla_precionada = {}

    while state != MORTO:
        clock.tick(FPS)

        #--Eventos do jogo
        for event in pygame.event.get():
            #---consequências 
            # se jogo fechar state = morto
            if event.type == pygame.QUIT:
                state = MORTO
            if state == JOGANDO:
                if event.type == pygame.KEYDOWN:
                    tecla_precionada[event.key] = True
                    if event.key == pygame.K_LEFT:
                        Jogador1.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        Jogador1.speedx += 8
                    if event.key == pygame.K_UP:
                            Jogador1.speedy -= 8 
                if event.type == pygame.KEYUP:
                    if event.key in tecla_precionada and tecla_precionada[event.key]:
                        if event.key == pygame.K_LEFT:
                            Jogador1.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            Jogador1.speedx -= 8
                        if event.key == pygame.K_UP:
                            Jogador1.speedy += 8
        
        all_sprites.update()
        
        # Saídas 
        tela.fill(PRETO)
        all_sprites.draw(tela)

        pygame.display.update()


