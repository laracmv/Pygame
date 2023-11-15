import pygame
from configuracoes import FPS, LARGURA, ALTURA, PRETO

def tela_de_jogo(tela):
    
    # def load_assets():
    assets = {}
    assets['jogador'] = pygame.image.load("assets//img//lutador1.png").convert_alpha()
        # return assets
    
    class Jogador(pygame.sprite.Sprite):
        def __init__(self, assets):
            pygame.sprite.Sprite.__init__(self)
        
            self.image = assets['jogador']
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 3
            self.speedy = 3
            self.assets = assets

        def update(self):
            self.react.x += self.speedx
            self.react.y += self.speedy

    # Para ajuste da velocidade
    clock = pygame.time.Clock()

    # assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

    #Criar jogadores 
    Jogador1 = Jogador(assets['jogador'])
    all_sprites.add(player)

    MORTO = 0
    JOGO = 1
    state = JOGO

    while state != MORTO:
        clock.tick(FPS)

        #--Eventos do jogo
        for event in pygame.event.get():
            #---consequências 
            # se jogo fechar state = morto
            if event.type == pygame.QUIT:
                state = MORTO
            if event.type == pygame.KEYUP:
                state = MORTO
        
        all_sprites.update()
        
        # Saídas 
        tela.fill((PRETO))
        all_sprites.draw(tela)

        pygame.display.update()


