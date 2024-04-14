import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Мой проект")
icon = pygame.image.load("images/icon.png").convert_alpha()
pygame.display.set_icon(icon)


p_a_c = 0

bg = pygame.image.load("BG/my_fon.png").convert_alpha()
bg2 = pygame.image.load("BG/my_fon.png").convert_alpha()
bg_x = 0
restart = True
enemy = pygame.image.load("enemys/monster0.png").convert_alpha()
enemy = pygame.transform.scale(enemy,(36, 36))
at = pygame.image.load('images/atake.png').convert_alpha()
at = pygame.transform.scale(at, (50, 30))
attaks = []

walk_left = [
pygame.image.load("player_animation/left1.png").convert_alpha(), pygame.image.load("player_animation/left2.png").convert_alpha(),
pygame.image.load("player_animation/left3.png").convert_alpha(), pygame.image.load("player_animation/left4.png").convert_alpha()
]

walk_right = [
pygame.image.load("player_animation/righ1.png").convert_alpha(), pygame.image.load("player_animation/righ2.png").convert_alpha(),
    pygame.image.load("player_animation/righ3.png").convert_alpha(), pygame.image.load("player_animation/righ4.png").convert_alpha()
]

spavn_enemy = []

ps = 5
px = 200
py = 450
start_pos = 200
speed = 5
score = 0
record = score
jump = False
height_jump = 10

bg_sound = pygame.mixer.Sound("music/music.mp3")
bg_sound.play()
millis = 1500
myfont = pygame.font.Font('font/myfont.ttf', 80)
myfont_b = pygame.font.Font('font/myfont.ttf', 50)
myfont3 = pygame.font.Font('font/myfont.ttf', 25)
text = myfont.render("ВЫ ПРОИГРАЛИ!", True, (103,148,181),)
text_b = myfont_b.render("Рестарт(кликните мышкой)", False, (181,100,69) )
text_b_rect = text_b.get_rect(topleft=(150, 300))


spavn = pygame.USEREVENT + 1
pygame.time.set_timer(spavn, millis)

energy = 10

running = True
while running:
    keys = pygame.key.get_pressed()
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg2, (bg_x + 1000, 0))
    text_score = myfont3.render("счет: " + str(score), True, 'Black')
    text_record = myfont3.render("рекорд: " + str(record), True, 'Black')
    text_energy = myfont3.render("енергия: " + str(energy), True, 'Black')
    screen.blit(text_score, (0,0))
    screen.blit(text_record, (0,20))
    screen.blit(text_energy, (0,40))
    mouse = pygame.mouse.get_pos()
    if text_b_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        restart = True
        px = start_pos
        spavn_enemy.clear()
        attaks.clear()
        score = 0
        millis = 1500
        speed = 5
        energy = 10


    if restart:
        pr = walk_left[0].get_rect(topleft=(px, py))
        if spavn_enemy:
            for (i, el) in enumerate(spavn_enemy):
                screen.blit(enemy, el)
                el.x -= speed

                if el.x < -50:
                    spavn_enemy.pop(i)
                    score += 1
                    speed += 0.25
                    energy += 0.25
                    millis -= 250
                    if record < score:
                        record = score
                    else:
                        record = record

                if pr.colliderect(el):
                    restart = False





        if attaks:
            for (i, el) in enumerate(attaks):
                screen.blit(at, (el.x, el.y))
                el.x += 10

                if el.x > 1050:
                    attaks.pop(i)

                if spavn_enemy:
                    for (ind, en) in enumerate(spavn_enemy):
                        if el.colliderect(en):
                            spavn_enemy.pop(ind)
                            attaks.pop(i)
                            score += 0.5
                            if record < score:
                                record = score
                            else:
                                record = record


        if keys[pygame.K_a]:
            screen.blit(walk_left[int(p_a_c)], (px, py))
        else:
            screen.blit(walk_right[int(p_a_c)], (px, py))

        if not jump:
            if keys[pygame.K_SPACE]:
                jump = True
        else:
            if height_jump >= -10:
                if height_jump > 0:
                    py -= (height_jump ** 2) / 4
                else:
                    py += (height_jump ** 2) / 4

                height_jump -= 1
            else:
                height_jump = 10
                jump = False

        if keys[pygame.K_d] and px < 975:
            px += ps
        elif keys[pygame.K_a] and px > 0:
            px -= ps


        if p_a_c == 3:
            p_a_c = 0
        else:
            p_a_c += 0.125

        bg_x -= 2
        if bg_x == -1000:
            bg_x = 0
    else:
        screen.fill('Grey')
        screen.blit(text, (175, 100))
        screen.blit(text_b, text_b_rect)
        screen.blit(text_score, (450,400))
        screen.blit(text_record, (450, 420))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


        if event.type == spavn:
            spavn_enemy.append(enemy.get_rect(topleft=(1050,450 )))
        if restart and event.type  == pygame.KEYDOWN and event.key == pygame.K_f and energy > 0.80:
            attaks.append(at.get_rect(topleft=(px + 20, py + 10)))
            energy -= 1

    clock.tick(60)
    print(record)
    print(score)
    print(jump)
    print(spavn_enemy, px, py, start_pos)
    print(millis)
    print(speed)
    print(attaks)
    print(energy)
