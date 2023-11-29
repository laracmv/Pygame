import pygame
import sys
from dados_jogo import *
from assets import *

class Botao:
    def __init__(self, texto, image_path, largura, altura, posicao):
        #atributos principais
        self.click = False


        self.retangulo = pygame.Rect(posicao, (largura, altura))
        self.cor = cor_inicio

        #carregar os caminhos das imagens
        #redimensiona a imagem para se ajustar ao botão
        self.image = pygame.transform.scale(pygame.image.load(image_path), (largura, altura))

        # fonte do texto
        self.fonte = pygame.font.Font(None, 30)

        #texto
        self.superficie_texto = self.fonte.render(texto, True, cor_texto_botao)
        self.retangulo_texto = self.superficie_texto.get_rect(center=self.retangulo.center)

    def draw(self):
        pygame.draw.rect(tela, self.cor, self.retangulo, border_radius=12) #esse border raius define o raio da borda do retangulo
        tela.blit(self.image, self.retangulo.topleft)
        tela.blit(self.superficie_texto, self.retangulo_texto)
        self.clicar()

    def clicar(self):
        posicao_mouse = pygame.mouse.get_pos() #saber a posição do mouse quando for clicar no botão
        if self.retangulo.collidepoint(posicao_mouse):
            self.cor = cinza
            if pygame.mouse.get_pressed()[0]: #se o jogador está pressionando o botao
                if not self.click:
                    print('clique')
                    self.click = True #se ele estiver pressionando, então é verdade
        else:
            self.cor = cor_inicio
            self.clicado = False

# Inicializa o Pygame após as definições de cores
pygame.init()

# Ajusta a largura total da tela para acomodar os quatro botões
tela = pygame.display.set_mode((tela_inicio[0], tela_inicio[1]))

pygame.display.set_caption('Fundos')
clock = pygame.time.Clock()

# argumentos para o botão: O que escreve nele, largura e altura dele, e onde fica.
posicao_botao1 = (50, tela_inicio[1] // 2 - 250 // 2)
posicao_botao2 = (50, tela_inicio[1] // 2 + 20)
posicao_botao3 = (tela_inicio[0] - 670, tela_inicio[1] // 2 - 200 // 2)
posicao_botao4 = (tela_inicio[0] - 670, tela_inicio[1] // 2 + 20)

# Instâncias de botão
botao1 = Botao('Botão 1', 'assets\\img\\fundo 1 jogo.jpg', 590, 280, posicao_botao1)
botao2 = Botao('Botão 2', 'assets\\img\\fundo 2 jogo.jpg', 590, 280, posicao_botao2)
botao3 = Botao('Botão 3', 'assets\\img\\fundo 3 jogo.jpg', 590, 280, posicao_botao3)
botao4 = Botao('Botão 4', 'assets\\img\\fundo 4 jogo.png', 590, 280, posicao_botao4)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(fundo_inicio)

    botao1.draw()
    botao2.draw()
    botao3.draw()
    botao4.draw()

    pygame.display.update()
    clock.tick(60)