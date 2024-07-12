import csv
import pygame
from settings import *

obstacles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 60, 61, 62, 63, 67]
bullet_obstacles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 61]

def load_world_data(ruta_archivo:str) -> list:
    """
    Carga los datos del mundo desde un archivo CSV y los convierte en una lista de listas de enteros.

    Args:
        ruta_archivo (str): La ruta al archivo CSV que contiene los datos del mundo.

    Returns:
        list: Una lista de listas, donde cada sublista representa una fila del mapa y cada elemento en la sublista representa una celda en esa fila.
    """
    world_data = []
    with open(ruta_archivo, newline="") as archivo:
        archivo_csv = csv.reader(archivo, delimiter=';') 
        for linea in archivo_csv:
            fila = []
            for tile in linea:
                fila.append(int(tile))
            world_data.append(fila)
    return world_data

def process_tiles() -> list:
    """
    Carga y procesa las imágenes de los tiles del juego.

    Returns:
        list: Una lista con todos los tiles del juego.
    """
    tile_list = []
    for x in range(105):
        tile_image = pygame.image.load(f"src/assets/images/tiles/tile({x+1}).png")
        tile_image = pygame.transform.scale(tile_image, (TILE_SIZE, TILE_SIZE))
        tile_list.append(tile_image)
    return tile_list

def process_data(data:list, tile_list:list) -> tuple:
    """
    Procesa los datos del mapa y genera listas de tiles, obstáculos, obstáculos para balas y el tile de salida.

    Args:
        data (list): Una lista de listas que representa el mapa del juego, donde cada número corresponde a un tile específico.
        tile_list (list): Una lista con todos los tiles del juego.

    Returns:
        tuple:
            - map_tiles (list): Lista de todos los tiles con su imagen, rectángulo y coordenadas.
            - obstaculos_tiles (list): Lista de tiles que actúan como obstáculos.
            - obstaculos_tiles_bullets (list): Lista de tiles que actúan como obstáculos para las balas.
            - exit_tile (list): El tile que representa la salida del nivel.
    """
    map_tiles = []
    obstaculos_tiles = []
    obstaculos_tiles_bullets = []
    exit_tile = []

    for y in range(len(data)):
        fila = data[y]
        for x in range(len(fila)):
            tile = fila[x]
            image = tile_list[tile]
            image_rect = image.get_rect()
            image_x = x * TILE_SIZE
            image_y = y * TILE_SIZE
            image_rect.center = (image_x, image_y)
            tile_data = [image, image_rect, image_x, image_y]
            map_tiles.append(tile_data)
            if tile in obstacles:
                obstaculos_tiles.append(tile_data)
            if tile in bullet_obstacles:
                obstaculos_tiles_bullets.append(tile_data)
            if tile == 78:
                exit_tile = tile_data

    return map_tiles, obstaculos_tiles, obstaculos_tiles_bullets, exit_tile

def draw_map(surface, map_tiles:list):
    """
    Dibuja los tiles en una superficie dada.

    Args:
        surface (pygame.Surface): Superficie sobre la que se dibujarán los tiles.
        map_tiles (list): Lista de tiles, donde cada tile es una lista que contiene una imagen y un rectángulo.
    """
    for tile in map_tiles:
        surface.blit(tile[0], tile[1])
