import pygame, random, pygame_gui, time
pygame.init()

#---Início das funções---

def mouse(startX,startY,altura,largura): # essa função é para retornar se o mouse esta na posição determinada!
    posicao = manager.get_mouse_position() 
    if posicao[0] >= startX and posicao[0] <= startX+altura:
        if posicao[1] >= startY and posicao[1] <= startY+largura:
            return True
        else:
            return False
    else:
        return False

def click(startX,startY,altura,largura):# essa é para saber quando e onde foi clicado
    mouse_click = pygame.mouse.get_pressed()
    if mouse(startX,startY,altura,largura):
        if mouse_click[0] == True:
            return True
        else:
            return False
    else:
        return False

def grade(): # essa faz a marcação dos quadrados
    quadrados = list()
    coluna = 40
    linha = 90
    for a in range(18):
        for b in range(19):
            quadrados.append([coluna,linha])
            coluna = 40+(b*33)
            linha = 90+(a*33)
            pygame.draw.rect(tela,Preto,(coluna,linha,30,30))
    return quadrados


class Cobra: #Na teoria é para gerir a cobra
    def __init__(self, quadrados=list()):
        self.vivo = True
        self.quadrados = quadrados

        lugar = random.randrange(0,len(self.quadrados))
        x = self.quadrados[lugar][0]
        y = self.quadrados[lugar][1]
        self.point = (x,y)
        self.x = x
        self.y = y

        self.rabo = list()
        self.tamanho_cobra = 0

        #Nessa parte eu defino em que direção a cobra começa a andar
        if self.x < 350 and self.y < 350:
            lado = random.randrange(0,1)
            if lado == 0:
                self.Yv = 33
                self.Xv = 0
                self.direcao = 'baixo'
            if lado == 1:
                self.Yv = 0
                self.Xv = 33
                self.direcao = 'direita'
        if self.x < 350 and self.y >= 350 and self.y < 400:
            self.Yv = 33
            self.Xv = 0
            self.direcao = 'baixo'
        if self.x < 350 and self.y >= 400:
            lado = random.randrange(0,1)
            if lado == 0:
                self.Yv = 33
                self.Xv = 0
                self.direcao = 'baixo'
            if lado == 1:
                self.Yv = 0
                self.Xv = -33
                self.direcao = 'esquerda'
        if self.x >= 350 and self.x < 400 and self.y < 350:
            self.Yv = 0
            self.Xv = 33
            self.direcao = 'direita'
        if self.x >= 350 and self.x < 400 and self.y >= 350 and self.y < 400:
            lado = random.randrange(0,3)
            if lado == 0:
                self.Yv = 33
                self.Xv = 0
                self.direcao = 'baixo'
            if lado == 1:
                self.Yv = 0
                self.Xv = 33
                self.direcao = 'direita'
            if lado == 2:
                self.Yv = -33
                self.Xv = 0
                self.direcao = 'cima'
            if lado == 3:
                self.Yv = 0
                self.Xv = -33
                self.direcao = 'esquerda'
        if self.x >= 350 and self.x < 400 and self.y >= 400:
            self.Yv = 0
            self.Xv = -33
            self.direcao = 'esquerda'
        if self.x >= 400 and self.y < 350:
            lado = random.randrange(0,1)
            if lado == 0:
                self.Yv = 0
                self.Xv = 33
                self.direcao = ' direita'
            if lado == 1:
                self.Yv = -33
                self.Xv = 0
                self.direcao = 'cima'
        if self.x >= 400 and self.y >= 350 and self.y < 400:
            self.Yv = -33
            self.Xv = 0
            self.direcao = 'cima'
        if self.x >= 400 and self.y >= 400:
            lado = random.randrange(0,1)
            if lado == 0:
                self.Yv = 0
                self.Xv = -33
                self.direcao = 'esquerda'
            if lado == 1:
                self.Yv = -33
                self.Xv = 0
                self.direcao = 'cima'


    def draw(self):                        
        for i in self.rabo:                                                       
            pygame.draw.rect(tela,Verde,(i[0],i[1],30,30))                    


    def update(self,pontos,ocupados):
        self.x += self.Xv
        self.y += self.Yv
        self.point = (self.x,self.y)
        self.tamanho_cobra = pontos


        if self.x < 40:
            self.vivo = False
        elif self.x > 634:
            self.vivo = False
        elif self.y < 90:
            self.vivo = False
        elif self.y > 651:
            self.vivo = False

        self.rabo = ocupados
        if self.tamanho_cobra >= 1:
            while len(self.rabo) > self.tamanho_cobra:
                self.rabo.pop(0)
        else:
            self.rabo.pop(0)

        for anel in self.rabo:
            if self.point == anel:
                self.vivo = False

class Comida: #Produz a comida -- dono dos meios de produção
    def __init__(self, quadrados=list()):
        self.quadrados = quadrados
        lugar = random.randrange(0,len(self.quadrados))
        self.x = self.quadrados[lugar][0]
        self.y = self.quadrados[lugar][1]
        self.point = (self.x,self.y)

    def draw(self):
        pygame.draw.rect(tela,Amarelo,(self.point[0],self.point[1],30,30))


#---Fim das funções---

#---Setting up---

Branco = (255,255,255) #coloca as corizinhas que eu vou usar
Cinza = (127,127,127)
Preto = (0,0,0)
Vermelho = (255,0,0)
Verdinho = (0,255,0)
Verde = (0,127,0)
Amarelo = (255,219,88)

tamanho_tela = (700,700)
pygame.display.set_caption('Jogo da Cobrinha!')
tela = pygame.display.set_mode(tamanho_tela) #seta a tela com seu tamanho e tals

Fundo = pygame.Surface(tamanho_tela)
Fundo.fill(Preto) #pinta o fundo de preto

fontinha = pygame.font.SysFont('Arial', 20) # seta as fontes e os tamanhos que eu vou usar
fonte = pygame.font.SysFont('Arial', 40)
fonteTT = pygame.font.SysFont('Arial', 70)

manager = pygame_gui.UIManager((700,700)) # inutil por enquanto !?

Tudo = True
espera = True
clock = pygame.time.Clock()

#---Início o menu---
while Tudo:
    time_delta = clock.tick(60)/1000.0

    while espera:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Tudo = False
                espera = False

        manager.update(time_delta)

        tela.blit(Fundo, (0,0))

        pygame.draw.rect(tela, Verdinho, (200,300,300,100))
        pygame.draw.rect(tela, Verdinho, (200,420,300,100))

        
        dev = fontinha.render('Developed by Kayãzin :)', True, Verdinho)
        tela.blit(dev,(470,670))

        jogar = fonteTT.render('Jogo da Cobrinha',True, Verdinho)
        tela.blit(jogar,(75,50)) # X e Y -- NESSA ORDEM

        if mouse(200,300,300,100):
            pygame.draw.rect(tela, Verde, (200,300,300,100), 5)
            playbutton = fonte.render('Jogar',True, Branco)
            if click(200,300,300,100):
                jogo = True
                espera = False
        else:
            playbutton = fonte.render('Jogar',True, Preto)
        
        tela.blit(playbutton,(295,325))

        if mouse(200,420,300,100):
            pygame.draw.rect(tela, Verde, (200,420,300,100), 5)
            exitbutton = fonte.render('Sair',True, Branco)
            if click(200,420,300,100):
                Tudo = False
                espera = False
                jogo = False
        else:
            exitbutton = fonte.render('Sair',True, Preto)

        tela.blit(exitbutton,(310,445))

        pygame.display.update()

    #---Fim do menu---

    #---Começo do jogo---

    vivo = True
    quadrados = grade()
    cobra = Cobra(quadrados)
    lanche = Comida(quadrados)
    ocupados = list()
    ocupados.insert(0, cobra.point)
    pontos = 0


    while jogo:
        ocupados = list()
        ocupados.insert(0, cobra.point)
        
        while cobra.vivo:
            quadrados = grade()
            tela.blit(Fundo, (0,0))
            pygame.draw.rect(tela,Cinza,(35,85,634,600))
            grade()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if cobra.direcao != 'direita' or pontos == 0:
                            cobra.Yv = 0
                            cobra.Xv = -33
                            cobra.direcao = 'esquerda'
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if cobra.direcao != 'esquerda' or pontos == 0:
                            cobra.Yv = 0
                            cobra.Xv = 33
                            cobra.direcao = 'direita'
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if cobra.direcao != 'baixo' or pontos == 0:
                            cobra.Xv = 0
                            cobra.Yv = -33
                            cobra.direcao = 'cima'
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if cobra.direcao != 'cima' or pontos == 0:
                            cobra.Xv = 0
                            cobra.Yv = 33
                            cobra.direcao = 'baixo'

            manager.update(time_delta)
        
            if cobra.x == lanche.x and cobra.y == lanche.y:
                igual = True
                pontos += 1
                while igual:
                    for a in quadrados:
                        for b in cobra.rabo:
                            if a == b:
                                quadrados.remove(a)
                    lugar = random.randrange(0,len(quadrados))
                    lanche.x = quadrados[lugar][0] 
                    lanche.y = quadrados[lugar][1]
                    lanche.point = (lanche.x,lanche.y) 
                    igual = False

            for i in cobra.rabo:
                if i[0] == lanche.x and i[1] == lanche.y:
                    igual = True
                    while igual:
                        for a in quadrados:
                            for b in cobra.rabo:
                                if a == b:
                                    quadrados.remove(a)
                        lugar = random.randrange(0,len(quadrados))
                        lanche.x = quadrados[lugar][0] 
                        lanche.y = quadrados[lugar][1]
                        lanche.point = (lanche.x,lanche.y) 
                        igual = False
        
            
            pygame.draw.rect(tela, Verdinho, (350,10,150,70))
            pygame.draw.rect(tela, Verdinho, (519,10,150,70))
            
            if mouse(350,10,150,70):
                pygame.draw.rect(tela, Verde, (350,10,150,70), 5)
                menubutton = fonte.render('Menu',True, Branco)
                if click(350,10,150,70):
                    cobra.vivo = False
                    jogo = False
                    espera = True
            else:
                menubutton = fonte.render('Menu',True, Preto)
            
            tela.blit(menubutton,(375,20))

            if mouse(519,10,150,70):
                pygame.draw.rect(tela, Verde, (519,10,150,70), 5)
                exitbutton = fonte.render('Sair',True, Branco)
                if click(519,10,150,70):
                    cobra.vivo = False
                    Tudo = False
                    jogo = False
            else:
                exitbutton = fonte.render('Sair',True, Preto)            

            tela.blit(exitbutton,(555,20))

            pontuação = fonte.render('pontuação: ' + str(pontos),True,Branco)
            tela.blit(pontuação, (35,20))


            cobra.draw()
            lanche.draw()

            cobra.update(pontos,ocupados)
            ocupados.append(cobra.point)
            

            pygame.display.update()
            pygame.time.delay(140)

        #---Pós Morte---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Tudo = False
                jogo = False

        manager.update(time_delta)
        pygame.draw.rect(tela,Preto,(350,10,519,70))
        pygame.draw.rect(tela, Verdinho, (350,10,150,70))
        pygame.draw.rect(tela, Verdinho, (519,10,150,70))
        pygame.draw.rect(tela, Verdinho, (241,330,218,70))

        if mouse(241,330,218,70):
            pygame.draw.rect(tela, Verde, (241,330,218,70),5)
            Againbutton = fonte.render('Denovo?', True, Branco)
            if click(241,330,218,70):
                quadrados = grade()
                cobra = Cobra(quadrados)
                lanche = Comida(quadrados)
                ocupados.clear()
                pontos  = 0
                pos_morte = False
        else:
            Againbutton = fonte.render('Denovo?', True, Preto)

        if mouse(350,10,150,70):
            pygame.draw.rect(tela, Verde, (350,10,150,70), 5)
            menubutton = fonte.render('Menu',True, Branco)
            if click(350,10,150,70):
                jogo = False
                espera = True
                pos_morte = False
        else:
            menubutton = fonte.render('Menu',True, Preto)
                        
        if mouse(519,10,150,70):
            pygame.draw.rect(tela, Verde, (519,10,150,70), 5)
            exitbutton = fonte.render('Sair',True, Branco)
            if click(519,10,150,70):
                jogo = False
                Tudo = False
        else:
            exitbutton = fonte.render('Sair',True, Preto)            

        morte = fonteTT.render('Morreu',True, Vermelho)

        tela.blit(menubutton,(375,20))
        tela.blit(exitbutton,(555,20))
        tela.blit(Againbutton,(270,340))
        tela.blit(morte,(241,250))
 
        pygame.display.update()



#---Fim do jogo---