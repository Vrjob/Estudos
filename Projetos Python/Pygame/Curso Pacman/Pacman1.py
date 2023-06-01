import pygame as pg

pg.init()

tela = pg.display.set_mode((640,480), 0)

#cores
preto = (0, 0, 0)
amarelo = (255, 255, 0)
#variaveis
x = 10
y = 10
fundo = preto
vel = 0.4
raio = 30
velx = vel
vely = vel

while True:

    #calcula regras
    x += velx
    y += vely
    if x + raio > 640:
        velx = -vel
    if x - raio < 0:
        velx = vel
    if y + raio > 480:
        vely = -vel
    if y - raio < 0:
        vely = vel

    #pinta
    tela.fill(fundo)
    pg.draw.circle(tela, (amarelo), (int(x), int(y)), raio, 0)
    pg.display.update()
    
    #eventos
    for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()
     
    