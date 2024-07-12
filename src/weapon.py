from settings import *
from data import bala_img

bullets = []

def create_bullet(jugador_pos, mouse_pos):
    """
    Crea una nueva bala y la añade a la lista de balas.

    Args:
    jugador_pos (pygame.Rect): Rectángulo que representa la posición del jugador.
    mouse_pos (tuple): Tupla que contiene las coordenadas (x, y) del cursor del ratón.

    Returns:
    None
    """
    bullet_rect = bala_img.get_rect()
    bullet_rect.center = jugador_pos.center
    
    player_x, player_y = jugador_pos.center
    mouse_x, mouse_y = mouse_pos

    delta_x = mouse_x - player_x
    delta_y = mouse_y - player_y


    if delta_x >= 0:
        abs_delta_x = delta_x 
    else:
        abs_delta_x = -delta_x
    if delta_y >= 0:
        abs_delta_y = delta_y
    else: 
        abs_delta_y = -delta_y


    if abs_delta_x > abs_delta_y:
        max_delta = abs_delta_x
    else:
        max_delta = abs_delta_y

    delta_x = delta_x * SPEED_BULLET // max_delta 
    delta_y = delta_y * SPEED_BULLET // max_delta 

    bullet = {
        "image": bala_img,
        "rect": bullet_rect,  
        "direction": (delta_x, delta_y)
    }

    bullets.append(bullet)

def update_bullets(obstaculos_tiles, enemigos, bullets):
    """
    Actualiza la posición de las balas y maneja las colisiones con obstáculos y enemigos.

    Args:
    obstaculos_tiles (list): Lista de tuplas que representan los obstáculos del juego.
    enemigos (list): Lista de diccionarios que representan a los enemigos del juego.
    bullets (list): Lista de diccionarios que representan las balas del jugador.

    Returns:
    None
    """
    updated_bullets = []

    for bullet in bullets:
        bullet["rect"].x += bullet["direction"][0]
        bullet["rect"].y += bullet["direction"][1]


        bullet_hit_obstacle = False
        for obstaculo in obstaculos_tiles:
            if obstaculo[1].colliderect(bullet["rect"]):
                bullet_hit_obstacle = True
        

        for enemigo in enemigos:
            if enemigo["shape"].colliderect(bullet["rect"]):
                enemigo["vidas"] -= 5
                bullet_hit_obstacle = True

        if bullet_hit_obstacle == False:
            updated_bullets.append(bullet)


    bullets[:] = updated_bullets

def draw_bullets(surface, bullets):
    """
    Dibuja las balas en la superficie del juego.

    Args:
    surface (pygame.Surface): Superficie donde se dibujarán las balas.
    bullets (list): Lista de diccionarios que representan las balas del jugador.

    Returns:
    None
    """
    for bullet in bullets:
        surface.blit(bullet["image"], bullet["rect"])