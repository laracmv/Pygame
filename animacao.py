import pygame

def pegaimagem(animacao, largura, altura, escala):
    imagem = pygame.Surface((largura, altura)).convert_alpha()
    imagem.blit(animacao, (0,0), (0,0, largura, altura)) #mostra imagem na tela. O 3 argumento pega a porcao da imagem a ser usada
    imagem = pygame.transform.scale(imagem, (largura * escala, altura * escala))
    return imagem