import pygame as pg

pg.init()

screen = pg.display.set_mode((800,600),0)

#cores
preto = (20, 20, 20)
amarelo = (255, 225, 60)
azul = (20,20,255)
vermelho = (255,  60, 60)
VELO = 1
 
class Cenario:
    def __init__(self, tamanho, pac):
        self.pacman = pac
        self.tamanho = tamanho
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]
    def pintarlinha(self, nrlinha, linha):
        for nrcoluna, coluna in enumerate(linha):
            x = nrcoluna * self.tamanho
            y = nrlinha * self.tamanho
            cor = preto
            half = self.tamanho // 2
            if coluna == 2:
                cor = azul
            pg.draw.rect(screen, cor, (x, y, self.tamanho, self.tamanho),0)
            if coluna == 1:
                pg.draw.circle(screen, amarelo, (x + half, y+  half), self.tamanho // 10, 0)
            elif coluna == 5:
                pg.draw.circle(screen, vermelho, (x + half, y + half),
                    self.tamanho // 2, 0)


    def pintar(self, screen):
        for nrlinha, linha in enumerate(self.matriz):
            self.pintarlinha(nrlinha, linha)


class Pacman:
    def __init__(self,tamanho):
        self.col = 1
        self.lin = 1
        self.centrox = 400
        self.centroy = 300
        self.tamanho = tamanho
        self.velx = 0.0
        self.vely = 0.0
        self.raio = self.tamanho // 2
        self.coluna_int = self.col
        self.linha_int = self.lin
    
    def calcular_regras(self):
        self.coluna_int = self.col + self.velx
        self.linha_int = self.lin + self.vely
        self.centrox = int(self.col * self.tamanho +self.raio)
        self.centroy = int(self.lin * self.tamanho +self.raio)


#        if self.centrox + self.raio> 800:
#            self.velx *= -1 
#        if self.centrox - self.raio < 0:
#            self.velx *= -1 
#        if self.centroy + self.raio> 600:
#            self.vely *= -1 
#        if self.centroy - self.raio < 0:
#            self.vely *= -1 



    def pintar(self, tela):
        pg.draw.circle(tela, amarelo, (self.centrox, self.centroy), self.raio, 0)

    def calcular_regras(self):
        col = self.pacman.coluna_int
        lin = self.pacman.linha_int
        if 0 <= col < 28 and 0 <= lin < 29:
            self.pacman.aceitar_mov()

#boca
        boca = (self.centrox,self.centroy)
        labio1 = (self.centrox + self.raio,self.centroy - self.raio)
        labio2 = (self.centrox + self.raio,self.centroy)
        pontos = [boca, labio1, labio2]
        pg.draw.polygon(tela, preto, pontos, 0)

#olho
        olhox = int(self.centrox + self.raio / 3)
        olhoy = int(self.centroy - self.raio * 0.7)
        olhor = int(self.raio / 10)
        pg.draw.circle(tela, preto, (olhox,olhoy), olhor,0)


    def processar_ev(self,eventos):
       for e in eventos:

            if e.type == pg.KEYDOWN:
                if e.key == pg.K_RIGHT:
                    self.velx = VELO     
            elif e.type == pg.KEYUP:
                if e.key == pg.K_RIGHT:
                    self.velx = 0 
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    self.velx = -VELO     
            elif e.type == pg.KEYUP:
                if e.key == pg.K_LEFT:
                    self.velx = 0

            if e.type == pg.KEYDOWN:
                if e.key == pg.K_UP:
                    self.vely = -VELO     
            elif e.type == pg.KEYUP:
                if e.key == pg.K_UP:
                    self.vely = 0                     
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_DOWN:
                    self.vely = VELO     
            elif e.type == pg.KEYUP:
                if e.key == pg.K_DOWN:
                    self.vely = 0  

    def aceitar_mov(self):
        self.lin = self.linha_int
        self.col = self.coluna_int
#    def processar_ev_mouse(self, eventos):
 #       DELAY = 100
  #      for e in eventos:
   #         if e.type == pg.MOUSEMOTION:
    #            mouse_x, mouse_y = e.pos
     #           self.col = (mouse_x - self.centrox)/DELAY
      #          self.lin = (mouse_y - self.centroy)/DELAY

if __name__ == "__main__":
    tamanho = 600 // 30
    pacman = Pacman(tamanho)
    cenario = Cenario(tamanho, pacman)

    while True:
#calcular regras
        pacman.calcular_regras()

#pintar tela
        screen.fill(preto)
        cenario.pintar(screen)
        pacman.pintar(screen)
        pg.display.update()
        pg.time.delay(100)

#captura eventos
        eventos = pg.event.get()
        for e in eventos:
                if e.type == pg.QUIT:
                    exit()
                pacman.processar_ev(eventos)

#                pacman.processar_ev_mouse(eventos)

