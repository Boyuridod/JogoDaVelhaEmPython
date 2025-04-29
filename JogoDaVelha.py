# TODO Organizar melhor o código

import pygame #pip install pygame
import sys

pygame.init()

# TODO Deixar o tamanho da janela do jogo responsiva com o tamanho do monitor

# Configurações da janela
largura, altura = 480, 640
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Velha")

# Cores
preto = (10, 10, 10)
vermelho = (255, 0, 0)
branco = (255, 255, 255)
cinza = (170, 170, 170)
cinza_claro = (100, 100, 100)

# Definindo a fonte
fonte = pygame.font.SysFont('arial', 12)

# Inicializa o placar
placar = [0, "O", 0]

# Variavel que define de qual jogador é a jogada
jogador = placar[1]

# Inicializa o tabuleiro
tabuleiro = []

for i in range(3):
    tabuleiro.append([])
    for j in range(3):
        tabuleiro[i].append("")

# Posição das informações na tela
posX = 10
posY = 10
tamX = 50
tamY = 50

# Inicializa o placar na tela
placarTela = [
    pygame.Rect((posX), (posY), (tamX), (tamY)),
    pygame.Rect((posX + 60), (posY), (tamX), (tamY)),
    pygame.Rect((posX + 120), (posY), (tamX), (tamY))
]

# Inicializa o tabuleiro de botões na tela
# FIXME Posso inicializar isto dinamicamente
tabuleiroBotao = [
    [pygame.Rect((posX), (posY + 60), (tamX), (tamY)),
     pygame.Rect((posX + 60), (posY + 60), (tamX), (tamY)),
     pygame.Rect((posX + 120), (posY + 60), (tamX), (tamY))],
    
    [pygame.Rect((posX), (posY + 120), (tamX), (tamY)),
     pygame.Rect((posX + 60), (posY + 120), (tamX), (tamY)),
     pygame.Rect((posX + 120), (posY + 120), (tamX), (tamY))],
    
    [pygame.Rect((posX), (posY + 180), (tamX), (tamY)),
     pygame.Rect((posX + 60), (posY + 180), (tamX), (tamY)),
     pygame.Rect((posX + 120), (posY + 180), (tamX), (tamY))],
]

#
def limpaTabuleiro():
    tabuleiro = []

    for i in range(3):
        tabuleiro.append([])
        for j in range(3):
            tabuleiro[i].append("")

# Função que desenha o tabuleiro na tela
def desenhaTela():
    mouse = pygame.mouse.get_pos()

    placar[1] = jogador

    for i in range(len(placar)):
        pygame.draw.rect(tela, cinza, placarTela[i])
        texto = fonte.render(str(placar[i]), True, preto)
        texto_rect = texto.get_rect(center = placarTela[i].center)
        tela.blit(texto, texto_rect)

    for i in range(len(tabuleiroBotao)):
        for j in range(len(tabuleiroBotao[i])):
            # TODO Trocar a cor para uma que faz sentido
            if (tabuleiroBotao[i][j].collidepoint(mouse) and tabuleiro[i][j] == ""):
                cor = vermelho
            else:
                cor = cinza

            pygame.draw.rect(tela, cor, tabuleiroBotao[i][j])

            texto = fonte.render(tabuleiro[i][j], True, preto)
            texto_rect = texto.get_rect(center = tabuleiroBotao[i][j].center)
            tela.blit(texto, texto_rect)

#
def verificaGanhador():
    if(tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2]):
        return tabuleiro[0][0]
        
    if(tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[0][2] == tabuleiro[2][0]):
        return tabuleiro[0][2]
        
    for i in range(len(tabuleiro)):
        if(tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][0] == tabuleiro[i][2]):
            return tabuleiro[i][0]
            
        elif(tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[0][i] == tabuleiro[2][i]):
            return tabuleiro[0][i]
    
    # TODO verificar velha
    return 0
            
# Loop principal
jogando = True
while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(tabuleiroBotao)):
                for j in range(len(tabuleiroBotao[i])):
                    btn = tabuleiroBotao[i][j]
                    if (btn.collidepoint(evento.pos) and tabuleiro[i][j] == ""):
                        tabuleiro[i][j] = jogador

                        if(jogador == "O"):
                            jogador = "X"
                        else:
                            jogador = "O"

                        print(jogador)

                        ganhador = verificaGanhador()

                        # TODO Fazer uma animação de ganhar
                        if(ganhador != ""):
                            if(ganhador == "O"):
                                placar[0] += 1
                            else:
                                placar[3] += 1
                            
                            # FIXME Ele não reinicia o tabuleiro
                            limpaTabuleiro()

    # TODO otimizar este trecho, pois ele está sempre apagando e desenhando a tela
    tela.fill(preto)
    desenhaTela()

    pygame.display.update()

pygame.quit()
sys.exit()