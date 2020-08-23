import sys

import pygame

pygame.init()
janela = pygame.display.set_mode([500, 500])
pygame.display.set_caption("The King of Prontera")

p_x = 240
p_y = 70
tela = 0
tela_principal = pygame.image.load('tela_principal.png')
tela4 = pygame.image.load('gameover.jpg')
tela5 = pygame.image.load('tela5.png')
tela1 = pygame.image.load('tela1.png')
magia = pygame.image.load('magia.png')
seta = pygame.image.load('seta.png')
fundo0 = pygame.image.load('fundo0.png')
fundo = pygame.image.load('tela.png')
fundo2 = pygame.image.load('tela2.png')
npc = pygame.image.load('npc.png')
npc2 = pygame.image.load('npc2.png')
personfrente = ['frente1.png', 'frente2.png', 'frente3.png', 'frente4.png']
persontras = ['tras1.png', 'tras2.png', 'tras3.png', 'tras4.png']
persondireita = ['direito1.png', 'direito2.png', 'direito3.png', 'direito4.png']
personesquerdo = ['esquerdo1.png', 'esquerdo2.png', 'esquerdo3.png', 'esquerdo4.png']
personload = pygame.image.load(personfrente[0])

cor_branca = (255, 255, 255)
cor_azul = (108, 194, 236)
cor_verde = (152, 231, 114)
cor_vermelho = (227, 57, 9)
cor_preta = (0, 0, 0)

pygame.font.init()
font_padrao = pygame.font.get_default_font()
font = pygame.font.SysFont(font_padrao, 30)
font1 = pygame.font.SysFont(font_padrao, 50)

andar = -1




def movimento():
    global andar
    andar += 1
    if andar < 3:
        return andar
    else:
        andar = 0
        return andar


def area(topx, topy, rightx, righty):
    global p_x;
    global p_y

    if p_x == topx and topy <= p_y <= righty:
        p_x -= 5
    if p_y == righty and topx <= p_x <= rightx:
        p_y += 5
    if p_x == rightx and topy <= p_y <= righty:
        p_x += 5
    if p_y == topy and topx <= p_x <= rightx:
        p_y -= 5
    return

pygame.mixer.music.load('intro.mp3')
pygame.mixer.music.play(-1)

setax = 95
setay = 235

while tela == 0:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT: sys.exit()
    janela.blit(tela_principal, (0, 0))
    janela.blit(seta, pygame.rect.Rect(setax, setay, 0, 0))
    pygame.display.update()
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_s]:
        setay = 300
    if comandos[pygame.K_w]:
        setay = 235
        tela_principal = pygame.image.load('tela_principal.png')
        pygame.display.update()
    if comandos[pygame.K_RETURN]:
        tela_principal = pygame.image.load('tela_principal.png')
        pygame.display.update()
        if setay == 235 and comandos[pygame.K_RETURN]:
            tela = 1
            pygame.time.delay(70)
        if setay == 300 and comandos[pygame.K_RETURN]:
            tela_principal = pygame.image.load('creditos.png')
            pygame.display.update()



while tela == 1:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    janela.blit(tela1, (0, 0))
    pygame.display.update()
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_SPACE]:
        tela = 2


musica_tocando = pygame.mixer.music.pause()
cont = 0


while tela == 2:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_s]:
        p_y += 5
        personload = pygame.image.load(personfrente[movimento()])

    elif comandos[pygame.K_w]:
        p_y -= 5
        personload = pygame.image.load(persontras[movimento()])

    elif comandos[pygame.K_a]:
        p_x -= 5
        personload = pygame.image.load(personesquerdo[movimento()])

    elif comandos[pygame.K_d]:
        p_x += 5
        personload = pygame.image.load(persondireita[movimento()])

    '''if p_x == 120 and p_y == 170:
        pygame.mixer.music.load('npc.ogg')
        pygame.mixer.music.play(-1)'''
    if comandos[pygame.K_RETURN]:
        tela = 3

    pygame.time.delay(70)
    janela.blit(fundo, (0, 0))
    #janela.blit(npc, pygame.rect.Rect(350, 150, 0, 0))
    janela.blit(npc2, pygame.rect.Rect(120, 150, 0, 0))
    janela.blit(personload, pygame.rect.Rect(p_x, p_y, 0, 0))
    pygame.display.update()

    if p_x == 120 and p_y == 170:
        pygame.mixer.music.load('npc.ogg')
        pygame.mixer.music.play(-1)
        musica_tocando = False

    else:
        musica_tocando = True


    # areas
    area(340, 140, 370, 160)  # npc1
    area(110, 140, 130, 155)  # npc2
    area(-25, 35, 215, 110)
    area(145, 85, 220, 230)
    area(-25, 35, 87, 450)
    area(-10, -10, 475, 30)
    area(-10, 30, 218, 112)
    area(265, 75, 300, 230)
    area(-10, 113, 87, 500)
    area(-15, 100, 90, 480)
    area(-10, 435, 500, 500)
    area(270, 30, 500, 105)
    area(385, 105, 500, 435)
    area(148, 110, 216, 220)  # escada-esquerda
    area(267, 105, 310, 225)  # escada-direita
    area(140, 260, 340, 280)
    area(155, 280, 180, 320)
    area(250, 280, 315, 450)
    area(315, 310, 500, 500)
    # print(f'x = {p_x}, y = {p_y}')


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.imagemInimigo = pygame.image.load('val_le.png')

        self.rect = self.imagemInimigo.get_rect()

        self.listaDisparoInimigo = []
        self.vida = True
        self.velocidadeMagiaInimigo = 20
        self.rect.top = pos_y
        self.rect.left = pos_x

    def movimentoDirInimigo(self):
        self.rect.right -= self.velocidadeMagiaInimigo
        self.__movimento()

    def movimentoEsqInimigo(self):
        self.rect.left += self.velocidadeMagiaInimigo
        self.__movimento()

    def __movimento(self):
        if self.vida == True:
            if self.rect.left <= 175:
                self.rect.left = 175
            elif self.rect.right > 350:
                self.rect.right = 350

    def disparar(self, i_x, i_y):
        magiainimigo = MagiaInimigo(i_x, i_y)
        self.listaDisparoInimigo.append(magiainimigo)

    def colocar(self, superficie):
        superficie.blit(self.imagemInimigo, self.rect)


class MagiaInimigo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.imagemMagiaInimigo = pygame.image.load('magia_inimigo.png')

        self.rect = self.imagemMagiaInimigo.get_rect()
        self.velocidadeMagia = 30
        self.rect.top = pos_y
        self.rect.left = pos_x - 20

    def trajetoriaInimigo(self):
        self.rect.top = self.rect.top + self.velocidadeMagia

    def colocar(self, superficie):
        superficie.blit(self.imagemMagiaInimigo, self.rect)


class Magia(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagemMagia = pygame.image.load('magia_ini.png')

        self.rect = self.imagemMagia.get_rect()
        self.velocidadeMagia = 20
        self.rect.top = posy - 30
        self.rect.left = posx - 10

    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeMagia

    def colocar(self, superficie):
        superficie.blit(self.imagemMagia, self.rect)


class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagemPersonagem = pygame.image.load('tras_cenario2.png')

        self.rect = self.imagemPersonagem.get_rect()
        self.rect.centerx = 250
        self.rect.centery = 390

        self.listaDisparo = []
        self.vida = True
        self.velocidade = 20

    def movimentoDireita(self):
        self.rect.right += self.velocidade
        self.__movimento()

    def movimentoEsquerda(self):
        self.rect.left -= self.velocidade
        self.__movimento()

    def __movimento(self):
        if self.vida == True:
            if self.rect.left <= 175:
                self.rect.left = 175
            elif self.rect.right > 330:
                self.rect.right = 330

    def dispararP(self, x, y):
        minhamagia = Magia(x, y)
        self.listaDisparo.append(minhamagia)

    def colocar(self, superficie):
        superficie.blit(self.imagemPersonagem, self.rect)


jogador = Personagem()
magia_disparar = Magia(250, 100)
c_inimigo = Inimigo(210, 110)
inimigo_disparar = MagiaInimigo(210, 110)

cont = 0
cont_j = 0

if tela == 3:
    pygame.mixer.music.load('audio.ogg')
    pygame.mixer.music.play(-1)

while tela == 3:
    inimigo_disparar.trajetoriaInimigo()
    magia_disparar.trajetoria()
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pressionar = pygame.key.get_pressed()
        if pressionar[pygame.K_a]:
            jogador.movimentoEsquerda()
            c_inimigo.movimentoEsqInimigo()

        elif pressionar[pygame.K_d]:
            jogador.movimentoDireita()
            c_inimigo.movimentoDirInimigo()

        elif pressionar[pygame.K_SPACE]:
            x, y = jogador.rect.center
            jogador.dispararP(x, y)
            i_x, i_y = c_inimigo.rect.center
            c_inimigo.disparar(i_x, i_y)

    pygame.time.delay(70)
    janela.blit(fundo2, (0, 0))
    jogador.colocar(janela)
    c_inimigo.colocar(janela)
    if len(jogador.listaDisparo) > 0:
        for x in jogador.listaDisparo:
            x.colocar(janela)
            x.trajetoria()
            if x.rect.colliderect(c_inimigo.rect):
                cont_j += 1
            if cont_j == 30:
                tela = 5
            if x.rect.top < 170:
                jogador.listaDisparo.remove(x)

    if len(c_inimigo.listaDisparoInimigo) > 0:
        for i_x in c_inimigo.listaDisparoInimigo:
            i_x.colocar(janela)
            i_x.trajetoriaInimigo()
            if i_x.rect.colliderect(jogador):
                cont += 1
            if cont == 9:
                tela = 4
            if i_x.rect.top > 380:
                c_inimigo.listaDisparoInimigo.remove(i_x)

    pygame.display.update()

    area(-15, -15, 500, 130)
    area(585, 25, 600, 385)
    area(120, 385, 600, 430)
    area(170, 340, 180, 390)
    area(290, 340, 300, 390)
    # print(f'x = {magia_x}, y = {magia_y}')

if tela == 4:
    pygame.mixer.music.pause()
while tela == 4:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    janela.blit(tela4, (0, 0))
    pygame.display.update()

if tela == 5:
    pygame.mixer.music.pause()

while tela == 5:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    janela.blit(tela5, (0,0))
    pygame.display.update()