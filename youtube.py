import pygame

#------para animações galinha
galinha_dic = {"idle": [],
                "hit": [],
                "run": []
                }

#para animacao da galinha em idle
gidle0 = pygame.image.load("assets//img//galinha//idle//tile000.png")
galinha_largura = gidle0.get_width() #estabelece largura da galinha
galinha_altura = gidle0.get_height() #estabelece largura da galinha
gidle0 = pygame.transform.scale(gidle0, (galinha_altura * 4 ,galinha_largura * 4 )) #redimenciona escala galinha
galinha_dic["idle"].append(gidle0) #adiciona no dicionario idle

i = 1
while i<13:
    if i>=1 and i<10:
        gidle = pygame.image.load(f'assets//img//galinha//idle//tile00{i}.png')
        gidle = pygame.transform.scale(gidle , (galinha_altura * 4 ,galinha_altura * 4 ))
    else:
        gidle = pygame.image.load(f'assets//img//galinha//idle//tile0{i}.png')
        gidle = pygame.transform.scale(gidle , (galinha_altura * 4 ,galinha_altura * 4 ))
    galinha_dic["idle"].append(gidle)
    i+=1

#Animação hit galinha
ghit0 = pygame.image.load("assets//img//galinha//hit//tile000.png")
ghit0 = pygame.transform.scale(ghit0, (galinha_altura * 4 ,galinha_largura * 4 ))
galinha_dic["hit"].append(ghit0)

i = 1
while i<5:
    ghit = pygame.image.load(f'assets//img//galinha//hit//tile00{i}.png')
    ghit = pygame.transform.scale(ghit, (galinha_altura * 4 ,galinha_largura * 4 ))
    galinha_dic["hit"].append(ghit)
    i+=1


#------para animações sapo 
sapo_dic = {"idle": [],
                "hit": [],
                "run": []
                }


galinha = galinha_dic