import pygame
import sys
from dados_jogo import *

class Botao:
    def __init__(self, texto, largura, altura, posicao):
        # retangulo de cima (top)
        self.retangulo_superior = pygame.Rect(posicao, (largura, altura))
        self.cor_superior = cor_inicio

        # fonte do texto
        self.fonte = pygame.font.Font(None, 30)

        # Texto
        self.superficie_texto = self.fonte.render(texto, True, black)
        self.rect_texto = self.superficie_texto.get_rect(center=self.retangulo_superior.center)

    def draw(self):
        pygame.draw.rect(tela, self.cor_superior, self.retangulo_superior)
        tela.blit(self.superficie_texto, self.rect_texto)

# Inicializa o Pygame após as definições de cores
pygame.init()
tela = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Início')
clock = pygame.time.Clock()

# Importa a cor black do arquivo dados_jogo
black = (0, 0, 0)

# Instancia o botão com os argumentos corretos
botao1 = Botao('Jogar', 200, 40, (200, 250))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(black)
    botao1.draw()

    # Corrige o erro de digitação na linha a seguir (update em vez de uptade)
    pygame.display.update()
    clock.tick(60)