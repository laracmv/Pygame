import pygame
import sys
import os
import assets
from jogo import *

# Inicialização do Pygame
pygame.init()

# Definindo algumas constantes
WIDTH, HEIGHT = 1500, 780
FPS = 60

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Classe para representar um botão simples
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

# Gerar tela principal
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo de Luta')


state = JOGO
# mudar para state = iniciar quando tiver criado tela de inicio
while state != FIM:
    # if state == INICIO:
    # Usa esse 1o if quanto tiver tela inicio
    if state == JOGO:
        # vai para tela do jogo
        state = tela_de_jogo(tela)
    else:  
        state = FIM
    
    tela.fill((PRETO))

pygame.quit()


# Criando a tela final
end_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tela Final")

# Carregando a imagem de "game_over2.jpg"
game_over_image = pygame.image.load(os.path.join("assets\\img\\game over2.jpg"))
game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))


# Criando o botão Jogar
play_button = Button(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50, "Jogar", "play")

# Variável para controlar a tela atual
current_screen = "start"

# Loop principal
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Troca para a tela do jogo quando a tecla de espaço é pressionada
                if current_screen == "start" and play_button.is_clicked(pygame.mouse.get_pos()):
                    current_screen = "game"
                # Troca para a tela final quando a tecla de espaço é pressionada na tela do jogo
                elif current_screen == "game":
                    current_screen = "end"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se o botão foi clicado
            if current_screen == "start" and event.button == 1 and play_button.is_clicked(event.pos):
                current_screen = "game"

    # Desenhar na tela de início
    if current_screen == "start":
        start_screen.fill(WHITE)
        play_button.draw(start_screen)

    # Desenhar na tela do jogo
    elif current_screen == "game":
        game_screen.fill(WHITE)
        # Adicione aqui o desenho ou a lógica do seu jogo

    # Desenhar na tela final
    elif current_screen == "end":
        end_screen.fill(WHITE)
        # Exibindo a imagem de "game_over2.jpg"
        end_screen.blit(game_over_image, (0, 0))

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()