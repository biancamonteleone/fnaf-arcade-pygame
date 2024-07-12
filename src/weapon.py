from settings import *
from data import bala_img

bullets = []

def create_bullet(jugador_pos, mouse_pos):
    bullet_rect = bala_img.get_rect()
    bullet_rect.center = jugador_pos.center
    
    player_x, player_y = jugador_pos.center
    mouse_x, mouse_y = mouse_pos

    delta_x = mouse_x - player_x
    delta_y = mouse_y - player_y

    #valores absolutos
    if delta_x >= 0:
        abs_delta_x = delta_x 
    else:
        abs_delta_x = -delta_x
    if delta_y >= 0:
        abs_delta_y = delta_y
    else: 
        abs_delta_y = -delta_y

    # Normalizar la dirección
    if abs_delta_x > abs_delta_y:
        max_delta = abs_delta_x
    else:
        max_delta = abs_delta_y

    if max_delta != 0:
        delta_x = delta_x * SPEED_BULLET // max_delta #SE VA A MOVER MAS EN UN EJE QUE EN OTRO
        delta_y = delta_y * SPEED_BULLET // max_delta 

    bullet = {
        "image": bala_img,
        "rect": bullet_rect,  # Cambiado a 'rect' en lugar de 'shape'
        "direction": (delta_x, delta_y)
    }

    bullets.append(bullet)

def update_bullets(obstaculos_tiles, enemigos, bullets):
    updated_bullets = []

    for bullet in bullets:
        # Mover la bala según su dirección
        bullet["rect"].x += bullet["direction"][0]
        bullet["rect"].y += bullet["direction"][1]

        # Verificar colisiones con obstáculos
        bullet_hit_obstacle = False
        for obstaculo in obstaculos_tiles:
            if obstaculo[1].colliderect(bullet["rect"]):
                bullet_hit_obstacle = True
        
        # Verificar colisiones con enemigos
        for enemigo in enemigos:
            if enemigo["shape"].colliderect(bullet["rect"]):
                enemigo["vidas"] -= 5
                bullet_hit_obstacle = True

        # Verificar si la bala está fuera de los límites de la pantalla
        if (bullet["rect"].x < 0 or bullet["rect"].x > WIDTH or
            bullet["rect"].y < 0 or bullet["rect"].y > HEIGHT):
            bullet_hit_obstacle = True

        if not bullet_hit_obstacle:
            updated_bullets.append(bullet)

    # Actualizar la lista global de balas
    bullets[:] = updated_bullets

def draw_bullets(surface, bullets):
    for bullet in bullets:
        surface.blit(bullet["image"], bullet["rect"])