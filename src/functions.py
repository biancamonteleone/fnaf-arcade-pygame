import pygame


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

def reiniciar(mover_derecha:bool, mover_izquierda:bool, mover_arriba:bool, mover_abajo:bool, jugador:dict, enemigos:list) -> tuple:
    """
    Reinicia el estado del juego.

    Args:
    mover_derecha (bool): Estado de movimiento hacia la derecha del jugador.
    mover_izquierda (bool): Estado de movimiento hacia la izquierda del jugador.
    mover_arriba (bool): Estado de movimiento hacia arriba del jugador.
    mover_abajo (bool): Estado de movimiento hacia abajo del jugador.
    jugador (dict): Diccionario que contiene información sobre el jugador.
    enemigos (list): Lista de enemigos.

    Returns:
    tuple: Una tupla que contiene los estados actualizados de movimiento del jugador,
           del diccionario del jugador, la lista de enemigos vacía, 
           y las banderas `flag_enemigos` y `flag_niños` establecidas en True.
    """
    flag_enemigos = True
    flag_niños = True
    mover_derecha = False
    mover_izquierda = False
    mover_arriba = False
    mover_abajo = False
    jugador["shape"] = pygame.Rect(380, 450, jugador["image"].get_width(), jugador["image"].get_height())
    jugador["vidas"] = 500
    jugador["score"] = 0
    for enemigo in enemigos:
        enemigos.remove(enemigo)
    return mover_derecha, mover_izquierda, mover_arriba, mover_abajo, jugador, enemigos, flag_enemigos, flag_niños

def calcular_vidas(cant_vidas:int, lista_corazones:list):
    """
    Calcula la imagen de corazón correspondiente según la cantidad de vidas del jugador.

    Args:
    cant_vidas (int): La cantidad de vidas del jugador.
    lista_corazones (list): Lista de imágenes de corazones.

    Returns:
    pygame.Surface: La imagen de corazón correspondiente.
    """
    if cant_vidas > 450:
        corazon_imagen = lista_corazones[0]
    elif cant_vidas <= 450 and cant_vidas > 400:
        corazon_imagen = lista_corazones[1]
    elif cant_vidas <= 400 and cant_vidas > 350:
        corazon_imagen = lista_corazones[2]
    elif cant_vidas <= 350 and cant_vidas > 300:
        corazon_imagen = lista_corazones[3]
    elif cant_vidas <= 300 and cant_vidas > 250:
        corazon_imagen = lista_corazones[4]
    elif cant_vidas <= 250 and cant_vidas > 200:
        corazon_imagen = lista_corazones[5]
    elif cant_vidas <= 200 and cant_vidas > 150:
        corazon_imagen = lista_corazones[6]
    elif cant_vidas <= 150 and cant_vidas > 100:
        corazon_imagen = lista_corazones[7]
    elif cant_vidas <= 100 and cant_vidas > 50:
        corazon_imagen = lista_corazones[8]
    elif cant_vidas <= 50 and cant_vidas > 0:
        corazon_imagen = lista_corazones[9]
    elif cant_vidas == 0:
        corazon_imagen = lista_corazones[10]
    return corazon_imagen


    
