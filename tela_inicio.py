import pygame
import sys
from dados_jogo import *
from assets import load_assets
from sprits import Jogador, Barradevida, BarraMana
from animacao import * 
from tela_de_jogo import *

class GameState:
    INICIO = "inicio"
    JOGO = "jogo"

    def __init__(self):
        self.state = self.INICIO
        self.next_state = None

    def transicao_para_jogo(self):
        self.next_state = self.JOGO

    def transicao_para_inicio(self):
        self.next_state = self.INICIO

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if self.state == self.INICIO:
                    tela_atual.botao_jogar.clicar()

    def update(self):
        if self.next_state:
            if self.next_state == self.JOGO:
                tela_atual = TelaJogo()
            elif self.next_state == self.INICIO:
                tela_atual = TelaInicio()
            self.state = self.next_state
            self.next_state = None

    def draw(self):
        tela_atual.update()
        tela_atual.draw()

class Botao:
    def __init__(self, texto, largura, altura, posicao, callback=None):
        self.pressed = False
        self.hovered = False

        self.retangulo_cima = pygame.Rect(posicao, (largura, altura))
        self.cor_cima = cor_inicio

        self.retangulo_baixo = pygame.Rect(posicao, (largura, altura))
        self.cor_baixo = cor_inicio

        self.fonte = pygame.font.Font(None, 30)
        self.surface_texto = self.fonte.render(texto, True, cor_texto_botao)
        self.retangulo_texto = self.surface_texto.get_rect(center=self.retangulo_cima.center)

        self.callback = callback

    def draw(self, tela):
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
                if self.pressed and self.callback:
                    self.pressed = False
                    self.callback()

        else:
            self.hovered = False
            self.cor_cima = cor_inicio
            
def tela_de_jogo(tela):
    def __init__(self):
        self.telaa = (1500, 780)
        self.tela = pygame.display.set_mode(self.telaa)
        pygame.display.set_caption('Jogo')
        self.fundo = pygame.image.load('assets\\img\\tela_jogo.jpg')  # Substitua pelo caminho correto
        self.fundo = pygame.transform.scale(self.fundo, self.telaa)

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        # Atualiza lógica do jogo se necessário
        pass

    def draw(self):
        self.tela.blit(self.fundo, (0, 0))
        tela_de_jogo(self.tela)  # Chama a função tela_de_jogo para desenhar a tela de jogo

    pass

class TelaInicio:
    def __init__(self):
        self.telaa = (1500, 780)
        self.tela = pygame.display.set_mode(self.telaa)
        pygame.display.set_caption('Início')
        self.fundo = pygame.image.load('assets\\img\\iniciooo.jpg')
        self.fundo = pygame.transform.scale(self.fundo, self.telaa)

        posicao_botao1 = (630, 330)
        self.botao_jogar = Botao('Jogar', 200, 40, posicao_botao1, callback=self.ir_para_tela_jogo)

    def ir_para_tela_jogo(self):
        self.proxima_tela = TelaJogo()

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                self.botao_jogar.clicar()

    def update(self):
        self.tela.blit(self.fundo, (0, 0))
        self.botao_jogar.draw(self.tela)

    def draw(self):
        pygame.display.flip()

class TelaJogo:
    def __init__(self):
        self.telaa = (1500, 780)
        self.tela = pygame.display.set_mode(self.telaa)
        pygame.display.set_caption('Jogo')
        self.fundo = pygame.image.load('assets\\img\\tela_jogo.jpg')  # Substitua pelo caminho correto
        self.fundo = pygame.transform.scale(self.fundo, self.telaa)

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        # Atualiza lógica do jogo se necessário
        pass

    def draw(self):
        self.tela.blit(self.fundo, (0, 0))
        #tela_de_jogo(self.tela)  # Chama a função tela_de_jogo para desenhar a tela de jogo


pygame.init()
game_state = GameState()
tela_atual = TelaInicio()
outra_tela = tela_de_jogo()

clock = pygame.time.Clock()
while True:
    eventos = pygame.event.get()
    tela_atual.processar_eventos(eventos)

    tela_atual.update()
    tela_atual.draw()
    outra_tela.draw

    if isinstance(tela_atual, TelaJogo):
        tela_atual.processar_eventos(eventos)
        tela_atual.update()
        tela_atual.draw()

    pygame.display.update()
    clock.tick(60)