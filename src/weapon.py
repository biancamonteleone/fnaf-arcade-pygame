import pygame
from settings import *
from data import bala_img

bullets = []
def create_bullet(jugador, mouse_pos):
    bullet_rect = bala_img.get_rect()
    bullet_rect.center = jugador["shape"].center
    direction = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(jugador["shape"].center)

    # Normalize direction vector
    direction = direction.normalize()

    # Determine the cardinal direction
    if abs(direction.x) > abs(direction.y):
        if direction.x > 0:
            bullet_direction = pygame.math.Vector2(1, 0)  # Right
        else:
            bullet_direction = pygame.math.Vector2(-1, 0)  # Left
    else:
        if direction.y > 0:
            bullet_direction = pygame.math.Vector2(0, 1)  # Down
        else:
            bullet_direction = pygame.math.Vector2(0, -1)  # Up

    # Calculate the angle for rotation
    angle = bullet_direction.angle_to(pygame.math.Vector2(1, 0))

    # Rotate the bullet image for cardinal directions
    rotated_bullet_image = pygame.transform.rotate(bala_img, +angle)

    # Adjust speed as needed
    speed = SPEED * 2
    direction *= speed

    bullets.append({"rect": bullet_rect, "direction": direction, "image": rotated_bullet_image})

def update_bullets(obstaculos_tiles, enemigos):
    global bullets
    updated_bullets = []

    for bullet in bullets:
        bullet["rect"].x += bullet["direction"].x
        bullet["rect"].y += bullet["direction"].y

        # Verificar colisiones con obstáculos
        bullet_hit_obstacle = False
        for obstaculo in obstaculos_tiles:
            if obstaculo[1].colliderect(bullet["rect"]):
                bullet_hit_obstacle = True
                break
        for enemigo in enemigos:
            if enemigo["shape"].colliderect(bullet["rect"]):
                enemigo["vidas"] -= 5
                bullet_hit_obstacle = True
        
        if bullet_hit_obstacle:
            continue  # No agregar la bala a la lista actualizada

        # Verificar si la bala está fuera de los límites de la pantalla
        if (bullet["rect"].x < 0 or bullet["rect"].x > WIDTH or
            bullet["rect"].y < 0 or bullet["rect"].y > HEIGHT):
            continue  # No agregar la bala a la lista actualizada

        # Agregar la bala a la lista actualizada
        updated_bullets.append(bullet)

    # Actualizar la lista de balas
    bullets = updated_bullets

def draw_bullets(surface):
    for bullet in bullets:
        surface.blit(bullet["image"], bullet["rect"])