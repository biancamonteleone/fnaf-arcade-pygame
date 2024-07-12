import pygame
from settings import *

def crear_jugador(jugador_img:pygame.surface) -> dict:
    """
    Crea un diccionario que representa al jugador con sus atributos iniciales.

    Args:
    jugador_img (pygame.Surface): Imagen del jugador.

    Returns:
    dict: Diccionario con los atributos del jugador.
    """
    jugador = {
    "image": jugador_img,
    "shape": pygame.Rect(380, 450, jugador_img.get_width(), jugador_img.get_height()),
    "flip": False,
    "velocidad": 2,
    "tipo": "player",
    "vidas": 500,
    "score": 0
    }   
    return jugador

def mover_jugador(mover_derecha:bool, mover_izquierda:bool, mover_arriba:bool, mover_abajo:bool, jugador:dict, obstaculos_tiles:list) -> None:
    """
    Mueve al jugador según las teclas presionadas y maneja las colisiones con los obstáculos.

    Args:
    mover_derecha (bool): Estado de movimiento hacia la derecha del jugador.
    mover_izquierda (bool): Estado de movimiento hacia la izquierda del jugador.
    mover_arriba (bool): Estado de movimiento hacia arriba del jugador.
    mover_abajo (bool): Estado de movimiento hacia abajo del jugador.
    jugador (dict): Diccionario que contiene información del jugador.
    obstaculos_tiles (list): Lista de tiles que actúan como obstáculos.

    Returns:
    None
    """
    delta_x = 0
    delta_y = 0
    if mover_izquierda:
        delta_x -= jugador["velocidad"]
    if mover_derecha:
        delta_x += jugador["velocidad"]
    if mover_arriba:
        delta_y -= jugador["velocidad"]
    if mover_abajo:
        delta_y += jugador["velocidad"]

    if delta_x < 0:
        jugador["flip"] = True
    if delta_x > 0:
        jugador["flip"] = False

    jugador["shape"].x += delta_x
    for obstaculo in obstaculos_tiles:
        if obstaculo[1].colliderect(jugador["shape"]):
            if delta_x > 0:
                jugador["shape"].right = obstaculo[1].left
            if delta_x < 0:
                jugador["shape"].left = obstaculo[1].right

    jugador["shape"].y += delta_y
    for obstaculo in obstaculos_tiles:
        if obstaculo[1].colliderect(jugador["shape"]):
            if delta_y > 0:
                jugador["shape"].bottom = obstaculo[1].top
            if delta_y < 0:
                jugador["shape"].top = obstaculo[1].bottom


def pasar_puerta(jugador:dict, exit_tile:tuple, score_needed:int) -> bool:
    """
    Verifica si el jugador tiene la puntuación necesaria para pasar por la puerta.

    Args:
    jugador (dict): Diccionario que contiene información sobre el jugador.
    exit_tile (tuple): Tupla con información sobre el tile de salida.
    score_needed (int): Puntuación necesaria para pasar por la puerta.

    Returns:
    bool: True si el jugador puede pasar por la puerta, False en caso contrario.
    """
    if jugador["score"] >= score_needed:
        if exit_tile[1].colliderect(jugador["shape"]):
            return True
    else:
        return False
    
def draw_jugador(interfaz:pygame.surface, jugador:dict) -> None:
    """
    Dibuja al jugador en la interfaz del juego.

    Args:
    interfaz (pygame.Surface): Superficie en la que se dibuja al jugador.
    jugador (dict): Diccionario que contiene información sobre el jugador.

    Returns:
    None
    """
    image_flip = pygame.transform.flip(jugador["image"], jugador["flip"], False)
    interfaz.blit(image_flip, jugador["shape"])