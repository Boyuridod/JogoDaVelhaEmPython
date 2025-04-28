import pygame #pip install pygame
import sys

pygame.init()

# Configurações da janela
largura, altura = 480, 640
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Meu Primeiro Jogo')

# Cores
preto = (10, 10, 10)
vermelho = (255, 0, 0)
branco = (255, 255, 255)
cinza = (170, 170, 170)
cinza_claro = (100, 100, 100)

# Definindo a fonte
fonte = pygame.font.SysFont('arial', 12)

#
posBtnX = 10
posBtnY = 10
tamBtnX = 50
tamBtnY = 50

tabuleiro = [
    [pygame.Rect((posBtnX), (posBtnY), (tamBtnX), (tamBtnY)),
     pygame.Rect((posBtnX + 60), (posBtnY), (tamBtnX), (tamBtnY)),
     pygame.Rect((posBtnX + 120), (posBtnY), (tamBtnX), (tamBtnY))],
    
    [pygame.Rect((posBtnX), (posBtnY + 60), (tamBtnX), (tamBtnY)),
     pygame.Rect((posBtnX + 60), (posBtnY + 60), (tamBtnX), (tamBtnY)),
     pygame.Rect((posBtnX + 120), (posBtnY + 60), (tamBtnX), (tamBtnY))],
    
    [pygame.Rect((posBtnX), (posBtnY + 120), (tamBtnX), (tamBtnY)),
     pygame.Rect((posBtnX + 60), (posBtnY + 120), (tamBtnX), (tamBtnY)),
     pygame.Rect((posBtnX + 120), (posBtnY + 120), (tamBtnX), (tamBtnY))],
]

#
def desenhaTabulero():
    mouse = pygame.mouse.get_pos()

    # TODO Trocar a cor para uma que faz sentido
    for linha in tabuleiro:
        for btn in linha:
            if btn.collidepoint(mouse):
                cor = vermelho
            else:
                cor = cinza

            pygame.draw.rect(tela, cor, btn)

            texto = fonte.render("O", True, preto)
            texto_rect = texto.get_rect(center=btn.center)
            tela.blit(texto, texto_rect)

jogador = 1

def vez(x):
    if (x == 1):
        return 0

    else: return 1

def jogada(botao):



    jogador = vez(jogador)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            for linha in tabuleiro:
                for btn in linha:
                    if btn.collidepoint(evento.pos):
                        jogada(btn)

    #TODO otimizar este trecho, pois ele está sempre apagando e desenhando a tela
    tela.fill(preto)
    desenhaTabulero()

    pygame.display.update()

pygame.quit()
sys.exit()