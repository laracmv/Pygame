import pygame
from dados_jogo import *
from assets import load_assets
from sprits import Jogador, Barradevida, BarraMana
from animacao import *
from tela_de_jogo import *

def tela_de_inicio(tela):
    fonte = pygame.font.Font(None, 36)
    texto_inicio = fonte.render("Bem-vindas(o) a Revolução dos Bichos !!", True, (255, 255, 255))
    instrucoes = fonte.render("Pressione ESPAÇO para começar", True, (255, 255, 255))

    pos_texto_inicio = ((LARGURA - texto_inicio.get_width()) // 2, ALTURA // 3)
    pos_instrucoes = ((LARGURA - instrucoes.get_width()) // 2, ALTURA // 2)

    clock = pygame.time.Clock()

    state = INICIAR

    while True:
        tela.fill((0, 0, 0))
        tela.blit(texto_inicio, pos_texto_inicio)
        tela.blit(instrucoes, pos_instrucoes)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                return JOGO

            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        clock.tick(FPS)

def main():
    pygame.init()
    pygame.mixer.init()

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Jogo de Luta')

    assets = load_assets()
 
    state = INICIAR

    while state != FIM:
        if state == INICIAR:
            state = tela_de_inicio(tela)

        elif state == JOGO:
            state = tela_de_jogo(tela, assets)

        else:
            state = FIM

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()