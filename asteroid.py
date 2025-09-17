import pygame

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, asteroid_image, x, y):
        super().__init__()
        self.image = asteroid_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 150


    def update(self, dt):
        self.rect.centery += self.speed * dt
        if self.rect.top > 720:
            print("Reached the bottom of the screen. Removing asteroid from game.")
            self.kill()