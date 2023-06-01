import pygame
from sys import exit
from random import randint

class Grass():
    def __init__(self,number_id,row,col):
        self.number_id = number_id
        self.row = int(row)
        self.col = int(col)
        self.surf = pygame.image.load('graphics/stay3.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft = ((int(self.row*90)-25),(int(self.col*165)-150)))

    def valor_obtido(self,valor):
        self.valor = valor




# General Setup
pygame.init()
clock = pygame.time.Clock()

# Main Window Setup
screen_width = 600
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Grass Lotery')

ground_surf = pygame.image.load('graphics/ground.png').convert()
ground_rect= ground_surf.get_rect(topleft = (0,0))

grass1 = Grass(1,1,1)
grass2 = Grass(2,2,1)
grass3 = Grass(3,3,1)
grass4 = Grass(4,1,2)
grass5 = Grass(5,2,2)
grass6 = Grass(6,3,2)
grass7 = Grass(7,1,3)
grass8 = Grass(8,2,3)
grass9 = Grass(9,3,3)



while True:
    # Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(ground_surf,ground_rect)
    screen.blit(grass1.surf,grass1.rect)
    screen.blit(grass2.surf,grass2.rect)
    screen.blit(grass3.surf,grass3.rect)
    screen.blit(grass4.surf,grass4.rect)
    screen.blit(grass5.surf,grass5.rect)
    screen.blit(grass6.surf,grass6.rect)
    screen.blit(grass7.surf,grass7.rect)
    screen.blit(grass8.surf,grass8.rect)
    screen.blit(grass9.surf,grass9.rect)



    # Updating Window
    pygame.display.flip()
    clock.tick(60)