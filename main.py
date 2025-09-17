import pygame
import random
from bullet import Bullet
from asteroid import Asteroid

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

bullet_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()

spawn_position = (640, 600)
player_image = pygame.image.load("assets/player/player1Ship.png").convert_alpha()
player_rectangle = player_image.get_rect()
player_rectangle.center = spawn_position
player_speed = 300

bullet_image = pygame.image.load("assets/laser/laserBlue.png").convert_alpha()

asteroid_image = pygame.image.load("assets/asteroid/asteroid1.png").convert_alpha()

ASTEROID_SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ASTEROID_SPAWN_EVENT, 2000)


while True:
    delta_time = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(bullet_image, player_rectangle)
                bullet_group.add(bullet)
        if event.type == ASTEROID_SPAWN_EVENT:
            asteroid = Asteroid(asteroid_image, random.randint(0, 1280), -50)
            asteroid_group.add(asteroid)


    keys = pygame.key.get_pressed()
    if keys:
        if keys[pygame.K_a]:
            player_rectangle.centerx -= player_speed * delta_time
        if keys[pygame.K_d]:
            player_rectangle.centerx += player_speed * delta_time
    if player_rectangle.left < 0:
        player_rectangle.left = 0
    if player_rectangle.right > 1280:
        player_rectangle.right = 1280


    for asteroid in asteroid_group:
        if player_rectangle.colliderect(asteroid.rect):
            asteroid.kill()
            print("Player has been hit. -1 lives!")

    bullet_with_asteroid_collisions = pygame.sprite.groupcollide(bullet_group, asteroid_group, True, True)
    if bullet_with_asteroid_collisions:
        print("Player has hit the asteroid with a laser bullet! +1 Points!")

    screen.fill((0, 128, 0))
    
    screen.blit(player_image, player_rectangle)

    bullet_group.draw(screen)
    bullet_group.update(delta_time)
    
    asteroid_group.draw(screen)
    asteroid_group.update(delta_time)
    pygame.display.flip()