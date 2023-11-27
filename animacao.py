import pygame

escala = 4 # usado para aumentar ou diminui imagens

#------para animações galinha
galinha_dic = {"idle": [],
                "hit": [],
                }

#para animacao da galinha parada
gidle0 = pygame.image.load("assets//img//galinha//idle//tile000.png")
galinha_largura = gidle0.get_width() #estabelece largura da galinha
galinha_altura = gidle0.get_height() #estabelece largura da galinha
gidle0 = pygame.transform.scale(gidle0, (galinha_altura * escala ,galinha_largura * escala)) #redimenciona escala galinha
galinha_dic["idle"].append(gidle0) #adiciona no dicionario idle

i = 1
while i<13:
    if i>=1 and i<10:
        gidle = pygame.image.load(f'assets//img//galinha//idle//tile00{i}.png')
        gidle = pygame.transform.scale(gidle , (galinha_altura * escala ,galinha_altura * escala))
    else:
        gidle = pygame.image.load(f'assets//img//galinha//idle//tile0{i}.png')
        gidle = pygame.transform.scale(gidle , (galinha_altura * escala,galinha_altura * escala))
    galinha_dic["idle"].append(gidle)
    i+=1

#Animação hit galinha
ghit0 = pygame.image.load("assets//img//galinha//hit//tile000.png")
ghit0 = pygame.transform.scale(ghit0, (galinha_altura * escala ,galinha_largura * escala ))
galinha_dic["hit"].append(ghit0)

i = 1
while i<5:
    ghit = pygame.image.load(f'assets//img//galinha//hit//tile00{i}.png')
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

#------animacao para pedra
pedra_dic = {"idle": [],
            "hit": []
            }

#animacao idle pedra
pedraidle0 = pygame.image.load("assets//img//pedra//idle//tile000.png")
pedraidle_largura = pedraidle0.get_width()
pedraidle_altura = pedraidle0.get_width()
pedraidle0 = pygame.transform.scale(sapoidle0, (pedraidle_altura * escala,pedraidle_largura * escala))
pedra_dic["idle"].append(pedraidle0)

i = 1
while i < 13:
    if i>=1 and i<10:
        pedraidle = pygame.image.load(f'assets//img//pedra//idle//tile00{i}.png')
        pedraidle = pygame.transform.scale(sapohit, (pedraidle_altura * escala,pedraidle_altura * escala))
        pedra_dic["idle"].append(pedraidle)
    else:
        pedraidle = pygame.image.load(f'assets//img//pedra//idle//tile0{i}.png')
        pedraidle = pygame.transform.scale(sapohit, (pedraidle_altura * escala,pedraidle_altura * escala))
        pedra_dic["idle"].append(pedraidle)
    i+=1

#animacao hit pedra
pedrahit0 = pygame.image.load("assets//img//pedra//hit//tile000.png")
pedrahit_largura = pedraidle0.get_width()
pedrahit_altura = pedraidle0.get_width()
pedrahit0 = pygame.transform.scale(sapoidle0, (pedraidle_altura * escala,pedraidle_largura * escala))
pedra_dic["hit"].append(pedrahit0)

i = 1
while i < 4:
    pedrahit = pygame.image.load(f'assets//img//pedra//hit//tile00{i}.png')
    pedrahit = pygame.transform.scale(sapohit, (pedrahit_altura * escala,pedrahit_altura * escala))
    pedra_dic["hit"].append(pedrahit)
    i+=1

#----dicionários com acoes dos personagens
galinha = galinha_dic 
sapo = sapo_dic
pedra = pedra_dic