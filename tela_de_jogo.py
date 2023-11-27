import pygame
from dados_jogo import *
from assets import load_assets
from sprits import Jogador, Barradevida, BarraMana
from animacao import * 

def tela_de_jogo(tela):
    
    # funcao do jogo pra ajuste da velocidade
    clock = pygame.time.Clock()

    # Carrega o arquivo assets.py
    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

    #--- Criar jogadores 
    jogador1 = Jogador(sapo, LARGURA / 4, ALTURA - 10, 1,2)
    jogador2 = Jogador(galinha, LARGURA / 1.5, ALTURA - 10, 2,1)
    # barradevida recebe o seu asset e posicao aonde ele vai ficar na tela
    barradevidaj1 = Barradevida(assets, 30, 10)
    barradevidaj2 = Barradevida(assets, 1200, 10) 
    barramanaj1 = BarraMana(assets, 30, 140, 1,2)
    barramanaj2 = BarraMana(assets, 1200, 140, 2,1)
    all_sprites.add(jogador1)
    all_sprites.add(jogador2)

    # ---Dados da contagem regressiva do jogo
    timermin = 1
    timersegundos = 30
    timerfonte = assets["tempo_fonte"]
    timertexto = timerfonte.render("01:30", True, CORAL)
    # userevent - evento personalidado o qual é associado com a variavel pygame.time.set_timer, possibilitando ter um delay de 1s a cada valor contado
    timer = pygame.USEREVENT + 1
    pygame.time.set_timer(timer, 1000)

    MORTO = 0
    JOGANDO = 1
    state = JOGANDO

    tecla_precionada = {}

    pygame.mixer.music.play(loops=-1)
    while state != MORTO:
        clock.tick(FPS)
        tempo = pygame.time.get_ticks()

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
                    if event.key == pygame.K_a:
                        jogador1.speedx -= 8
                    if event.key == pygame.K_d:
                        jogador1.speedx += 8
                    if event.key == pygame.K_w:
                        jogador1.pulo()
                    if event.key == pygame.K_s:
                        jogador1.defesa()
                    if event.key == pygame.K_q and jogador2.defende == False:
                        # se o jogador 1 apertar espaço e o jogador 2 estiver perto, ele vai poder bater
                        jogador1.bateu(jogador1, jogador2)

                    # Teclas jogador 2
                    if event.key == pygame.K_LEFT:
                        jogador2.speedx -=8
                    if event.key == pygame.K_RIGHT:
                        jogador2.speedx +=8
                    if event.key == pygame.K_UP:
                        jogador2.pulo()
                    if event.key == pygame.K_DOWN:
                        jogador2.defesa()
                    if event.key == pygame.K_SPACE and jogador1.defende == False: 
                        # consegue atacar somente se o oponente não estiver defendendo
                        # se o jogador 2 apertar a tecla e o jogador 1 estiver perto, ele vai poder bater
                        jogador2.bateu(jogador2, jogador1)
                    
                if event.type == pygame.KEYUP:
                    if event.key in tecla_precionada and tecla_precionada[event.key]:
                        # Teclas jogador 1
                        if event.key == pygame.K_a:
                            jogador1.speedx += 8
                        if event.key == pygame.K_d:
                            jogador1.speedx -= 8
                        if event.key == pygame.K_s:
                            jogador1.defende = False

                        # Teclas jogador 2
                        if event.key == pygame.K_LEFT:
                            jogador2.speedx +=8
                        if event.key == pygame.K_RIGHT:
                            jogador2.speedx -=8
                        if event.key == pygame.K_DOWN:
                            jogador2.defende = False
                
                # checa eventos de tempo
                if event.type == timer:
                    # se o temporizador for maior que 0 vair rodar
                    if timersegundos > 0 or timermin > 0:
                        if timersegundos > 0:
                            timersegundos -= 1
                        else:
                            # serve para transformar minutos em segundos
                            timermin -= 1
                            timersegundos = 59
                        timertexto = timerfonte.render("%02d:%02d" % (timermin, timersegundos), True, (255, 255, 200))
                    else: 
                        # quando termina o evento de tempo acaba
                        pygame.time.set_timer(timer,0)
                        state = MORTO
                
        # Atualiza estado do jogo
        all_sprites.update()
        barramanaj1.update()
        barramanaj2.update()


        # Se o jogador 1 ou 2 perder toda vida o jogo acaba
        if jogador1.saude <= 0 or jogador2.saude <=0: 
            state = MORTO
        
        # ----Saídas 
        tela.fill((72,61,139))
        all_sprites.draw(tela)

        # ela.blit(pegaimagem(assets['galinha_idle'],32,34,3), (0,0))t
        
        # Atualiza barra de vida
        barradevidaj1.desenhar_barra(tela, jogador1.saude)
        barradevidaj2.desenhar_barra(tela,jogador2.saude)
        barramanaj1.drawbarra(tela)
        barramanaj2.drawbarra(tela)
        # atualiza o temporizador
        tela.blit(timertexto, (820, 50))
    
        pygame.display.update()


