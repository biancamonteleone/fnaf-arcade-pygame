import pygame
from settings import WIDTH_PERSONAJE, HEIGHT_PERSONAJE

def get_path_actual(nombre_archivo:str) -> str:
    """
    Obtiene la ruta completa del archivo especificado en el directorio actual del script.

    Args:
        nombre_archivo (str): El nombre del archivo para el cual se desea obtener la ruta completa.

    Returns:
        str: La ruta completa del archivo especificado.
    """
    import os
    ubi = os.path.dirname(__file__)

    return os.path.join(ubi, nombre_archivo)

def cargar_archivo_json(nombre_archivo:str) -> any:
    """
    Carga los datos de un archivo JSON y los devuelve como una estructura de datos de Python.

    Args:
        nombre_archivo (str): El nombre del archivo JSON que contiene los datos.

    Returns:
        any: La estructura de datos de Python obtenida del archivo JSON
    """
    import json
    with open(get_path_actual(nombre_archivo), "r", encoding="utf-8") as archivo:
        return json.load(archivo)
    
def escalar_img(image, scale:int):
    """
    Escala una imagen a una nueva dimensión.

    Args:
        image (pygame.Surface): La imagen que se desea escalar.
        scale (int): El factor de escala que se aplicará a la imagen.

    Returns:
        pygame.Surface: La imagen escalada a las nuevas dimensiones.
    """
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

def reiniciar(mover_derecha, mover_izquierda, mover_arriba, mover_abajo, jugador, enemigos):
    flag_enemigos = True
    flag_niños = True
    mover_derecha = False
    mover_izquierda = False
    mover_arriba = False
    mover_abajo = False
    jugador["shape"] = pygame.Rect(380, 450, WIDTH_PERSONAJE, HEIGHT_PERSONAJE)
    jugador["vidas"] = 500
    jugador["score"] = 0
    for enemigo in enemigos:
        enemigos.remove(enemigo)
    return mover_derecha, mover_izquierda, mover_arriba, mover_abajo, jugador, enemigos, flag_enemigos, flag_niños

    
