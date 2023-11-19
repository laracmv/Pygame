import pygame
from dados_jogo import largura,altura

#inicia
pygame.init()
#tamanho da tela
tela = pygame.display.set_mode(largura,altura)
#titulo da tela
pygame.display.set_caption('Jogo')
#variaveis
fundo = pygame.image.load('C:\\Users\\laisa\\Downloads\\WhatsApp Image 2023-11-13 at 15.37.07.jpeg')

#fazer o loop
jogo = True

while True:
    #definir a tela de fundo
    tela.blit(fundo, (0,0)) #preenche a tela
    #para cada coisa que acontece no jogo, clicar, fechar, etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
    
    
    #tela.fill((255,255,255))
    pygame.display.update()

#finaliza
pygame.quit()