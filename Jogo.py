import pygame
from random import randint

pygame.init()

x = 367  # maximo 570 minimo 140
y = 20
pos_x1 = 100
pos_y_a = 800
pos_y = 0
pos_y_b = 600
pos_y_c = 600

timer = 0
tempo_segundo = 0

velocidade_outros = 30
velocidade = 30

fundo = pygame.image.load('rua.png') # cenario
carro = pygame.image.load('carrotaxi.png')  # taxi
carro4 = pygame.image.load('carro4.png')  # policia
carro2 = pygame.image.load('carro2.png')  # carro branco
carro3 = pygame.image.load('carro3.png')  # carro vermelho
ambulancia = pygame.image.load('ambulancia.png') # ambulancia


font = pygame.font.SysFont('arial black', 30)
texto = font.render("Tempo:", True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = 65, 50

janela = pygame.display.set_mode((800, 700))
pygame.display.set_caption('Taxi Driver')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_w]:
        y -= velocidade
    if comandos[pygame.K_s]:
        y += velocidade
    if comandos[pygame.K_d]:
        x += velocidade
    if comandos[pygame.K_a]:
        x -= velocidade
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT] and x <= 570:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 140:
        x -= velocidade

    if ((pos_x1 > x and y > pos_y_a)):
        y = 1200

    if (pos_y_a <= -300 and pos_y_b <= -300 and pos_y_c <= -300 and pos_y <= -300):
        pos_y_a = randint(600, 1600)  # taxi
        pos_y = randint(800, 2300)  # carro branco
        pos_y_b = randint(1300, 3000)  # carro vermelho
        pos_y_c = randint(1300, 2300)  # ambulancia

    if timer < 20:
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo:" + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0

    pos_y_a -= velocidade_outros + 2  # taxi
    pos_y -= velocidade_outros + 6 # carro branco
    pos_y_b -= velocidade_outros + 4  # carro vermelho
    pos_y_c -= velocidade_outros + 6  # ambulancia

    janela.blit(fundo, (0, 0))
    janela.blit(carro4, (x, y))  # policia
    janela.blit(carro, (pos_x1 + 460, pos_y_a + 200))  # taxi
    janela.blit(carro2, (pos_x1 + 50, pos_y + 300))  # carro branco
    janela.blit(carro3, (pos_x1 + 185, pos_y_b + 100))  # carro vermelho
    janela.blit(ambulancia, (pos_x1 + 320, pos_y_c + 400))  # ambulancia

    janela.blit(texto, pos_texto)  # placar

    pygame.display.update()

pygame.quit()
