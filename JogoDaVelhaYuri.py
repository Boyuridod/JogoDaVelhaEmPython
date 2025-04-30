# TODO Organizar melhor o código
# Desenvolvido por: Yuri David Silva Duarte
# Instagram @yuridsduarte

# python -m PyInstaller --onefile --windowed --icon=Images/favicon.ico --add-data "Images;Images" JogoDaVelhaYuri.py
# python -m PyInstaller --onefile --windowed --icon=Images/favicon.ico --add-data 'Images;"Images"' JogoDaVelhaYuri.py

import pygame #pip install pygame
import os
import sys
import tkinter as tk

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Diretório temporário criado pelo PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")  # Modo normal (sem empacotar)

    return os.path.join(base_path, relative_path)

# Pega o tamanho da tela com tkinter (sem abrir janela)
root = tk.Tk()
root.withdraw()
largura = root.winfo_screenwidth()
altura = root.winfo_screenheight()
root.destroy()  # Libera recursos do tkinter

pygame.init()

# Configurações da janela
larguraJogo = largura * 0.2
alturaJogo = altura * 0.5
tela = pygame.display.set_mode((larguraJogo, alturaJogo))
pygame.display.set_caption("Jogo da Velha | Por: Yuri Duarte")

# Carrega o ícone (formato PNG recomendado)
icone = pygame.image.load(resource_path("Images/Icone.png"))

# Define o ícone da janela
pygame.display.set_icon(icone)

# Cores
preto = (10, 10, 10)
vermelho = (200, 14, 14)
branco = (255, 255, 255)
cinza = (170, 170, 170)
cinza_claro = (100, 100, 100)

# Definindo a fonte
fonte = pygame.font.SysFont('arial', int(larguraJogo * 0.10))

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
larX = larguraJogo * 0.3
larY = alturaJogo * 0.22
distanciaX = (larguraJogo - larX) * 0.034
distanciaY = (alturaJogo - larY) * 0.03

# Inicializa o placar na tela
placarTela = [
    pygame.Rect((distanciaX + ((distanciaX + larX) * 0)), (distanciaY + ((distanciaY + larY) * 0)), larX, larY),
    pygame.Rect((distanciaX + ((distanciaX + larX) * 1)), (distanciaY + ((distanciaY + larY) * 0)), larX, larY),
    pygame.Rect((distanciaX + ((distanciaX + larX) * 2)), (distanciaY + ((distanciaY + larY) * 0)), larX, larY),
]

# Inicializa o tabuleiro de botões na tela
tabuleiroBotao = [
    [pygame.Rect((distanciaX + ((distanciaX + larX) * 0)), (distanciaY + ((distanciaY + larY) * 1)), larX, larY),
     pygame.Rect((distanciaX + ((distanciaX + larX) * 1)), (distanciaY + ((distanciaY + larY) * 1)), larX, larY),
     pygame.Rect((distanciaX + ((distanciaX + larX) * 2)), (distanciaY + ((distanciaY + larY) * 1)), larX, larY)],

    [pygame.Rect((distanciaX + ((distanciaX + larX) * 0)), (distanciaY + ((distanciaY + larY) * 2)), larX, larY),
     pygame.Rect((distanciaX + ((distanciaX + larX) * 1)), (distanciaY + ((distanciaY + larY) * 2)), larX, larY),
     pygame.Rect((distanciaX + ((distanciaX + larX) * 2)), (distanciaY + ((distanciaY + larY) * 2)), larX, larY)],

    [pygame.Rect((distanciaX + ((distanciaX + larX) * 0)), (distanciaY + ((distanciaY + larY) * 3)), larX, larY),
     pygame.Rect((distanciaX + ((distanciaX + larX) * 1)), (distanciaY + ((distanciaY + larY) * 3)), larX, larY),
     pygame.Rect((distanciaX + ((distanciaX + larX) * 2)), (distanciaY + ((distanciaY + larY) * 3)), larX, larY)],
]

# Função que limpa o tabuleiro
def limpaTabuleiro():
    tabuleiro = []

    for i in range(3):
        tabuleiro.append([])
        for j in range(3):
            tabuleiro[i].append("")

    return tabuleiro

# Função que desenha o tabuleiro na tela
def desenhaTela():
    mouse = pygame.mouse.get_pos()

    placar[1] = jogador

    for i in range(len(placar)):
        pygame.draw.rect(tela, vermelho, placarTela[i])
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

# Verifica se algum jogador ganhou
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
    
    return verificaVelha()

# Verifica se deu velha
def verificaVelha():
    for linha in tabuleiro:
        for i in linha:
            if(i == ''):
                return i
    
    return "V"
            
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

                        ganhador = verificaGanhador()

                        # TODO Fazer uma animação de ganhar ou dar velha
                        if(ganhador != ""):
                            if(ganhador == "O"):
                                placar[0] += 1
                            elif(ganhador == "X"):
                                placar[2] += 1
                            else:
                                print(ganhador)

                            tabuleiro = limpaTabuleiro()

    # TODO otimizar este trecho, pois ele está sempre apagando e desenhando a tela
    tela.fill(preto)
    desenhaTela()

    pygame.display.update()

pygame.quit()
sys.exit()