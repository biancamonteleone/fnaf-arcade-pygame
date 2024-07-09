import pygame
from settings import *
from data import jugador_img

def crear_jugador():
    jugador = {
    "image": jugador_img,
    "shape": pygame.Rect(380, 450, WIDTH_PERSONAJE, HEIGHT_PERSONAJE),
    "flip": False,
    "tipo": "player",
    "vidas": 500,
    "score": 0
    }   
    return jugador

def draw_jugador(interfaz, jugador):
    #Voltea la imagen del jugador si es necesario
    image_flip = pygame.transform.flip(jugador["image"], jugador["flip"], False)
    #Dibuja la imagen del jugador en la interfaz en la posición especificada por su 'shape'
    interfaz.blit(image_flip, jugador["shape"])

def mover_jugador(mover_derecha, mover_izquierda, mover_arriba, mover_abajo, jugador, obstaculos_tiles):
    delta_x = 0
    delta_y = 0
    if mover_izquierda:
        delta_x -= SPEED
    if mover_derecha:
        delta_x += SPEED
    if mover_arriba:
        delta_y -= SPEED
    if mover_abajo:
        delta_y += SPEED

    if delta_x < 0:
        jugador["flip"] = True
    if delta_x > 0:
        jugador["flip"] = False

    # Mover en el eje x
    jugador["shape"].x += delta_x
    for obstaculo in obstaculos_tiles:
        if obstaculo[1].colliderect(jugador["shape"]):
            if delta_x > 0:
                jugador["shape"].right = obstaculo[1].left
            if delta_x < 0:
                jugador["shape"].left = obstaculo[1].right

    # Mover en el eje y
    jugador["shape"].y += delta_y
    for obstaculo in obstaculos_tiles:
        if obstaculo[1].colliderect(jugador["shape"]):
            if delta_y > 0:
                jugador["shape"].bottom = obstaculo[1].top
            if delta_y < 0:
                jugador["shape"].top = obstaculo[1].bottom

def pasar_puerta(jugador, exit_tile, score_needed):
    if jugador["score"] >= score_needed:
        if jugador["tipo"] == "player" and exit_tile[1].colliderect(jugador["shape"]):
            return True
    else:
        return False
    