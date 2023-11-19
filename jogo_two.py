import pygame
from dados_jogo import largura, altura, l, a, posg, posk
from sys import exit

pygame.init()
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock() #controla os frames por segundo

#imagem do céu
sky_surface = pygame.image.load('C:\\Users\\laisa\\OneDrive\\Área de Trabalho\\imagem_tela_inicio.webp')

#pygame.Surface((l,a))
#teste_surface.fill(branco)
#imagem do chão

ground_surface = pygame.image.load('C:\\Users\\laisa\\OneDrive\\Área de Trabalho\\ground.jpg')

#
jogo = True

while True:
    for event in pygame.event.get(): #dá todos os eventos
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #o loop acaba, ele nao uptade anymore
            
    
    tela.blit(sky_surface,posk) #aqui recebe a surface e a position
    tela.blit(ground_surface,posg)
    pygame.display.update() #ele atualiza a display.set_mode
    clock.tick(60) #esse loop não vai correr a mais que 60 frames por segundo, not run too fast