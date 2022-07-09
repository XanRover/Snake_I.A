import pygame
from pygame.locals import *
from sys import exit
from random import randrange

black = (0,0,0)
white = (255,255,255)

pygame.init()

pygame.mixer.music.set_volume(0.01)
music_fundo = pygame.mixer.music.load('BoxCat Games - Battle (Boss).mp3')
pygame.mixer.music.play(-1)

music_colizao = pygame.mixer.Sound('smw_coin.wav')
music_colizao.set_volume(1)

largura = 600
altura = 520
tamanho = 20
tam = 15

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

x_control = 20
y_control = 0


x_maca = randrange(20, 600)
y_maca = randrange(50, 410)

velocidade = 20

fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake')
tempo = pygame.time.Clock()
lista_cobra = []

comprimento_inicial = 5
morreu = False

def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1,(x,y))

def aumenta_cobra(lista_cobra) :
    for XeY in lista_cobra :
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], tamanho, tamanho))


def reiniciar_jogo() :
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randrange(0, largura - tamanho, 20)
    y_maca = randrange(0, largura - tamanho, 20)

    morreu = False


while True :
    tela.fill((white))
    tempo.tick(10)

    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            exit()

        if event.type == KEYDOWN :
            if event.key == K_LEFT and y_control != 0 :
                x_control = -velocidade
                y_control = 0
            if event.key == K_RIGHT and y_control != 0 :
                x_control = velocidade
                y_control = 0
            if event.key == K_UP and x_control != 0 :
                x_control = 0
                y_control = -velocidade
            if event.key == K_DOWN and x_control != 0 :
                x_control = 0
                y_control = velocidade

    x_cobra = x_cobra + x_control
    y_cobra = y_cobra + y_control

    if x_cobra + tamanho > largura :
        x_cobra = 0
    if x_cobra < 0 :
        x_cobra = largura - tamanho
    if y_cobra < 0 :
        y_cobra = (altura-80) - tamanho
    if y_cobra + tamanho > altura - 80 :
        y_cobra = 0

    placar = pygame.draw.rect(tela,(0,0,0), (0, altura-80, largura,80))
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 10, 10))
    maca = pygame.draw.rect(tela, (100, 25, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randrange(0, largura, tam)
        y_maca = randrange(0, altura - 80, tam)
        pontos = pontos + 1
        comprimento_inicial = comprimento_inicial + 1
        music_colizao.play()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        tela.fill(white)
        texto('Game over! Aperta R para jogar novamente', black, 20, largura//2, altura/2)
        morreu = True
        while morreu is True :
            for event in pygame.event.get() :
                if event.type == QUIT :
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN :
                    if event.type == K_r :
                        reiniciar_jogo()

            pygame.display.update()

    if len(lista_cobra) > comprimento_inicial :
        del lista_cobra[0]
    texto('Pontos: ' +str(pontos), white, 45, 10, altura - 75)
    aumenta_cobra(lista_cobra)
    pygame.display.update()
