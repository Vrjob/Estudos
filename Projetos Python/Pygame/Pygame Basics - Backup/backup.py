import pygame
from sys import exit
from random import randint

def display_score():
    
    current_time = int((pygame.time.get_ticks() - start_time)/1000)
    score_surf = test_font.render(f"Score: {current_time}", False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 6

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf,obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)


        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []
def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): 
                return True
    return False
def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:

        player_surf = player_jump3
        if cair:
            player_surf = player_fall
        if jump == 1:
            player_surf = player_jump1
        if jump == 2:
            player_surf = player_jump2    
        
    else:
        player_index += 0.1
        if player_index >= len(player_walk): 
            player_index = 0

        player_surf = player_walk[int(player_index)]
def frame_animation():
    global frame_index, snail_surf, fly_surf, worm_surf, snaka_surf, snakab_surf, buddy_surf, bat_surf
    frame_index += 0.1
    if frame_index >= len(snail_frame): 
        frame_index = 0
    snail_surf = snail_frame[int(frame_index)]
    fly_surf = fly_frame[int(frame_index)]
    worm_surf = worm_frame[int(frame_index)]
    snaka_surf = snaka_frame[int(frame_index)]
    snakab_surf = snakab_frame[int(frame_index)]
    bat_surf = bat_frame[int(frame_index)]
    buddy_surf = buddy_frame[int(frame_index)]

gravidade = 1
player_life = 420
imortal = False

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Joguinho')
ico = pygame.image.load('graphics/player/player_ico.png').convert_alpha()

pygame.display.set_icon(ico)
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
sky_rect1 = sky_surface.get_rect(topleft = (0,0))
sky_rect2 = sky_surface.get_rect(topleft = (800,0))


ground_surface = pygame.image.load('graphics/ground.png').convert()
ground_rect1 = ground_surface.get_rect(topleft = (0,300))
ground_rect2 = ground_surface.get_rect(topleft = (800,300))


#score_surf = test_font.render('My Game', False, (64,64,64))
#score_rect = score_surf.get_rect(center = (400, 50))

#mosters / obstacles - - - - - - - - - -
frame_index = 0
#Snail  V:4
snail_frame1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frame3 = pygame.image.load('graphics/snail/snail3.png').convert_alpha()
snail_frame4 = pygame.image.load('graphics/snail/snail4.png').convert_alpha()
snail_frame = [snail_frame1, snail_frame2, snail_frame3, snail_frame4, snail_frame3, snail_frame2]
snail_surf = snail_frame[frame_index]
#Fly    V:5
fly_frame1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frame3 = pygame.image.load('graphics/fly/fly3.png').convert_alpha()
fly_frame4 = pygame.image.load('graphics/fly/fly4.png').convert_alpha()
fly_frame = [fly_frame1, fly_frame2, fly_frame3, fly_frame4, fly_frame3, fly_frame2]
fly_surf = fly_frame[frame_index]
#Worm   V:3
worm_frame1 = pygame.image.load('graphics/snail/worm1.png').convert_alpha()
worm_frame2 = pygame.image.load('graphics/snail/worm2.png').convert_alpha()
worm_frame3 = pygame.image.load('graphics/snail/worm3.png').convert_alpha()
worm_frame4 = pygame.image.load('graphics/snail/worm4.png').convert_alpha()
worm_frame = [worm_frame1, worm_frame2, worm_frame3, worm_frame4, worm_frame3, worm_frame2]
worm_surf = worm_frame[frame_index]
#Buddy  V:2
buddy_frame1 = pygame.image.load('graphics/snail/buddy1.png').convert_alpha()
buddy_frame2 = pygame.image.load('graphics/snail/buddy2.png').convert_alpha()
buddy_frame3 = pygame.image.load('graphics/snail/buddy3.png').convert_alpha()
buddy_frame4 = pygame.image.load('graphics/snail/buddy4.png').convert_alpha()
buddy_frame = [buddy_frame1, buddy_frame2, buddy_frame3, buddy_frame4, buddy_frame3, buddy_frame2]
buddy_surf = buddy_frame[frame_index]
#Bat    V:1
bat_frame1 = pygame.image.load('graphics/fly/bat1.png').convert_alpha()
bat_frame2 = pygame.image.load('graphics/fly/bat2.png').convert_alpha()
bat_frame3 = pygame.image.load('graphics/fly/bat3.png').convert_alpha()
bat_frame4 = pygame.image.load('graphics/fly/bat4.png').convert_alpha()
bat_frame = [bat_frame1, bat_frame2, bat_frame3, bat_frame4, bat_frame3, bat_frame2]
bat_surf = bat_frame[frame_index]



obstacle_rect_list = []



snaka_frame1 = pygame.image.load('graphics/snail/snaka1.png').convert_alpha()
snaka_frame2 = pygame.image.load('graphics/snail/snaka2.png').convert_alpha()
snaka_frame = [snaka_frame1, snaka_frame2, snaka_frame1, snaka_frame2, snaka_frame1, snaka_frame2,]
frame_index = 0
snaka_surf = snaka_frame[frame_index]
snaka_rect= snaka_surf.get_rect(topleft = (0,0))

snakab_frame1 = pygame.image.load('graphics/snail/snaka11.png').convert_alpha()
snakab_frame2 = pygame.image.load('graphics/snail/snaka12.png').convert_alpha()
snakab_frame = [snakab_frame1, snakab_frame2, snakab_frame1, snakab_frame2, snakab_frame1, snakab_frame2]
snakab_surf = snakab_frame[frame_index]
snakab_rect= snaka_surf.get_rect(topleft = (0,0))


player_walk1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk3 = pygame.image.load('graphics/player/player_walk_3.png').convert_alpha()
player_walk4 = pygame.image.load('graphics/player/player_walk_4.png').convert_alpha()
player_walk5 = pygame.image.load('graphics/player/player_walk_5.png').convert_alpha()
player_walk = [player_walk1, player_walk2, player_walk3, player_walk4, player_walk5, player_walk4, player_walk3,player_walk2]
player_index = 0

player_jump1 = pygame.image.load('graphics/player/jump1.png').convert_alpha()
player_jump2 = pygame.image.load('graphics/player/jump2.png').convert_alpha()
player_jump3 = pygame.image.load('graphics/player/jump3.png').convert_alpha()
player_fall = pygame.image.load('graphics/player/jump4.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect= player_surf.get_rect(bottomleft = (player_life,300))


imortal_img = pygame.image.load('graphics/player/safe4.png').convert_alpha()
imortal_rect = imortal_img.get_rect(topleft = (0,0))

player_gravity = 0

#intro
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Joguinho', False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,70))

game_message = test_font.render('Press Space to run!', False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,340))

#timer
obstacle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer, 2000)
frame_timer = pygame.USEREVENT +2
pygame.time.set_timer(frame_timer, 400)





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20     

#movimentos
            if event.type == pygame.KEYDOWN:
                #pulo
                if event.key == pygame.K_UP and player_rect.bottom == 300:
                    gravidade = 1
                    jump = 1
                    player_gravity = -20
                #agachar
                elif event.key == pygame.K_DOWN and player_rect.bottom < 300:
                    player_gravity = 20
                    cair = True

                #pulo duplo
                elif event.key == pygame.K_UP and player_rect.bottom < 300 and jump == 1:
                    player_gravity = -10
                    jump += 1

                #planar
                elif event.key == pygame.K_UP and player_rect.bottom < 300 and jump == 2:
                    gravidade = 0.1
                    jump += 1

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_rect.midbottom = (player_life,300)
                    countdown = 0
                    game_active = True
                    start_time = pygame.time.get_ticks()
        if game_active:
            if event.type == obstacle_timer and game_active:
                velocity = randint(4,6)
                if velocity == 5:
                    obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900,1100),300)))
                if velocity == 4:
                    obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,1100),randint(80,150))))
                #if velocity == 3:
                #    obstacle_rect_list.append(worm_surf.get_rect(midbottom = (randint(900,1100),310)))
                #if velocity == 2:
                #    obstacle_rect_list.append(buddy_surf.get_rect(midbottom = (randint(900,1100),300)))
                #if velocity == 1:
                #    obstacle_rect_list.append(bat_surf.get_rect(midbottom = (randint(900,1100),randint(80,150))))






        player_surf = player_walk[int(player_index)]

    if game_active:
        screen.blit(sky_surface,sky_rect1)
        screen.blit(sky_surface,sky_rect2)
        screen.blit(snakab_surf,snakab_rect)
        screen.blit(ground_surface,ground_rect1)
        screen.blit(ground_surface,ground_rect2)
        score = display_score()

        sky_rect1.left -= 1
        sky_rect2.left -= 1
        if sky_rect1.right <= 0:
            sky_rect1.left = 0 
            sky_rect2.left = 800   
        ground_rect1.left -= 3
        ground_rect2.left -= 3
        if ground_rect1.right <= 0:
            ground_rect1.left = 0 
            ground_rect2.left = 800   
  



        #worm_rect.right -= 2
        #if worm_rect.right <= -50:
        #    worm_rect.right = 850   
        #screen.blit(worm_surf, worm_rect)

        #player
        player_gravity += gravidade
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            cair = False
        player_animation()
        frame_animation()
        if player_rect.top <= 20:
            player_rect.top = 20
        screen.blit(player_surf,player_rect)
    

        #Obstacle Mov
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collision
        
        if (collisions(player_rect,obstacle_rect_list))and imortal == False:

            player_rect.left -= 20
            countdown = int((pygame.time.get_ticks() - start_time)/1000)
            imortal = True
        



        #imortal
        if imortal == True:
            imortal_rect.left = player_rect.left
            imortal_rect.left -= 8
            imortal_rect.top = player_rect.top
            imortal_rect.top -= 2
            screen.blit(imortal_img,imortal_rect)

            imortal_img = pygame.image.load('graphics/player/safe1.png').convert_alpha()
                
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 1:
                imortal_img = pygame.image.load('graphics/player/safe2.png').convert_alpha()
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 1.2:
                imortal_img = pygame.image.load('graphics/player/safe3.png').convert_alpha()
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 1.4:
                imortal_img = pygame.image.load('graphics/player/safe4.png').convert_alpha()
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 1.6:
                imortal_img = pygame.image.load('graphics/player/safe5.png').convert_alpha()
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 1.8:
                imortal_img = pygame.image.load('graphics/player/safe6.png').convert_alpha()
            if (((pygame.time.get_ticks() - start_time)/1000) - countdown) >= 2:
                imortal_img = pygame.image.load('graphics/player/safe7.png').convert_alpha()
                imortal = False 

        screen.blit(snaka_surf,snaka_rect)

        #game over
        if player_rect.left <= 20:
            imortal = False 

            game_active = False

    else:
        screen.fill((84,129,162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        score_message = test_font.render(f'Your Score: {score}', False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)

        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)


    pygame.display.update()
    clock.tick(60)


