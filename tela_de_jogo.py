import pygame
from configuracoes import FPS, LARGURA, ALTURA, PRETO, JOGADOR1_LARGURA, JOGADOR1_ALTURA
from assets import load_assets
from sprits import Jogador

def tela_de_jogo(tela):
    
    # funcao do jogo
    # Para ajuste da velocidade
    clock = pygame.time.Clock()

    # Carrega o arquivo assets.py
    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

    #Criar jogadores 
    # Jogador(grupo, )
    jogador1 = Jogador(assets, LARGURA / 4, ALTURA - 10, 1)
    jogador2 = Jogador(assets, LARGURA / 1.5, ALTURA - 10, 2)
    all_sprites.add(jogador1)
    all_sprites.add(jogador2)

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
                    # Teclas jogador 1
                    if event.key == pygame.K_LEFT:
                        jogador1.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        jogador1.speedx += 8
                    if event.key == pygame.K_UP:
                        jogador1.pulo() 
                    # Teclas jogador 2
                    if event.key == pygame.K_a:
                        jogador2.speedx -=8
                    if event.key == pygame.K_d:
                        jogador2.speedx +=8
                    if event.key == pygame.K_w:
                        jogador2.pulo()
                if event.type == pygame.KEYUP:
                    if event.key in tecla_precionada and tecla_precionada[event.key]:
                        # Teclas jogador 1
                        if event.key == pygame.K_LEFT:
                            jogador1.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            jogador1.speedx -= 8
                        # Teclas jogador 2
                        if event.key == pygame.K_a:
                            jogador2.speedx +=8
                        if event.key == pygame.K_d:
                            jogador2.speedx -=8

        # Atualiza estado do jogo
        all_sprites.update()
        
        # Saídas 
        tela.fill(PRETO)
        all_sprites.draw(tela)

        pygame.display.update()


