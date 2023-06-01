import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >=screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >=screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_height/2 , screen_width/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Main Window Setup
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Game Retangles

    # BALL
speed = 5
ball_speed_x = speed * random.choice((1,-1))
ball_speed_y = speed * random.choice((1,-1))
ball_dia = 30
ball_ray = ball_dia/2
ball = pygame.Rect( screen_width/2 - ball_ray, screen_height/2 - ball_ray, ball_dia, ball_dia)

    # Players
player_speed = 0 
opponent_speed = speed
player_x = 10
player_y = 140
player = pygame.Rect(screen_width - (player_x * 2), screen_height/2 - (player_y/2), player_x, player_y)
opponent = pygame.Rect((player_x ), screen_height/2 - (player_y/2), player_x, player_y)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)



while True:
    # Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += speed
            if event.key == pygame.K_UP:
                player_speed -= speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= speed
            if event.key == pygame.K_UP:
                player_speed += speed


    ball_animation()
    player_animation()
    opponent_ai()


    # Visuals
    screen.fill(bg_color)

    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    # Updating Window
    pygame.display.flip()
    clock.tick(60)
