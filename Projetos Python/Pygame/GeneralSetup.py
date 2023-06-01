import pygame

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Main Window Setup
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Titulo')

while True:
    # Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Updating Window
    pygame.display.flip()
    clock.tick(60)