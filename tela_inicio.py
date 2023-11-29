import pygame
import sys

cor_inicio = (255, 255, 255)
cor_texto_botao = (0, 0, 0)
cinza = (128, 128, 128)

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
                if self.pressed:
                    self.pressed = False
                    if self.callback:
                        self.callback()

        else:
            self.hovered = False
            self.cor_cima = cor_inicio

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
        #Desenha a imagem de fundo
        self.tela.blit(self.fundo, (0, 0))
        #Desenha o botão
        self.botao_jogar.draw(self.tela)

    def draw(self):
        pygame.display.flip()

class TelaJogo:
    def __init__(self):
        self.telaa = (1500, 780)
        self.tela = pygame.display.set_mode(self.telaa)
        pygame.display.set_caption('Jogo')

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.tela.fill((255, 255, 255))

pygame.init()
tela_atual = TelaInicio()

clock = pygame.time.Clock()
while True:
    eventos = pygame.event.get()
    tela_atual.processar_eventos(eventos)

    tela_atual.update()
    tela_atual.draw()

    pygame.display.update()
    clock.tick(60)