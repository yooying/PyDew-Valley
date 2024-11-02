import pygame
from player import Player

class Level:
    def __init__(self):
        # Sprite group for all sprites
        self.all_sprites = pygame.sprite.Group()
        
        # Create and add player to the group
        self.player = Player((100, 100), self.all_sprites)  # Adjust position

    def run(self, dt):
        # Update and draw all sprites
        self.all_sprites.update(dt)
        self.all_sprites.draw(pygame.display.get_surface())
