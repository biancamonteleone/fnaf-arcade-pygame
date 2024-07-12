import pygame
from settings import *
from player import *
from enemys import *
from weapon import *
from data import *
from functions import *
#---------------------------------------------------------------------------------------------------------------------------
pygame.init()
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Escape from Freddy's")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

cambiar_imagen_evento = pygame.USEREVENT + 1
pygame.time.set_timer(cambiar_imagen_evento, 100)
cambiar_imagen_jumpscare = pygame.USEREVENT + 2
pygame.time.set_timer(cambiar_imagen_jumpscare, 35)

jugador = crear_jugador(jugador_img)
enemigos = []
#---------------------------------------------------------------------------------------------------------------------------
def title_screen(imagen):
    SCREEN.blit(imagen, [0,0])
    SCREEN.blit(tittle_text_1, (80, 40))
    SCREEN.blit(tittle_text_2, (80, 110))
    SCREEN.blit(tittle_text_3, (80, 180))
    pygame.draw.rect(SCREEN, (NEGRO), play_button)
    pygame.draw.rect(SCREEN, (NEGRO), instructions_button)
    pygame.draw.rect(SCREEN, (NEGRO), exit_button_0)
    SCREEN.blit(play_text, (80, 310))
    SCREEN.blit(instructions_text, (80, 390))
    SCREEN.blit(exit_text_0, (80, 480))
    pygame.display.update()

def instructions_screen(imagen):
    SCREEN.fill(COLOR_FONDO)
    SCREEN.blit(imagen, [0,0])
    pygame.display.update()

def difficulty_screen(imagen):
    SCREEN.blit(imagen, [0,0])
    SCREEN.blit(difficulty_text_1, (80,40))
    SCREEN.blit(difficulty_text_2, (80,110))
    SCREEN.blit(difficulty_text_3, (80,180))
    pygame.draw.rect(SCREEN, (NEGRO), easy_button)
    pygame.draw.rect(SCREEN, (NEGRO), medium_button)
    pygame.draw.rect(SCREEN, (NEGRO), hard_button)
    SCREEN.blit(easy_text, (80,310))
    SCREEN.blit(medium_text, (80,390))
    SCREEN.blit(hard_text, (80,480))
    pygame.display.update()

def pantalla_pause():
    pygame.draw.rect(SCREEN, (BLANCO), pause_botton)
    pygame.draw.rect(SCREEN, (NEGRO), back_menu_button_3)
    pygame.draw.rect(SCREEN, (NEGRO), exit_button_3)
    SCREEN.blit(pause_text, (300, 150))
    SCREEN.blit(back_menu_text_3, (250, 300))
    SCREEN.blit(exit_text_3, (350, 380))
    pygame.display.update() 

def game_over_screen(imagen):
    SCREEN.blit(imagen, [0,0])
    SCREEN.blit(tittle_game_over_text, (220, 100))
    pygame.draw.rect(SCREEN, (NEGRO), back_menu_button_1)
    pygame.draw.rect(SCREEN, (NEGRO), exit_button_1)
    SCREEN.blit(back_menu_text_1, (255, 320))
    SCREEN.blit(exit_text_1, (345, 400))
    pygame.display.update()

def pantalla_win(imagen, score:int):
    score_text_2 = font.render(f"Score: {score}", True, BLANCO)
    SCREEN.blit(imagen, [0,0])
    SCREEN.blit(tittle_victory_text, (160, 10))
    pygame.draw.rect(SCREEN, (NEGRO), back_menu_button_2)
    pygame.draw.rect(SCREEN, (NEGRO), exit_button_2)
    SCREEN.blit(score_text_2, (260, 100))
    SCREEN.blit(back_menu_text_2, (250, 200))
    SCREEN.blit(exit_text_2, (350, 270))
    pygame.display.update()

def pantalla_jumpscare(imagen):
    SCREEN.blit(imagen, [0,0])
    pygame.display.update()
#---------------------------------------------------------------------------------------------------------------------------
indice_imagen_actual = 0
tiempo_linterna_uso = 0
espera_linterna = 0
pause_star = 0
pause_duration = 0

mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

is_running = True
mostrar_title_screen = True
mostrar_instructions_screen = False
mostrar_difficulty_screen = False
mostrar_game = False
mostrar_game_over_screen = False
mostrar_victory_screen = False
mostrar_pause_screen = False

mostrar_jumpscare_freddy = False
mostrar_jumpscare_bonnie = False
mostrar_jumpscare_chica = False
mostrar_jumpscare_foxy = False
mostrar_jumpscare_puppet = False

flag_primeros_enemigos = True
flag_niños = True
linterna_on = False
#---------------------------------------------------------------------------------------------------------------------------
while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
        if mostrar_title_screen:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.collidepoint(event.pos):
                    sonido_boton.play()
                    mostrar_title_screen = False
                    mostrar_difficulty_screen = True
                if instructions_button.collidepoint(event.pos):
                    sonido_boton.play()
                    mostrar_title_screen = False
                    indice_imagen_actual = 0
                    mostrar_instructions_screen = True
                if exit_button_0.collidepoint(event.pos):
                    is_running = False
            if event.type == cambiar_imagen_evento:
                indice_imagen_actual = (indice_imagen_actual + 1) % len(title_images)
        
        elif mostrar_instructions_screen:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sonido_boton.play()
                mostrar_instructions_screen = False
                mostrar_title_screen = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    sonido_boton.play()
                    indice_imagen_actual = (indice_imagen_actual + 1) % len(instructions_images)
                if event.button == 1:
                    sonido_boton.play()
                    indice_imagen_actual = (indice_imagen_actual - 1) % len(instructions_images)
        
        elif mostrar_difficulty_screen:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sonido_boton.play()
                mostrar_difficulty_screen = False
                mostrar_title_screen = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if easy_button.collidepoint(event.pos):
                    sonido_boton.play()
                    CANT_ENEMIGOS = 3
                    score_needed = 500
                    mostrar_difficulty_screen = False
                    indice_imagen_actual = 0
                    mostrar_game = True
                elif medium_button.collidepoint(event.pos):
                    sonido_boton.play()
                    CANT_ENEMIGOS = 4
                    score_needed = 1000
                    mostrar_difficulty_screen = False
                    indice_imagen_actual = 0
                    mostrar_game = True
                elif hard_button.collidepoint(event.pos):
                    sonido_boton.play()
                    CANT_ENEMIGOS = 6
                    score_needed = 1500
                    mostrar_difficulty_screen = False
                    indice_imagen_actual = 0
                    mostrar_game = True
            elif event.type == cambiar_imagen_evento:
                indice_imagen_actual = (indice_imagen_actual + 1) % len(title_images)

        elif mostrar_game:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    mover_izquierda = True
                if event.key == pygame.K_d:
                    mover_derecha = True
                if event.key == pygame.K_w:
                    mover_arriba = True
                if event.key == pygame.K_s:
                    mover_abajo = True
                if event.key == pygame.K_ESCAPE:
                    pause_start = pygame.time.get_ticks()
                    mostrar_pause_screen = True
                    mostrar_game = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    mover_izquierda = False
                if event.key == pygame.K_d:
                    mover_derecha = False
                if event.key == pygame.K_w:
                    mover_arriba = False
                if event.key == pygame.K_s:
                    mover_abajo = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    create_bullet(jugador["shape"], event.pos)
                    sonido_disparo.play()
                if event.button == 3:
                    if linterna_on == False:
                        if pygame.time.get_ticks() - espera_linterna >= 10000:
                                tiempo_linterna_uso = pygame.time.get_ticks()
                                linterna_on = True
                                sonido_linterna.play()
                        else:
                            sonido_no_linterna.play()
                    else:
                        sonido_no_linterna.play()
        
        elif mostrar_pause_screen:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_menu_button_3.collidepoint(event.pos):
                    sonido_boton.play()
                    mostrar_pause_screen = False
                    mostrar_title_screen = True
                if exit_button_3.collidepoint(event.pos):
                    is_running = False
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause_end = pygame.time.get_ticks()
                pause_duration = pause_end - pause_start
                espera_linterna += pause_duration
                mostrar_pause_screen = False
                pygame.mixer.music.unpause()
                mostrar_game = True
        
        elif mostrar_game_over_screen:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_menu_button_1.collidepoint(event.pos):
                    sonido_boton.play()
                    mostrar_game_over_screen = False
                    musica_win.stop()
                    mostrar_title_screen = True
                if exit_button_1.collidepoint(event.pos):
                    is_running = False
            if event.type == cambiar_imagen_evento:
                indice_imagen_actual = (indice_imagen_actual + 1) % len(game_over_images)
        
        elif mostrar_victory_screen:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_menu_button_2.collidepoint(event.pos):
                    sonido_boton.play()
                    musica_win.stop()
                    mostrar_victory_screen = False
                    mostrar_title_screen = True
                if exit_button_2.collidepoint(event.pos):
                    is_running = False
            if event.type == cambiar_imagen_evento:
                indice_imagen_actual = (indice_imagen_actual + 1) % len(victory_images)
        
        elif mostrar_jumpscare_freddy:
            if event.type == cambiar_imagen_jumpscare:
                if indice_imagen_actual < 15:
                    indice_imagen_actual = indice_imagen_actual + 1 % len(jumpscare_freddy)
                else:
                    indice_imagen_actual = 0
                    mostrar_jumpscare_freddy = False
                    mostrar_game_over_screen = True

        elif mostrar_jumpscare_bonnie:
            if event.type == cambiar_imagen_jumpscare:
                if indice_imagen_actual < 15:
                    indice_imagen_actual = indice_imagen_actual + 1 % len(jumpscare_bonnie)
                else:
                    indice_imagen_actual = 0
                    mostrar_jumpscare_bonnie = False
                    mostrar_game_over_screen = True

        elif mostrar_jumpscare_chica:
            if event.type == cambiar_imagen_jumpscare:
                if indice_imagen_actual < 15:
                    indice_imagen_actual = indice_imagen_actual + 1 % len(jumpscare_chica)
                else:
                    indice_imagen_actual = 0
                    mostrar_jumpscare_chica = False
                    mostrar_game_over_screen = True

        elif mostrar_jumpscare_foxy:
            if event.type == cambiar_imagen_jumpscare:
                if indice_imagen_actual < 13:
                    indice_imagen_actual = indice_imagen_actual + 1 % len(jumpscare_foxy)
                else:
                    indice_imagen_actual = 0
                    mostrar_jumpscare_foxy = False
                    mostrar_game_over_screen = True

        elif mostrar_jumpscare_puppet:
            if event.type == cambiar_imagen_jumpscare:
                if indice_imagen_actual < 15:
                    indice_imagen_actual = indice_imagen_actual + 1 % len(jumpscare_puppet)
                else:
                    indice_imagen_actual = 0
                    mostrar_jumpscare_puppet = False
                    mostrar_game_over_screen = True
    #---------------------------------------------------------------------------------------------------------------------------
    if mostrar_title_screen:
        mover_derecha, mover_izquierda, mover_arriba, mover_abajo, jugador, enemigos, flag_primeros_enemigos, flag_niños = reiniciar(mover_derecha, mover_izquierda, mover_arriba, mover_abajo, jugador, enemigos)
        title_screen(title_images[indice_imagen_actual])
        pygame.mixer.music.play(-1)

    elif mostrar_instructions_screen:
        instructions_screen(instructions_images[indice_imagen_actual])

    elif mostrar_difficulty_screen:
        difficulty_screen(title_images[indice_imagen_actual])

    elif mostrar_game:
        if flag_primeros_enemigos:
            for i in range (CANT_ENEMIGOS):
                enemigo = crear_enemigo(jugador)
                enemigos.append(enemigo)
            flag_primeros_enemigos = False

        corazon_imagen = calcular_vidas(jugador["vidas"], lista_corazones)

        if linterna_on:
            linterna_imagen = lista_linterna[1]
            if pygame.time.get_ticks() - tiempo_linterna_uso >= 3000:
                linterna_on = False
                espera_linterna = pygame.time.get_ticks()
        else:
            linterna_imagen = lista_linterna[0]

        score_text = font_data.render(f"Score: {jugador["score"]}", True, BLANCO)
                                      
        mover_jugador(mover_derecha, mover_izquierda, mover_arriba, mover_abajo, jugador, obstaculos_personajes)

        if jugador["score"] == score_needed:
            if flag_niños:
                sonido_niños.play()
                flag_niños = False

        flag_puerta = pasar_puerta(jugador, exit_tile, score_needed)
        if flag_puerta:
            indice_imagen_actual = 0
            mostrar_game = False
            mostrar_victory_screen = True
            pygame.mixer.music.stop()
        
        for enemigo in enemigos:
            if enemigo["vidas"] == 0:
                enemigos.remove(enemigo)
                jugador["score"] += 100
                nuevo_enemigo = crear_enemigo(jugador)
                enemigos.append(nuevo_enemigo)

        if linterna_on == False:
            for enemigo in enemigos:
                mover_enemigo(enemigo, jugador)
                if jugador["shape"].colliderect(enemigo["shape"]):
                    jugador["vidas"] -= 1
                    if jugador["vidas"] == 0:
                        indice_imagen_actual = 0
                        mostrar_game = False
                        if enemigo["tipo"] == "freddy":
                            mostrar_jumpscare_freddy = True
                        if enemigo["tipo"] == "bonnie":
                            mostrar_jumpscare_bonnie = True
                        if enemigo["tipo"] == "chica":
                            mostrar_jumpscare_chica = True
                        if enemigo["tipo"] == "foxy":
                            mostrar_jumpscare_foxy = True
                        if enemigo["tipo"] == "puppet":
                            mostrar_jumpscare_puppet = True
        
        SCREEN.fill(NEGRO)
        draw_map(SCREEN, map_tiles)
        draw_jugador(SCREEN, jugador)
        update_bullets(obstaculos_balas, enemigos, bullets)
        draw_bullets(SCREEN, bullets)
        draw_enemigos(SCREEN, enemigos)
        SCREEN.blit(corazon_imagen, (10, 10))
        SCREEN.blit(linterna_imagen, (150, -5))
        SCREEN.blit(score_text, (500, 10))
        pygame.display.update()

    elif mostrar_pause_screen:
        pause_star = pygame.time.get_ticks()
        pantalla_pause()
        pygame.mixer.music.pause()

    elif mostrar_game_over_screen:
        game_over_screen(game_over_images[indice_imagen_actual])

    elif mostrar_victory_screen:
        pantalla_win(victory_images[indice_imagen_actual], jugador["score"])
        pygame.mixer.music.stop()
        musica_win.play()

    elif mostrar_jumpscare_freddy:
        pantalla_jumpscare(jumpscare_freddy[indice_imagen_actual])
        pygame.mixer.music.stop()
        sonido_jumpscare.play()

    elif mostrar_jumpscare_bonnie:
        pantalla_jumpscare(jumpscare_bonnie[indice_imagen_actual])
        pygame.mixer.music.stop()
        sonido_jumpscare.play()
     
    elif mostrar_jumpscare_chica:
        pantalla_jumpscare(jumpscare_chica[indice_imagen_actual])
        pygame.mixer.music.stop()
        sonido_jumpscare.play()

    elif mostrar_jumpscare_foxy:
        pantalla_jumpscare(jumpscare_foxy[indice_imagen_actual])
        pygame.mixer.music.stop()
        sonido_jumpscare.play()

    elif mostrar_jumpscare_puppet:
        pantalla_jumpscare(jumpscare_puppet[indice_imagen_actual])
        pygame.mixer.music.stop()
        sonido_jumpscare.play()

pygame.quit()