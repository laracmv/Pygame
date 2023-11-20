import pygame
from dados_jogo import FPS, LARGURA, ALTURA, PRETO, JOGADOR1_LARGURA, JOGADOR1_ALTURA
from assets import load_assets
from sprits import Jogador, Barradevida

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
    barradevidaj1 = Barradevida(jogador1.saude, assets, 10, 10)
    barradevidaj2 = Barradevida( jogador2.saude, assets, 1200, 10)
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
            # se jogo fechar state = morto, acaba o jogo
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
                    if event.key == pygame.K_q:
                        # se o jogador 1 apertar espaço e o jogador 2 estiver perto, ele vai poder bater
                        jogador1.bateu(jogador1, jogador2)

                    # Teclas jogador 2
                    if event.key == pygame.K_a:
                        jogador2.speedx -=8
                    if event.key == pygame.K_d:
                        jogador2.speedx +=8
                    if event.key == pygame.K_w:
                        jogador2.pulo()
                    if event.key == pygame.K_SPACE:
                        # se o jogador 2 apertar espaço e o jogador 1 estiver perto, ele vai poder bater
                        jogador2.bateu(jogador2, jogador1)

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

        # Se o jogador 1 ou 2 perder toda vida o jogo acaba
        if jogador1.saude <= 0 or jogador2.saude <=0: 
            state = MORTO

        
        # Saídas 
        tela.fill((72,61,139))
        all_sprites.draw(tela)
        barradevidaj1.desenhar_barra(tela)
        barradevidaj2.desenhar_barra(tela)

        pygame.display.update()


