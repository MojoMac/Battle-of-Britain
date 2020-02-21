import pygame as pg
from settings import *
import sprites

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

def scoredisplay(score):
    font = pg.font.SysFont('Impact', 14, False, False)
    text = font.render('Score: {}'.format(score),True, RED)
    screen.blit(text, (10,10))

def gamestart():
    pg.init()

    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    font = pg.font.SysFont('Impact',30, False, False)
    font2 = pg.font.SysFont('Times New Roman',50, False, False)
    title_text = 'THE BATTLE OF BRITAIN'
    start_text1 = 'Press Enter to start'
    start_text2 = 'or ESC to exit'

    title = font2.render(title_text, True, RED)
    titlerect = title.get_rect()
    titlerect.midtop = (400, 60)
    text1 = font.render(start_text1, True, RED)
    text1rect = text1.get_rect()
    text1rect.midtop = (160, 460)
    text2 = font.render(start_text2, True, RED)
    text2rect = text2.get_rect()
    text2rect.midtop = (640, 460)

    #score = 0

    playing = False

    background_image2 = pg.image.load('BoBback1.jpg')

    pg.mixer.music.load('Epic Orchestra2.mp3')
    pg.mixer.music.set_endevent(pg.constants.USEREVENT)
    pg.mixer.music.play()

    # Loop until the user stops program
    while not playing:

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                quit()
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                playing = True
            if event.type == pg.constants.USEREVENT:
                # This event is triggered when the song stops playing.
                pg.mixer.music.load('Epic Orchestra2.mp3')
                pg.mixer.music.play()
            screen.fill(WHITE)
            screen.blit(background_image2, [-175, 0])
            screen.blit(text1, text1rect)
            screen.blit(text2, text2rect)
            screen.blit(title, titlerect)

            pg.display.flip()

            clock.tick(FPS)
def gameover(score):

    go_screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    backg = pg.image.load('JG26_Erfolg_Spitfire.jpg')
    start_text1 = 'FINAL SCORE: {}'.format(score)
    font = pg.font.SysFont('Times New Roman', 50, False, False)
    text1 = font.render(start_text1, True, RED)
    textrect = text1.get_rect()
    textrect.midtop = (400, 60)
    start_text2 = 'press "Enter" to retry or "Esc" to exit'
    text2 = font.render(start_text2, True, RED)
    textrect2 = text2.get_rect()
    textrect2.midtop = (400, 200)


    started = False

    while not started:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                quit()
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                started = True
        go_screen.fill(WHITE)
        go_screen.blit(backg, [0, 50])
        go_screen.blit(text1, textrect)
        go_screen.blit(text2, textrect2)
        pg.display.flip()

        clock.tick(FPS)

    return True

def gameplay():
    # creating screen and clock objects
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    # sprite groups orated here
    all_sprites = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()
    blast_sprites = pg.sprite.Group()

    # player sprite created here
    player = sprites.Player()
    all_sprites.add(player)

    # enemy sprite created here
    for x in range(10):
        enemy = sprites.Enemy()
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)

    global game_score
    game_score = 0

    background_image1 = pg.image.load('field background.jpg')

    click_sound = pg.mixer.Sound("8-bit-laser.aiff")

    playing = True


    while playing:
        #--- Main event loop
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): #if user clicked close
                started = False #Flag that user is done and exit loop
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                marshmellow = sprites.Bullet()
                marshmellow.rect.bottom = player.rect.top
                marshmellow.rect.centerx = player.rect.centerx
                blast_sprites.add(marshmellow)
                all_sprites.add(marshmellow)
                click_sound.play()
        screen.fill(BLACK) #set screen background color
        screen.blit(background_image1, [0, 0])
        #text = font.render("Score: " + str(score), True, RED)

        #update
        all_sprites.update()
        hits = pg.sprite.spritecollide(player, enemy_sprites, False)

        if hits:
            playing = False


        hits2 = pg.sprite.groupcollide(blast_sprites, enemy_sprites, True, True)

        for hit in hits2:
            enemy = sprites.Enemy()
            enemy_sprites.add(enemy)
            all_sprites.add(enemy)
            game_score += 10
    # --- DRAWING CODE--- ###############################################################################################
        scoredisplay(game_score)
        all_sprites.draw(screen)
        #screen.blit(text, [10, 10])
    #####################################################################################################################

        #waits to display the screen until the program has finished drawing,
        # then "flips" the graphics drawn to the screen
        pg.display.flip()

        # Limit framerate to (FPS) frames per second
        clock.tick(FPS)
gamestart()
while True:
    gameplay()
    gameover(game_score)
    input()
pg.quit()
