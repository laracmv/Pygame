import pygame
import sys

# Defina as cores
cor_inicio = (100, 100, 100)
cinza = (150, 150, 150)
cor_texto_botao = (255, 255, 255)
fundo_inicio = (0, 0, 0)

# Defina as configurações da tela
tela_inicio = (800, 600)

# Classe Botao modificada para incluir espaços para imagens e tornar os botões clicáveis
class Botao:
    def __init__(self, imagem_path, largura, altura, posicao):
        self.pressed = False
        self.rect = pygame.Rect(posicao, (largura, altura))
        self.cor = cor_inicio

        # Carrega a imagem
        self.imagem = pygame.image.load(imagem_path)
        # Redimensiona a imagem para se ajustar ao botão
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))

    def draw(self):
        pygame.draw.rect(tela, self.cor, self.rect, border_radius=12)
        # Desenha a imagem no botão
        tela.blit(self.imagem, self.rect.topleft)

    def clicar(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.cor = cinza
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    print('foi')
                    self.pressed = False
        else:
            self.cor = cor_inicio



pygame.init()
tela = pygame.display.set_mode(tela_inicio)
pygame.display.set_caption('Fundos')
clock = pygame.time.Clock()

botao1 = Botao('assets\\img\\fundo 1 jogo.jpg', 200, 40, (50, 50))
botao2 = Botao('assets\\img\\fundo 2 jogo.jpg', 200, 40, (50, 150))
botao3 = Botao('assets\\img\\fundo 3 jogo.jpg', 200, 40, (50, 250))
botao4 = Botao('assets\\img\\fundo 4 jogo.png', 200, 40, (50, 350))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(fundo_inicio)

    # desenha cada botão e clica nele
    botao1.draw()
    botao1.clicar()

    botao2.draw()
    botao2.clicar()

    botao3.draw()
    botao3.clicar()

    botao4.draw()
    botao4.clicar()

    pygame.display.update()
    clock.tick(60)