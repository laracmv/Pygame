import pygame
import sys
import os
from jogo import *


pygame.init()

WIDTH, HEIGHT = 1500, 780
FPS = 60

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# Criando a tela de início
start_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tela de Início")


# Criando a tela do jogo
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tela do Jogo")


# Criando a tela final
end_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tela Final")


# Carregando a imagem de "game_over2.jpg"
game_over_image = pygame.image.load(os.path.join("assets", "img", "game over2.jpg"))
game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

# Criando o botão Jogar
play_button = Button(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50, "Jogar", "play")


# Variável para controlar o estado do jogo
state = "start"


# Loop principal
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if state == "start":
        start_screen.fill(WHITE)
        play_button.draw(start_screen)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = "game"
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and play_button.is_clicked(event.pos):
                state = "game"

    elif state == "game":

        # Vai para tela do jogo
        #vai para a tela de inicio

        #tela_inicio(start_screen)

        tela_de_jogo(game_screen)
        pygame.display.flip()

        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting_for_key = False
                elif event.type == pygame.QUIT:
                    running = False
                    waiting_for_key = False


        #após a tela de jogo, vá para a tela final
        state = "end"

    elif state == "end":
        end_screen.fill(WHITE)
        end_screen.blit(game_over_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False


    # Atualizar a tela
    pygame.display.flip()


# Encerrar o Pygame
pygame.quit()
sys.exit()