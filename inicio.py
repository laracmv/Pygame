import pygame
import sys
from dados_jogo import *

class Botao:
    def __init__(self, texto, largura, altura, posicao):
        #atributos principais
        self.pressed = False
        self.hovered = False

        #retangulo de cima (top)
        self.retangulo_cima = pygame.Rect(posicao, (largura, altura))
        self.cor_cima = cor_inicio

        #retangulo de baixo
        self.retangulo_baixo = pygame.Rect(posicao, (largura, altura))
        self.cor_baixo = cor_inicio

        #fonte do texto
        self.fonte = pygame.font.Font(None, 30)

        #Texto
        self.surface_texto = self.fonte.render(texto, True, cor_texto_botao)
        self.retangulo_texto = self.surface_texto.get_rect(center=self.retangulo_cima.center)

    def draw(self):
        pygame.draw.rect(tela, self.cor_cima, self.retangulo_cima, border_radius=12)

        if self.pressed or self.hovered:
            pygame.draw.rect(tela, self.cor_baixo, self.retangulo_baixo, border_radius=12)
        else:
            pygame.draw.rect(tela, cor_inicio, self.retangulo_baixo, border_radius=12)

        tela.blit(self.surface_texto, self.retangulo_texto)
        self.clicar()

    def clicar(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.retangulo_cima.collidepoint(mouse_pos):
            self.cor_cima = cinza

            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    print('click')
                    self.pressed = False
        else:
            self.hovered = False
            self.cor_cima = cor_inicio

#Inicializa o Pygame após as definições de cores
pygame.init()
telaa = (1500,780)
tela = pygame.display.set_mode(telaa)
pygame.display.set_caption('Início')
clock = pygame.time.Clock()

# Carrega a imagem de fundo
fundo = pygame.image.load('assets\\img\\tela inicio.jpg')
fundo = pygame.transform.scale(fundo, telaa)

#botoes
posicao_botao1 = ((telaa[0] - 200) // 2, (telaa[1] - 40) // 2 - 40)
posicao_botao2 = ((telaa[0] - 200) // 2, (telaa[1] - 40) // 2 + 40)

# argumentos para o botão: O que escreve nele, largura e altura dele, e onde fica.
botao1 = Botao('Jogar', 200, 40, botao_top)
botao2 = Botao('Instruções', 200, 40, botao_baixo)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.blit(fundo, (0, 0))  #Desenha a imagem de fundo

    botao1.draw()
    botao2.draw()

    pygame.display.update()
    clock.tick(60)