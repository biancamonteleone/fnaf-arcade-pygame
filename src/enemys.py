import pygame
from settings import *
from random import randint
from functions import escalar_img
from data import freddy_img, bonnie_img, chica_img, foxy_img, puppet_img, obstaculos_personajes

def crear_enemigo(jugador: dict) -> dict:
    """
    Crea un enemigo con una posición y una imagen aleatoria.

    Args:
    jugador (dict): Diccionario que contiene información sobre el jugador.

    Returns:
    dict: Diccionario con los atributos del enemigo.
    """
    posiciones_enemigos = [(100, 100), (380, 70), (380, 250), (30, 275), (380, 320), (700, 250), (700, 500), (70, 500)]
    imagenes_enemigos = [freddy_img, bonnie_img, chica_img, foxy_img, puppet_img]

    indice_posicion = randint(0, len(posiciones_enemigos) - 1)
    indice_imagen = randint(0, len(imagenes_enemigos) - 1)

    cordenada_random = posiciones_enemigos[indice_posicion]
    imagen_random = imagenes_enemigos[indice_imagen]

    if imagen_random == freddy_img:
        tipo = "freddy"
    elif imagen_random == bonnie_img:
        tipo = "bonnie"
    elif imagen_random == chica_img:
        tipo = "chica"
    elif imagen_random == foxy_img:
        tipo = "foxy"
    elif imagen_random == puppet_img:
        tipo = "puppet"

    x, y = cordenada_random

    imagen_random = escalar_img(imagen_random, ESCALA_PERSONAJES)
    enemigo = {
        "image": imagen_random,
        "shape": pygame.Rect(x, y, imagen_random.get_width(), imagen_random.get_height()),
        "flip": False,
        "velocidad": 1,
        "tipo": tipo,
        "vidas": 75,
        "seguir": jugador
    }
    return enemigo

def mover_enemigo(enemigo: dict, jugador: dict) -> None:
    """
    Mueve al enemigo hacia el jugador y maneja las colisiones con obstáculos.

    Args:
    enemigo (dict): Diccionario que contiene información sobre el enemigo.
    jugador (dict): Diccionario que contiene información sobre el jugador.

    Returns:
    None
    """
    delta_x = 0
    delta_y = 0

    if enemigo["shape"].x < jugador["shape"].x:
        delta_x += enemigo["velocidad"]
        enemigo["flip"] = False
    elif enemigo["shape"].x > jugador["shape"].x:
        delta_x -= enemigo["velocidad"]
        enemigo["flip"] = True
    if enemigo["shape"].y < jugador["shape"].y:
        delta_y += enemigo["velocidad"]
    elif enemigo["shape"].y > jugador["shape"].y:
        delta_y -= enemigo["velocidad"]

    enemigo["shape"].x += delta_x
    if enemigo_colision_obstaculos(enemigo["shape"], obstaculos_personajes):
        enemigo["shape"].x -= delta_x

    enemigo["shape"].y += delta_y
    if enemigo_colision_obstaculos(enemigo["shape"], obstaculos_personajes):
        enemigo["shape"].y -= delta_y

def enemigo_colision_obstaculos(shape: pygame.Rect, obstaculos: list) -> bool:
    """
    Verifica si el enemigo colisiona con algún obstáculo.

    Args:
    shape (pygame.Rect): Rectángulo que representa la forma del enemigo.
    obstaculos (list): Lista de obstáculos.

    Returns:
    bool: True si el enemigo colisiona con un obstáculo, False en caso contrario.
    """
    for obstaculo in obstaculos:
        if shape.colliderect(obstaculo[1]):
            return True
    return False

def draw_enemigos(interfaz: pygame.Surface, enemigos: list) -> None:
    """
    Dibuja a los enemigos en la interfaz del juego.

    Args:
    interfaz (pygame.Surface): Superficie en la que se dibujan los enemigos.
    enemigos (list): Lista de diccionarios que contienen información sobre los enemigos.

    Returns:
    None
    """
    for enemigo in enemigos:
        image_flip = pygame.transform.flip(enemigo["image"], enemigo["flip"], False)
        interfaz.blit(image_flip, enemigo["shape"])