import pygame
from map import draw_map, map_tiles, obstaculos_personajes, obstaculos_balas, exit_tile
from settings import *
from player import *
from enemys import *
from weapon import *
from data import *
from functions import reiniciar
#---------------------------------------------------------------------------------------------------------------------------
pygame.init()
#---------------------------------------------------------------------------------------------------------------------------
#personajes
jugador = crear_jugador()
enemigos = []
#---------------------------------------------------------------------------------------------------------------------------
#eventos de usuario
cambiar_imagen_evento = pygame.USEREVENT + 1
pygame.time.set_timer(cambiar_imagen_evento, 100) #(tipo de evento, cada cuando se genera el evento)
cambiar_imagen_jumpscare = pygame.USEREVENT + 2
pygame.time.set_timer(cambiar_imagen_jumpscare, 50) #(tipo de evento, cada cuando se genera el evento)
cambiar_imagen_foxy = pygame.USEREVENT + 3
pygame.time.set_timer(cambiar_imagen_foxy, 35) #(tipo de evento, cada cuando se genera el evento)
#---------------------------------------------------------------------------------------------------------------------------
#pantalla
SCREEN = pygame.display.set_mode(SCREEN_SIZE) #establecer tamaño de la pantalla
pygame.display.set_caption("Escape from Freddy's") #nombrar al juego
pygame.display.set_icon(icon) #mostrar icono
clock = pygame.time.Clock() #reloj
#---------------------------------------------------------------------------------------------------------------------------
#pantallas
def title_screen(imagen):
    SCREEN.blit(imagen, [0,0])
    SCREEN.blit(tittle_text_1, (80, 40)) #botom.x botom.y
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
    SCREEN.fill(COLOR)
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

def game_over_screen(imagen):
    SCREEN.blit(imagen, [0,0])
    SCREEN.blit(tittle_game_over_text, (220, 100)) #botom.x botom.y
    pygame.draw.rect(SCREEN, (NEGRO), back_menu_button_1)
    pygame.draw.rect(SCREEN, (NEGRO), exit_button_1)
    SCREEN.blit(back_menu_text_1, (255, 320))
    SCREEN.blit(exit_text_1, (345, 400))
    pygame.display.update()

def pantalla_win(imagen, score):
    score_text_2 = font.render(f"Score: {score}", True, BLANCO)
    SCREEN.blit(imagen, [0,0])
    SCREEN.blit(tittle_victory_text, (160, 10)) #botom.x botom.y
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
#variables
indice_imagen_actual = 0
tiempo_linterna = 0
espera_linterna = 0
#---------------------------------------------------------------------------------------------------------------------------
#movimiento
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False
#---------------------------------------------------------------------------------------------------------------------------
#banderas
is_running = True
mostrar_title_screen = True
mostrar_instructions_screen = False
mostrar_difficulty_screen = False
mostrar_game = False
mostrar_game_over_screen = False
mostrar_victory_screen = False

mostrar_jumpscare_freddy = False
mostrar_jumpscare_bonnie = False
mostrar_jumpscare_chica = False
mostrar_jumpscare_foxy = False
mostrar_jumpscare_puppet = False

flag_primeros_enemigos = True
flag_niños = True
flag_puerta = False
flag_linterna = False
flag_linterna_disponible = True
#---------------------------------------------------------------------------------------------------------------------------
while is_running:
    clock.tick(FPS) # limita al while en cada iteracion 

    if mostrar_game: 
        for event in pygame.event.get(): #retorna lista de eventos (que ocurrieron desde la ultima vez que llame a 'get')
            if event.type == pygame.QUIT: #QUIT = 256(cruz)
                is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    mover_izquierda = True
                if event.key == pygame.K_d:
                    mover_derecha = True
                if event.key == pygame.K_w:
                    mover_arriba = True
                if event.key == pygame.K_s:
                    mover_abajo = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    mover_izquierda = False
                if event.key == pygame.K_d:
                    mover_derecha = False
                if event.key == pygame.K_w:
                    mover_arriba = False
                if event.key == pygame.K_s:
                    mover_abajo = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Right-click
                create_bullet(jugador, event.pos)
                sonido_disparo.play()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if pygame.time.get_ticks() - espera_linterna >= 10000:
                    if flag_linterna_disponible:
                        tiempo_linterna = pygame.time.get_ticks()
                        flag_linterna = True
                        sonido_linterna.play()
                        flag_linterna_disponible = False
                    elif flag_linterna_disponible == False:
                        sonido_no_linterna.play()
                else: 
                    sonido_no_linterna.play() 
        #---------------------------------------------------------------------------------------------------------------------------
        if flag_primeros_enemigos:
            for i in range (CANT_ENEMIGOS):
                enemigo = crear_enemigo(jugador, obstaculos_personajes)
                enemigos.append(enemigo)
            flag_primeros_enemigos = False

        #imagenes vida
        if jugador["vidas"] > 450:
            corazon_imagen = lista_corazones[0]
        elif jugador["vidas"] <= 450 and jugador["vidas"] > 400:
            corazon_imagen = lista_corazones[1]
        elif jugador["vidas"] <= 400 and jugador["vidas"] > 350:
            corazon_imagen = lista_corazones[2]
        elif jugador["vidas"] <= 350 and jugador["vidas"] > 300:
            corazon_imagen = lista_corazones[3]
        elif jugador["vidas"] <= 300 and jugador["vidas"] > 250:
            corazon_imagen = lista_corazones[4]
        elif jugador["vidas"] <= 250 and jugador["vidas"] > 200:
            corazon_imagen = lista_corazones[5]
        elif jugador["vidas"] <= 200 and jugador["vidas"] > 150:
            corazon_imagen = lista_corazones[6]
        elif jugador["vidas"] <= 150 and jugador["vidas"] > 100:
            corazon_imagen = lista_corazones[7]
        elif jugador["vidas"] <= 100 and jugador["vidas"] > 50:
            corazon_imagen = lista_corazones[8]
        elif jugador["vidas"] <= 50 and jugador["vidas"] > 0:
            corazon_imagen = lista_corazones[9]
        elif jugador["vidas"] == 0:
            corazon_imagen = lista_corazones[10]

        #linterna
        if flag_linterna: #si la linterna está en uso
            if pygame.time.get_ticks() - tiempo_linterna >= 3000:
                flag_linterna = False
                espera_linterna = pygame.time.get_ticks()
            linterna_imagen = lista_linterna[1]
        else:
            linterna_imagen = lista_linterna[0]
            flag_linterna_disponible = True

        #texto score
        score_text = font_data.render(f"Score: {jugador["score"]}", True, BLANCO)
                                      
        #mover jugador
        mover_jugador(mover_derecha, mover_izquierda, mover_arriba, mover_abajo, jugador, obstaculos_personajes)

        #puntaje
        if jugador["score"] == score_needed:
            if flag_niños:
                sonido_niños.play()
                flag_niños = False

        # verificar si se completó el nivel
        flag_puerta = pasar_puerta(jugador, exit_tile, score_needed)
        if flag_puerta:
            mostrar_game = False
            mostrar_victory_screen = True
            pygame.mixer.music.stop()
        
        #quitar vida a enemigo
        for enemigo in enemigos:
            if enemigo["vidas"] == 0:
                enemigos.remove(enemigo)
                jugador["score"] += 100
                nuevo_enemigo = crear_enemigo(jugador, obstaculos_personajes)
                enemigos.append(nuevo_enemigo)

        #quitar vida a jugador
        if flag_linterna == False:
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
        
        #dibujar en pantalla
        SCREEN.fill(NEGRO)
        draw_map(SCREEN, map_tiles)
        draw_jugador(SCREEN, jugador)
        update_bullets(obstaculos_balas, enemigos)
        draw_bullets(SCREEN)
        draw_enemigos(SCREEN, enemigos)
        SCREEN.blit(corazon_imagen, (10, 10))
        SCREEN.blit(linterna_imagen, (150, -5))
        SCREEN.blit(score_text, (500, 10))
        pygame.display.update()
    #---------------------------------------------------------------------------------------------------------------------------
    elif mostrar_title_screen:
        mover_derecha, mover_izquierda, mover_arriba, mover_abajo, jugador, enemigos, flag_primeros_enemigos, flag_niños = reiniciar(mover_derecha, mover_izquierda, mover_arriba, mover_abajo, jugador, enemigos)
        pygame.mixer.music.play(-1)
        title_screen(title_images[indice_imagen_actual])
        for event in pygame.event.get(): #procesa todos los eventos desde la ultima iteracion
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.collidepoint(event.pos): #si el clic ocurre dentro de boton jugar
                    sonido_boton.play()
                    mostrar_title_screen = False 
                    indice_imagen_actual = 0
                    mostrar_difficulty_screen = True
                if instructions_button.collidepoint(event.pos):
                    sonido_boton.play()
                    mostrar_title_screen = False
                    indice_imagen_actual = 0
                    mostrar_instructions_screen = True
                if exit_button_0.collidepoint(event.pos): #si el clic ocurre dentro de boton salir
                    is_running = False
            if event.type == cambiar_imagen_evento:
                indice_imagen_actual = (indice_imagen_actual + 1) % len(title_images)
    #---------------------------------------------------------------------------------------------------------------------------
    elif mostrar_instructions_screen:
        instructions_screen(instructions_images[indice_imagen_actual])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sonido_boton.play()
                    mostrar_instructions_screen = False
                    indice_imagen_actual = 0
                    mostrar_title_screen = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # Clic derecho
                    sonido_boton.play()
                    indice_imagen_actual += 1
                    if indice_imagen_actual >= len(instructions_images):
                        indice_imagen_actual = 0
                if event.button == 1:  # Clic izquierdo
                    sonido_boton.play()
                    indice_imagen_actual -= 1
                    if indice_imagen_actual < 0:
                        indice_imagen_actual = len(instructions_images) - 1
    #---------------------------------------------------------------------------------------------------------------------------
    elif mostrar_difficulty_screen:
        difficulty_screen(title_images[indice_imagen_actual])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sonido_boton.play()
                    mostrar_difficulty_screen = False
                    indice_imagen_actual = 0
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
            if event.type == cambiar_imagen_evento:
                indice_imagen_actual = (indice_imagen_actual + 1) % len(title_images)
    #---------------------------------------------------------------------------------------------------------------------------
    elif mostrar_game_over_screen:
        game_over_screen(game_over_images[indice_imagen_actual])
        # pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_menu_button_1.collidepoint(event.pos):
                    sonido_boton.play()
                    mostrar_game_over_screen = False
                    indice_imagen_actual = 0
                    mostrar_title_screen = True
                if exit_button_1.collidepoint(event.pos):
                    is_running = False
            if event.type == cambiar_imagen_evento:
                indice_imagen_actual = (indice_imagen_actual + 1) % len(game_over_images)
    #---------------------------------------------------------------------------------------------------------------------------
    elif mostrar_victory_screen:
        pantalla_win(victory_images[indice_imagen_actual], jugador["score"])
        pygame.mixer.music.stop()
        musica_win.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_menu_button_2.collidepoint(event.pos):
                    sonido_boton.play()
                    mostrar_victory_screen = False
                    indice_imagen_actual = 0
                    musica_win.stop()
                    mostrar_title_screen = True
                if exit_button_2.collidepoint(event.pos):
                    is_running = False
            if event.type == cambiar_imagen_evento:
                indice_imagen_actual = (indice_imagen_actual + 1) % len(victory_images)
    #---------------------------------------------------------------------------------------------------------------------------
    elif mostrar_jumpscare_freddy:
        pantalla_jumpscare(jumpscare_freddy[indice_imagen_actual])
        pygame.mixer.music.stop()
        sonido_jumpscare.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == cambiar_imagen_foxy:
                if indice_imagen_actual < 15:
                    indice_imagen_actual = indice_imagen_actual + 1 % len(jumpscare_freddy)
                else:
                    mostrar_jumpscare_freddy = False
                    indice_imagen_actual = 0
                    mostrar_game_over_screen = True
    #---------------------------------------------------------------------------------------------------------------------------
    elif mostrar_jumpscare_bonnie:
        pantalla_jumpscare(jumpscare_bonnie[indice_imagen_actual])
        pygame.mixer.music.stop()
        sonido_jumpscare.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == cambiar_imagen_foxy:
                if indice_imagen_actual < 15:
                    indice_imagen_actual = indice_imagen_actual + 1 % len(jumpscare_bonnie)
                else:
                    mostrar_jumpscare_bonnie = False
                    indice_imagen_actual = 0
                    mostrar_game_over_screen = True
    #---------------------------------------------------------------------------------------------------------------------------        
    elif mostrar_jumpscare_chica:
        pantalla_jumpscare(jumpscare_chica[indice_imagen_actual])
        pygame.mixer.music.stop()
        sonido_jumpscare.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == cambiar_imagen_foxy:
                if indice_imagen_actual < 15:
                    indice_imagen_actual = indice_imagen_actual + 1 % len(jumpscare_chica)
                else:
                    mostrar_jumpscare_chica = False
                    indice_imagen_actual = 0
                    mostrar_game_over_screen = True
    #---------------------------------------------------------------------------------------------------------------------------
    elif mostrar_jumpscare_foxy:
        pantalla_jumpscare(jumpscare_foxy[indice_imagen_actual])
        pygame.mixer.music.stop()
        sonido_jumpscare.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == cambiar_imagen_foxy:
                if indice_imagen_actual < 13:
                    indice_imagen_actual = indice_imagen_actual + 1 % len(jumpscare_foxy)
                else:
                    mostrar_jumpscare_foxy = False
                    indice_imagen_actual = 0
                    mostrar_game_over_screen = True
    #---------------------------------------------------------------------------------------------------------------------------
    elif mostrar_jumpscare_puppet:
        pantalla_jumpscare(jumpscare_puppet[indice_imagen_actual])
        pygame.mixer.music.stop()
        sonido_jumpscare.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == cambiar_imagen_foxy:
                if indice_imagen_actual < 15:
                    indice_imagen_actual = indice_imagen_actual + 1 % len(jumpscare_foxy)
                else:
                    mostrar_jumpscare_puppet = False
                    indice_imagen_actual = 0
                    mostrar_game_over_screen = True
pygame.quit()