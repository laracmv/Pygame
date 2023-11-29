import pygame
import sys
from dados_jogo import *

pygame.init()

GAME = 1
GAME_OVER = 2
waiting_for_key = 2

# Inicialização da janela
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("troca telas")

# Função para a tela de início
def start_screen():
    screen.fill(0,0,0)

    pygame.display.flip()
    waiting_for_key()


# Função para a tela de game over
def game_over_screen():
    screen.fill(105,89,205)

    pygame.display.flip()
    waiting_for_key()


# Função para aguardar clicar no espaço para troca de telas
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False


# Função teste do jogo
def game_loop():
    # Inicialização de variáveis do jogo
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Lógica do jogo
        # Adicione aqui a lógica específica do seu jogo

        # Renderização
        screen.fill(black)
        # Adicione aqui elementos da tela do jogo (por exemplo, personagens, obstáculos)
        pygame.display.flip()

        # Controle de FPS
        pygame.time.Clock().tick(FPS)

    pygame.quit()
    sys.exit()

# Loop principal
game_state = JOGO

while True:
    if game_state == JOGO:
        start_screen()
        game_state = GAME
    elif game_state == GAME:
        game_loop()
        game_state = GAME_OVER
    elif game_state == GAME_OVER:
        game_over_screen()
        game_state = JOGO