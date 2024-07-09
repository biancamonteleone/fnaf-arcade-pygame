import pygame
from settings import *
from random import randint
from functions import escalar_img
from data import freddy_img, bonnie_img, chica_img, foxy_img, puppet_img

def crear_enemigo(jugador:dict, obstaculos:list) -> dict:
    
    posiciones_enemigos = [(100,100), (380,70), (380,250), (30,275), (380,320), (700,250), (700,500), (70,500)]
    imagenes_enemigos = [freddy_img, bonnie_img, chica_img, foxy_img, puppet_img]

    indice_posicion = randint(0, len(posiciones_enemigos) -1)
    indice_imagen= randint(0, len(imagenes_enemigos) -1)

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

    imagen_random = escalar_img(imagen_random, ESCALA_PERSONAJE)
    enemigo = {
        "image": imagen_random,
        "shape": pygame.Rect(x, y, WIDTH_PERSONAJE, HEIGHT_PERSONAJE),
        "flip": False,
        "velocidad": 1,
        "seguir": jugador, #Referencia al jugador para seguirlo
        "tipo": tipo,
        "obstaculos": obstaculos,
        "vidas": 75,
    }
    return enemigo

def mover_enemigo(enemigo: dict, jugador) -> None:
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

    # Intentar mover en el eje X
    enemigo["shape"].x += delta_x
    if enemigo_colision_obstaculos(enemigo["shape"], enemigo["obstaculos"]):
        enemigo["shape"].x -= delta_x  # Revertir movimiento si hay colisión

    # Intentar mover en el eje Y
    enemigo["shape"].y += delta_y
    if enemigo_colision_obstaculos(enemigo["shape"], enemigo["obstaculos"]):
        enemigo["shape"].y -= delta_y  # Revertir movimiento si hay colisión

def enemigo_colision_obstaculos(shape, obstaculos: list) -> bool:
    for obstaculo in obstaculos:
        if shape.colliderect(obstaculo[1]):  # Acceder al rectángulo de la tupla
            return True
    return False

def enemigo_colision_obstaculos(shape, obstaculos:list) -> bool:
    for obstaculo in obstaculos:
        if shape.colliderect(obstaculo[1]):  # Acceder al rectángulo de la tupla
            return True
    return False

def draw_enemigos(interfaz, enemigos:list) -> None:
    for enemigo in enemigos:
        image_flip = pygame.transform.flip(enemigo["image"], enemigo["flip"], False)
        interfaz.blit(image_flip, enemigo["shape"])