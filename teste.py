import pygame
import sys
from dados_jogo import *

class Botao:
    def __init__(self, texto, largura, altura, posicao):
        #atributos principais
        self.pressed = False

        # retangulo de cima (top)
        self.retangulo_cima = pygame.Rect(posicao, (largura, altura))
        self.cor_cima = cor_inicio

        #retangulo de baixo
        self.retangulo_baixo = pygame.Rect(posicao, (100,50))
        self.cor_baixo = cor_inicio

        # fonte do texto
        self.fonte = pygame.font.Font(None, 30)

        # Texto
        self.surface_texto = self.fonte.render(texto, True, cor_texto_botao)
        self.retangulo_texto = self.surface_texto.get_rect(center=self.retangulo_cima.center)

        self.surfaceb_texto = self.fonte.render(texto, True, cor_texto_botao)
        self.retangulob_texto = self.surfaceb_texto.get_rect(top=self.retangulo_baixo.top)


    def draw(self):
        pygame.draw.rect(tela, self.cor_cima, self.retangulo_cima,border_radius = 12) #esse border raius define o raio da borda do retangulo

        pygame.draw.rect(tela,self.cor_baixo,self.retangulo_baixo, border_radius=12)

        tela.blit(self.surface_texto, self.retangulo_texto)
        tela.blit(self.surface_texto, self.retangulo_texto)
        self.clicar()
    

    def clicar(self):
        mouse_pos = pygame.mouse.get_pos() #saber a posição do mouse quando for clicar no botão
        if self.retangulo_cima.collidepoint(mouse_pos): #se nosso mouse ta no nosso botão
            self.cor_cima = cinza

            if pygame.mouse.get_pressed()[0]: #se o jogador está pressionando o botao
                self.pressed = True #se ele estiver pressionando, então é verdade
            else:
                if self.pressed == True:
                    print('click')
                    self.pressed = False #so mostra o click se foi clicado, se não não
        else:
            self.cor_cima = cor_inicio


# Inicializa o Pygame após as definições de cores
pygame.init()
tela = pygame.display.set_mode(tela_inicio)
pygame.display.set_caption('Início')
clock = pygame.time.Clock()


# argumentos para o botão: O que escreve nele, largura e altura dele, e onde fica.
botao1 = Botao('Jogar', 200, 40, botao_top)
botao2 = Botao('Sair',200, 40, botao_baixo)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(fundo_inicio)
    botao1.draw()
    botao2.draw()

    # Corrige o erro de digitação na linha a seguir (update em vez de uptade)
    pygame.display.update()
    clock.tick(60)