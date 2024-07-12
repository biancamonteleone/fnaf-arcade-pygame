import pygame
from settings import *
from functions import cargar_archivo_json, escalar_img
from map import *

pygame.font.init()
rutas = cargar_archivo_json("rutas.json")
world_data = load_world_data("src/mapa.csv")
tile_list = process_tiles()
map_tiles, obstaculos_personajes, obstaculos_balas, exit_tile = process_data(world_data, tile_list)


icon = pygame.image.load(rutas[R_EXTRAS]["ruta icono"])
bala_img = escalar_img(pygame.image.load(rutas[R_EXTRAS]["ruta bala"]), ESCALA_BALA)
lista_linterna = []
for i in range(2):
    image = pygame.image.load(rutas[R_EXTRAS][f"ruta linterna {i}"])
    image = escalar_img(image, 0.2)
    lista_linterna.append(image)

title_images = []
for i in range(15):
    image = pygame.image.load(rutas[R_IMAGENES_TITLE][f"ruta inicio {i}"])
    title_images.append(image)

instructions_images = []
for i in range(8):
    image = pygame.image.load(rutas[R_IMAGENES_INSTRUCTIONS][f"ruta instructions {i}"])
    instructions_images.append(image)

game_over_images = []
for i in range(8):
    image = pygame.image.load(rutas[R_IMAGENES_OVER][f"ruta over {i}"])
    game_over_images.append(image)

victory_images = []
for i in range(8):
    image = pygame.image.load(rutas[R_IMAGENES_VICTORY][f"ruta victory {i}"])
    victory_images.append(image)

jumpscare_freddy = []
for i in range(16):
    image = pygame.image.load(rutas[R_JUMPSCARE_FREDDY][f"ruta jumpscare freddy {i}"])
    jumpscare_freddy.append(image)

jumpscare_bonnie = []
for i in range(16):
    image = pygame.image.load(rutas[R_JUMPSCARE_BONNIE][f"ruta jumpscare bonnie {i}"])
    jumpscare_bonnie.append(image)

jumpscare_chica = []
for i in range(16):
    image = pygame.image.load(rutas[R_JUMPSCARE_CHICA][f"ruta jumpscare chica {i}"])
    jumpscare_chica.append(image)

jumpscare_foxy = []
for i in range(14):
    image = pygame.image.load(rutas[R_JUMPSCARE_FOXY][f"ruta jumpscare foxy {i}"])
    jumpscare_foxy.append(image)

jumpscare_puppet = []
for i in range(16):
    image = pygame.image.load(rutas[R_JUMPSCARE_PUPPET][f"ruta jumpscare puppet {i}"])
    jumpscare_puppet.append(image)

lista_corazones = []
for i in range(11):
    image = pygame.image.load(rutas[R_CORAZONES][f"ruta corazones {i}"])
    image = escalar_img(image, 0.2)
    lista_corazones.append(image)

jugador_img = pygame.image.load(rutas[R_PERSONAJES]["ruta guardia"])
jugador_img = escalar_img(jugador_img, ESCALA_PERSONAJES)
freddy_img = pygame.image.load(rutas[R_PERSONAJES]["ruta freddy"])
bonnie_img = pygame.image.load(rutas[R_PERSONAJES]["ruta bonnie"])
chica_img = pygame.image.load(rutas[R_PERSONAJES]["ruta chica"])
foxy_img = pygame.image.load(rutas[R_PERSONAJES]["ruta foxy"])
puppet_img = pygame.image.load(rutas[R_PERSONAJES]["ruta puppet"])

pygame.mixer.init()
musica_win = pygame.mixer.Sound(rutas[R_AUDIO]["ruta musica win"])
pygame.mixer.music.load(rutas[R_AUDIO]["ruta musica"])

sonido_boton = pygame.mixer.Sound(rutas[R_AUDIO]["ruta sonido boton"])
sonido_disparo = pygame.mixer.Sound(rutas[R_AUDIO]["ruta sonido disparo"])
sonido_jumpscare = pygame.mixer.Sound(rutas[R_AUDIO]["ruta sonido jumpscare"])
sonido_niños = pygame.mixer.Sound(rutas[R_AUDIO]["ruta sonido niños"])
sonido_vida = pygame.mixer.Sound(rutas[R_AUDIO]["ruta sonido vida"])
sonido_estatica = pygame.mixer.Sound(rutas[R_AUDIO]["ruta sonido estatica"])
sonido_linterna = pygame.mixer.Sound(rutas[R_AUDIO]["ruta sonido linterna"])
sonido_no_linterna = pygame.mixer.Sound(rutas[R_AUDIO]["ruta sonido no linterna"])

font = pygame.font.Font(rutas[R_FUENTE]["ruta fuente"], 40)
font_tittle = pygame.font.Font(rutas[R_FUENTE]["ruta fuente"], 60)
font_data = pygame.font.Font(rutas[R_FUENTE]["ruta fuente"], 20)

tittle_text_1 = font_tittle.render("Escape", True, BLANCO)
tittle_text_2 = font_tittle.render("from", True, BLANCO)
tittle_text_3 = font_tittle.render("Freddy's", True, BLANCO)
play_text = font.render("New game", True, BLANCO)
instructions_text = font.render("Instructions", True, BLANCO)
exit_text_0 = font.render("Exit", True, BLANCO)

difficulty_text_1 = font_tittle.render("Choose", True, BLANCO)
difficulty_text_2 = font_tittle.render("the", True, BLANCO)
difficulty_text_3 = font_tittle.render("Difficulty", True, BLANCO)
easy_text = font.render("Easy", True, BLANCO)
medium_text = font.render("Medium", True, BLANCO)
hard_text = font.render("Hard", True, BLANCO)

tittle_game_over_text = font_tittle.render("Game Over", True, BLANCO)
back_menu_text_1 = font.render("Back to menu", True, BLANCO)
exit_text_1 = font.render("Exit", True, BLANCO)

tittle_victory_text = font_tittle.render("¡You Escaped!", True, BLANCO)
back_menu_text_2 = font.render("Back to menu", True, BLANCO)
exit_text_2 = font.render("Exit", True, BLANCO)

pause_text = font_tittle.render("PAUSE", True, NEGRO)
back_menu_text_3 = font.render("Back to menu", True, BLANCO)
exit_text_3 = font.render("Exit", True, BLANCO)

play_button = pygame.Rect(75, 310, 225, 50)
instructions_button = pygame.Rect(75, 390, 315, 50)
exit_button_0 = pygame.Rect(75, 480, 90, 50)

easy_button = pygame.Rect(75, 310, 125, 50)
medium_button = pygame.Rect(75, 390, 165, 50)
hard_button = pygame.Rect(75, 480, 125, 50)

back_menu_button_1 = pygame.Rect(255, 320, 300, 50)
exit_button_1 = pygame.Rect(345, 400, 90, 50)

back_menu_button_2 = pygame.Rect(250, 200, 300, 50)
exit_button_2 = pygame.Rect(350, 270, 90, 50)

pause_botton = pygame.Rect(290, 150, 235, 80)
back_menu_button_3 = pygame.Rect(250, 300, 300, 50)
exit_button_3 = pygame.Rect(350, 380, 90, 50)


