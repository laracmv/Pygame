import pygame 
from dados_jogo import *
from assets import *
from tela_de_jogo import *
from assets import *

def tela_final(tela):
    clock = pygame.time.Clock()

    #para dizer quem ganhou
    if Jogador.j1ganhou == True:
        ganhador = 'Sapo'
    else:
        ganhador = 'Galinha'

    #trecho extraido de chat.openai.com
    fonte = pygame.font.Font(None, 60)  # Você também pode fornecer o nome de uma fonte e o tamanho

    # Renderize o texto desejado
    texto = fonte.render(f" {ganhador} Ganhou! Tecle cima para jogar e baixo para fechar", True, white)

    # Posicione o texto no centro da tela
    pos_texto = texto.get_rect(center=(LARGURA// 2, ALTURA // 2))

    #trecho extraido de https://dessoft.insper-comp.com.br/conteudo/projeto
    running = True
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = FIM
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    state = JOGO
                    running = False
                if event.key == pygame.K_DOWN:
                    state = FIM
                    running = False

        tela.fill(PRETO)

        tela.blit(texto, pos_texto)

        pygame.display.flip()

    return state
