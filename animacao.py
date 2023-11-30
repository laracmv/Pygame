import pygame

escala = 4 # usado para aumentar ou diminui imagens

#------para animações galinha
galinha_dic = {"idle": [],
                "hit": [],
                }

#para animacao da galinha parada
gidle0 = pygame.image.load("assets//img//galinha//idle//tile000.png")
gidle0 = pygame.transform.flip(gidle0, True, False)
galinha_largura = gidle0.get_width() #estabelece largura da galinha
galinha_altura = gidle0.get_height() #estabelece largura da galinha
gidle0 = pygame.transform.scale(gidle0, (galinha_altura * escala ,galinha_largura * escala)) #redimenciona escala galinha
galinha_dic["idle"].append(gidle0) #adiciona no dicionario idle

i = 1
while i<13:
    if i>=1 and i<10:
        gidle = pygame.image.load(f'assets//img//galinha//idle//tile00{i}.png')
        gidle = pygame.transform.flip(gidle, True, False)
        gidle = pygame.transform.scale(gidle , (galinha_altura * escala ,galinha_altura * escala))
    else:
        gidle = pygame.image.load(f'assets//img//galinha//idle//tile0{i}.png')
        gidle = pygame.transform.flip(gidle, True, False)
        gidle = pygame.transform.scale(gidle , (galinha_altura * escala,galinha_altura * escala))
    galinha_dic["idle"].append(gidle)
    i+=1

#Animação hit galinha
ghit0 = pygame.image.load("assets//img//galinha//hit//tile000.png")
ghit0 = pygame.transform.flip(ghit0, True, False)
ghit0 = pygame.transform.scale(ghit0, (galinha_altura * escala ,galinha_largura * escala ))
galinha_dic["hit"].append(ghit0)

i = 1
while i<5:
    ghit = pygame.image.load(f'assets//img//galinha//hit//tile00{i}.png')
    ghit = pygame.transform.flip(ghit, True, False)
    ghit = pygame.transform.scale(ghit, (galinha_altura * escala,galinha_largura * escala))
    galinha_dic["hit"].append(ghit)
    i+=1

#------para animações sapo 
sapo_dic = {"idle": [],
                "hit": [],
                }

#para animacao do sapo parada
sapoidle0 = pygame.image.load("assets//img//sapo//idle//tile000.png")
sapo_largura = sapoidle0.get_width() #estabelece largura da galinha
sapo_altura = sapoidle0.get_height() #estabelece largura da galinha
sapoidle0= pygame.transform.scale(sapoidle0, (sapo_altura * escala,sapo_largura * escala)) #redimenciona escala sapo
sapo_dic["idle"].append(sapoidle0) #adiciona no dicionario idle

i = 1
while i < 11:
    if i>=1 and i<10:
        sapoidle = pygame.image.load(f'assets//img//sapo//idle//tile00{i}.png')
        sapoidle = pygame.transform.scale(sapoidle, (sapo_altura * escala,sapo_altura * escala))
    else:
        sapoidle = pygame.image.load(f'assets//img//sapo//idle//tile0{i}.png')
        sapoidle = pygame.transform.scale(sapoidle, (sapo_altura * escala,sapo_altura * escala))
    sapo_dic["idle"].append(sapoidle)
    i+=1

#animacao sapo batendo
sapohit0 = pygame.image.load("assets//img//sapo//hit//tile000.png")
sapohit0= pygame.transform.scale(sapohit0, (sapo_altura * escala,sapo_largura * escala))
sapo_dic["hit"].append(sapohit0)

i=1
while i<7:
    sapohit = pygame.image.load(f'assets//img//sapo//hit//tile00{i}.png')
    sapohit = pygame.transform.scale(sapohit, (sapo_altura * escala,sapo_altura * escala))
    sapo_dic["hit"].append(sapohit)
    i+=1

#----dicionários com acoes dos personagens
galinha = galinha_dic 
sapo = sapo_dic