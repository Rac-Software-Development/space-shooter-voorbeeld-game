import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, player):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (player.centerx, player.y)
        self.speed = -300


    def update(self, dt):
        self.rect.centery += self.speed * dt
        if self.rect.bottom < 0:
            print("Reached the top of the screen. Removing bullet from game.")
            self.kill()